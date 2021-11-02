## **一、JVM内存结构** 

![img](https://pic2.zhimg.com/80/v2-267e596297bfe4964e97e72b76588b79_720w.jpg)



由上图可以清楚的看到**JVM的内存空间分为3大部分：**

1. **堆内存**
2. **方法区**
3. **栈内存**

其中**栈内存**可以再细分为**java虚拟机栈和本地方法栈,堆内存可以划分为新生代和老年代,**新生代中还可以再次划分为Eden区、From Survivor区和To Survivor区。

其中一部分是线程共享的，包括 Java 堆和方法区；另一部分是线程私有的，包括虚拟机栈和本地方法栈，以及程序计数器这一小部分内存。

问题：String s = new String("xyz");创建了几个String Object? 二者之间有什么区别？

两个或一个，”xyz”对应一个对象，这个对象放在字符串常量缓冲区，常量”xyz”不管出现多少遍，都是缓冲区中的那一个。New
String每写一遍，就创建一个新的对象，它一句那个常量”xyz”对象的内容来创建出一个新String对象。如果以前就用过’xyz’，这句代表就不会创建”xyz”自己了，直接从缓冲区拿。



内存存在情况：S-栈上  xyz-方法区  对象-堆上



## 堆内存（Heap）

java 堆（Java Heap）是Java 虚拟机所管理的内存中最大的一块。堆是被所有线程共享的区域，实在虚拟机启动时创建的。堆里面存放的都是对象的实例（new 出来的对象都存在堆中）。

**此内存区域的唯一目的就是存放对象实例（new的对象），几乎所有的对象实例都在这里分配内存。**



堆内存分为两个部分：**年轻代和老年代**。我们平常所说的垃圾回收，主要回收的就是堆区。更细一点划分新生代又可划分为Eden区和2个Survivor区（From Survivor和To Survivor）。

下图中的Perm代表的是永久代，但是注意永久代并不属于堆内存中的一部分，同时jdk1.8之后永久代已经被移除。



![img](https://pic3.zhimg.com/80/v2-f664c6aa75d6358acff54dd67d075b86_720w.jpg)



新生代 ( Young ) 与老年代 ( Old ) 的比例的值为 1:2 ( 该值可以通过参数 –XX:NewRatio 来指定 )

默认的，Eden : from : to = 8 : 1 : 1 ( 可以通过参数 –XX:SurvivorRatio 来设定 )，即： Eden = 8/10 的新生代空间大小，from = to = 1/10 的新生代空间大小。

## **方法区（Method Area）** 

方法区也称”**永久代**“，它用于**存储虚拟机加载的类信息、常量、静态变量**、是各个**线程共享的内存区域**。

在JDK8之前的HotSpot JVM，存放这些”永久的”的区域叫做“永久代(permanent generation)”。永久代是一片连续的堆空间，在JVM启动之前通过在命令行设置参数-XX:MaxPermSize来设定永久代最大可分配的内存空间，**默认大小是64M**（64位JVM默认是85M）。

随着JDK8的到来，JVM不再有 **永久代(PermGen)**。但类的元数据信息（metadata）还在，只不过不再是存储在连续的堆空间上，而是移动到叫做“Metaspace”的本地内存（Native memory。

**方法区或永生代相关设置**

- -XX:PermSize=64MB 最小尺寸，初始分配
- -XX:MaxPermSize=256MB 最大允许分配尺寸，按需分配
- XX:+CMSClassUnloadingEnabled -XX:+CMSPermGenSweepingEnabled 设置垃圾不回收
- 默认大小
- -server选项下默认MaxPermSize为64m
- -client选项下默认MaxPermSize为32m



## **虚拟机栈(JVM Stack)** 

java虚拟机栈是**线程私有**，生命周期与线程相同。创建线程的时候就会创建一个java虚拟机栈。

虚拟机执行java程序的时候，每个方法都会创建一个栈帧，栈帧存放在java虚拟机栈中，通过压栈出栈的方式进行方法调用。



栈帧又分为一下几个区域：**局部变量表、操作数栈、动态连接、方法出口**等。
平时我们所说的变量存在栈中，这句话说的不太严谨，应该说局部变量存放在java虚拟机栈的局部变量表中。
java的8中基本类型的局部变量的值存放在虚拟机栈的局部变量表中，如果是引用型的变量，则只存储对象的引用地址。



## **本地方法栈(Native Stack)** 

本地方法栈（Native Method Stacks）与虚拟机栈所发挥的作用是非常相似的，其区别不过是虚拟机栈为虚拟机执行Java方法（也就是字节码）服务，而**本地方法栈则是为虚拟机使用到的Native方法服务。**



## **程序计数器（PC Register）** 

程序计数器就是记录当前线程执行程序的位置，改变计数器的值来确定执行的下一条指令，比如循环、分支、方法跳转、异常处理，线程恢复都是依赖程序计数器来完成。
Java虚拟机多线程是通过线程轮流切换并分配处理器执行时间的方式实现的。为了线程切换能恢复到正确的位置，每条线程都需要一个独立的程序计数器，所以它是**线程私有**的。





## 直接内存 

直接内存并不是虚拟机内存的一部分，也不是Java虚拟机规范中定义的内存区域。jdk1.4中新加入的NIO，引入了通道与缓冲区的IO方式，它可以调用Native方法直接分配堆外内存，这个堆外内存就是本机内存，不会影响到堆内存的大小。



## **二、JVM内存参数设置** 

![img](https://pic1.zhimg.com/80/v2-376aad413889f372db4dfbca4f2f9504_720w.jpg)



- -Xms设置堆的最小空间大小。
- -Xmx设置堆的最大空间大小。
- -Xmn:设置年轻代大小
- -XX:NewSize设置新生代最小空间大小。
- -XX:MaxNewSize设置新生代最大空间大小。
- -XX:PermSize设置永久代最小空间大小。
- -XX:MaxPermSize设置永久代最大空间大小。
- -Xss设置每个线程的堆栈大小
- -XX:+UseParallelGC:选择垃圾收集器为并行收集器。此配置仅对年轻代有效。即上述配置下,年轻代使用并发收集,而年老代仍旧使用串行收集。
- -XX:ParallelGCThreads=20:配置并行收集器的线程数,即:同时多少个线程一起进行垃圾回收。此值最好配置与处理器数目相等。

## **典型JVM参数配置参考:** 

- java-Xmx3550m-Xms3550m-Xmn2g-Xss128k
- -XX:ParallelGCThreads=20
- -XX:+UseConcMarkSweepGC-XX:+UseParNewGC

-Xmx3550m:设置JVM最大可用内存为3550M。

-Xms3550m:设置JVM促使内存为3550m。此值可以设置与-Xmx相同,以避免每次垃圾回收完成后JVM重新分配内存。

> 注意：在通常情况下，服务器项目在运行过程中，堆空间会不断的收缩与扩张，势必会造成不必要的系统压力。
> 所以在生产环境中， `JVM`的 `Xms`和 `Xmx`要设置成一样的，能够避免 `GC`在调整堆大小带来的不必要的压力。

-Xmn2g:设置年轻代大小为2G。整个堆大小=年轻代大小+年老代大小+持久代大小。持久代一般固定大小为64m,所以增大年轻代后,将会减小年老代大小。此值对系统性能影响较大,官方推荐配置为整个堆的3/8。

-Xss128k:设置每个线程的堆栈大小。JDK5.0以后每个线程堆栈大小为1M,以前每个线程堆栈大小为256K。更具应用的线程所需内存大小进行调整。在相同物理内存下,减小这个值能生成更多的线程。但是操作系统对一个进程内的线程数还是有限制的,不能无限生成,经验值在3000~5000左右。



## 三、JVM面试题

什么是 `JVM`?

- `JVM` 是一台虚拟计算机, `JVM` 是运行在操作系统之上的, 没有和硬件直接交互, 不同的操作系统有不同的虚拟机, 它类似一个小而高效的 `CPU`, 它包括字节码指令、寄存器、栈、堆、垃圾回收器和一个存储方法域的地方

为什么 `Java` 能够跨平台?

- `Java` 源文件通过编译器产生相应的字节码 `【.class】` 文件, 字节码文件通过 `JVM` 中的解释器, 编译成特定机器上的机器码, 每一种平台上的解释器都是不同的, 这就是为什么 Java 能够跨平台的原因

![img](https://img-blog.csdnimg.cn/20200306081411686.png#pic_center)

### 类加载机制

```
JVM` 的类加载机制分为了五个部分 `加载、验证、准备、解析、初始化、使用和卸载
```

![img](https://img-blog.csdnimg.cn/20200306065837919.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zODI1MTg3MQ==,size_16,color_FFFFFF,t_70#pic_center)

​	

```python
加载
在内存中生成一个代表这个类的 Class 对象, 作为方法区这个类的各种数据的入口

验证
确保 Class 文件中的字节流中包含的信息是否符合当前虚拟机的要求, 并且不会对 JVM 产生危害

准备
正式为类变量分配内存并设置类变量初始值阶段, 在方法区中分配这些变量的内存空间, 比如 public static String MSG = "Hello World", 在这个阶段的初始赋值为 null, 是在解析阶段才把值赋给 MSG 变量, 但是如果你声明为 final 类型的变量, 那么在这个阶段 JVM 就会根据 ConstantValue 属性将值赋给 MSG 变量

解析
JVM 将常量池中的 符号引用 替换为 直接引用
符号引用 : 其引用的目标并不一定要已经加装到内存中, 而是各种虚拟机实现的内存布局可以各不相同, 但是他们所接受的符号引用必须是相同的, 因为符号引用的字面量形式明确定义在 JVM 规范的 Class 文件格式中
直接引用 : 是指向目标的指针、相对偏移量、一个能间接定位到目标的句柄, 如果有直接引用, 那引用的目标已经确定在内存中存在
    
初始化
开始执行类中定义的 Java 程序代码, 是执行类的构造方法的过程, 构造方法是由编译器自动收集类中的类变量的赋值操作和静态语句块中的语句合并而成的, 虚拟机会保证子类的构造方法执行之前, 父类的构造方法已经执行完毕, 当一个没有对静态变量赋值也没有静态代码块, 那么编译器可以不为这个类生成构造方法
不会执行类初始化的情况 :
通过子类引用父类的静态字段, 只会触发父类的初始化
定义对象数组, 不会触发该类的初始化
常量在编译期间会存入调用类的常量池中, 本质上并没有直接引用定义常量的类, 不会触发定义常量所在的类
通过类名获取 Class 对象
通过反射 Class.forName(String class) 加载指定类的时候, 当设置指定的参数 initialize = false 的情况下
通过类加载器的 loadClass() 加载
 
```







前言
总结了JVM一些经典面试题，分享出我自己的解题思路，希望对大家有帮助，有哪里你觉得不正确的话，欢迎指出，后续有空会更新。

#### 1.什么情况下会发生栈内存溢出。

思路： 描述栈定义，再描述为什么会溢出，再说明一下相关配置参数，OK的话可以给面试官手写是一个栈溢出的demo。

我的答案：

栈是线程私有的，他的生命周期与线程相同，每个方法在执行的时候都会创建一个栈帧，用来存储局部变量表，操作数栈，动态链接，方法出口等信息。局部变量表又包含基本数据类型，对象引用类型如果线程请求的栈深度大于虚拟机所允许的最大深度，将抛出StackOverflowError异常，方法递归调用产生这种结果。

如果Java虚拟机栈可以动态扩展，并且扩展的动作已经尝试过，但是无法申请到足够的内存去完成扩展，或者在新建立线程的时候没有足够的内存去创建对应的虚拟机栈，那么Java虚拟机将抛出一个OutOfMemory 异常。(线程启动过多)

参数 -Xss 去调整JVM栈的大小

#### 2.详解JVM内存模型

思路： 给面试官画一下JVM内存模型图，并描述每个模块的定义，作用，以及可能会存在的问题，如栈溢出等。

我的答案：

JVM内存结构

![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAxOS83LzIyLzE2YzFhNDI2ZWQ5YWI0OGI_aW1hZ2VWaWV3Mi8wL3cvMTI4MC9oLzk2MC9mb3JtYXQvd2VicC9pZ25vcmUtZXJyb3IvMQ?x-oss-process=image/format,png)



**程序计数器**：当前线程所执行的字节码的行号指示器，用于记录正在执行的虚拟机字节指令地址，线程私有。

**Java虚拟栈**：存放基本数据类型、对象的引用、方法出口等，线程私有。

**Native方法栈**：和虚拟栈相似，只不过它服务于Native方法，线程私有。

**Java堆**：java内存最大的一块，所有对象实例、数组都存放在java堆，GC回收的地方，线程共享。

**方法区**：存放已被加载的类信息、常量、静态变量、即时编译器编译后的代码数据等。（即永久带），回收目标主要是常量池的回收和类型的卸载，各线程共享

#### 3.JVM内存为什么要分成新生代，老年代，持久代。新生代中为什么要分为Eden和Survivor。

![img](https://pic2.zhimg.com/80/v2-267e596297bfe4964e97e72b76588b79_720w.jpg)

思路： 先讲一下JAVA堆，新生代的划分，再谈谈它们之间的转化，相互之间一些参数的配置（如： –XX:NewRatio，–XX:SurvivorRatio等），再解释为什么要这样划分，最好加一点自己的理解。

我的答案：

##### 1）共享内存区划分

共享内存区 = 持久带 + 堆
持久带 = 方法区 + 其他
Java堆 = 老年代 + 新生代
新生代 = Eden + S0 + S1

##### 2）一些参数的配置

默认的，新生代 ( Young ) 与老年代 ( Old ) 的比例的值为 1:2 ，可以通过参数 –XX:NewRatio 配置。
默认的，Edem : from : to = 8 : 1 : 1 ( 可以通过参数 –XX:SurvivorRatio 来设定)
Survivor区中的对象被复制次数为15(对应虚拟机参数 -XX:+MaxTenuringThreshold)

#### 3)为什么要分为Eden和Survivor?为什么要设置两个Survivor区？

如果没有Survivor，Eden区每进行一次Minor GC，存活的对象就会被送到老年代。老年代很快被填满，触发Major GC.老年代的内存空间远大于新生代，进行一次Full GC消耗的时间比Minor GC长得多,所以需要分为Eden和Survivor。
Survivor的存在意义，就是减少被送到老年代的对象，进而减少Full GC的发生，Survivor的预筛选保证，只有经历16次Minor GC还能在新生代中存活的对象，才会被送到老年代。
设置两个Survivor区最大的好处就是解决了碎片化，刚刚新建的对象在Eden中，经历一次Minor GC，Eden中的存活对象就会被移动到第一块survivor space S0，Eden被清空；等Eden区再满了，就再触发一次Minor GC，Eden和S0中的存活对象又会被复制送入第二块survivor space S1（这个过程非常重要，因为这种复制算法保证了S1中来自S0和Eden两部分的存活对象占用连续的内存空间，避免了碎片化的发生）

#### 4.JVM中一次完整的GC流程是怎样的，对象如何晋升到老年代

思路： 先描述一下Java堆内存划分，再解释Minor GC，Major GC，full GC，描述它们之间转化流程。

我的答案：

Java堆 = 老年代 + 新生代
新生代 = Eden + S0 + S1
当 Eden 区的空间满了， Java虚拟机会触发一次 Minor GC，以收集新生代的垃圾，存活下来的对象，则会转移到 Survivor区。

大对象（需要大量连续内存空间的Java对象，如那种很长的字符串）直接进入老年态；
如果对象在Eden出生，并经过第一次Minor GC后仍然存活，并且被Survivor容纳的话，年龄设为1，每熬过一次Minor GC，年龄+1，若年龄超过一定限制（15），则被晋升到老年态。即长期存活的对象进入老年态。
老年代满了而无法容纳更多的对象，Minor GC 之后通常就会进行Full GC，Full GC 清理整个内存堆 – 包括年轻代和年老代。
Major GC 发生在老年代的GC，清理老年区，经常会伴随至少一次Minor GC，比Minor GC慢10倍以上。

#### 5.你知道哪几种垃圾收集器，各自的优缺点，重点讲下cms和G1，包括原理，流程，优缺点。

思路： 一定要记住典型的垃圾收集器，尤其cms和G1，它们的原理与区别，涉及的垃圾回收算法。

我的答案：

1）几种垃圾收集器：

Serial收集器： 单线程的收集器，收集垃圾时，必须stop the world，使用复制算法。
ParNew收集器： Serial收集器的多线程版本，也需要stop the world，复制算法。
Parallel Scavenge收集器： 新生代收集器，复制算法的收集器，并发的多线程收集器，目标是达到一个可控的吞吐量。如果虚拟机总共运行100分钟，其中垃圾花掉1分钟，吞吐量就是99%。
Serial Old收集器： 是Serial收集器的老年代版本，单线程收集器，使用标记整理算法。
Parallel Old收集器： 是Parallel Scavenge收集器的老年代版本，使用多线程，标记-整理算法。
CMS(Concurrent Mark Sweep) 收集器： 是一种以获得最短回收停顿时间为目标的收集器，标记清除算法，运作过程：初始标记，并发标记，重新标记，并发清除，收集结束会产生大量空间碎片。
G1收集器： 标记整理算法实现，运作流程主要包括以下：初始标记，并发标记，最终标记，筛选标记。不会产生空间碎片，可以精确地控制停顿。
2）CMS收集器和G1收集器的区别：

CMS收集器是老年代的收集器，可以配合新生代的Serial和ParNew收集器一起使用；
G1收集器收集范围是老年代和新生代，不需要结合其他收集器使用；
CMS收集器以最小的停顿时间为目标的收集器；
G1收集器可预测垃圾回收的停顿时间
CMS收集器是使用“标记-清除”算法进行的垃圾回收，容易产生内存碎片
G1收集器使用的是“标记-整理”算法，进行了空间整合，降低了内存空间碎片。

#### 6.JVM内存模型的相关知识了解多少，比如重排序，内存屏障，happen-before，主内存，工作内存。

思路： 先画出Java内存模型图，结合例子volatile ，说明什么是重排序，内存屏障，最好能给面试官写以下demo说明。

我的答案：

1）Java内存模型图：

![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAxOS83LzIzLzE2YzFjMTk4MmUzNjA5YjE_aW1hZ2VWaWV3Mi8wL3cvMTI4MC9oLzk2MC9mb3JtYXQvd2VicC9pZ25vcmUtZXJyb3IvMQ?x-oss-process=image/format,png)



Java内存模型规定了所有的变量都存储在主内存中，每条线程还有自己的工作内存，线程的工作内存中保存了该线程中是用到的变量的主内存副本拷贝，线程对变量的所有操作都必须在工作内存中进行，而不能直接读写主内存。不同的线程之间也无法直接访问对方工作内存中的变量，线程间变量的传递均需要自己的工作内存和主存之间进行数据同步进行。

2）指令重排序。

在这里，先看一段代码  

```java
public class PossibleReordering {
static int x = 0, y = 0;
static int a = 0, b = 0;
 
public static void main(String[] args) throws InterruptedException {
    Thread one = new Thread(new Runnable() {
        public void run() {
            a = 1;
            x = b;
        }
    });
 
    Thread other = new Thread(new Runnable() {
        public void run() {
            b = 1;
            y = a;
        }
    });
    one.start();other.start();
    one.join();other.join();
    System.out.println(“(” + x + “,” + y + “)”);
}
```



运行结果可能为(1,0)、(0,1)或(1,1)，也可能是(0,0)。因为，在实际运行时，代码指令可能并不是严格按照代码语句顺序执行的。大多数现代微处理器都会采用将指令乱序执行（out-of-order execution，简称OoOE或OOE）的方法，在条件允许的情况下，直接运行当前有能力立即执行的后续指令，避开获取下一条指令所需数据时造成的等待3。通过乱序执行的技术，处理器可以大大提高执行效率。而这就是指令重排。

3）内存屏障

内存屏障，也叫内存栅栏，是一种CPU指令，用于控制特定条件下的重排序和内存可见性问题。

LoadLoad屏障：对于这样的语句Load1; LoadLoad; Load2，在Load2及后续读取操作要读取的数据被访问前，保证Load1要读取的数据被读取完毕。
StoreStore屏障：对于这样的语句Store1; StoreStore; Store2，在Store2及后续写入操作执行前，保证Store1的写入操作对其它处理器可见。
LoadStore屏障：对于这样的语句Load1; LoadStore; Store2，在Store2及后续写入操作被刷出前，保证Load1要读取的数据被读取完毕。
StoreLoad屏障：对于这样的语句Store1; StoreLoad; Load2，在Load2及后续所有读取操作执行前，保证Store1的写入对所有处理器可见。它的开销是四种屏障中最大的。 在大多数处理器的实现中，这个屏障是个万能屏障，兼具其它三种内存屏障的功能。
4）happen-before原则

单线程happen-before原则：在同一个线程中，书写在前面的操作happen-before后面的操作。 锁的happen-before原则：同一个锁的unlock操作happen-before此锁的lock操作。
volatile的happen-before原则：对一个volatile变量的写操作happen-before对此变量的任意操作(当然也包括写操作了)。
happen-before的传递性原则：如果A操作 happen-before B操作，B操作happen-before C操作，那么A操作happen-before C操作。
线程启动的happen-before原则：同一个线程的start方法happen-before此线程的其它方法。
线程中断的happen-before原则 ：对线程interrupt方法的调用happen-before被中断线程的检测到中断发送的代码。
线程终结的happen-before原则： 线程中的所有操作都happen-before线程的终止检测。
对象创建的happen-before原则： 一个对象的初始化完成先于他的finalize方法调用。
7.简单说说你了解的类加载器，可以打破双亲委派么，怎么打破。
思路： 先说明一下什么是类加载器，可以给面试官画个图，再说一下类加载器存在的意义，说一下双亲委派模型，最后阐述怎么打破双亲委派模型。

我的答案：

1) 什么是类加载器？

类加载器 就是根据指定全限定名称将class文件加载到JVM内存，转为Class对象。

启动类加载器（Bootstrap ClassLoader）：由C++语言实现（针对HotSpot）,负责将存放在<JAVA_HOME>\lib目录或-Xbootclasspath参数指定的路径中的类库加载到内存中。
其他类加载器：由Java语言实现，继承自抽象类ClassLoader。如：
扩展类加载器（Extension ClassLoader）：负责加载<JAVA_HOME>\lib\ext目录或java.ext.dirs系统变量指定的路径中的所有类库。
应用程序类加载器（Application ClassLoader）。负责加载用户类路径（classpath）上的指定类库，我们可以直接使用这个类加载器。一般情况，如果我们没有自定义类加载器默认就是用这个加载器。
2）双亲委派模型

双亲委派模型工作过程是：

如果一个类加载器收到类加载的请求，它首先不会自己去尝试加载这个类，而是把这个请求委派给父类加载器完成。每个类加载器都是如此，只有当父加载器在自己的搜索范围内找不到指定的类时（即ClassNotFoundException），子加载器才会尝试自己去加载。

双亲委派模型图：

![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAxOS83LzIzLzE2YzFjNTRjZjRhZDg4NmI_aW1hZ2VWaWV3Mi8wL3cvMTI4MC9oLzk2MC9mb3JtYXQvd2VicC9pZ25vcmUtZXJyb3IvMQ?x-oss-process=image/format,png)



 

3）为什么需要双亲委派模型？

在这里，先想一下，如果没有双亲委派，那么用户是不是可以自己定义一个java.lang.Object的同名类，java.lang.String的同名类，并把它放到ClassPath中,那么类之间的比较结果及类的唯一性将无法保证，因此，为什么需要双亲委派模型？防止内存中出现多份同样的字节码

4）怎么打破双亲委派模型？

打破双亲委派机制则不仅要继承ClassLoader类，还要重写loadClass和findClass方法。

8.说说你知道的几种主要的JVM参数
思路： 可以说一下堆栈配置相关的，垃圾收集器相关的，还有一下辅助信息相关的。

我的答案：

1）堆栈配置相关

java -Xmx3550m -Xms3550m -Xmn2g -Xss128k 
-XX:MaxPermSize=16m -XX:NewRatio=4 -XX:SurvivorRatio=4 -XX:MaxTenuringThreshold=0
-Xmx3550m： 最大堆大小为3550m。

-Xms3550m： 设置初始堆大小为3550m。

-Xmn2g： 设置年轻代大小为2g。

-Xss128k： 每个线程的堆栈大小为128k。

-XX:MaxPermSize： 设置持久代大小为16m

-XX:NewRatio=4: 设置年轻代（包括Eden和两个Survivor区）与年老代的比值（除去持久代）。

-XX:SurvivorRatio=4： 设置年轻代中Eden区与Survivor区的大小比值。设置为4，则两个Survivor区与一个Eden区的比值为2:4，一个Survivor区占整个年轻代的1/6

-XX:MaxTenuringThreshold=0： 设置垃圾最大年龄。如果设置为0的话，则年轻代对象不经过Survivor区，直接进入年老代。

2）垃圾收集器相关

-XX:+UseParallelGC
-XX:ParallelGCThreads=20
-XX:+UseConcMarkSweepGC 
-XX:CMSFullGCsBeforeCompaction=5
-XX:+UseCMSCompactAtFullCollection：
-XX:+UseParallelGC： 选择垃圾收集器为并行收集器。

-XX:ParallelGCThreads=20： 配置并行收集器的线程数

-XX:+UseConcMarkSweepGC： 设置年老代为并发收集。

-XX:CMSFullGCsBeforeCompaction：由于并发收集器不对内存空间进行压缩、整理，所以运行一段时间以后会产生“碎片”，使得运行效率降低。此值设置运行多少次GC以后对内存空间进行压缩、整理。

-XX:+UseCMSCompactAtFullCollection： 打开对年老代的压缩。可能会影响性能，但是可以消除碎片

3）辅助信息相关

-XX:+PrintGC
-XX:+PrintGCDetails
-XX:+PrintGC 输出形式:

[GC 118250K->113543K(130112K), 0.0094143 secs] [Full GC 121376K->10414K(130112K), 0.0650971 secs]

-XX:+PrintGCDetails 输出形式:

[GC [DefNew: 8614K->781K(9088K), 0.0123035 secs] 118250K->113543K(130112K), 0.0124633 secs] [GC [DefNew: 8614K->8614K(9088K), 0.0000665 secs][Tenured: 112761K->10414K(121024K), 0.0433488 secs] 121376K->10414K(130112K), 0.0436268 secs

9.怎么打出线程栈信息。
思路： 可以说一下jps，top ，jstack这几个命令，再配合一次排查线上问题进行解答。

我的答案：

输入jps，获得进程号。
top -Hp pid 获取本进程中所有线程的CPU耗时性能
jstack pid命令查看当前java进程的堆栈状态
或者 jstack -l > /tmp/output.txt 把堆栈信息打到一个txt文件。
可以使用fastthread 堆栈定位，fastthread.io/
10.强引用、软引用、弱引用、虚引用的区别？
思路： 先说一下四种引用的定义，可以结合代码讲一下，也可以扩展谈到ThreadLocalMap里弱引用用处。

我的答案：

1）强引用

我们平时new了一个对象就是强引用，例如 Object obj = new Object();即使在内存不足的情况下，JVM宁愿抛出OutOfMemory错误也不会回收这种对象。

2）软引用

如果一个对象只具有软引用，则内存空间足够，垃圾回收器就不会回收它；如果内存空间不足了，就会回收这些对象的内存。

SoftReference<String> softRef=new SoftReference<String>(str);     // 软引用
用处： 软引用在实际中有重要的应用，例如浏览器的后退按钮。按后退时，这个后退时显示的网页内容是重新进行请求还是从缓存中取出呢？这就要看具体的实现策略了。

（1）如果一个网页在浏览结束时就进行内容的回收，则按后退查看前面浏览过的页面时，需要重新构建

（2）如果将浏览过的网页存储到内存中会造成内存的大量浪费，甚至会造成内存溢出

如下代码：

```java
Browser prev = new Browser();               // 获取页面进行浏览
SoftReference sr = new SoftReference(prev); // 浏览完毕后置为软引用        
if(sr.get()!=null){ 
    rev = (Browser) sr.get();           // 还没有被回收器回收，直接获取
}else{
    prev = new Browser();               // 由于内存吃紧，所以对软引用的对象回收了
    sr = new SoftReference(prev);       // 重新构建
}
```



3）弱引用

具有弱引用的对象拥有更短暂的生命周期。在垃圾回收器线程扫描它所管辖的内存区域的过程中，一旦发现了只具有弱引用的对象，不管当前内存空间足够与否，都会回收它的内存。

```java
String str=new String("abc");    
WeakReference<String> abcWeakRef = new WeakReference<String>(str);
str=null;
等价于
str = null;
System.gc();
```



4）虚引用

如果一个对象仅持有虚引用，那么它就和没有任何引用一样，在任何时候都可能被垃圾回收器回收。虚引用主要用来跟踪对象被垃圾回收器回收的活动。


#### 7.内存调优用到的工具有哪些

工具主要是为了解决问题而生的，就是由于我们的程序存在着一些性能问题，才有了这些工具。其实当我们在下载完成JDK之后，那些工具就被SUN公司随之送给我们了。

我们可以在我们的JDK安装目录，下看看会有很多这样的工具。

![img](https://pics7.baidu.com/feed/03087bf40ad162d945f4ae38440689e98b13cddf.jpeg?token=19e6f8dd6e8a99a2ff571aaaecf8d263&s=A59A5D321D07624B467D50DF0000D0B2)

我们会发现很多这样的exe文件，这里面有很多都是性能监控工具。我们就抽出来几个进行讲解。

![img](https://pics7.baidu.com/feed/6d81800a19d8bc3e1e09b5f9da52861ba9d345da.png?token=361e169d523405abdc45d14f81036b61&s=1AAA74235DD841CA1C5D94CA0300E0B1)

常见的几个工具都已经列出来了，还有一些其他的工具，其实用起来比JDK自带的还要好，我会在今后的文章中列出来。OK，我们就一个一个去分析一下这些工具是干嘛的，以及如何去使用的。

二、工具

1、jps:虚拟机进程状况工具

jps主要用来输出JVM中运行的进程状态信息。语法格式如下：

jps [options] [hostid]

第一个参数：options

-q 不输出类名、Jar名和传入main方法的参数-m 输出传入main方法的参数-l 输出main类或Jar的全限名-v 输出传入JVM的参数

第二个参数：hostid

主机或者是服务器的id，如果不指定，就默认为当前的主机或者是服务器。

我是在Windows10系统下测试的，当然你可以在linux下试验，方式是一样的，结果可能有不同。你可以选择不同的参数选项来进行测试。打开CMD输入相应命令

![img](https://pics2.baidu.com/feed/4610b912c8fcc3ce5f26458dc79cf68dd63f208c.jpeg?token=27132261b914113d2d9263d70c6bfd58)

2、jstack：堆栈跟踪工具

jstack用于生成虚拟机当前时刻的线程快照。语法格式如下：

jstack [option] vmid

第一个参数：option

![img](https://pics1.baidu.com/feed/37d3d539b6003af35d0f963c63f3e6591138b617.png?token=15a7c34b4c9f8ee190938f636fbee4e4&s=1A2874238DA0450356FCA1DE0300C0B1)

第二个参数：vmid

vmid是Java虚拟机ID，在Linux/Unix系统上一般就是进程ID。

我们直接在CMD中操作一下：

![img](https://pics3.baidu.com/feed/d31b0ef41bd5ad6e1982cf9bd51219deb7fd3ca2.jpeg?token=e336b0f86343c7d16a3d8d4a41d1afc3&s=0DE272228BE08A4B5C7DB50F000070C1)

3、jstat:虚拟机统计信息监控工具

jstat监视虚拟机各种运行状态信息，可以显示本地或者是远程虚拟机进程中的类装载、内存、垃圾收集、JIT编译等运行数据。语法格式如下：

jstat [ generalOption | outputOptions vmid [interval] [count]] ]

第一个参数：generalOption | outputOptions

这个参数表示的option，代表着用户希望查询的虚拟机信息，分为类加载、垃圾收集、运行期编译状况3类。

![img](https://pics7.baidu.com/feed/b151f8198618367ae3252a817aaaabd1b21ce518.jpeg?token=5d86fe924dd5722ae81742a8395effa9&s=3EAA70239D9844C85EFD45DA0100C0B1)

第二个参数：vmid

vmid是Java虚拟机ID，在Linux/Unix系统上一般就是进程ID。

第三个参数：interval

interval是采样时间间隔，

第四个参数：count

count表示的是采样数。

下面我们就是用一下这个工具，打开我们的CMD，输入相应的命令：

![img](https://pics2.baidu.com/feed/8b82b9014a90f603c70774796dcb931eb151edbc.jpeg?token=996ae0d68d207a21ca2fef14f99c843c&s=45D33A66DFEDBB704C71DC1F0000A0C3)

4、jinfo：实时地查看和调整虚拟机各项参数

命令格式:

jinfo [option] pid

第一个参数：option

![img](https://pics4.baidu.com/feed/71cf3bc79f3df8dc74aa127798c8528e4510289b.png?token=f36fe6690ad2eef4d6ae1d21db99f222&s=1AAA74239BA059031E5D90DE0300C0B1)

第二个参数：pid

指定显示的进程id。

在CMD中进行测试：

![img](https://pics4.baidu.com/feed/a5c27d1ed21b0ef41ab2f25d891d71df80cb3ebc.jpeg?token=5ae7f70c62faa7374b1e6a64fe10d122&s=EDE03A6613A483494E5DBD0F0000E0C3)

5、jmap：生成虚拟机的内存转储快照（heapdump文件）

jmap（Memory Map for Java，内存映像工具），用于生成堆转存的快照，一般是heapdump或者dump文件。如果不适用jmap命令，可以使用-XX:+HeapDumpOnOutOfMemoryError参数，当虚拟机发生内存溢出的时候可以产生快照。或者使用kill -3 pid也可以产生。jmap的作用并不仅仅是为了获取dump文件，它可以查询finalize执行队列，java堆和永久代的详细信息，如空间使用率，当前用的哪种收集器。命令格式如下：

jmap [option] vmid

第一个参数：

![img](https://pics5.baidu.com/feed/d8f9d72a6059252d24ddc5946042233e59b5b9b3.jpeg?token=b5b6d5d2cc3be15e31b6d772e2da34bb&s=5AAA346399D844C80E5CD4CF0000A0B1)

第二个参数：vmid

vmid是Java虚拟机ID，在Linux/Unix系统上一般就是进程ID.

在cmd中测试：

![img](https://pics0.baidu.com/feed/ac6eddc451da81cb7409ae1306bff0130b24315a.jpeg?token=93e2a4769589c40a59109e43ce1b1cfa&s=4DC33A6653A5834F0E5CA41B000070C3)

6、jhat：分析内存转储快照，不推荐使用，而且慢

由于这个工具功能比较简陋，运行起来也比较耗时，所以这个工具不推荐使用，推荐使用MAT。

7、JConsole：JMX的可视化管理工具

这个工具相比较前面几个工具，使用率比较高，很重要。它是一个java GUI监视工具，可以以图表化的形式显示各种数据。并可通过远程连接监视远程的服务器VM。用java写的GUI程序，用来监控VM，并可监控远程的VM，非常易用，而且功能非常强。

在cmd里面输入 jconsole，选则进程就可以了。（前提是在IDE工具先建立一个线程运行着）

![img](https://pics4.baidu.com/feed/359b033b5bb5c9ea5dbaad7a81e096053bf3b338.jpeg?token=540c9335ce9b5dafb1440d53931567e4&s=49008D1A515E55CC58F515DA0000C0B1)

然后我们选择了相应的选项之后，进入这个工具就会出现下面这个界面

![img](https://pics2.baidu.com/feed/bd315c6034a85edfe69876d11c8d2926dc54750e.jpeg?token=dbf4f034d60e8173c3d2c2a00351dcdc&s=AD8A55320B0E444D1C5508CA0000D0B2)

在上面有菜单，我们可以选择其中一个进行查看，就可以了，这个用具用起来很方便，也是我之前用的比较多的工具。

8、VisualVM：多合一故障管理工具

这个工具也很牛bility。它同jconsole都是一个基于图形化界面的、可以查看本地及远程的JAVA GUI监控工具，Jvisualvm同jconsole的使用方式一样，直接在命令行打入jvisualvm即可启动，jvisualvm界面更美观一些，数据更实时：

![img](https://pics4.baidu.com/feed/d1160924ab18972b3f49b403b2145b8c9c510ae2.jpeg?token=964d4a7ea666e14f0ff647efd2c52218&s=F490EC381ECE74C8445C58DF000010B2)

最上面也有菜单，你可以选择不同的选项来展示。自己动手试一遍是最好的。

三、总结

这些工具就先写这么多，在文章一开始我们其实已经发现了，jdk自带的工具那是超级的多，而且随着jdk版本的不断更新，工具还有不断加强增多的趋势，想要每一个都掌握那太费时间了，我们遇到哪些问题去搜索一下，看看能用到哪些工具就可以了，列出的这几种工具，对于初学者来说还是比较适用的。

