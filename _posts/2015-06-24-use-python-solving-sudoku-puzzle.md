---
layout: post
title: "用 Python 解决数独问题"
description: "在这篇文章中，我要处理求解任意数独这个问题。用了两个想法（idea）：约束传播和搜索后，它其实是很简单的（主旨大约只有一页代码，加上润色后也不过两页）。"
tags: [技术]
---

在这篇文章中，我要处理求解任意数独这个问题。用了两个想法（idea）：[约束传播](http://en.wikipedia.org/wiki/Constraint_satisfaction)和[搜索](http://en.wikipedia.org/wiki/Search_algorithm)后，它其实是很简单的（主旨大约只有一页[代码](http://norvig.com/sudopy.shtml)，加上润色后也不过两页）。

## 数独记号和初步概念

首先我们要在记号上达成一致。一个数独谜题是由 81 个方块组成的网格。大部分爱好者把列标为 1-9，把行标为 A-I，把 9 个方块的一组（列，行，或者方框）称为一个单元，把处于同一单元的方块称为对等方块。谜题中有些方块是空白的，其他的填入了数字。谜题的主旨是这样的：

> 当每个单元的方块填入了 1 到 9 的一个排列时，谜题就解决了。

也就是说，在一个单元中，任何数字都不能出现两次，而且每个数字都要出现一次。这意味着每个方块的值和它的对等方块的值是不同的。下面是方块的名字、一个典型的谜题及其解答：

{% highlight python %}
A1 A2 A3| A4 A5 A6| A7 A8 A9    4 . . |. . . |8 . 5     4 1 7 |3 6 9 |8 2 5 
 B1 B2 B3| B4 B5 B6| B7 B8 B9    . 3 . |. . . |. . .     6 3 2 |1 5 8 |9 4 7
 C1 C2 C3| C4 C5 C6| C7 C8 C9    . . . |7 . . |. . .     9 5 8 |7 2 4 |3 1 6 
---------+---------+---------    ------+------+------    ------+------+------
 D1 D2 D3| D4 D5 D6| D7 D8 D9    . 2 . |. . . |. 6 .     8 2 5 |4 3 7 |1 6 9 
 E1 E2 E3| E4 E5 E6| E7 E8 E9    . . . |. 8 . |4 . .     7 9 1 |5 8 6 |4 3 2 
 F1 F2 F3| F4 F5 F6| F7 F8 F9    . . . |. 1 . |. . .     3 4 6 |9 1 2 |7 5 8 
---------+---------+---------    ------+------+------    ------+------+------
 G1 G2 G3| G4 G5 G6| G7 G8 G9    . . . |6 . 3 |. 7 .     2 8 9 |6 4 3 |5 7 1 
 H1 H2 H3| H4 H5 H6| H7 H8 H9    5 . . |2 . . |. . .     5 7 3 |2 9 1 |6 8 4 
 I1 I2 I3| I4 I5 I6| I7 I8 I9    1 . 4 |. . . |. . .     1 6 4 |8 7 5 |2 9 3
{% endhighlight %}

每个方块都属于 3 个单元，有 20 个对等方块。例如，如下是方块 C2 的单元和对等方块：

{% highlight python %}
    A2   |         |                    |         |            A1 A2 A3|         |         
    B2   |         |                    |         |            B1 B2 B3|         |         
    C2   |         |            C1 C2 C3| C4 C5 C6| C7 C8 C9   C1 C2 C3|         |         
---------+---------+---------  ---------+---------+---------  ---------+---------+---------
    D2   |         |                    |         |                    |         |         
    E2   |         |                    |         |                    |         |         
    F2   |         |                    |         |                    |         |         
---------+---------+---------  ---------+---------+---------  ---------+---------+---------
    G2   |         |                    |         |                    |         |         
    H2   |         |                    |         |                    |         |         
    I2   |         |                    |         |                    |         |
{% endhighlight %}

我们可以用 Python 按如下方式来实现单元、对等方块、方块的概念：

{% highlight python %}
def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]
 
digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
squares  = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in unitlist if s in u]) 
             for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s]))
             for s in squares)
{% endhighlight %}

