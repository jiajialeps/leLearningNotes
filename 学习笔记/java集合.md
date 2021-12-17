## 1.Java中的集合框架有哪些？

回答：Java 集合框架主要包括两种类型的容器，一种是集合（Collection），存储一个元素集合，另一种是图（Map），存储键/值对映射。

Collection 接口又有 3 种子类型，List、Set 和 Queue，再下面是一些抽象类，最后是具体实现类，常用的有 ArrayList、LinkedList、HashSet、LinkedHashSet、HashMap、TreeMap、LinkedHashMap 等等。

![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcyMDE4LmNuYmxvZ3MuY29tL290aGVyLzE0MDgxODMvMjAxOTExLzE0MDgxODMtMjAxOTExMTkxODQxNDk1NTktMTU3MTU5NTY2OC5qcGc?x-oss-process=image/format,png)

### 集合框架底层数据结构

Collection

1. List

- Arraylist： Object数组
- Vector： Object数组
- LinkedList： 双向循环链表

1. Set

- HashSet（无序，唯一）：基于 HashMap 实现的，底层采用 HashMap 来保存元素
- LinkedHashSet： LinkedHashSet 继承与 HashSet，并且其内部是通过 LinkedHashMap 来实现的。有点类似于我们之前说的LinkedHashMap 其内部是基于 Hashmap 实现一样，不过还是有一点点区别的。
- TreeSet（有序，唯一）： 红黑树(自平衡的排序二叉树。)

Map

- HashMap： JDK1.8之前HashMap由数组+链表组成的，数组是HashMap的主体，链表则是主要为了解决哈希冲突而存在的（“拉链法”解决冲突）.JDK1.8以后在解决哈希冲突时有了较大的变化，当链表长度大于阈值（默认为8）时，将链表转化为红黑树，以减少搜索时间
- LinkedHashMap：LinkedHashMap 继承自 HashMap，所以它的底层仍然是基于拉链式散列结构即由数组和链表或红黑树组成。另外，LinkedHashMap 在上面结构的基础上，增加了一条双向链表，使得上面的结构可以保持键值对的插入顺序。同时通过对链表进行相应的操作，实现了访问顺序相关逻辑。
- HashTable： 数组+链表组成的，数组是 HashMap 的主体，链表则是主要为了解决哈希冲突而存在的
- TreeMap： 红黑树（自平衡的排序二叉树）

### 哪些集合类是线程安全的？

- vector：就比arraylist多了个同步化机制（线程安全），因为效率较低，现在已经不太建议使用。在web应用中，特别是前台页面，往往效率（页面响应速度）是优先考虑的。
- statck：堆栈类，先进后出。
- hashtable：就比hashmap多了个线程安全。
- enumeration：枚举，相当于迭代器。



## 2.ArrayList和LinkedList的底层实现和区别？

回答：ArrayList底层使用的是 **Object**数组；LinkedList底层使用的是 **双向链表** 数据结构。

ArrayList:增删慢、查询快，线程不安全，对元素必须连续存储。

LinkedList:增删快，查询慢，线程不安全。

### 追问：说说ArrayList的扩容机制？

回答：通过阅读ArrayList的源码我们可以发现当以无参数构造方法创建 ArrayList 时，实际上初始化赋值的是一个**空数组**。当真正对数组进行添加元素操作时，才真正分配容量。即向数组中添加第一个元素时，数组容量扩为 **10**。当插入的元素个数大于当前容量时，就需要进行扩容了， **ArrayList 每次扩容之后容量都会变为原来的 1.5 倍左右**。

## 3.HashMap的底层实现？扩容？是否线程安全？

回答：在jdk1.7之前HashMap是基于数组和链表实现的，而且采用头插法。

而jdk1.8 之后在解决哈希冲突时有了较大的变化，当链表长度大于阈值（默认为 8）（将链表转换成红黑树前会判断，如果当前数组的长度小于 64，那么会选择先进行数组扩容，而不是转换为红黑树）时，将链表转化为红黑树，以减少搜索时间。采用尾插法。

