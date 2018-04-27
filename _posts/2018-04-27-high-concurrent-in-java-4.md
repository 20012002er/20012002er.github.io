---
layout: post
title: "高并发Java（4）：无锁"
description: "高并发Java系列"
tags: [并发]
---

## 1 无锁类的原理详解

### 1.1 CAS

CAS算法的过程是这样：它包含3个参数CAS(V,E,N)。V表示要更新的变量，E表示预期值，N表示新值。仅当V值等于E值时，才会将V的值设为N，如果V值和E值不同，则说明已经有其他线程做了更新，则当前线程什么都不做。最后，CAS返回当前V的真实值。CAS操作是抱着乐观的态度进行的，它总是认为自己可以成功完成操作。当多个线程同时使用CAS操作一个变量时，只有一个会胜出，并成功更新，其余均会失败。失败的线程不会被挂起，仅是被告知失败，并且允许再次尝试，当然也允许失败的线程放弃操作。基于这样的原理，CAS操作即使没有锁，也可以发现其他线程对当前线程的干扰，并进行恰当的处理。

我们会发现，CAS的步骤太多，有没有可能在判断V和E相同后，正要赋值时，切换了线程，更改了值。造成了数据不一致呢？

事实上，这个担心是多余的。CAS整一个操作过程是一个原子操作，它是由一条CPU指令完成的。

### 1.2 CPU指令

CAS的CPU指令是cmpxchg

指令代码如下：

{% highlight java %}
/*
    accumulator = AL, AX, or EAX, depending on whether
    a byte, word, or doubleword comparison is being performed
    */
    if(accumulator == Destination) {
    ZF = 1;
    Destination = Source;
    }
    else {
    ZF = 0;
    accumulator = Destination;
    }
{% endhighlight %}

目标值和寄存器里的值相等的话，就设置一个跳转标志，并且把原始数据设到目标里面去。如果不等的话，就不设置跳转标志了。

Java当中提供了很多无锁类，下面来介绍下无锁类。

## 2 无所类的使用

我们已经知道，无锁比阻塞效率要高得多。我们来看看Java是如何实现这些无锁类的。

### 2.1. AtomicInteger

AtomicInteger和Integer一样，都继承与Number类

{% highlight java %}
public class AtomicInteger extends Number implements java.io.Serializable
{% endhighlight %}

AtomicInteger里面有很多CAS操作，典型的有：

{% highlight java %}
public final boolean compareAndSet(int expect, int update) {
        return unsafe.compareAndSwapInt(this, valueOffset, expect, update);
    }
{% endhighlight %}

这里来解释一下unsafe.compareAndSwapInt方法，他的意思是，对于this这个类上的偏移量为valueOffset的变量值如果与期望值expect相同，那么把这个变量的值设为update。

其实偏移量为valueOffset的变量就是value

{% highlight java %}
static {
      try {
        valueOffset = unsafe.objectFieldOffset
            (AtomicInteger.class.getDeclaredField("value"));
      } catch (Exception ex) { throw new Error(ex); }
}
{% endhighlight %}

我们此前说过，CAS是有可能会失败的，但是失败的代价是很小的，所以一般的实现都是在一个无限循环体内，直到成功为止。

{% highlight java %}
public final int getAndIncrement() {
        for (;;) {
            int current = get();
            int next = current + 1;
            if (compareAndSet(current, next))
                return current;
        }
    }
{% endhighlight %}

### 2.2 Unsafe

从类名就可知，Unsafe操作是非安全的操作，比如：

* 根据偏移量设置值（在刚刚介绍的AtomicInteger中已经看到了这个功能）
* park()（把这个线程停下来，在以后的Blog中会提到）
* 底层的CAS操作

非公开API，在不同版本的JDK中，可能有较大差异

### 2.3. AtomicReference

前面已经提到了AtomicInteger，当然还有AtomicBoolean，AtomicLong等等，都大同小异。

这里要介绍的是AtomicReference。

AtomicReference是一种模板类

{% highlight java %}
public class AtomicReference<V>  implements java.io.Serializable
{% endhighlight %}

它可以用来封装任意类型的数据。

比如String

{% highlight java %}
package test;
 