如果你对 Python 的一些特性不熟悉，请注意‘字典’是哈希表在Python中的叫法，它将每个键映射到一个值。dict((s, [...]) for s in squares) 创建了一个字典，把每个方块 s 映射到是一个列表的值。表达式 [u for u in unitlist if s in u] 的意思是：这个值是由那些包含s的单元u构成的列表。所以这个赋值表达式要这么读：units是一个字典，其中每个方块映射到包含它的单元组成的列表。类似地，下一个赋值语句要这么读：peers 是个字典，其中每个方块s映射到s所属单元的方块的并集，但不包括 s 自身。

做一些测试是没有坏处的（它们都通过了）：

{% highlight python %}
def test():
    "A set of unit tests."
    assert len(squares) == 81
    assert len(unitlist) == 27
    assert all(len(units[s]) == 3 for s in squares)
    assert all(len(peers[s]) == 20 for s in squares)
    assert units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                           ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
                           ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
    assert peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                               'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                               'A1', 'A3', 'B1', 'B3'])
    print 'All tests pass.'
{% endhighlight %}

既然我们有了方块、单元和对等方块，下一步是定义数独网格。事实上我们需要两个表示(representations)：首先要有一个用来指定谜题初始状态的文本格式（译注：指字符串），我们会为之保留 grid 这个名字；然后还需要谜题的任何状态（部分解决或完成）的内部表示，我们称之为 values 集合，因为对于每个方块，它将给出剩余可能的值。对于文本格式（网格），我们允许字符串中用 1-9 表示数字，0 或句点表示空方块。所有其他的字符都会被忽略（包括空格，换行，破折号）。因此以下的三个网格字符串代表了同样的谜题：

{% highlight python %}
"4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
 
"""
400000805
030000000
000700000
020000060
000080400
000010000
000603070
500200000
104000000"""
 
"""
4 . . |. . . |8 . 5 
. 3 . |. . . |. . . 
. . . |7 . . |. . . 
------+------+------
. 2 . |. . . |. 6 . 
. . . |. 8 . |4 . . 
. . . |. 1 . |. . . 
------+------+------
. . . |6 . 3 |. 7 . 
5 . . |2 . . |. . . 
1 . 4 |. . . |. . . 
"""
{% endhighlight %}

现在来说 values。有人可能认为 9×9 的数组是很显然的数据结构。但是方块的名字是 ‘A1′ 这种，而不是（0,0）。因此 values 将会是字典，以方块为键。每个键的值是那个方块的可能的数字：如果数字是作为谜题的一部分给定的，或者我们已经确定它必定的值，那么就是一个数字；如果我们还不确定，那就是一堆数字。这堆数字可以用Python集合或列表来表示，但我选择用数字字符串来表示（稍后会看到为什么）。因此，A1 为 7，C7 为空的网格 可以表示为 {‘A1′: ’7′, ‘C7′: ’123456789′, …}。

这是将网格解析成 values 字典的代码：

{% highlight python %}
def parse_grid(grid):
    
"""Convert grid to a dict of possible values, {square: digits}, or
    
return False if a contradiction is detected."""
    
## To start, every square can be any digit; then assign values from the grid.
    values = dict((s, digits) for s in squares)
    for s,d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False 
## (Fail if we can't assign d to square s.)
    return values
 
def grid_values(grid):
    "Convert grid into a dict of {square: char} with '0' or '.' for empties."
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))
{% endhighlight %}

## 约束传播

parse_grid 函数调用 assign(values, s, d)。我们可以把这实现为 values[s] = d，但我们可以做的更多。有解决数独谜题经验的人知道，在朝着填满所有方块前进时，有两个重要的策略：

> (1) 如果一个方块只有一个可能值，把这个值从方块的对等方块（的可能值）中排除。
> (2) 如果一个单元只有一个可能位置来放某个值，就把值放那。

作为策略（1）的例子，如果我们把 7 填入 A1，也就是 {‘A1′: ’7′, ‘A2′:’123456789′, …}，我们看到 A1 只有一个值，因此7可以从A1的对等方块A2（也包括其他所有对等方块）中移除，得到{‘A1′: ’7′, ‘A2′: ’12345689′, …}。作为策略（2）的例子，如果A3到A9都不能以3作为可能值，那么3必定属于A2，我们可以更新为{‘A1′: ’7′, ‘A2′:’3′, …}。对A2的更新，反过来可能导致对它的对等方块以及对等方块的对等方块的更新，等等。这个过程称为约束传播。