HashMap默认的初始化大小为 16。当HashMap中的**元素个数之和**大于负载因子*当前容量的时候就要进行扩充，容量变为原来的 2 倍。（这里注意不是数组中的个数，而且数组中和链/树中的所有元素个数之和！）

> 注意：我们还可以在预知存储数据量的情况下，提前设置初始容量（初始容量 = 预知数据量 / 加载因子）。这样做的好处是可以减少 resize() 操作，提高 HashMap 的效率
>
> 美团面试的时候问到这个问题，还给出具体的值，让我算出初始值设置为多少合适？

HashMap是**线程不安全**的，其主要体现：

1.在jdk1.7中，在多线程环境下，扩容时会造成**环形链**或数据丢失。

2.在jdk1.8中，在多线程环境下，会发生**数据覆盖**的情况。

### 追问：HashMap扩容的时候为什么是2的n次幂？

回答：数组下标的计算方法是（n-1）& hash，取余(%)操作中如果除数是2的幂次则等价于与其除数减一的与(&)操作（也就是说 hash%length==hash&(length-1)的前提是 length 是2的 n 次方；）。并且采用二进制位操作 &，相对于%能够提高运算效率，这就解释了 HashMap 的长度为什么是2的幂次方。



**第一问：** 为什么使用链表+数组：要知道为什么使用链表首先需要知道Hash冲突是如何来的：

答： 由于我们的数组的值是限制死的，我们在对key值进行散列取到下标以后，放入到数组中时，难免出现两个key值不同，但是却放入到下标相同的**格子**中，此时我们就可以使用链表来对其进行链式的存放。

**第二问** 我⽤LinkedList代替数组结构可以吗？对于题目的意思是说，在源码中我们是这样的

```javascript
Entry[] table=new Entry[capacity];// entry就是一个链表的节点
```

现在进行替换，进行如下的实现

```sql
List table=new LinkedList();
```

是否可以行得通？ 答案当然是肯定的。

**第三问** 那既然可以使用进行替换处理，为什么有偏偏使用到数组呢？因为⽤数组效率最⾼！ 在HashMap中，定位节点的位置是利⽤元素的key的哈希值对数组⻓度取模得到。此时，我们已得到节点的位置。显然数组的查 找效率⽐LinkedList⼤(底层是链表结构)。那ArrayList，底层也是数组，查找也快啊，为啥不⽤ArrayList? 因为采用基本数组结构，扩容机制可以⾃⼰定义，HashMap中数组扩容刚好是**2的次幂**，在做取模运算的效率⾼。 ⽽ArrayList的扩容机制是1.5倍扩容(这一点我相信学习过的都应该清楚)，那ArrayList为什么是1.5倍扩容这就不在本⽂说明了。

### 追问：HashMap的put方法说一下。

![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly91cGxvYWQtaW1hZ2VzLmppYW5zaHUuaW8vdXBsb2FkX2ltYWdlcy83ODk2ODkwLTc5OGYxMzg3ZTNmOGRlOWEucG5n?x-oss-process=image/format,png)

回答：通过阅读源码，可以从jdk1.7和1.8两个方面来回答

1.根据key通过哈希算法与与运算得出数组下标

2.如果数组下标元素为空，则将key和value封装为Entry对象（JDK1.7是Entry对象，JDK1.8是Node对象）并放入该位置。

3.如果数组下标位置元素不为空，则要分情况

(i)如果是在JDK1.7，则**首先会判断是否需要扩容**，如果要扩容就进行扩容，如果不需要扩容就生成Entry对象，并使用**头插法**添加到当前链表中。

(ii)如果是在JDK1.8中，则会先判断当前位置上的TreeNode类型，看是红黑树还是链表Node

(a)如果是红黑树TreeNode，则将key和value封装为一个红黑树节点并添加到红黑树中去，在这个过程中会判断红黑树中是否存在当前key，如果存在则更新value。

