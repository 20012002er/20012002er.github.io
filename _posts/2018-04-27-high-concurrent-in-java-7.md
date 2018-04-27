---
layout: post
title: "高并发Java（7）：并发设计模式"
description: "高并发Java系列"
tags: [并发]
---

## 1. 什么是设计模式

在软件工程中，设计模式（design pattern）是对软件设计中普遍存在（反复出现）的各种问题 ，所提出的解决方案。这个术语是由埃里希·伽玛（Erich Gamma）等人在1990年代从建筑设计领 域引入到计算机科学的。

著名的4人帮： Erich Gamma，Richard Helm, Ralph Johnson ,John Vlissides （Gof）

《设计模式：可复用面向对象软件的基础》收录23种模式

## 2. 单例模式

单例对象的类必须保证只有一个实例存在。许多时候整个系统只需要拥有一个的全局对象，这样有利于我们协调系统整体的行为

比如：全局信息配置

单例模式最简单的实现：

{% highlight java %}
public class Singleton {
	private Singleton() {
		System.out.println("Singleton is create");
	}
	private static Singleton instance = new Singleton();
	public static Singleton getInstance() {
		return instance;
	}
}
{% endhighlight %}

由私有构造方法和static来确定唯一性。

缺点：何时产生实例 不好控制

虽然我们知道，在类Singleton第一次被加载的时候，就产生了一个实例。

但是如果这个类中有其他属性

{% highlight java %}
public class Singleton {
	public static int STATUS=1; 
	private Singleton() {
		System.out.println("Singleton is create");
	}
	private static Singleton instance = new Singleton();
	public static Singleton getInstance() {
		return instance;
	}
}
{% endhighlight %}

当使用

{% highlight java %}
System.out.println(Singleton.STATUS);
{% endhighlight %}

这个实例就被产生了。也许此时你并不希望产生这个实例。

如果系统特别在意这个问题，这种单例的实现方法就不太好。

第二种单例模式的解决方式：

{% highlight java %}
public class Singleton {
	private Singleton() {
		System.out.println("Singleton is create");
	}
	private static Singleton instance = null;
	public static synchronized Singleton getInstance() {
		if (instance == null)
			instance = new Singleton();
		return instance;
	}
}
{% endhighlight %}

让instance只有在调用getInstance()方式时被创建，并且通过synchronized来确保线程安全。

这样就控制了何时创建实例。

这种方法是延迟加载的典型。

但是有一个问题就是，在高并发的场景下性能会有影响，虽然只有一个判断就return了，但是在并发量很高的情况下，或多或少都会有点影响，因为都要去拿synchronized的锁。

为了高效，有了第三种方式：

{% highlight java %}
public class StaticSingleton {
	private StaticSingleton(){  
		System.out.println("StaticSingleton is create");
	}
	private static class SingletonHolder {
		private static StaticSingleton instance = new StaticSingleton();
	}
	public static StaticSingleton getInstance() {
		return SingletonHolder.instance;
	}
}
{% endhighlight %}

由于加载一个类时，其内部类不会被加载。这样保证了只有调用getInstance()时才会产生实例，控制了生成实例的时间，实现了延迟加载。

并且去掉了synchronized，让性能更优，用static来确保唯一性。

## 3. 不变模式

一个类的内部状态创建后，在整个生命期间都不会发生变化时，就是不变类

不变模式不需要同步

创建一个不变的类：

{% highlight java %}
public final class Product {
	// 确保无子类
	private final String no;
	// 私有属性，不会被其他对象获取
	private final String name;
	// final保证属性不会被2次赋值
	private final double price;

	public Product(String no, String name, double price) {
		// 在创建对象时，必须指定数据
		super();
		// 因为创建之后，无法进行修改
		this.no = no;
		this.name = name;
		this.price = price;
	}

	public String getNo() {
		return no;
	}

	public String getName() {
		return name;
	}

	public double getPrice() {
		return price;
	}

}
{% endhighlight %}

Java中不变的模式的案例有：

* java.lang.String
* java.lang.Boolean
* java.lang.Byte
* java.lang.Character
* java.lang.Double
* java.lang.Float
* java.lang.Integer
* java.lang.Long
* java.lang.Short

## 4. Future模式

核心思想是异步调用

第一次的call_return由于任务还没完成，所以返回的是一个空的。

但是这个返回类似于购物中的订单，将来可以根据这个订单来得到一个结果。

所以这个Future模式意思就是，“未来”可以得到，就是指这个订单或者说是契约，“承诺”未来就会给结果。

Future模式简单的实现：

调用者得到的是一个Data，一开始可能是一个FutureData，因为RealData构建很慢。在未来的某个时间，可以通过FutureData来得到RealData。

代码实现：

{% highlight java %}
public interface Data {     
	public String getResult (); 
}
{% endhighlight %}