函数assign(values, s, d)会返回更新后的values（包括来自约束传播的更新），但是如果产生了矛盾（即赋值不能保证一致），assign会返回False。例如，如果网格是以数字’77…’开头的，当我们试图把7赋给A2时，assign会注意到A2不可能是7，因为A2为7的可能性已经被它的对等方块A1排除了。

对于一个方块来说，基本操作不是赋值，而是排除一个可能的值，我们用eliminate(values, s, d)来实现它。一旦我们有了eliminate，assign(values, s, d)就可以定义为“从s中排除d以外的所有值”。

{% highlight python %}
def assign(values, s, d):
    
"""Eliminate all the other values (except d) from values[s] and propagate.
    
Return values, except return False if a contradiction is detected."""
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False
 
def eliminate(values, s, d):
    
"""Eliminate d from values[s]; propagate when values or places <= 2.
    
Return values, except return False if a contradiction is detected."""
    if d not in values[s]:
        return values 
## Already eliminated
    values[s] = values[s].replace(d,'')
    
## (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
    if len(values[s]) == 0:
    return False 
## Contradiction: removed last value
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    
## (2) If a unit u is reduced to only one place for a value d, then put it there.
    for u in units[s]:
    dplaces = [s for s in u if d in values[s]]
    if len(dplaces) == 0:
        return False 
## Contradiction: no place for this value
    elif len(dplaces) == 1:
        
# d can only be in one place in unit; assign it there
            if not assign(values, dplaces[0], d):
                return False
    return values
{% endhighlight %}

在能走得更远之前，我们需要能显示一个谜题：

{% highlight python %}
def display(values):
    "Display these values as a 2-D grid."
    width = 1+max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print ''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols)
        if r in 'CF': print line
    print
{% endhighlight %}