(b)如果此位置上的Node对象是链表节点，则将key和value封装为一个Node并通过尾插法插入到链表的最后位置去，因为是尾插法，所以需要遍历链表，在遍历过程中会判断是否存在当前key，如果存在则更新其value，当遍历完链表后，将新的Node插入到链表中，插入到链表后，会看当前链表的节点个数，如果大于8，则会将链表转为红黑树

(c)将key和value封装为Node插入到链表或红黑树后，在判断是否需要扩容，如果需要扩容，就结束put方法。

### 追问：HashMap源码中在计算hash值的时候为什么要右移16位？

回答：我的理解是让元素在HashMap中更加均匀的分布，具体的可以看下图，下图是《阿里调优手册》里说的。

![图片](https://mmbiz.qpic.cn/mmbiz_png/GG9HBCEFx2UkGCDeZD4Ye5r3fBafibyM06HxvFU5ibKkaqDTSGJrOCGJV6ibicFxjurZ4vruaf2RZ1XzRAZfWgv1mA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 4.Java中线程安全的集合有哪些？

Vector：就比Arraylist多了个同步化机制（线程安全）。

Hashtable：就比Hashmap多了个线程安全。

ConcurrentHashMap:是一种高效但是线程安全的集合。

Stack：栈，也是线程安全的，继承于Vector。

### 追问：说一下ConcurrentHashMap的底层实现，它为什么是线程安全的？

回答：在jdk1.7是 **分段的数组+链表** ，jdk1.8的时候跟HashMap1.8的时候一样都是基于数组+链表/红黑树。

ConcurrentHashMap是线程安全的

（1）在jdk1.7的时候是使用分段所segment，每一把锁只锁容器其中一部分数据，多线程访问容器里不同数据段的数据，就不会存在锁竞争，提高并发访问率。

（2）在jdk1.8的时候摒弃了 Segment的概念，而是直接用 Node 数组+链表+红黑树的数据结构来实现，并发控制使用 **synchronized** 和 **CAS** 来操作。synchronized只锁定当前链表或红黑二叉树的首节点。

## 5.HashMap和Hashtable的区别

回答：

（1）**线程是否安全：** `HashMap` 是非线程安全的，`HashTable` 是线程安全的,因为 `HashTable` 内部的方法基本都经过`synchronized` 修饰。（如果你要保证线程安全的话就使用 `ConcurrentHashMap` 吧！）；

（2）**对 Null key 和 Null value 的支持：** `HashMap` 可以存储 null 的 key 和 value，但 null 作为键只能有一个，null 作为值可以有多个；HashTable 不允许有 null 键和 null 值，否则会抛出 `NullPointerException`。

（3）**初始容量大小和每次扩充容量大小的不同 ：** ① 创建时如果不指定容量初始值，`Hashtable` 默认的初始大小为 11，之后每次扩充，容量变为原来的 2n+1。`HashMap` 默认的初始化大小为 16。之后每次扩充，容量变为原来的 2 倍。② 创建时如果给定了容量初始值，那么 Hashtable 会直接使用你给定的大小，而 `HashMap` 会将其扩充为 2 的幂次方大小（`HashMap` 中的`tableSizeFor()`方法保证，下面给出了源代码）。也就是说 `HashMap` 总是使用 2 的幂作为哈希表的大小,后面会介绍到为什么是 2 的幂次方。

（4）**底层数据结构：** JDK1.8 以后的 `HashMap` 在解决哈希冲突时有了较大的变化，当链表长度大于阈值（默认为 8）（将链表转换成红黑树前会判断，如果当前数组的长度小于 64，那么会选择先进行数组扩容，而不是转换为红黑树）时，将链表转化为红黑树，以减少搜索时间。Hashtable 没有这样的机制。

（5）**效率：** 因为线程安全的问题，`HashMap` 要比 `HashTable` 效率高一点。另外，`HashTable` 基本被淘汰，不要在代码中使用它；

## 6.HashMap和TreeMap的区别？

回答：

1、HashMap是通过hash值进行快速查找的；HashMap中的元素是没有顺序的；TreeMap中所有的元素都是有某一固定顺序的，如果需要得到一个有序的结果，就应该使用TreeMap；

2、HashMap和TreeMap都是线程不安全的；

3、HashMap继承AbstractMap类；覆盖了hashcode() 和equals() 方法，以确保两个相等的映射返回相同的哈希值；

TreeMap继承SortedMap类；他保持键的有序顺序；

4、HashMap：基于hash表实现的；使用HashMap要求添加的键类明确定义了hashcode() 和equals() （可以重写该方法）；为了优化HashMap的空间使用，可以调优初始容量和负载因子；

TreeMap：基于红黑树实现的；TreeMap就没有调优选项，因为红黑树总是处于平衡的状态；

5、HashMap：适用于Map插入，删除，定位元素；

TreeMap：适用于按自然顺序或自定义顺序遍历键（key）

# ConcurrentHashMap在jdk1.7和jdk1.8中的不同；



## CouncurrentHashMap 线程安全

### 一、CouncurrentHashMap<jdk1.7>

#### 1、底层：

##### （1）底层数据结构：

<jdk1.7>：数组（Segment） + 数组（HashEntry） + 链表（HashEntry节点）
底层一个Segments数组，存储一个Segments对象，一个Segments中储存一个Entry数组，存储的每个Entry对象又是一个链表头结点。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190426100401737.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODg0OTc2,size_16,color_FFFFFF,t_70)

