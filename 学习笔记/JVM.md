## 1. 什么是JVM内存结构？

![图片](https://mmbiz.qpic.cn/mmbiz_png/EyPNic5dZCg8FHJlP9F0gqmZtLe5rbUYhqicuLoicq1aDveh6UYRKFexzPzNgdLAlnXVfmKDVbpJhhAJRN4Xia4Nicg/640?wx_fmt=png&wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

jvm将虚拟机分为5大区域，程序计数器、虚拟机栈、本地方法栈、java堆、方法区；

- 程序计数器：线程私有的，是一块很小的内存空间，作为当前线程的行号指示器，用于记录当前虚拟机正在执行的线程指令地址；
- 虚拟机栈：线程私有的，每个方法执行的时候都会创建一个栈帧，用于存储局部变量表、操作数、动态链接和方法返回等信息，当线程请求的栈深度超过了虚拟机允许的最大深度时，就会抛出StackOverFlowError；
- 本地方法栈：线程私有的，保存的是native方法的信息，当一个jvm创建的线程调用native方法后，jvm不会在虚拟机栈中为该线程创建栈帧，而是简单的动态链接并直接调用该方法；
- 堆：java堆是所有线程共享的一块内存，几乎所有对象的实例和数组都要在堆上分配内存，因此该区域经常发生垃圾回收的操作；
- 方法区：存放已被加载的类信息、常量、静态变量、即时编译器编译后的代码数据。即永久代，在jdk1.8中不存在方法区了，被元数据区替代了，原方法区被分成两部分；1：加载的类信息，2：运行时常量池；加载的类信息被保存在元数据区中，运行时常量池保存在堆中；

#### 

![img](https://pic2.zhimg.com/80/v2-267e596297bfe4964e97e72b76588b79_720w.jpg)

思路： 先讲一下JAVA堆，新生代的划分，再谈谈它们之间的转化，相互之间一些参数的配置（如： –XX:NewRatio，–XX:SurvivorRatio等），再解释为什么要这样划分，最好加一点自己的理解。

我的答案：

* 1. 共享内存区划分

共享内存区 = 持久带 + 堆
持久带 = 方法区 + 其他
Java堆 = 老年代 + 新生代
新生代 = Eden + S0 + S1

* 2. 一些参数的配置

     ![img](https://pic3.zhimg.com/80/v2-f664c6aa75d6358acff54dd67d075b86_720w.jpg)

默认的，新生代 ( Young ) 与老年代 ( Old ) 的比例的值为 1:2 ，可以通过参数 –XX:NewRatio 配置。
默认的，Edem : from : to = 8 : 1 : 1 ( 可以通过参数 –XX:SurvivorRatio 来设定)
Survivor区中的对象被复制次数为15(对应虚拟机参数 -XX:+MaxTenuringThreshold)



**JVM内存参数设置：**

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



*  3.为什么要分为Eden和Survivor?为什么要设置两个Survivor区？

如果没有Survivor，Eden区每进行一次Minor GC，存活的对象就会被送到老年代。老年代很快被填满，触发Major GC.老年代的内存空间远大于新生代，进行一次Full GC消耗的时间比Minor GC长得多,所以需要分为Eden和Survivor。
Survivor的存在意义，就是减少被送到老年代的对象，进而减少Full GC的发生，Survivor的预筛选保证，只有经历16次Minor GC还能在新生代中存活的对象，才会被送到老年代。
设置两个Survivor区最大的好处就是解决了碎片化，刚刚新建的对象在Eden中，经历一次Minor GC，Eden中的存活对象就会被移动到第一块survivor space S0，Eden被清空；等Eden区再满了，就再触发一次Minor GC，Eden和S0中的存活对象又会被复制送入第二块survivor space S1（这个过程非常重要，因为这种复制算法保证了S1中来自S0和Eden两部分的存活对象占用连续的内存空间，避免了碎片化的发生）

**项目中jar包启动脚本**

```shell
ps -ef | grep liuzhou_kafka_websocket-0.0.1-SNAPSHOT.jar | grep -v grep | cut -c 9-15 | xargs kill -9
nohup java -jar -server -Xmx4g -Xms2g -XX:+UseParallelGC -XX:ParallelGCThreads=32 -XX:PermSize=256m -XX:MaxPermSize=512m  /service/websocket_kafka_service/liuzhou_kafka_websocket-0.0.1-SNAPSHOT.jar --spring.config.local=/service/websocket_kafka_service/application.yml >> /service/websocket_kafka_service/websocket_kafka.log 2>&1 &
~                                                                                                   
```



JVM参数的含义 

1. -Xms 最小堆的大小， 也就是当你的虚拟机启动后， 就会分配这么大的堆内存给你 

2. -Xmx 是最大堆的大小 

3. 当最小堆占满后，会尝试进行GC，如果GC之后还不能得到足够的内存(GC未必会收集到所有当前可用内存)，分配新的对象，那么就会扩展堆，如果-Xmx设置的太小，扩展堆就会失败，导致OutOfMemoryError错误提示。  

4. JVM参数的含义 实例见[实例分析](http://www.cnblogs.com/redcreen/archive/2011/05/05/2038331.html)

   | 参数名称        | 含义                        | 默认值               |                                                              |
   | --------------- | --------------------------- | -------------------- | ------------------------------------------------------------ |
   | -Xms            | 初始堆大小                  | 物理内存的1/64(<1GB) | 默认(MinHeapFreeRatio参数可以调整)空余堆内存小于40%时，JVM就会增大堆直到-Xmx的最大限制. |
   | -Xmx            | 最大堆大小                  | 物理内存的1/4(<1GB)  | 默认(MaxHeapFreeRatio参数可以调整)空余堆内存大于70%时，JVM会减少堆直到 -Xms的最小限制 |
   | -Xmn            | 年轻代大小(1.4or lator)     |                      | 注意：此处的大小是（eden+ 2 survivor space).与jmap -heap中显示的New gen是不同的。 整个堆大小=年轻代大小 + 年老代大小 + 持久代大小. 增大年轻代后,将会减小年老代大小.此值对系统性能影响较大,Sun官方推荐配置为整个堆的3/8 |
   | -XX:NewSize     | 设置年轻代大小(for 1.3/1.4) |                      |                                                              |
   | -XX:MaxNewSize  | 年轻代最大值(for 1.3/1.4)   |                      |                                                              |
   | -XX:PermSize    | 设置持久代(perm gen)初始值  | 物理内存的1/64       |                                                              |
   | -XX:MaxPermSize | 设置持久代最大值            | 物理内存的1/4        |                                                              |
   | -Xss            | 每个线程的堆栈大小          |                      | JDK5.0以后每个线程堆栈大小为1M,以前每个线程堆栈大小为256K.更具应用的线程所需内存大小进行 调整.在相同物理内存下,减小这个值能生成更多的线程.但是操作系统对一个进程内的线程数还是有限制的,不能无限生成,经验值在3000~5000左右 一般小的应用， 如果栈不是很深， 应该是128k够用的 大的应用建议使用256k。这个选项对性能影响比较大，需要严格的测试。（校长） 和threadstacksize选项解释很类似,官方文档似乎没有解释,在论坛中有这样一句话:"” -Xss is translated in a VM flag named ThreadStackSize” 一般设置这个值就可以了。 |



## 2. 什么是JVM内存模型？

**Java 内存模型**（下文简称 **JMM**）就是在底层处理器内存模型的基础上，定义自己的多线程语义。它明确指定了一组排序规则，来保证线程间的可见性。

这一组规则被称为 **Happens-Before**, JMM 规定，要想保证 B 操作能够看到 A 操作的结果（无论它们是否在同一个线程），那么 A 和 B 之间必须满足 **Happens-Before 关系**：

- **单线程规则**：一个线程中的每个动作都 happens-before 该线程中后续的每个动作
- **监视器锁定规则**：监听器的**解锁**动作 happens-before 后续对这个监听器的**锁定**动作
- **volatile 变量规则**：对 volatile 字段的写入动作 happens-before 后续对这个字段的每个读取动作
- **线程 start 规则**：线程 **start()** 方法的执行 happens-before 一个启动线程内的任意动作
- **线程 join 规则**：一个线程内的所有动作 happens-before 任意其他线程在该线程 **join()** 成功返回之前
- **传递性**：如果 A happens-before B, 且 B happens-before C, 那么 A happens-before C

怎么理解 happens-before 呢？如果按字面意思，比如第二个规则，线程（不管是不是同一个）的解锁动作发生在锁定之前？这明显不对。happens-before 也是为了保证可见性，比如那个解锁和加锁的动作，可以这样理解，线程1释放锁退出同步块，线程2加锁进入同步块，那么线程2就能看见线程1对共享对象修改的结果。

![图片](https://mmbiz.qpic.cn/mmbiz_png/EyPNic5dZCg8FHJlP9F0gqmZtLe5rbUYhowMG0iaEAcyDj8pTGRTT9VicezplBictKUPVfdCiaDjocOiakAVpicibnlvMA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

Java 提供了几种语言结构，包括 *volatile*, *final* 和 *synchronized*, 它们旨在帮助程序员向**编译器**描述程序的并发要求，其中：

- **volatile** - 保证**可见性**和**有序性**
- **synchronized** - 保证**可见性**和**有序性**; 通过**管程（Monitor）**保证一组动作的**原子性**
- **final** - 通过禁止**在构造函数初始化**和**给 final 字段赋值**这两个动作的重排序，保证**可见性**（如果 **this 引用逃逸**就不好说可见性了）

编译器在遇到这些关键字时，会插入相应的内存屏障，保证语义的正确性。

有一点需要**注意**的是，**synchronized** **不保证**同步块内的代码禁止重排序，因为它通过锁保证同一时刻只有**一个线程**访问同步块（或临界区），也就是说同步块的代码只需满足 **as-if-serial** 语义 - 只要单线程的执行结果不改变，可以进行重排序。

所以说，Java 内存模型描述的是多线程对共享内存修改后彼此之间的可见性，另外，还确保正确同步的 Java 代码可以在不同体系结构的处理器上正确运行。

## 3. heap 和stack 有什么区别？

**（1**）申请方式

stack:由系统自动分配。例如，声明在函数中一个局部变量 int b; 系统自动在栈中为 b 开辟空间

heap:需要程序员自己申请，并指明大小，在 c 中 malloc 函数，对于Java 需要手动 new Object()的形式开辟

**（2**）申请后系统的响应

stack：只要栈的剩余空间大于所申请空间，系统将为程序提供内存，否则将报异常提示栈溢出。

heap：首先应该知道操作系统有一个记录空闲内存地址的链表，当系统收到程序的申请时，会遍历该链表，寻找第一个空间大于所申请空间的堆结点，然后将该结点从空闲结点链表中删除，并将该结点的空间分配给程序。另外，由于找到的堆结点的大小不一定正好等于申请的大小，系统会自动的将多余的那部分重新放入空闲链表中。

**（3**）申请大小的限制

stack：栈是向低地址扩展的数据结构，是一块连续的内存的区域。这句话的意思是栈顶的地址和栈的最大容量是系统预先规定好的，在 WINDOWS 下，栈的大小是 2M（默认值也取决于虚拟内存的大小），如果申请的空间超过栈的剩余空间时，将提示 overflow。因此，能从栈获得的空间较小。

heap：堆是向高地址扩展的数据结构，是不连续的内存区域。这是由于系统是用链表来存储的空闲内存地址的， 自然是不连续的，而链表的遍历方向是由低地址向高地址。堆的大小受限于计算机系统中有效的虚拟内存。由此可见， 堆获得的空间比较灵活，也比较大。

**（4**）申请效率的比较

stack：由系统自动分配，速度较快。但程序员是无法控制的。

heap：由 new 分配的内存，一般速度比较慢，而且容易产生内存碎片,不过用起来最方便。

**（5**）heap和stack中的存储内容

stack：在函数调用时，第一个进栈的是主函数中后的下一条指令（函数调用语句的下一条可执行语句）的地址， 然后是函数的各个参数，在大多数的 C 编译器中，参数是由右往左入栈的，然后是函数中的局部变量。注意静态变量是不入栈的。

当本次函数调用结束后，局部变量先出栈，然后是参数，最后栈顶指针指向最开始存的地址，也就是主函数中的下一条指令，程序由该点继续运行。

heap：一般是在堆的头部用一个字节存放堆的大小。堆中的具体内容有程序员安排。

## 4. 什么情况下会发生栈内存溢出？

1、栈是线程私有的，栈的生命周期和线程一样，每个方法在执行的时候就会创建一个栈帧，它包含局部变量表、操作数栈、动态链接、方法出口等信息，局部变量表又包括基本数据类型和对象的引用；2、当线程请求的栈深度超过了虚拟机允许的最大深度时，会抛出StackOverFlowError异常，方法递归调用肯可能会出现该问题；3、调整参数-xss去调整jvm栈的大小

## 5. 谈谈对 OOM 的认识？如何排查 OOM 的问题？

除了程序计数器，其他内存区域都有 OOM 的风险。

- 栈一般经常会发生 StackOverflowError，比如 32 位的 windows 系统单进程限制 2G 内存，无限创建线程就会发生栈的 OOM
- Java 8 常量池移到堆中，溢出会出 java.lang.OutOfMemoryError: Java heap space，设置最大元空间大小参数无效；
- 堆内存溢出，报错同上，这种比较好理解，GC 之后无法在堆中申请内存创建对象就会报错；
- 方法区 OOM，经常会遇到的是动态生成大量的类、jsp 等；
- 直接内存 OOM，涉及到 -XX:MaxDirectMemorySize 参数和 Unsafe 对象对内存的申请。

排查 OOM 的方法：

- 增加两个参数 -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp/heapdump.hprof，当 OOM 发生时自动 dump 堆内存信息到指定目录；
- 同时 jstat 查看监控 JVM 的内存和 GC 情况，先观察问题大概出在什么区域；
- 使用 MAT 工具载入到 dump 文件，分析大对象的占用情况，比如 HashMap 做缓存未清理，时间长了就会内存溢出，可以把改为弱引用 。

## 6. 谈谈 JVM 中的常量池？

JVM常量池主要分为**Class文件常量池、运行时常量池，全局字符串常量池，以及基本类型包装类对象常量池**。

- **Class文件常量池**。class文件是一组以字节为单位的二进制数据流，在java代码的编译期间，我们编写的java文件就被编译为.class文件格式的二进制数据存放在磁盘中，其中就包括class文件常量池。
- **运行时常量池**：运行时常量池相对于class常量池一大特征就是具有动态性，java规范并不要求常量只能在运行时才产生，也就是说运行时常量池的内容并不全部来自class常量池，在运行时可以通过代码生成常量并将其放入运行时常量池中，这种特性被用的最多的就是String.intern()。
- **全局字符串常量池**：字符串常量池是JVM所维护的一个字符串实例的引用表，在HotSpot VM中，它是一个叫做StringTable的全局表。在字符串常量池中维护的是字符串实例的引用，底层C++实现就是一个Hashtable。这些被维护的引用所指的字符串实例，被称作”被驻留的字符串”或”interned string”或通常所说的”进入了字符串常量池的字符串”。
- 基本类型包装类对象常量池：java中基本类型的包装类的大部分都实现了常量池技术，这些类是Byte,Short,Integer,Long,Character,Boolean,另外两种浮点数类型的包装类则没有实现。另外上面这5种整型的包装类也只是在对应值小于等于127时才可使用对象池，也即对象不负责创建和管理大于127的这些类的对象。

## 7. 如何判断一个对象是否存活？

判断一个对象是否存活，分为两种算法1：引用计数法；2：可达性分析算法；

**引用计数法**：给每一个对象设置一个引用计数器，当有一个地方引用该对象的时候，引用计数器就+1，引用失效时，引用计数器就-1；当引用计数器为0的时候，就说明这个对象没有被引用，也就是垃圾对象，等待回收；缺点：无法解决循环引用的问题，当A引用B，B也引用A的时候，此时AB对象的引用都不为0，此时也就无法垃圾回收，所以一般主流虚拟机都不采用这个方法；

**可达性分析法**从一个被称为GC Roots的对象向下搜索，如果一个对象到GC Roots没有任何引用链相连接时，说明此对象不可用，在java中可以作为GC Roots的对象有以下几种：

- 虚拟机栈中引用的对象
- 方法区类静态属性引用的变量
- 方法区常量池引用的对象
- 本地方法栈JNI引用的对象

但一个对象满足上述条件的时候，不会马上被回收，还需要进行两次标记；第一次标记：判断当前对象是否有finalize()方法并且该方法没有被执行过，若不存在则标记为垃圾对象，等待回收；若有的话，则进行第二次标记；第二次标记将当前对象放入F-Queue队列，并生成一个finalize线程去执行该方法，虚拟机不保证该方法一定会被执行，这是因为如果线程执行缓慢或进入了死锁，会导致回收系统的崩溃；如果执行了finalize方法之后仍然没有与GC Roots有直接或者间接的引用，则该对象会被回收；

## 8. 强引用、软引用、弱引用、虚引用是什么，有什么区别？

- 强引用，就是普通的对象引用关系，如 String s = new String("ConstXiong")
- 软引用，用于维护一些可有可无的对象。只有在内存不足时，系统则会回收软引用对象，如果回收了软引用对象之后仍然没有足够的内存，才会抛出内存溢出异常。SoftReference 实现
- 弱引用，相比软引用来说，要更加无用一些，它拥有更短的生命周期，当 JVM 进行垃圾回收时，无论内存是否充足，都会回收被弱引用关联的对象。WeakReference 实现
- 虚引用是一种形同虚设的引用，在现实场景中用的不是很多，它主要用来跟踪对象被垃圾回收的活动。PhantomReference 实现

**GC回收之引用（强引用、软引用、弱引用、虚引用）详解**： https://blog.csdn.net/weixin_41133233/article/details/103789929



| 引用类型 | GC回收时间     | 用处                 | 存活时间      |
| -------- | -------------- | -------------------- | ------------- |
| 强引用   | 从来不会被回收 | 一般对象的引用       | JVM停止运行时 |
| 软引用   | 在内存不足时   | 对象缓存             | 内存不足时    |
| 弱引用   | 在垃圾回收时   | 对象缓存             | GC回收后      |
| 虚引用   | 任何时间       | 监控对象的创建和销毁 | Unknow        |

> 在程序设计中弱引用与虚引用一般很少使用，软引用使用的几率比较大，因为软引用可以加速JVM对垃圾内存的回收速度，可以维护系统的运行安全，防止内存溢出（OutOfMemory）等问题的产生。



引申问题：java的while循环中被new的对象在一次循环结束后 会被垃圾回收吗?

while循环完一次，会被回收。但是至于什么时候被回收，要看jvm的回收线程。
不过我们可以指向null，例如：test = null，用完会立即回收。
还有就是System.gc();方法，已通知jvm进行回收。



## 9. 被引用的对象就一定能存活吗？

> 不一定，看 Reference 类型，弱引用在 GC 时会被回收，软引用在内存不足的时候，即 OOM 前会被回收，但如果没有在 Reference Chain 中的对象就一定会被回收。

## 10. Java中的垃圾回收算法有哪些？

java中有四种垃圾回收算法，分别是标记清除法、标记整理法、复制算法、分代收集算法；

**标记清除法**：
第一步：利用可达性去遍历内存，把存活对象和垃圾对象进行标记；
第二步：在遍历一遍，将所有标记的对象回收掉；
特点：效率不行，标记和清除的效率都不高；标记和清除后会产生大量的不连续的空间分片，可能会导致之后程序运行的时候需分配大对象而找不到连续分片而不得不触发一次GC；

![图片](https://mmbiz.qpic.cn/mmbiz_png/EyPNic5dZCg8FHJlP9F0gqmZtLe5rbUYhftHVcOx5JjibnQPZdaFRYKWqRsjF7f7MTMWjZEVe34SD0EibtQoM1cNg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**标记整理法**：
第一步：利用可达性去遍历内存，把存活对象和垃圾对象进行标记；
第二步：将所有的存活的对象向一段移动，将端边界以外的对象都回收掉；
特点：适用于存活对象多，垃圾少的情况；需要整理的过程，无空间碎片产生；

![图片](https://mmbiz.qpic.cn/mmbiz_png/EyPNic5dZCg8FHJlP9F0gqmZtLe5rbUYhJSMicBmo3j2smckztzqey9u0Lk19xpDhh98TzNhQ6OUGzHsXbRDE2BA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**复制算法**：
将内存按照容量大小分为大小相等的两块，每次只使用一块，当一块使用完了，就将还存活的对象移到另一块上，然后在把使用过的内存空间移除；
特点：不会产生空间碎片；内存使用率极低；

**分代收集算法**：
根据内存对象的存活周期不同，将内存划分成几块，java虚拟机一般将内存分成新生代和老生代，
在新生代中，有大量对象死去和少量对象存活，所以采用复制算法，只需要付出少量存活对象的复制成本就可以完成收集；
老年代中因为对象的存活率极高，没有额外的空间对他进行分配担保，所以采用标记清理或者标记整理算法进行回收；

**对比**

![图片](https://mmbiz.qpic.cn/mmbiz_png/EyPNic5dZCg8FHJlP9F0gqmZtLe5rbUYhiadoVx5UuLV8W32ibbEqTzHSEAtwg2bML8Pv6IOAOjdsj4Sya25tfficg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 11. 有哪几种垃圾回收器，各自的优缺点是什么？

垃圾回收器主要分为以下几种：Serial、ParNew、Parallel Scavenge、Serial Old、Parallel Old、CMS、G1；

- Serial:单线程的收集器，收集垃圾时，必须stop the world，使用复制算法。它的最大特点是在进行垃圾回收时，需要对所有正在执行的线程暂停（stop the world），对于有些应用是难以接受的，但是如果应用的实时性要求不是那么高，只要停顿的时间控制在N毫秒之内，大多数应用还是可以接受的，是client级别的默认GC方式。
- ParNew:Serial收集器的多线程版本，也需要stop the world，复制算
- Parallel Scavenge:新生代收集器，复制算法的收集器，并发的多线程收集器，目标是达到一个可控的吞吐量，和ParNew的最大区别是GC自动调节策略；虚拟机会根据系统的运行状态收集性能监控信息，动态设置这些参数，以提供最优停顿时间和最高的吞吐量；
- Serial Old:Serial收集器的老年代版本，单线程收集器，使用标记整理算法。
- Parallel Old：是Parallel Scavenge收集器的老年代版本，使用多线程，标记-整理算法。
- CMS:是一种以获得最短回收停顿时间为目标的收集器，标记清除算法，运作过程：初始标记，并发标记，重新标记，并发清除，收集结束会产生大量空间碎片；
- G1:标记整理算法实现，运作流程主要包括以下：初始标记，并发标记，最终标记，筛选回收。不会产生空间碎片，可以精确地控制停顿；G1将整个堆分为大小相等的多个Region（区域），G1跟踪每个区域的垃圾大小，在后台维护一个优先级列表，每次根据允许的收集时间，优先回收价值最大的区域，已达到在有限时间内获取尽可能高的回收效率；

```sh
nohup java -jar -server -Xmx8g -Xms4g -XX:+UseG1GC -XX:ParallelGCThreads=32 -XX:PermSize=256m -XX:MaxPermSize=512m  /service/websocket_kafka_service/liuzhou_kafka_websocket-0.0.1-SNAPSHOT.jar --spring.config.local=/service/websocket_kafka_service/application.yml >> /service/websocket_kafka_service/websocket_kafka.log 2>&1 &

```

####  G1垃圾回收器参数配置 下面是完整的 G1 的 GC 开关参数列表.

| 选项/默认值                          | 说明                                                         |
| :----------------------------------- | :----------------------------------------------------------- |
| -XX:+UseG1GC                         | 使用 G1 (Garbage First) 垃圾收集器                           |
| -XX:MaxGCPauseMillis=n               | 设置最大GC停顿时间(GC pause time)指标(target). 这是一个软性指标(soft goal), JVM 会尽量去达成这个目标. |
| -XX:InitiatingHeapOccupancyPercent=n | 启动并发GC周期时的堆内存占用百分比. G1之类的垃圾收集器用它来触发并发GC周期,基于整个堆的使用率,而不只是某一代内存的使用比. 值为 0 则表示"一直执行GC循环". 默认值为 45. |
| -XX:NewRatio=n                       | 新生代与老生代(new/old generation)的大小比例(Ratio). 默认值为 2. |
| -XX:SurvivorRatio=n                  | eden/survivor 空间大小的比例(Ratio). 默认值为 8.             |
| -XX:MaxTenuringThreshold=n           | 提升年老代的最大临界值(tenuring threshold). 默认值为 15.     |
| -XX:ParallelGCThreads=n              | 设置垃圾收集器在并行阶段使用的线程数,默认值随JVM运行的平台不同而不同. |
| -XX:ConcGCThreads=n                  | 并发垃圾收集器使用的线程数量. 默认值随JVM运行的平台不同而不同. |
| -XX:G1ReservePercent=n               | 设置堆内存保留为假天花板的总量,以降低提升失败的可能性. 默认值是 10. |
| -XX:G1HeapRegionSize=n               | 使用G1时Java堆会被分为大小统一的的区(region)。此参数可以指定每个heap区的大小. 默认值将根据 heap size 算出最优解. 最小值为 1Mb, 最大值为 32Mb. |



**垃圾回收器间的配合使用图：**

![图片](https://mmbiz.qpic.cn/mmbiz_png/EyPNic5dZCg8FHJlP9F0gqmZtLe5rbUYhGibVRzHc4GKM8YCQF04VWfQXeMWDkqciaCylVoUbrz9k1o428eGmbT1w/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**各个垃圾回收器对比**：

![图片](https://mmbiz.qpic.cn/mmbiz_png/EyPNic5dZCg8FHJlP9F0gqmZtLe5rbUYhuzOdDxIE4KSiclKulfQLvGLl4LcBBaAxztxXbEATSovTpCgYSSlqicDA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 12. 详细说一下CMS的回收过程？CMS的问题是什么？

CMS(Concurrent Mark Sweep，并发标记清除) 收集器是以获取最短回收停顿时间为目标的收集器（追求低停顿），它在垃圾收集时使得用户线程和 GC 线程并发执行，因此在垃圾收集过程中用户也不会感到明显的卡顿。

从名字就可以知道，CMS是基于“标记-清除”算法实现的。CMS 回收过程分为以下四步：

1. 初始标记 （CMS initial mark)：主要是标记 GC Root 开始的下级（注：仅下一级）对象，这个过程会 STW，但是跟 GC Root 直接关联的下级对象不会很多，因此这个过程其实很快。
2. 并发标记 (CMS concurrent mark)：根据上一步的结果，继续向下标识所有关联的对象，直到这条链上的最尽头。这个过程是多线程的，虽然耗时理论上会比较长，但是其它工作线程并不会阻塞，没有 STW。
3. 重新标记（CMS remark）：顾名思义，就是要再标记一次。为啥还要再标记一次？因为第 2 步并没有阻塞其它工作线程，其它线程在标识过程中，很有可能会产生新的垃圾。
4. 并发清除（CMS concurrent sweep）：清除阶段是清理删除掉标记阶段判断的已经死亡的对象，由于不需要移动存活对象，所以这个阶段也是可以与用户线程同时并发进行的。

**CMS 的问题：**

**1. 并发回收导致CPU资源紧张：**

在并发阶段，它虽然不会导致用户线程停顿，但却会因为占用了一部分线程而导致应用程序变慢，降低程序总吞吐量。CMS默认启动的回收线程数是：（CPU核数 + 3）/ 4，当CPU核数不足四个时，CMS对用户程序的影响就可能变得很大。

**2. 无法清理浮动垃圾：**

在CMS的并发标记和并发清理阶段，用户线程还在继续运行，就还会伴随有新的垃圾对象不断产生，但这一部分垃圾对象是出现在标记过程结束以后，CMS无法在当次收集中处理掉它们，只好留到下一次垃圾收集时再清理掉。这一部分垃圾称为“浮动垃圾”。

**3. 并发失败（Concurrent Mode Failure）：**

由于在垃圾回收阶段用户线程还在并发运行，那就还需要预留足够的内存空间提供给用户线程使用，因此CMS不能像其他回收器那样等到老年代几乎完全被填满了再进行回收，必须预留一部分空间供并发回收时的程序运行使用。默认情况下，当老年代使用了 92% 的空间后就会触发 CMS 垃圾回收，这个值可以通过 -XX**:** CMSInitiatingOccupancyFraction 参数来设置。

这里会有一个风险：要是CMS运行期间预留的内存无法满足程序分配新对象的需要，就会出现一次“并发失败”（Concurrent Mode Failure），这时候虚拟机将不得不启动后备预案：Stop The World，临时启用 Serial Old 来重新进行老年代的垃圾回收，这样一来停顿时间就很长了。

**4.内存碎片问题：**

CMS是一款基于“标记-清除”算法实现的回收器，这意味着回收结束时会有内存碎片产生。内存碎片过多时，将会给大对象分配带来麻烦，往往会出现老年代还有很多剩余空间，但就是无法找到足够大的连续空间来分配当前对象，而不得不提前触发一次 Full GC 的情况。

为了解决这个问题，CMS收集器提供了一个 -XX**:**+UseCMSCompactAtFullCollection 开关参数（默认开启），用于在 Full GC 时开启内存碎片的合并整理过程，由于这个内存整理必须移动存活对象，是无法并发的，这样停顿时间就会变长。还有另外一个参数 -XX**:**CMSFullGCsBeforeCompaction，这个参数的作用是要求CMS在执行过若干次不整理空间的 Full GC 之后，下一次进入 Full GC 前会先进行碎片整理（默认值为0，表示每次进入 Full GC 时都进行碎片整理）。

## 13. 详细说一下G1的回收过程？

G1（Garbage First）回收器采用面向局部收集的设计思路和基于Region的内存布局形式，是一款主要面向服务端应用的垃圾回收器。G1设计初衷就是替换 CMS，成为一种全功能收集器。G1 在JDK9 之后成为服务端模式下的默认垃圾回收器，取代了 Parallel Scavenge 加 Parallel Old 的默认组合，而 CMS 被声明为不推荐使用的垃圾回收器。G1从整体来看是基于 标记-整理 算法实现的回收器，但从局部（两个Region之间）上看又是基于 标记-复制 算法实现的。

**G1 回收过程**，G1 回收器的运作过程大致可分为四个步骤：

1. 初始标记（会STW）：仅仅只是标记一下 GC Roots 能直接关联到的对象，并且修改TAMS指针的值，让下一阶段用户线程并发运行时，能正确地在可用的Region中分配新对象。这个阶段需要停顿线程，但耗时很短，而且是借用进行Minor GC的时候同步完成的，所以G1收集器在这个阶段实际并没有额外的停顿。
2. 并发标记：从 GC Roots 开始对堆中对象进行可达性分析，递归扫描整个堆里的对象图，找出要回收的对象，这阶段耗时较长，但可与用户程序并发执行。当对象图扫描完成以后，还要重新处理在并发时有引用变动的对象。
3. 最终标记（会STW）：对用户线程做短暂的暂停，处理并发阶段结束后仍有引用变动的对象。
4. 清理阶段（会STW）：更新Region的统计数据，对各个Region的回收价值和成本进行排序，根据用户所期望的停顿时间来制定回收计划，可以自由选择任意多个Region构成回收集，然后把决定回收的那一部分Region的存活对象复制到空的Region中，再清理掉整个旧Region的全部空间。这里的操作涉及存活对象的移动，必须暂停用户线程，由多条回收器线程并行完成的。

## 14.  JVM中一次完整的GC是什么样子的？

先描述一下Java堆内存划分。

在 Java 中，堆被划分成两个不同的区域：新生代 ( Young )、老年代 ( Old )，新生代默认占总空间的 1/3，老年代默认占 2/3。新生代有 3 个分区：Eden、To Survivor、From Survivor，它们的默认占比是 8:1:1。

新生代的垃圾回收（又称Minor GC）后只有少量对象存活，所以选用复制算法，只需要少量的复制成本就可以完成回收。

老年代的垃圾回收（又称Major GC）通常使用“标记-清理”或“标记-整理”算法。

![图片](https://mmbiz.qpic.cn/mmbiz_png/EyPNic5dZCg8FHJlP9F0gqmZtLe5rbUYhxqyXIFOEBzvYt7YAsHMWZ1bvlSBbOVCjNdLrMLvyEnW3VPUShIggKg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

再描述它们之间转化流程：

- 对象优先在Eden分配。当 eden 区没有足够空间进行分配时，虚拟机将发起一次 Minor GC。

- - Eden 区再次 GC，这时会采用复制算法，将 Eden 和 from 区一起清理，存活的对象会被复制到 to 区；
  - 移动一次，对象年龄加 1，对象年龄大于一定阀值会直接移动到老年代。GC年龄的阀值可以通过参数 -XX:MaxTenuringThreshold 设置，默认为 15；
  - 动态对象年龄判定：Survivor 区相同年龄所有对象大小的总和 > (Survivor 区内存大小 * 这个目标使用率)时，大于或等于该年龄的对象直接进入老年代。其中这个使用率通过 -XX:TargetSurvivorRatio 指定，默认为 50%；
  - Survivor 区内存不足会发生担保分配，超过指定大小的对象可以直接进入老年代。
  - 在 Eden 区执行了第一次 GC 之后，存活的对象会被移动到其中一个 Survivor 分区；

- 大对象直接进入老年代，大对象就是需要大量连续内存空间的对象（比如：字符串、数组），为了避免为大对象分配内存时由于分配担保机制带来的复制而降低效率。

- 老年代满了而**无法容纳更多的对象**，Minor GC 之后通常就会进行Full GC，Full GC 清理整个内存堆 – **包括年轻代和老年代**。

## 15. Minor GC 和 Full GC 有什么不同呢？

Minor GC：只收集新生代的GC。

Full GC: 收集整个堆，包括 新生代，老年代，永久代(在 JDK 1.8及以后，永久代被移除，换为metaspace 元空间)等所有部分的模式。

**Minor GC触发条件：**当Eden区满时，触发Minor GC。

**Full GC触发条件**：

- 通过Minor GC后进入老年代的平均大小大于老年代的可用内存。如果发现统计数据说之前Minor GC的平均晋升大小比目前old gen剩余的空间大，则不会触发Minor GC而是转为触发full GC。
- 老年代空间不够分配新的内存（或永久代空间不足，但只是JDK1.7有的，这也是用元空间来取代永久代的原因，可以减少Full GC的频率，减少GC负担，提升其效率）。
- 由Eden区、From Space区向To Space区复制时，对象大小大于To Space可用内存，则把该对象转存到老年代，且老年代的可用内存小于该对象大小。
- 调用System.gc时，系统建议执行Full GC，但是不必然执行。

## 16. 介绍下空间分配担保原则？

如果YougGC时新生代有大量对象存活下来，而 survivor 区放不下了，这时必须转移到老年代中，但这时发现老年代也放不下这些对象了，那怎么处理呢？其实JVM有一个老年代空间分配担保机制来保证对象能够进入老年代。

在执行每次 YoungGC 之前，JVM会先检查老年代最大可用连续空间是否大于新生代所有对象的总大小。因为在极端情况下，可能新生代 YoungGC 后，所有对象都存活下来了，而 survivor 区又放不下，那可能所有对象都要进入老年代了。这个时候如果老年代的可用连续空间是大于新生代所有对象的总大小的，那就可以放心进行 YoungGC。但如果老年代的内存大小是小于新生代对象总大小的，那就有可能老年代空间不够放入新生代所有存活对象，这个时候JVM就会先检查 -XX:HandlePromotionFailure 参数是否允许担保失败，如果允许，就会判断老年代最大可用连续空间是否大于历次晋升到老年代对象的平均大小，如果大于，将尝试进行一次YoungGC，尽快这次YoungGC是有风险的。如果小于，或者 -XX:HandlePromotionFailure 参数不允许担保失败，这时就会进行一次 Full GC。

在允许担保失败并尝试进行YoungGC后，可能会出现三种情况：

- ① YoungGC后，存活对象小于survivor大小，此时存活对象进入survivor区中
- ② YoungGC后，存活对象大于survivor大小，但是小于老年大可用空间大小，此时直接进入老年代。
- ③ YoungGC后，存活对象大于survivor大小，也大于老年大可用空间大小，老年代也放不下这些对象了，此时就会发生“Handle Promotion Failure”，就触发了 Full GC。如果 Full GC后，老年代还是没有足够的空间，此时就会发生OOM内存溢出了。

通过下图来了解空间分配担保原则：

![图片](https://mmbiz.qpic.cn/mmbiz_png/EyPNic5dZCg8FHJlP9F0gqmZtLe5rbUYh08xEquozNoO5QHb4dVR9hNA6pT5dxEIFkEZ4T0SD0VhVqDOqBR4Uug/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 17. 什么是类加载？类加载的过程？

虚拟机把描述类的数据加载到内存里面，并对数据进行校验、解析和初始化，最终变成可以被虚拟机直接使用的class对象；

类的整个生命周期包括：加载（Loading）、验证（Verification）、准备(Preparation)、解析(Resolution)、初始化(Initialization)、使用(Using)和卸载(Unloading)7个阶段。其中准备、验证、解析3个部分统称为连接（Linking）。如图所示：

![图片](https://mmbiz.qpic.cn/mmbiz_png/EyPNic5dZCg8FHJlP9F0gqmZtLe5rbUYhnc1OicdwaVWa0h2ddm2dFibETMGLtMnkDQcTZQ0bG7ibYT5hCcWh6tkqQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)image-20210329231258940

加载、验证、准备、初始化和卸载这5个阶段的顺序是确定的，类的加载过程必须按照这种顺序按部就班地开始，而解析阶段则不一定：它在某些情况下可以在初始化阶段之后再开始，这是为了支持Java语言的运行时绑定（也称为动态绑定或晚期绑定）

类加载过程如下：

- 加载，加载分为三步：1、通过类的全限定性类名获取该类的二进制流；2、将该二进制流的静态存储结构转为方法区的运行时数据结构；3、在堆中为该类生成一个class对象；
- 验证：验证该class文件中的字节流信息复合虚拟机的要求，不会威胁到jvm的安全；
- 准备：为class对象的静态变量分配内存，初始化其初始值；
- 解析：该阶段主要完成符号引用转化成直接引用；
- 初始化：到了初始化阶段，才开始执行类中定义的java代码；初始化阶段是调用类构造器的过程；

## 18. 什么是类加载器，常见的类加载器有哪些？

类加载器是指：通过一个类的全限定性类名获取该类的二进制字节流叫做类加载器；类加载器分为以下四种：

- 启动类加载器（BootStrapClassLoader）：用来加载java核心类库，无法被java程序直接引用；
- 扩展类加载器（Extension ClassLoader）：用来加载java的扩展库，java的虚拟机实现会提供一个扩展库目录，该类加载器在扩展库目录里面查找并加载java类；
- 系统类加载器（AppClassLoader）：它根据java的类路径来加载类，一般来说，java应用的类都是通过它来加载的；
- 自定义类加载器：由java语言实现，继承自ClassLoader；

![图片](https://mmbiz.qpic.cn/mmbiz_png/EyPNic5dZCg8FHJlP9F0gqmZtLe5rbUYhlGjuBYYPIG8q58lKlP59FZlN3EPBqax164KABSWxr2bUInzZgEbngA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 19. 什么是双亲委派模型？为什么需要双亲委派模型？

当一个类加载器收到一个类加载的请求，他首先不会尝试自己去加载，而是将这个请求委派给父类加载器去加载，只有父类加载器在自己的搜索范围类查找不到给类时，子加载器才会尝试自己去加载该类；

为了防止内存中出现多个相同的字节码；因为如果没有双亲委派的话，用户就可以自己定义一个java.lang.String类，那么就无法保证类的唯一性。

补充：**那怎么打破双亲委派模型**？

自定义类加载器，继承ClassLoader类，重写loadClass方法和findClass方法。

## 20. 列举一些你知道的打破双亲委派机制的例子，为什么要打破？

- JNDI 通过引入线程上下文类加载器，可以在 Thread.setContextClassLoader 方法设置，默认是应用程序类加载器，来加载 SPI 的代码。有了线程上下文类加载器，就可以完成父类加载器请求子类加载器完成类加载的行为。打破的原因，是为了 JNDI 服务的类加载器是启动器类加载，为了完成高级类加载器请求子类加载器（即上文中的线程上下文加载器）加载类。

- Tomcat，应用的类加载器优先自行加载应用目录下的 class，并不是先委派给父加载器，加载不了才委派给父加载器。

  tomcat之所以造了一堆自己的classloader，大致是出于下面三类目的：

  tomcat类加载器如下图：

  ![图片](https://mmbiz.qpic.cn/mmbiz_png/EyPNic5dZCg8FHJlP9F0gqmZtLe5rbUYhxxGqQdGRmxr72VVSn1jTSO4SG994Y3fJic34JVGx0nBpR3ooDKhVADA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

- - 对于各个 `webapp`中的 `class`和 `lib`，需要相互隔离，不能出现一个应用中加载的类库会影响另一个应用的情况，而对于许多应用，需要有共享的lib以便不浪费资源。
  - 与 `jvm`一样的安全性问题。使用单独的 `classloader`去装载 `tomcat`自身的类库，以免其他恶意或无意的破坏；
  - 热部署。

- OSGi，实现模块化热部署，为每个模块都自定义了类加载器，需要更换模块时，模块与类加载器一起更换。其类加载的过程中，有平级的类加载器加载行为。打破的原因是为了实现模块热替换。

- JDK 9，Extension ClassLoader 被 Platform ClassLoader 取代，当平台及应用程序类加载器收到类加载请求，在委派给父加载器加载前，要先判断该类是否能够归属到某一个系统模块中，如果可以找到这样的归属关系，就要优先委派给负责那个模块的加载器完成加载。打破的原因，是为了添加模块化的特性。

## 21.说一下 JVM 调优的命令？

- jps：JVM Process Status Tool,显示指定系统内所有的HotSpot虚拟机进程。
- jstat：jstat(JVM statistics Monitoring)是用于监视虚拟机运行时状态信息的命令，它可以显示出虚拟机进程中的类装载、内存、垃圾收集、JIT编译等运行数据。
- jmap：jmap(JVM Memory Map)命令用于生成heap dump文件，如果不使用这个命令，还阔以使用-XX:+HeapDumpOnOutOfMemoryError参数来让虚拟机出现OOM的时候·自动生成dump文件。jmap不仅能生成dump文件，还阔以查询finalize执行队列、Java堆和永久代的详细信息，如当前使用率、当前使用的是哪种收集器等。
- jhat：jhat(JVM Heap Analysis Tool)命令是与jmap搭配使用，用来分析jmap生成的dump，jhat内置了一个微型的HTTP/HTML服务器，生成dump的分析结果后，可以在浏览器中查看。在此要注意，一般不会直接在服务器上进行分析，因为jhat是一个耗时并且耗费硬件资源的过程，一般把服务器生成的dump文件复制到本地或其他机器上进行分析。
- jstack：jstack用于生成java虚拟机当前时刻的线程快照。jstack来查看各个线程的调用堆栈，就可以知道没有响应的线程到底在后台做什么事情，或者等待什么资源。如果java程序崩溃生成core文件，jstack工具可以用来获得core文件的java stack和native stack的信息，从而可以轻松地知道java程序是如何崩溃和在程序何处发生问题。

## 22.真实项目中如何排查jvm问题

对于还在正常运行的系统：
1.可以使用jmap来查看jvm中各个区域的使用情况
2.可以通过使用jstack来查看线程的运行情况，比如哪些线程阻塞、是否出现了死锁
3.可以通过jstat命令来查看垃圾回收的情况，特别是fullgc，如果发现fullgc比较频繁，那么就得进行调优了
4.通过各个命令的结果，或者jvisualvm等工具来进行分析
5.首先，初步猜测频繁发送fullgc的原因，如果频繁发生fullgc但是又一直没有出现内存溢出，那么表示fullgc实际上是回收了很多对象了，所以这些对象最好能在younggc过程中就直接回收掉，避免这些对象进入老年代，对于这种情况，就要考虑这些存活时间不长的对象是不是比较大，导致年轻代放不下，直接进入了老年代，尝试加大年轻代的大小，如果改完之后，fullgc减少，则证明修改有效
6.同时，还可以找到占用CPU最多的线程，定位到具体的方法，优化这个方法的执行，看是否能避免某些对象的创建，从而节省内存

对于已经发生OOM的系统：
1.一般生产系统中都会设置当系统发生OOM时，生成当时的dump文件（-XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/usr/local/base）
2.我们可以利用jvisualvm等工具来分析dump文件
3.根据dump文件找到异常的实例对象，和异常的线程（占用CPU高），定位到具体的代码
4.然后再进行详细的分析和调试

总之，调优不是一蹴而就的，需要分析、推理、实践、总结、再分析，最终定位到具体的问题



## 23. System.GC

**在 Java 中，如何手动的让 GC 进行垃圾回收？**

这个方法其实有很多种。常见骚操作有 System.gc()，通过 jmap 来触发，或者通过 jvmti 做强制 GC 等。

**System.gc 是 Full Gc 吗？**

System.gc 其实是做一次 full gc。这一点可以根据 DisableExplicitGC 的注释说明来看。Tells whether calling System.gc() does a full GC。

**System.gc 的危害是什么？**

因为 System.gc 是一个 Full gc，所以会暂停整个进程。如果进程经常被频繁暂停，就要注意超时、并发等问题。

**如何避免 System.gc ？**

通过 -XX:+DisableExplicitGC 禁掉 System.gc。

**System.gc 的 Full Gc 如何做到暂停整个进程？**

Java 里面的 GC 有一个重要的线程 VMThread。在 jvm 里，这个线程会不断轮询它的队列，这个队列里主要是存一些 VM_operation 的动作，比如最常见的就是内存分配失败要求做 GC 操作的请求等，在对 gc 这些操作执行的时候会先将其他业务线程都进入到安全点，也就是这些线程从此不再执行任何字节码指令，只有当出了安全点的时候才让他们继续执行原来的指令，因此这其实就是我们说的 stop the world(STW)，整个进程相当于静止了。

**并行的 Full GC 是否有了解？**

并行 Full GC 也同样会做 YGC 和 CMS GC，但是效率高就搞在 CMS GC 是走的 background 的，整个暂停的过程主要是 YGC、CMS_initMark、CMS_remark 几个阶段。background 顾名思义是在后台做的，也就是可以不影响正常的业务线程跑，触发条件比如说 old 的内存占比超过多少的时候就可能触发一次 background 式的 cms gc，这个过程会经历 CMS GC 的所有阶段，该暂停的暂停，该并行的并行，效率相对来说还比较高，毕竟有和业务线程并行的 gc 阶段；而 foreground 则不然，它发生的场景比如业务线程请求分配内存，但是内存不够了，于是可能触发一次 cms gc，这个过程就必须是要等内存分配到了线程才能继续往下面走的，因此整个过程必须是STW的，因此 CMS GC 整个过程都是暂停应用的，但是为了提高效率，它并不是每个阶段都会走的，只走其中一些阶段，这些省下来的阶段主要是并行阶段。