import java.util.concurrent.atomic.AtomicReference;
 
public class Test
{ 
    public final static AtomicReference<String> atomicString = new AtomicReference<String>("hosee");
    public static void main(String[] args)
    {
        for (int i = 0; i < 10; i++)
        {
            final int num = i;
            new Thread() {
                public void run() {
                    try
                    {
                        Thread.sleep(Math.abs((int)Math.random()*100));
                    }
                    catch (Exception e)
                    {
                        e.printStackTrace();
                    }
                    if (atomicString.compareAndSet("hosee", "ztk"))
                    {
                        System.out.println(Thread.currentThread().getId() + "Change value");
                    }else {
                        System.out.println(Thread.currentThread().getId() + "Failed");
                    }
                };
            }.start();
        }
    }
}
{% endhighlight %}

结果：

{% highlight java %}
10Failed
13Failed
9Change value
11Failed
12Failed
15Failed
17Failed
14Failed
16Failed
18Failed
{% endhighlight %}

可以看到只有一个线程能够修改值，并且后面的线程都不能再修改。

### 2.4.AtomicStampedReference

我们会发现CAS操作还是有一个问题的

比如之前的AtomicInteger的incrementAndGet方法

{% highlight java %}
public final int incrementAndGet() {
        for (;;) {
            int current = get();
            int next = current + 1;
            if (compareAndSet(current, next))
                return next;
        }
    }
{% endhighlight %}

假设当前value=1当某线程int current = get()执行后，切换到另一个线程，这个线程将1变成了2，然后又一个线程将2又变成了1。此时再切换到最开始的那个线程，由于value仍等于1，所以还是能执行CAS操作，当然加法是没有问题的，如果有些情况，对数据的状态敏感时，这样的过程就不被允许了。

此时就需要AtomicStampedReference类。

其内部实现一个Pair类来封装值和时间戳。

{% highlight java %}
private static class Pair<T> {
        final T reference;
        final int stamp;
        private Pair(T reference, int stamp) {
            this.reference = reference;
            this.stamp = stamp;
        }
        static <T> Pair<T> of(T reference, int stamp) {
            return new Pair<T>(reference, stamp);
        }
    }
{% endhighlight %}

这个类的主要思想是加入时间戳来标识每一次改变。

{% highlight java %}
//比较设置 参数依次为：期望值 写入新值 期望时间戳 新时间戳
public boolean compareAndSet(V   expectedReference,
                                 V   newReference,
                                 int expectedStamp,
                                 int newStamp) {
        Pair<V> current = pair;
        return
            expectedReference == current.reference &&
            expectedStamp == current.stamp &&
            ((newReference == current.reference &&
              newStamp == current.stamp) ||
             casPair(current, Pair.of(newReference, newStamp)));
    }
{% endhighlight %}

当期望值等于当前值，并且期望时间戳等于现在的时间戳时，才写入新值，并且更新新的时间戳。

这里举个用AtomicStampedReference的场景，可能不太适合，但是想不到好的场景了。

场景背景是，某公司给余额少的用户免费充值，但是每个用户只能充值一次。

{% highlight java %}
package test;
 
import java.util.concurrent.atomic.AtomicStampedReference;
 
public class Test
{
    static AtomicStampedReference<Integer> money = new AtomicStampedReference<Integer>(
            19, 0);
 
    public static void main(String[] args)
    {
        for (int i = 0; i < 3; i++)
        {
            final int timestamp = money.getStamp();
            new Thread()
            {
                public void run()
                {
                    while (true)
                    {
                        while (true)
                        {
                            Integer m = money.getReference();
                            if (m < 20)
                            {
                                if (money.compareAndSet(m, m + 20, timestamp,
                                        timestamp + 1))
                                {
                                    System.out.println("充值成功，余额:"
                                            + money.getReference());
                                    break;
                                }
                            }
                            else
                            {
                                break;
                            }
                        }
                    }
                };
            }.start();
        }
 
        new Thread()
        {
            public void run()
            {
                for (int i = 0; i < 100; i++)
                {
                    while (true)
                    {
                        int timestamp = money.getStamp();
                        Integer m = money.getReference();
                        if (m > 10)
                        {
                            if (money.compareAndSet(m, m - 10, timestamp,
                                    timestamp + 1))
                            {
                                System.out.println("消费10元，余额:"
                                            + money.getReference());
                                break;
                            }
                        }else {
                            break;
                        }
                    }
                    try
                    {
                        Thread.sleep(100);
                    }
                    catch (Exception e)
                    {
                        // TODO: handle exception
                    }
                }
            };
        }.start();
    }
 
}
{% endhighlight %}