##### （2）基本属性：

jdk1,7
两个主要的内部类：
class Segment内部类，继承ReentrantLock，有一个HashEntry数组，用来存储链表头结点

jdk1,7
两个主要的内部类：
class Segment内部类，继承ReentrantLock，有一个HashEntry数组，用来存储链表头结点

```java
int  count ；  // 此对象中存放的HashEntry个数
int threshold ； //扩容阈值
volatile HashEntry<K,V>[] table;   //储存entry的数组，每一个entry都是链表的头部
float loadFactor;    //加载因子
```

方法：

```java
 v  get（Object key, int hash）； 获取相应元素  
注意：此方法并不加锁，因为只是读操作，
 V put(K key, int hash, V value, boolean onlyIfAbsent)
注意：此方法加锁
```

class HashEntry 定义的节点，里面存储的数据和下一个节点，在此不分析

##### （3）主要方法：

get（）：
1、第一次哈希 找到 对应的Segment段，
调用Segment中的get方法
2、再次哈希找到对应的链表，
3、最后在链表中查找。

```java
// 外部类方法
public V get(Object key) {
    int hash = hash(key.hashCode());
    return segmentFor(hash).get(key, hash); // 第一次hash 确定段的位置
}

//以下方法是在Segment对象中的方法；

//确定段之后在段中再次hash，找出所属链表的头结点。
final Segment<K,V> segmentFor(int hash) {    
    return segments[(hash >>> segmentShift) & segmentMask];
}

V get(Object key, int hash) {
    if (count != 0) { // read-volatile
        HashEntry<K,V> e = getFirst(hash);
        while (e != null) {
            if (e.hash == hash && key.equals(e.key)) {
                V v = e.value;
                if (v != null)
                    return v;
                return readValueUnderLock(e); // recheck
            }
            e = e.next;
        }
    }
    return null;
}
12345678910111213141516171819202122232425262728
```

put（）：
1、首先确定段的位置，
调用Segment中的put方法：
2、加锁
3、检查当前Segment数组中包含的HashEntry节点的个数，如果超过阈值就重新hash
4、然后再次hash确定放的链表。
5、在对应的链表中查找是否相同节点，如果有直接覆盖，如果没有将其放置链表尾部