现在我们准备好了。我从来自于欧拉计划[数独问题](http://projecteuler.net/index.php?section=problems&id=96)的一系列[简单谜题](http://norvig.com/easy50.txt)中挑出了第一个例子：

{% highlight python %}
>>> grid1 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
 
>>> display(parse_grid(grid1))
4 8 3 |9 2 1 |6 5 7
9 6 7 |3 4 5 |8 2 1
2 5 1 |8 7 6 |4 9 3
------+------+------
5 4 8 |1 3 2 |9 7 6
7 2 9 |5 6 4 |1 3 8
1 3 6 |7 9 8 |2 4 5
------+------+------
3 7 2 |6 8 9 |5 1 4
8 1 4 |2 5 3 |7 6 9
6 9 5 |4 1 7 |3 8 2
{% endhighlight %}

在这个例子中，谜题完全是靠生搬硬套策略（1）和（2）解决的。不幸的是，这并不总能行得通。这是一系列[困难谜题](http://magictour.free.fr/top95)中的第一个例子：

{% highlight python %}
>>> grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
 
>>> display(parse_grid(grid2))
   4      1679   12679  |  139     2369    269   |   8      1239     5   
 26789     3    1256789 | 14589   24569   245689 | 12679    1249   124679
  2689   15689   125689 |   7     234569  245689 | 12369   12349   123469
------------------------+------------------------+------------------------
  3789     2     15789  |  3459   34579    4579  | 13579     6     13789 
  3679   15679   15679  |  359      8     25679  |   4     12359   12379 
 36789     4     56789  |  359      1     25679  | 23579   23589   23789 
------------------------+------------------------+------------------------
  289      89     289   |   6      459      3    |  1259     7     12489 
   5      6789     3    |   2      479      1    |   69     489     4689 
   1      6789     4    |  589     579     5789  | 23569   23589   23689
{% endhighlight %}

在这个例子中，我们离解决谜题还差得远呢！有61个方块还不确定。接下来要怎么做？我们可以编码[更复杂的策略](http://www.sudokudragon.com/sudokustrategy.htm)。例如，naked twins策略寻找同一单元的两个方块，它们有着相同的两个可能数字。给定{‘A5′: ’26′, ‘A6′:’26′, …}，我们可以断定2和6必定在A5和A6中（尽管我们不知道分别在哪个方块），因此对于A行单元的其他方块，我们可以排除2和6。我们在eliminate中加上elif len(values[s]) == 2测试来实现这条策略。

像这样编码策略是一条可能的路线，但会需要几百行代码（有几十条这样的策略），我们也不确定能否解决每个谜题。

## 搜索

另一条路线是搜索一个解答：系统地尝试所有可能性直到找到一个解。这个方法的代码只有十几行，但是我们冒着另一个风险：程序可能要运行很长时间。考虑上面的grid2，A2有4种可能性（1679)），A3有5种可能性（12679）。总共就是20种可能性，如果我们一直[乘下去](http://www.google.com/search?hl=en&q=4*5*3*4*3*4*5*7*5*5*6*5*4*6*4*5*6*6*6*5*5*6*4*5*4*5*4*5*5*4*5*5*3*5*5*5*5*5*3*5*5*5*5*3*2*3*3*4*5*4*3*2*3*4*4*3*3*4*5*5*5)，对于整个谜题是 4.62838344192 × 1038 种可能性。我们要怎么应对？有两个选择。

首先，我们可以尝试暴力方法。假设我们有一个非常高效的程序，计算一个位置只需一条指令；我们可以利用下一代的计算技术，比方说1024核的10GHz处理器，假设我们可以用上一百万这样的处理器；再假设我们购物时选了一个时光机，可以回退130亿年到宇宙的起点，开始运行我们的程序。我们可以[算出](http://www.google.com/search?&q=10+GHz+*+1024+*+1+million+*+13+billion+years+%2F+4.6e38+in+percent)至今我们差不多完成了这个谜题的1%。

第二个选择是每条机器指令处理远多于一种可能性。这看起来不可能，但幸运的是这恰好就是约束传播所做的。我们不需要尝试所有4 × 1038种可能性，因为尝试一种后，我们立即就能排除很多其他的可能性。例如，这个谜题的方块H7有两种可能性，6和9。我们可以尝试9，很快就发现有矛盾。这意味着我们排除的不是一种可能性，而是4 × 1038种选择中的一半。

事实上，要解决这个特定的谜题我们只要考虑25种可能性，61个未填充的方块中我们只需显式地搜索9个，约束传播会帮我们搞定剩下的。对于清单中的95个[困难谜题](http://magictour.free.fr/top95)，平均起来每个谜题只要考虑64种可能性，在所有谜题中都不需要搜索超过16个方块。

这个搜索算法是什么呢？很简单：首先确保我们还没有发现解或者矛盾，选择一个未填充的方块，考虑它的所有可能值。每次考虑一个值，尝试把它赋给方块，从得到的局面继续搜索。换言之，我们搜索这样的值d：我们可以从将d赋给方块s后的局面成功地搜索到一个解。如果搜索导致失败的局面，返回并考虑d的另一个值。这是一个递归的搜索，我们称之为[深度优先搜索](http://en.wikipedia.org/wiki/Depth-first_search)，因为在考虑s取另一不同值之前，我们（递归地）考虑values[s] = d条件下的所有可能性。

为了避免记录的复杂，每次递归调用search我们都创建values的新的拷贝。这样，搜索树的每个分支都是独立的，不会与另一个分支混淆。（这就是为什么将方块的可能值集合实现为字符串：我可以用values.copy()来拷贝values，简单又高效。如果我用Python集合或列表来实现可能值，我就要用copy.deepcopy(values)，就没那么高效了。）另一种方法是记录每次对values的改动，走进死胡同时撤销改动。这就是所谓的[回溯搜索](http://en.wikipedia.org/wiki/Backtracking_search)。当搜索中的每一步只对大的数据结构做单个改动时，这是可行的。但当每次赋值会通过约束传播导致很多其他的改动时，这么做很复杂。

当我们实现搜索时要做两个选择：变量顺序（先尝试哪个方块？）和值顺序（对于当前方块先尝试哪个数字？）。对于变量顺序，我们用一种称为最小剩余值的常见启发方法，也就是说选择可能值数目最少的方块（或之一）。为什么这么做？考虑上面的grid2。假设我们先选择B3。它有7种可能值（1256789），因此我们猜错的期望是6/7。如果我们选择G2，它只有2种可能值，我们猜错的期望只有1/2。因此我们选择有最少可能值、猜对概率最高的方块。对于值顺序，我们不会做什么特别的事情，只是按数字大小顺序来考虑。

现在我们已经准备好用search函数来定义solve函数了：

{% highlight python %}
def solve(grid): return search(parse_grid(grid))
 
def search(values):
    "Using depth-first search and propagation, try all possible values."
    if values is False:
        return False 
## Failed earlier
    if all(len(values[s]) == 1 for s in squares): 
        return values 
## Solved!
    
## Chose the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) 
        for d in values[s])
 
def some(seq):
    "Return some element of seq that is true."
    for e in seq:
        if e: return e
    return False
{% endhighlight %}

就这样，我们搞定了。只用了一页代码，现在我们可以解决任何数独谜题了。

## 结果

你可以查看[完整程序](http://norvig.com/sudopy.shtml)。下面是在命令行运行程序的输出。它解决了来自文件的[50个简单谜题](http://projecteuler.net/project/sudoku.txt)和[95个困难谜题](http://norvig.com/top95.txt)（请看[95个谜题解答](http://norvig.com/top95solutions.html)），我通过搜索[最难的数独](http://www.google.com/search?q=hardest+sudoku)找到的[11个谜题](http://norvig.com/hardest.txt)，以及一批随机谜题：

{% highlight python %}
% python sudo.py
All tests pass.
Solved 50 of 50 easy puzzles (avg 0.01 secs (86 Hz), max 0.03 secs).
Solved 95 of 95 hard puzzles (avg 0.04 secs (24 Hz), max 0.18 secs).
Solved 11 of 11 hardest puzzles (avg 0.01 secs (71 Hz), max 0.02 secs).
Solved 99 of 99 random puzzles (avg 0.01 secs (85 Hz), max 0.02 secs).
{% endhighlight %}

## 分析

上面的每个谜题都用不到五分之一秒解决。真正困难的谜题会怎么样呢？芬兰数学家Arto Inkala把他的[2006 puzzle](http://www.usatoday.com/news/offbeat/2006-11-06-sudoku_x.htm)描述为“目前已知最难的数独”，把[2010 puzzle](http://www.mirror.co.uk/fun-games/sudoku/2010/08/19/world-s-hardest-sudoku-can-you-solve-dr-arto-inkala-s-puzzle-115875-22496946/)描述为“我创作过的最难数独”。我的程序都在0.01秒内解决了它们（solve_all将会在下面定义）：

{% highlight python %}
>>> solve_all(from_file("hardest.txt")[0:2], 'Inkala')
8 5 . |. . 2 |4 . . 
7 2 . |. . . |. . 9
. . 4 |. . . |. . . 
------+------+------
. . . |1 . 7 |. . 2
3 . 5 |. . . |9 . . 
. 4 . |. . . |. . . 
------+------+------
. . . |. 8 . |. 7 . 
. 1 7 |. . . |. . . 
. . . |. 3 6 |. 4 . 
 
8 5 9 |6 1 2 |4 3 7
7 2 3 |8 5 4 |1 6 9
1 6 4 |3 7 9 |5 2 8
------+------+------
9 8 6 |1 4 7 |3 5 2
3 7 5 |2 6 8 |9 1 4
2 4 1 |5 9 3 |7 8 6
------+------+------
4 3 2 |9 8 1 |6 7 5
6 1 7 |4 2 5 |8 9 3
5 9 8 |7 3 6 |2 4 1
 
(0.01 seconds)
 
. . 5 |3 . . |. . . 
8 . . |. . . |. 2 . 
. 7 . |. 1 . |5 . . 
------+------+------
4 . . |. . 5 |3 . . 
. 1 . |. 7 . |. . 6
. . 3 |2 . . |. 8 . 
------+------+------
. 6 . |5 . . |. . 9
. . 4 |. . . |. 3 . 
. . . |. . 9 |7 . . 
 
1 4 5 |3 2 7 |6 9 8
8 3 9 |6 5 4 |1 2 7
6 7 2 |9 1 8 |5 4 3
------+------+------
4 9 6 |1 8 5 |3 7 2
2 1 8 |4 7 3 |9 5 6
7 5 3 |2 9 6 |4 8 1
------+------+------
3 6 7 |5 4 2 |8 1 9
9 8 4 |7 6 1 |2 3 5
5 2 1 |8 3 9 |7 6 4
 
(0.01 seconds)
 
Solved 2 of 2 Inkala puzzles (avg 0.01 secs (99 Hz), max 0.01 secs).
{% endhighlight %}

我猜如果我想要一个真正困难的谜题，我得自己来制作。我不知道怎么创作困难的谜题，因此我生成了一百万个随机谜题。我用来生成随机谜题的算法很简单：首先，随机打乱方块的顺序。考虑到可能的数字选择，挨个在每个方块中填入随机数字。如果出现了矛盾，就重新来过。如果填充了至少17个方块以及8种不同的数字，就结束这个过程。（注意：如果填充少于17个方块或者用了不到8种不同数字，数独会有多个解。感谢Olivier Grégoire关于8种不同数字的很好的建议。)即使有这些检查，我的随机谜题仍不能保证有唯一解。很多有多个解，还有一些（大约0.2%）没有解。出现在书报上的谜题总是有唯一解。

{% highlight python %}
0.032%    (1 in 3,000)    took more than 0.1 seconds
0.014%    (1 in 7,000)    took more than 1 second
0.003%    (1 in 30,000)    took more than 10 seconds
0.0001%    (1 in 1,000,000)    took more than 100 seconds
{% endhighlight %}

解决一个随机谜题平均用时为0.01秒，超过99.95%用了不到0.1秒，但有一些用时长得多：

{% highlight python %}
0.032%    (1 in 3,000)    超过0.1秒
0.014%    (1 in 7,000)    超过1秒
0.003%    (1 in 30,000)    超过10秒
0.0001%    (1 in 1,000,000)    超过100秒
{% endhighlight %}

这里是100万个谜题中用时超过1秒的139个，排好序了，分别用线性和对数坐标表示：

<figure>
    <img src="http://ww4.sinaimg.cn/mw690/6941baebjw1etd2qmbqbyg20n10k2jrh.gif" alt="">
</figure>

很难从图中做出结论。最后几个值的上涨是显著的吗？如果我生成一千万个谜题，会不会有一个用时超过1000秒？下面是一百万个随机谜题中最难的（对于我的程序来说）：

{% highlight python %}
>>> hard1  = '.....6....59.....82....8....45........3........6..3.54...325..6..................'
>>> solve_all([hard1])
. . . |. . 6 |. . . 
. 5 9 |. . . |. . 8
2 . . |. . 8 |. . . 
------+------+------
. 4 5 |. . . |. . . 
. . 3 |. . . |. . . 
. . 6 |. . 3 |. 5 4
------+------+------
. . . |3 2 5 |. . 6
. . . |. . . |. . . 
. . . |. . . |. . . 
 
4 3 8 |7 9 6 |2 1 5
6 5 9 |1 3 2 |4 7 8
2 7 1 |4 5 8 |6 9 3
------+------+------
8 4 5 |2 1 9 |3 6 7
7 1 3 |5 6 4 |8 2 9
9 2 6 |8 7 3 |1 5 4
------+------+------
1 9 4 |3 2 5 |7 8 6
3 6 2 |9 8 7 |5 4 1
5 8 7 |6 4 1 |9 3 2
 
(188.79 seconds)
{% endhighlight %}

不幸的是，这不是一个真正的数独谜题，因为它有多个解。（它是在我包含了Olivier Grégoire关于8种不同数字的建议之前生成的，因此对于这个谜题的任何解，交换1和7，都得到另一个解。）但这是一个本质上很难的谜题吗？或者它的困难性是我的search程序所使用的变量顺序和值顺序方案的产物？为了检验，我随机化了值顺序（我把search最后一行中的for d in values[s]改成for d in shuffled(values[s])，我用了random.shuffle来实现shuffled）。结果明显地两边倒：30次尝试中的27次用了不到0.02秒，其他的3次每次用时都超过190秒（大约长了10000倍）。这个谜题有多个解，随机化的search找到13个不同的解。我的猜测是在搜索早期的某处，有一系列的方块（可能2个），如果我们选则了某种错误的值的组合来填充方块，就需要大约190秒来发现矛盾。但如果做了其他选择，我们很快要么发现一个解，要么发现矛盾，从另一个选择前进。因此算法的速度取决于它是否能避免选中致命的值组合。

随机化大部分时候都是有效的（30次中的27次），但通过考虑更好的值顺序我们可能会做的更好（一个流行的启发方式是最少约束值，也就是先选对对等方块约束最少的值），或者尝试更智能的变量顺序。

在我能给出对困难谜题一个好的刻画前，还需要更多的实验。我决定在另一个一百万随机谜题上做实验，这次保留运行时间的平均值，50th（中位数），90和99分位数，最大值和标准差这些统计值。结果是相似的，除了这次有两个谜题用时超过100秒，还有一个长得多：1439秒。事实上这个谜题是那没有解的0.2%中的一个，因此它可能不算。但主要的信息是即使我们抽样更多，平均值和中位数差不多保持不变，但最大值引人注目地保持增长。标准差也有微升，但主要是由于99分位数之外的那些很少的长用时。这是重尾分布，而不是正态分布。

为了比较，下面左边的表给出了解决谜题用时的统计，右边的表给出了从平均值为0.014，标准差为1.4794的正态（高斯）分布抽样的统计。注意对于一百万的抽样，高斯分布的最大值是平均值之上5个标准差（大致就是你对高斯分布所期望的），然而最长谜题运行时间在平均值之上1000个标准差。

<figure>
    <img src="http://ww3.sinaimg.cn/mw690/6941baebjw1etd2qmsnq0j20st08zjw9.jpg" alt="">
</figure>

这里是用时1439秒的无解谜题：

{% highlight python %}
. . . |. . 5 |. 8 . 
. . . |6 . 1 |. 4 3 
. . . |. . . |. . . 
------+------+------
. 1 . |5 . . |. . . 
. . . |1 . 6 |. . . 
3 . . |. . . |. . 5 
------+------+------
5 3 . |. . . |. 6 1 
. . . |. . . |. . 4 
. . . |. . . |. . .
{% endhighlight %}

下面是定义solve_all的以及用它来验证来自文件和随机谜题的代码：

{% highlight python %}
import time, random
 
def solve_all(grids, name='', showif=0.0):
    
"""Attempt to solve a sequence of grids. Report results.
    
When showif is a number of seconds, display puzzles that take longer.
    
When showif is None, don't display any puzzles."""
    def time_solve(grid):
        start = time.clock()
        values = solve(grid)
        t = time.clock()-start
        
## Display puzzles that take long enough
        if showif is not None and t > showif:
            display(grid_values(grid))
            if values: display(values)
            print '(%.2f seconds)n' % t
        return (t, solved(values))
    times, results = zip(*[time_solve(grid) for grid in grids])
    N = len(grids)
    if N > 1:
        print "Solved %d of %d %s puzzles (avg %.2f secs (%d Hz), max %.2f secs)." % (
            sum(results), N, name, sum(times)/N, N/sum(times), max(times))
 
def solved(values):
    "A puzzle is solved if each unit is a permutation of the digits 1 to 9."
    def unitsolved(unit): return set(values[s] for s in unit) == set(digits)
    return values is not False and all(unitsolved(unit) for unit in unitlist)
 
def from_file(filename, sep='n'):
    "Parse a file into a list of strings, separated by sep."
    return file(filename).read().strip().split(sep)
 
def random_puzzle(N=17):
    
"""Make a random puzzle with N or more assignments. Restart on contradictions.
    
Note the resulting puzzle is not guaranteed to be solvable, but empirically
    
about 99.8% of them are solvable. Some have multiple solutions."""
    values = dict((s, digits) for s in squares)
    for s in shuffled(squares):
        if not assign(values, s, random.choice(values[s])):
            break
        ds = [values[s] for s in squares if len(values[s]) == 1]
        if len(ds) >= N and len(set(ds)) >= 8:
            return ''.join(values[s] if len(values[s])==1 else '.' for s in squares)
    return random_puzzle(N) 
## Give up and make a new puzzle
 
def shuffled(seq):
    "Return a randomly shuffled copy of the input sequence."
    seq = list(seq)
    random.shuffle(seq)
    return seq
 
grid1  = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
grid2  = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
hard1  = '.....6....59.....82....8....45........3........6..3.54...325..6..................'
 
if __name__ == '__main__':
    test()
    solve_all(from_file("easy50.txt", '========'), "easy", None)
    solve_all(from_file("top95.txt"), "hard", None)
    solve_all(from_file("hardest.txt"), "hardest", None)
    solve_all([random_puzzle() for _ in range(99)], "random", 100.0)
{% endhighlight %}

## 为什么？

我为什么要做这个？如计算机安全专家[Ben Laurie](http://en.wikipedia.org/wiki/Ben_Laurie)说的，数独是“对人的理智的拒绝服务攻击”（译注：指数独容易让人上瘾）。我所知道的几个人（包括我的妻子）都被这个病毒感染了，我想这篇文章可以证明他们不用再在数独上花时间了。这对于我的朋友没起作用（尽管我的妻子自此之后不靠我的帮助独立改掉了这个嗜好），但至少有一位陌生人写到这篇文章对他有用，因此我使得世界更多产了。也许沿途我还教了点关于Python，约束传播和搜索的东西。