{% highlight java %}
public class FutureData implements Data {     
	protected RealData realdata = null;   //FutureData是RealData的包装     
	protected boolean isReady = false;     
	public synchronized void setRealData(RealData realdata) {         
		if (isReady) {              
			return;         
		}         
		this.realdata = realdata;         
		isReady = true;         
		notifyAll();    //RealData已经被注入，通知getResult()     
	}     
	public synchronized String getResult()//会等待RealData构造完成         
	{  
		while (!isReady) {             
			try {                 
				wait();    //一直等待，知道RealData被注入            
			} catch (InterruptedException e) {             
				}         
		}         
		return realdata.result;  //由RealData实现       
	} 
}
{% endhighlight %}

{% highlight java %}
public class RealData implements Data {
	protected final String result;
	public RealData(String para) {
		// RealData的构造可能很慢，需要用户等待很久，这里使用sleep模拟
		StringBuffer sb = new StringBuffer();
		for (int i = 0; i < 10; i++) {
			sb.append(para);
			try {
				// 这里使用sleep，代替一个很慢的操作过程
				Thread.sleep(100);
			} catch (InterruptedException e) {
			}
		}
		result = sb.toString();
	}
	public String getResult() {
		return result;
	}
}
{% endhighlight %}

{% highlight java %}
public class Client {     
	public Data request(final String queryStr) {         
		final FutureData future = new FutureData();         
		new Thread() {
			public void run() 
			{
				// RealData的构建很慢，           
				//所以在单独的线程中进行                
				RealData realdata = new RealData(queryStr);                 
				future.setRealData(realdata);             
			}                                                        
		}.start();         
		return future; // FutureData会被立即返回     
	} 
}
{% endhighlight %}

{% highlight java %}
public static void main(String[] args) {
		Client client = new Client();
		// 这里会立即返回，因为得到的是FutureData而不是RealData
		Data data = client.request("name");
		System.out.println("请求完毕");
		try {
			// 这里可以用一个sleep代替了对其他业务逻辑的处理
			// 在处理这些业务逻辑的过程中，RealData被创建，从而充分利用了等待时间
			Thread.sleep(2000);
		} catch (InterruptedException e) {
		}
		// 使用真实的数据
		System.out.println("数据 = " + data.getResult());
	}
{% endhighlight %}

JDK中也有多Future模式的支持：

接下来使用JDK提供的类和方法来实现刚刚的代码：

{% highlight java %}
import java.util.concurrent.Callable;

public class RealData implements Callable<String> {
	private String para;

	public RealData(String para) {
		this.para = para;
	}

	@Override
	public String call() throws Exception {
		StringBuffer sb = new StringBuffer();
		for (int i = 0; i < 10; i++) {
			sb.append(para);
			try {
				Thread.sleep(100);
			} catch (InterruptedException e) {

			}
		}
		return sb.toString();
	}
}
{% endhighlight %}

{% highlight java %}
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.FutureTask;

public class FutureMain {
	public static void main(String[] args) throws InterruptedException,
			ExecutionException {
		// 构造FutureTask
		FutureTask<String> future = new FutureTask<String>(new RealData("a"));
		ExecutorService executor = Executors.newFixedThreadPool(1);
		// 执行FutureTask，相当于上例中的 client.request("a") 发送请求
		// 在这里开启线程进行RealData的call()执行
		executor.submit(future);
		System.out.println("请求完毕");
		try {
			// 这里依然可以做额外的数据操作，这里使用sleep代替其他业务逻辑的处理
			Thread.sleep(2000);
		} catch (InterruptedException e) {
		}
		// 相当于data.getResult ()，取得call()方法的返回值
		// 如果此时call()方法没有执行完成，则依然会等待
		System.out.println("数据 = " + future.get());
	}
}
{% endhighlight %}

这里要注意的是FutureTask是即具有 Future功能又具有Runnable功能的类。所以又可以运行，最后还能get。

当然如果在调用到future.get()时，真实数据还没准备好，仍然会产生阻塞状况，直到数据准备完成。

当然还有更加简便的方式：

{% highlight java %}
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class FutureMain2 {
	public static void main(String[] args) throws InterruptedException,
			ExecutionException {
		ExecutorService executor = Executors.newFixedThreadPool(1);
		// 执行FutureTask，相当于上例中的 client.request("a") 发送请求
		// 在这里开启线程进行RealData的call()执行
		Future<String> future = executor.submit(new RealData("a"));
		System.out.println("请求完毕");
		try {
			// 这里依然可以做额外的数据操作，这里使用sleep代替其他业务逻辑的处理
			Thread.sleep(2000);
		} catch (InterruptedException e) {
		}
		// 相当于data.getResult ()，取得call()方法的返回值
		// 如果此时call()方法没有执行完成，则依然会等待
		System.out.println("数据 = " + future.get());
	}
}
{% endhighlight %}

由于Callable是有返回值的，可以直接返回future对象。

## 5. 生产者消费者

生产者-消费者模式是一个经典的多线程设计模式。它为多线程间的协作提供了良好的解决方案。 在生产者-消费者模式中，通常由两类线程，即若干个生产者线程和若干个消费者线程。生产者线 程负责提交用户请求，消费者线程则负责具体处理生产者提交的任务。生产者和消费者之间则通 过共享内存缓冲区进行通信。