```java
//外部类方法
public V put(K key, V value) {
        if (value == null)
            throw new NullPointerException();
        int hash = hash(key.hashCode());
        return segmentFor(hash).put(key, hash, value, false);  //先确定段的位置
    }

   // Segment类中的方法    
V put(K key, int hash, V value, boolean onlyIfAbsent) {
    lock();
    try {
        int c = count;
        if (c++ > threshold) // 如果当个数超过阈值，就重新hash当前段的元素 ，
            rehash();  
        HashEntry<K,V>[] tab = table;
        int index = hash & (tab.length - 1);
        HashEntry<K,V> first = tab[index];
        HashEntry<K,V> e = first;
        while (e != null && (e.hash != hash || !key.equals(e.key)))
            e = e.next;
  
        V oldValue;
        if (e != null) {
            oldValue = e.value;
            if (!onlyIfAbsent)
                e.value = value;
        }
        else {
            oldValue = null;
            ++modCount;
            tab[index] = new HashEntry<K,V>(key, hash, first, value);
            count = c; // write-volatile
        }
        return oldValue;
    } finally {
        unlock();
    }
}
 
```

##### （4） 重哈希方式 ：重点：

重哈希的方式 ：只是对 Segments对象中的Hashentry数组进行重哈希

#### 2、通过什么保证线程安全

<JDK1.7>，
分段锁 对整个桶数组进行了分割分段(Segment)，每一把锁只锁容器其中一部分数据，[多线程](https://so.csdn.net/so/search?from=pc_blog_highlight&q=多线程)访问容器里不同数据段的数据，就不会存在锁竞争，提高并发访问率。
<jdk1.8>
使用的是优化的synchronized 关键字同步代码块 和 cas操作了维护并发。

#### 3、和 hashTable的保证线程安全的机制有何联系

Hashtable通过synchronized修饰方法 来保证线程安全
通过segment（继承了ReentrantLock）调用父类的锁对象加锁来实现，

#### 4、hashMap、 hashTable、 和 ConcurrentHashMap的区别

主要区别：
（1）：实现线程安全的方式
hashMap是线程不安全的，
hashTable是线程安全的，实现线程安全的机制是使用Synchronized关键字修饰方法。
ConcurrentHashMap
<JDK1.7>，
ConcurrentHashMap（分段锁） 对整个桶数组进行了分割分段(Segment)，每一把锁只锁容器其中一部分数据，多线程访问容器里不同数据段的数据，就不会存在锁竞争，提高并发访问率。
<jdk1.8>
使用的是优化的synchronized 关键字 和 cas操作了维护并发。
（2）：底层数据结构：
hashMap同hashTable；都是使用数组 + 链表结构
ConcurrentHashMap
<jdk1.7> ：使用 Segment数组 + HashEntry数组 + 链表
<jdk1.8> ：使用 Node数组+链表+ 红黑树
（3） ： 效率
hashMap只能单线程操作，效率低下
hashTable使用的是synchronized方法锁，若一个线程抢夺了锁，其他线程只能等到持锁线程操作完成之后才能抢锁操作
《1.7》ConcurrentHashMap 使用的分段锁，如果一个线程占用一段，别的线程可以操作别的部分，
《1.8》简化结构，put和get不用二次哈希，一把锁只锁住一个链表或者一棵树，并发效率更加提升。

### 二、CouncurrentHashMap<jdk1.8>

#### 1.底层：

#### (1) 数据结构：

Node数组+链表 / 红黑树： 类似hashMap<jdk1.8>
Node数组使用来存放树或者链表的头结点，当一个链表中的数量到达一个数目时，会使查询速率降低，所以到达一定阈值时，会将一个链表转换为一个红黑二叉树，通告查询的速率。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190426101108134.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODg0OTc2,size_16,color_FFFFFF,t_70)

#### (2)主要属性：