解释下代码，有3个线程在给用户充值，当用户余额少于20时，就给用户充值20元。有100个线程在消费，每次消费10元。用户初始有9元，当使用AtomicStampedReference来实现时，只会给用户充值一次，因为每次操作使得时间戳+1。运行结果：

{% highlight java %}
充值成功，余额:39
消费10元，余额:29
消费10元，余额:19
消费10元，余额:9
{% endhighlight %}

如果使用AtomicReference<Integer>或者 Atomic Integer来实现就会造成多次充值。

{% highlight java %}
充值成功，余额:39
消费10元，余额:29
消费10元，余额:19
充值成功，余额:39
消费10元，余额:29
消费10元，余额:19
充值成功，余额:39
消费10元，余额:29
{% endhighlight %}

### 2.5. AtomicIntegerArray

与AtomicInteger相比，数组的实现不过是多了一个下标。

{% highlight java %}
public final boolean compareAndSet(int i, int expect, int update) {
        return compareAndSetRaw(checkedByteOffset(i), expect, update);
    }
{% endhighlight %}

它的内部只是封装了一个普通的array

{% highlight java %}
private final int[] array;
{% endhighlight %}

里面有意思的是运用了二进制数的前导零来算数组中的偏移量。

{% highlight java %}
shift = 31 - Integer.numberOfLeadingZeros(scale);
{% endhighlight %}

前导零的意思就是比如8位表示12,00001100，那么前导零就是1前面的0的个数，就是4。

具体偏移量如何计算，这里就不再做介绍了。

### 2.6. AtomicIntegerFieldUpdater

AtomicIntegerFieldUpdater类的主要作用是让普通变量也享受原子操作。

就比如原本有一个变量是int型，并且很多地方都应用了这个变量，但是在某个场景下，想让int型变成AtomicInteger，但是如果直接改类型，就要改其他地方的应用。AtomicIntegerFieldUpdater就是为了解决这样的问题产生的。

{% highlight java %}
package test;
 
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicIntegerFieldUpdater;
 
public class Test
{
    public static class V{
        int id;
        volatile int score;
        public int getScore()
        {
            return score;
        }
        public void setScore(int score)
        {
            this.score = score;
        }
 
    }
    public final static AtomicIntegerFieldUpdater<V> vv = AtomicIntegerFieldUpdater.newUpdater(V.class, "score");
 
    public static AtomicInteger allscore = new AtomicInteger(0);
 
    public static void main(String[] args) throws InterruptedException
    {
        final V stu = new V();
        Thread[] t = new Thread[10000];
        for (int i = 0; i < 10000; i++)
        {
            t[i] = new Thread() {
                @Override
                public void run()
                {
                    if(Math.random()>0.4)
                    {
                        vv.incrementAndGet(stu);
                        allscore.incrementAndGet();
                    }
                }
            };
            t[i].start();
        }
        for (int i = 0; i < 10000; i++)
        {
            t[i].join();
        }
        System.out.println("score="+stu.getScore());
        System.out.println("allscore="+allscore);
    }
}
{% endhighlight %}

上述代码将score使用 AtomicIntegerFieldUpdater变成 AtomicInteger。保证了线程安全。

这里使用allscore来验证，如果score和allscore数值相同，则说明是线程安全的。

小说明：

* Updater只能修改它可见范围内的变量。因为Updater使用反射得到这个变量。如果变量不可见，就会出错。比如如果某变量申明为private，就是不可行的。
* 为了确保变量被正确的读取，它必须是volatile类型的。如果我们原有代码中未申明这个类型，那么简单得申明一下就行，这不会引起什么问题。
* 由于CAS操作会通过对象实例中的偏移量直接进行赋值，因此，它不支持static字段（Unsafe.objectFieldOffset()不支持静态变量）。