```java
外部类的基本属性
volatile Node<K,V>[] table;   // Node数组用于存放链表或者树的头结点
static final int TREEIFY_THRESHOLD = 8;   // 链表转红黑树的阈值 > 8 时
static final int UNTREEIFY_THRESHOLD = 6;  // 红黑树转链表的阈值  <= 6 时
static final int TREEBIN   = -2;    // 树根节点的hash值
static final float LOAD_FACTOR = 0.75f;// 负载因子
static final int DEFAULT_CAPACITY = 16;   // 默认大小为16
内部类 
class Node<K,V> implements Map.Entry<K,V> {
    int hash;       
   final K key;       
   volatile V val;
   volatile Node<K,V> next;
}
jdk1.8中虽然不在使用分段锁，但是仍然有Segment这个类，但是没有实际作用
```

#### (3）主要方法：

##### 1、构造方法：

构造方法并没有直接new出来一个Node的数组，只是检查数值之后确定了容量大小。

```java
ConcurrentHashMap(int initialCapacity) {
        if (initialCapacity < 0)   
            throw new IllegalArgumentException(); 
       // 如果传入的数值>= 最大容量的一半，就使用最大容量，否则使用
       //1.5*initialCapacity +1 ，然后向上取最近的 2 的 n 次方数； 
        int cap = ((initialCapacity >= (MAXIMUM_CAPACITY >>> 1)) ?
                   MAXIMUM_CAPACITY :
                   tableSizeFor(initialCapacity + (initialCapacity >>> 1) + 1));
        this.sizeCtl = cap;
    }
```

##### 2、put方法：

步骤：
1、检查Key或者Value是否为null，
2、得到Kye的hash值
3、如果Node数组是空的，此时才初始化 initTable()，
4、如果找的对应的下标的位置为空，直接new一个Node节点并放入， break；
5、如果对应头结点不为空， 进入同步代码块
判断此头结点的hash值，是否大于零，大于零则说明是链表的头结点在链表中寻找，
如果有相同hash值并且key相同，就直接覆盖，返回旧值 结束
如果没有则就直接放置在链表的尾部
此头节点的Hash值小于零，则说明此节点是红黑二叉树的根节点
调用树的添加元素方法
判断当前数组是否要转变为红黑树

```java
public V put(K key, V value) {
    return putVal(key, value, false);
}
final V putVal(K key, V value, boolean onlyIfAbsent) {
    if (key == null || value == null) throw new NullPointerException();
    int hash = spread(key.hashCode());// 得到 hash 值
    int binCount = 0;   // 用于记录相应链表的长度
    for (Node<K,V>[] tab = table;;) {
        Node<K,V> f; int n, i, fh;
        // 如果数组"空"，进行数组初始化
        if (tab == null || (n = tab.length) == 0)
            // 初始化数组
            tab = initTable();
 
        // 找该 hash 值对应的数组下标，得到第一个节点 f
        else if ((f = tabAt(tab, i = (n - 1) & hash)) == null) {
            // 如果数组该位置为空，
            //    用一次 CAS 操作将新new出来的 Node节点放入数组i下标位置
            //          如果 CAS 失败，那就是有并发操作，进到下一个循环
            if (casTabAt(tab, i, null,
                         new Node<K,V>(hash, key, value, null)))
                break;          // no lock when adding to empty bin
        }
        // hash 居然可以等于 MOVED，这个需要到后面才能看明白，不过从名字上也能猜到，肯定是因为在扩容
         else if ((fh = f.hash) == MOVED)
            // 帮助数据迁移，这个等到看完数据迁移部分的介绍后，再理解这个就很简单了
            tab = helpTransfer(tab, f);
 
        else { // 到这里就是说，f 是该位置的头结点，而且不为空
 
            V oldVal = null;
            // 获取链表头结点监视器对象
            synchronized (f) {
                if (tabAt(tab, i) == f) {
                    if (fh >= 0) { // 头结点的 hash 值大于 0，说明是链表
                        // 用于累加，记录链表的长度
                        binCount = 1;
                        // 遍历链表
                        for (Node<K,V> e = f;; ++binCount) {
                            K ek;
                            // 如果发现了"相等"的 key，判断是否要进行值覆盖，然后也就可以 break 了
                            if (e.hash == hash &&
                                ((ek = e.key) == key ||
                                 (ek != null && key.equals(ek)))) {
                                oldVal = e.val;
                                if (!onlyIfAbsent)
                                    e.val = value;
                                break;
                            }
                            // 到了链表的最末端，将这个新值放到链表的最后面
                            Node<K,V> pred = e;
                            if ((e = e.next) == null) {
                                pred.next = new Node<K,V>(hash, key,
                                                          value, null);
                                break;
                            }
                        }
                    }
                    else if (f instanceof TreeBin) { // 红黑树
                        Node<K,V> p;
                        binCount = 2;
                        // 调用红黑树的插值方法插入新节点
                        if ((p = ((TreeBin<K,V>)f).putTreeVal(hash, key,
                                                       value)) != null) {
                            oldVal = p.val;
                            if (!onlyIfAbsent)
                                p.val = value;
                        }
                    }
                }
            }
            // binCount != 0 说明上面在做链表操作
            if (binCount != 0) {
                // 判断是否要将链表转换为红黑树，临界值： 8
                if (binCount >= TREEIFY_THRESHOLD)
                    // 如果当前数组的长度小于 64，那么会进行数组扩容，而不是转换为红黑树
                    treeifyBin(tab, i);   // 如果超过64，会转成红黑树
                if (oldVal != null)
                    return oldVal;
                break;
            }
        }
    }
    // 
    addCount(1L, binCount);
    return null;
}
```

##### 3、get 方法

首先获取到Key的hash值，
然后找到对应的数组下标处的元素
如果次元素是我们要找的，直接返回，
如果次元素是null 返回null
如果Key的值< 0 ,说明是红黑树，

```java
public V get(Object key) {
        Node<K,V>[] tab; Node<K,V> e, p; int n, eh; K ek;
        int h = spread(key.hashCode());   //获得Hash值
        if ((tab = table) != null && (n = tab.length) > 0 &&
            (e = tabAt(tab, (n - 1) & h)) != null) {
            if ((eh = e.hash) == h) {  // 比较 此头结点e是否是我们需要的元素
                if ((ek = e.key) == key || (ek != null && key.equals(ek)))
                    return e.val;   // 如果是，就返回
            }
            else if (eh < 0)   // 如果小于零，说明此节点是红黑树 
                return (p = e.find(h, key)) != null ? p.val : null;
            while ((e = e.next) != null) {
                // 开始循环 查找
                if (e.hash == h &&
                    ((ek = e.key) == key || (ek != null && key.equals(ek))))
                    return e.val;
            }
        }
        return null;
    }
```

##### 4、扩容：tryPresize（）

容后数组容量为原来的 2 倍。

```java
private final void tryPresize(int size) {
        int c = (size >= (MAXIMUM_CAPACITY >>> 1)) ? MAXIMUM_CAPACITY :
            tableSizeFor(size + (size >>> 1) + 1);
        int sc;
        while ((sc = sizeCtl) >= 0) {
            Node<K,V>[] tab = table; int n;
            if (tab == null || (n = tab.length) == 0) {
                n = (sc > c) ? sc : c;
                if (U.compareAndSwapInt(this, SIZECTL, sc, -1)) {
                    try {
                        if (table == tab) {
                            @SuppressWarnings("unchecked")
                            Node<K,V>[] nt = (Node<K,V>[])new Node<?,?>[n];
                            table = nt;
                            sc = n - (n >>> 2);
                        }
                    } finally {
                        sizeCtl = sc;
                    }
                }
            }
            else if (c <= sc || n >= MAXIMUM_CAPACITY)
                break;
            else if (tab == table) {
                int rs = resizeStamp(n);
                if (sc < 0) {
                    Node<K,V>[] nt;
                    if ((sc >>> RESIZE_STAMP_SHIFT) != rs || sc == rs + 1 ||
                        sc == rs + MAX_RESIZERS || (nt = nextTable) == null ||
                        transferIndex <= 0)
                        break;
                    if (U.compareAndSwapInt(this, SIZECTL, sc, sc + 1))
                        transfer(tab, nt);
                }
                else if (U.compareAndSwapInt(this, SIZECTL, sc,
                                             (rs << RESIZE_STAMP_SHIFT) + 2))
                    transfer(tab, null);
            }
        }
    }
```

##### 5.其他内部类结构

Node：
ConcurrentHashMap存储结构的基本单元，实现了Map.Entry接口，用于存储数据。它对value和next属性设置了volatile同步锁(与JDK7的Segment相同)，它不允许调用setValue方法直接改变Node的value域，它增加了find方法辅助map.get()方法。
TreeNode：
继承于Node，但是数据结构换成了二叉树结构，它是红黑树的数据的存储结构，用于红黑树中存储数据，当链表的节点数大于8时会转换成红黑树的结构，他就是通过TreeNode作为存储结构代替Node来转换成黑红树。
TreeBin：
从字面含义中可以理解为存储树形结构的容器，而树形结构就是指TreeNode，所以TreeBin就是封装TreeNode的容器，它提供转换黑红树的一些条件和锁的控制。
ForwardingNode：
一个用于连接两个table的节点类。它包含一个nextTable指针，用于指向下一张表。而且这个节点的key value next指针全部为null，它的hash值为-1. 这里面定义的find的方法是从nextTable里进行查询节点，而不是以自身为头节点进行查找。
Unsafe和CAS：
在ConcurrentHashMap中，随处可以看到U, 大量使用了U.compareAndSwapXXX的方法，这个方法是利用一个CAS算法实现无锁化的修改值的操作，他可以大大降低锁代理的性能消耗。这个算法的基本思想就是不断地去比较当前内存中的变量值与你指定的一个变量值是否相等，如果相等，则接受你指定的修改的值，否则拒绝你的操作。因为当前线程中的值已经不是最新的值，你的修改很可能会覆盖掉其他线程修改的结果。这一点与乐观锁，SVN的思想是比较类似的。

##### 6、通过什么保证线程安全

通过使用Synchroized关键字来同步代码块，而且只是在put方法中加锁，在get方法中没有加锁
在加锁时是使用头结点作为同步锁对象。，并且定义了三个原子操作方法

```java
/ 获取tab数组的第i个node<br>   
 @SuppressWarnings("unchecked")
static final <K,V> Node<K,V> tabAt(Node<K,V>[] tab, int i) {
    return (Node<K,V>)U.getObjectVolatile(tab, ((long)i << ASHIFT) + ABASE);
}
// 利用CAS算法设置i位置上的node节点。csa（你叫私有空间的值和内存中的值是否相等），即这个操作有可能不成功。
static final <K,V> boolean casTabAt(Node<K,V>[] tab, int i,
                                    Node<K,V> c, Node<K,V> v) {
    return U.compareAndSwapObject(tab, ((long)i << ASHIFT) + ABASE, c, v);
}
// 利用volatile方法设置第i个节点的值，这个操作一定是成功的。
static final <K,V> void setTabAt(Node<K,V>[] tab, int i, Node<K,V> v) {
    U.putObjectVolatile(tab, ((long)i << ASHIFT) + ABASE, v);
}
```

#### 2.和 hashTable的保证线程安全的机制有何联系

Hashtable通过synchronized修饰方法 来保证线程安全
通过synchronized同步代码块和 CAS操作来实现线程安全
由此抛出的问题：
为什么要用synchronized，cas不是已经可以保证操作的线程安全吗？
原因：
CAS也是适用一些场合的，比如资源竞争小时，是非常适用的，不用进行内核态和用户态之间
的线程上下文切换，同时自旋概率也会大大减少，提升性能，但资源竞争激烈时（比如大量线
程对同一资源进行写和读操作）并不适用，自旋概率会大大增加，从而浪费CPU资源，降低性
能