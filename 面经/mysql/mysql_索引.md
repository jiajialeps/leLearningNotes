### 一、索引是什么？

![图片](https://mmbiz.qpic.cn/mmbiz_png/sMmr4XOCBzFf5QJ3PsZT6VlERVkFaQGvJn8odMXyQlKrYfmst1Z9kfTTfIWqa61xobo4JElTKBwpY8dCdLRvsw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

- 索引是一种能提高数据库查询效率的数据结构。它可以比作一本字典的目录，可以帮你快速找到对应的记录。
- 索引一般存储在磁盘的文件中，它是占用物理空间的。
- 正所谓水能载舟，也能覆舟。适当的索引能提高查询效率，过多的索引会影响数据库表的插入和更新功能。

### 二、索引有哪些类型类型

![图片](https://mmbiz.qpic.cn/mmbiz_png/sMmr4XOCBzFf5QJ3PsZT6VlERVkFaQGvUdjUicXoOSApdvxdNllOAhMkRN6nu8OJ7tGsdgInTHxjibsc4JN8sYkw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

#### 数据结构维度

- B+树索引：所有数据存储在叶子节点，复杂度为O(logn)，适合范围查询。
- 哈希索引:  适合等值查询，检索效率高，一次到位。
- 全文索引：MyISAM和InnoDB中都支持使用全文索引，一般在文本类型char,text,varchar类型上创建。
- R-Tree索引: 用来对GIS数据类型创建SPATIAL索引

#### 物理存储维度

- 聚集索引：聚集索引就是以主键创建的索引，在叶子节点存储的是表中的数据。
- 非聚集索引：非聚集索引就是以非主键创建的索引，在叶子节点存储的是主键和索引列。

#### 逻辑维度

- 主键索引：一种特殊的唯一索引，不允许有空值。
- 普通索引：MySQL中基本索引类型，允许空值和重复值。
- 联合索引：多个字段创建的索引，使用时遵循最左前缀原则。
- 唯一索引：索引列中的值必须是唯一的，但是允许为空值。
- 空间索引：MySQL5.7之后支持空间索引，在空间索引这方面遵循OpenGIS几何数据模型规则。



###  三、主键索引和非主键索引有什么区别？



例如对于下面这个表(其实就是上面的表中增加了一个k字段),且ID是主键。

![img](https://img2018.cnblogs.com/blog/1644694/201905/1644694-20190505155016157-1108127109.png)

 

主键索引和非主键索引的示意图如下：

![img](https://img2018.cnblogs.com/blog/1644694/201905/1644694-20190505155026646-1387513390.png)

 

其中R代表一整行的值。

从图中不难看出，主键索引和非主键索引的区别是：非主键索引的叶子节点存放的是**主键的值**，而主键索引的叶子节点存放的是**整行数据**，其中非主键索引也被称为**二级索引**，而主键索引也被称为**聚簇索引**。

根据这两种结构我们来进行下查询，看看他们在查询上有什么区别。

1、如果查询语句是 select * from table where ID = 100,即主键查询的方式，则只需要搜索 ID 这棵 B+树。

2、如果查询语句是 select * from table where k = 1，即非主键的查询方式，则先搜索k索引树，得到ID=100,再到ID索引树搜索一次，这个过程也被称为回表。



### 四、为什么选择B+树作为索引结构

可以从这几个维度去看这个问题，查询是否够快，效率是否稳定，存储数据多少，以及查找磁盘次数等等。为什么不是哈希结构？为什么不是二叉树，为什么不是平衡二叉树，为什么不是B树，而偏偏是B+树呢？

我们写业务SQL查询时，大多数情况下，都是范围查询的，如下SQL

```
select * from employee where age between 18 and 28;
```

#### 为什么不使用哈希结构？

我们知道哈希结构，类似k-v结构，也就是，key和value是一对一关系。它用于**「等值查询」**还可以，但是范围查询它是无能为力的哦。

#### 为什么不使用二叉树呢？

先回忆下二叉树相关知识啦~ 所谓**「二叉树，特点如下：」**

- 每个结点最多两个子树，分别称为左子树和右子树。
- 左子节点的值小于当前节点的值，当前节点值小于右子节点值
- 顶端的节点称为根节点，没有子节点的节点值称为叶子节点。

我们脑海中，很容易就浮现出这种二叉树结构图：

![图片](https://mmbiz.qpic.cn/mmbiz_png/sMmr4XOCBzFf5QJ3PsZT6VlERVkFaQGvIzqtnAG7q0kGVqVmOCD97sLO8LAwfjzqKLicDUATfQ2T1Gjn4V36N4w/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

但是呢，有些特殊二叉树，它可能这样的哦：

![图片](https://mmbiz.qpic.cn/mmbiz_png/sMmr4XOCBzFf5QJ3PsZT6VlERVkFaQGv9HiaTEQl6pItpgh4KD0clUYvd5BIZSUtgxJZnXF6XzqP7Y8MosicyHnQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

如果二叉树特殊化为一个链表，相当于全表扫描。那么还要索引干嘛呀？因此，一般二叉树不适合作为索引结构。

#### 为什么不使用平衡二叉树呢？

平衡二叉树特点：它也是一颗二叉查找树，任何节点的两个子树高度最大差为1。所以就不会出现特殊化一个链表的情况啦。

![图片](https://mmbiz.qpic.cn/mmbiz_png/sMmr4XOCBzFf5QJ3PsZT6VlERVkFaQGvIzqtnAG7q0kGVqVmOCD97sLO8LAwfjzqKLicDUATfQ2T1Gjn4V36N4w/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

但是呢：

- 平衡二叉树插入或者更新时，需要左旋右旋维持平衡，维护代价大
- 如果数量多的话，树的高度会很高。因为数据是存在磁盘的，以它作为索引结构，每次从磁盘读取一个节点，操作IO的次数就多啦。

#### 为什么不使用B树呢？

数据量大的话，平衡二叉树的高度会很高，会增加IO嘛。那为什么不选择同样数据量，**「高度更矮的B树」**呢？

![图片](https://mmbiz.qpic.cn/mmbiz_png/sMmr4XOCBzFf5QJ3PsZT6VlERVkFaQGvc1ePFmBK3HTBYkgYE1Lk1ddAnH2p1icuJwKafZsu1uQBYdkPiaicWcDYg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

B树相对于平衡二叉树，就可以存储更多的数据，高度更低。但是最后为甚选择B+树呢？因为B+树是B树的升级版：

> ❝
>
> - B+树非叶子节点上是不存储数据的，仅存储键值，而B树节点中不仅存储键值，也会存储数据。innodb中页的默认大小是16KB，如果不存储数据，那么就会存储更多的键值，相应的树的阶数（节点的子节点树）就会更大，树就会更矮更胖，如此一来我们查找数据进行磁盘的IO次数有会再次减少，数据查询的效率也会更快。
> - B+树索引的所有数据均存储在叶子节点，而且数据是按照顺序排列的，链表连着的。那么B+树使得范围查找，排序查找，分组查找以及去重查找变得异常简单。
>
> ❞

### 五、一次B+树索引搜索过程

**「面试官：」** 假设有以下表结构，并且有这几条数据

```
CREATE TABLE `employee` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `sex` int(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_age` (`age`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into employee values(100,'小伦',43,'2021-01-20','0');
insert into employee values(200,'俊杰',48,'2021-01-21','0');
insert into employee values(300,'紫琪',36,'2020-01-21','1');
insert into employee values(400,'立红',32,'2020-01-21','0');
insert into employee values(500,'易迅',37,'2020-01-21','1');
insert into employee values(600,'小军',49,'2021-01-21','0');
insert into employee values(700,'小燕',28,'2021-01-21','1');
```

**「面试官：」** 如果执行以下的查询SQL，需要执行几次的树搜索操作？可以画下对应的索引结构图~

```
select * from Temployee where age=32;
```

**「解析：」** 其实这个，面试官就是考察候选人是否熟悉B+树索引结构图。可以像酱紫回答~

- 先画出`idx_age`索引的索引结构图，大概如下：

![图片](https://mmbiz.qpic.cn/mmbiz_png/sMmr4XOCBzFf5QJ3PsZT6VlERVkFaQGvZBdQyHHHgFPeBWKniaicCO42RCxg94PJ7yZps92jX2ibeu1bCcxyVS17Q/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

- 再画出id主键索引，我们先画出聚族索引结构图，如下：

![图片](https://mmbiz.qpic.cn/mmbiz_png/sMmr4XOCBzFf5QJ3PsZT6VlERVkFaQGvmyS6ofx81UKe4t2nmKictM32XkMszoCiavu6aPaEOvd5DiaToFY3EYXKg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

因此，这条 SQL 查询语句执行大概流程就是酱紫：

- 1. 搜索`idx_age`索引树，将磁盘块1加载到内存，由于32<37,搜索左路分支，到磁盘寻址磁盘块2。

     

  2. 将磁盘块2加载到内存中，在内存继续遍历，找到age=32的记录，取得id = 400.

     

  3. 拿到id=400后，回到id主键索引树。

     

  4. 搜索`id主键`索引树，将磁盘块1加载内存，在内存遍历，找到了400，但是B+树索引非叶子节点是不保存数据的。索引会继续搜索400的右分支，到磁盘寻址磁盘块3.

     

  5. 将磁盘块3加载内存，在内存遍历，找到id=400的记录，拿到R4这一行的数据，好的，大功告成。

因此，这个SQL查询，执行了几次树的搜索操作，是不是一步了然了呀。**「特别的」**，在`idx_age`二级索引树找到主键`id`后，回到id主键索引搜索的过程,就称为回表。

> ❝
>
> 什么是回表？拿到主键再回到主键索引查询的过程，就叫做**「回表」**
>
> ❞

### 六、覆盖索引

**「面试官：」** 如果不用`select *`, 而是使用`select id,age`，以上的题目执行了几次树搜索操作呢？

**「解析：」** 这个问题，主要考察候选人的覆盖索引知识点。回到`idx_age`索引树，你可以发现查询选项id和age都在叶子节点上了。因此，可以直接提供查询结果啦，根本就不需要再回表了~

![图片](https://mmbiz.qpic.cn/mmbiz_png/sMmr4XOCBzFf5QJ3PsZT6VlERVkFaQGv92TnuqU86R7ryO7vo6femMJwgTQtAoLGrIdb2eYFSjXxp1AZQu1Owg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

> ❝
>
> 覆盖索引：在查询的数据列里面，不需要回表去查，直接从索引列就能取到想要的结果。换句话说，你SQL用到的索引列数据，覆盖了查询结果的列，就算上覆盖索引了。
>
> ❞

所以，相对于上个问题，就是省去了回表的树搜索操作。

### 七、索引失效

**「面试官：」** 如果我现在给`name`字段加上普通索引，然后用个like模糊搜索，那会执行多少次查询呢？SQL如下：

```
select * from employee where name like '%杰伦%';
```

**「解析：」** 这里考察的知识点就是，like是否会导致不走索引，看先该SQL的explain执行计划吧。其实like 模糊搜索，会导致不走索引的，如下:

![图片](https://mmbiz.qpic.cn/mmbiz_png/sMmr4XOCBzFf5QJ3PsZT6VlERVkFaQGvX46kfxLrRFtDtMrKffeVRT8rNQaYsGsGhiboSiblgjhrtCuPU4D4beaQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

因此，这条SQL最后就全表扫描啦~日常开发中，这几种骚操作都可能会导致索引失效，如下：

- 查询条件包含or，可能导致索引失效
- 如何字段类型是字符串，where时一定用引号括起来，否则索引失效
- like通配符可能导致索引失效。
- 联合索引，查询时的条件列不是联合索引中的第一个列，索引失效。
- 在索引列上使用mysql的内置函数，索引失效。
- 对索引列运算（如，+、-、*、/），索引失效。
- 索引字段上使用（！= 或者 < >，not in）时，可能会导致索引失效。
- 索引字段上使用is null， is not null，可能导致索引失效。
- 左连接查询或者右连接查询查询关联的字段编码格式不一样，可能导致索引失效。
- mysql估计使用全表扫描要比使用索引快,则不使用索引。

### 八、联合索引之最左前缀原则

**「面试官：」** 如果我现在给name,age字段加上联合索引索引，以下SQL执行多少次树搜索呢？先画下索引树？

```
select * from employee where name like '小%' order by age desc;
```

**「解析：」** 这里考察联合索引的最左前缀原则以及like是否中索引的知识点。组合索引树示意图大概如下：

![图片](https://mmbiz.qpic.cn/mmbiz_png/sMmr4XOCBzFf5QJ3PsZT6VlERVkFaQGv50Rhl86ABicHbnefEsOiafNtEoiahB6fMUBHzQEVmicklLrZCD9SfBpLsQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

联合索引项是先按姓名name从小到大排序，如果名字name相同，则按年龄age从小到大排序。面试官要求查所有名字第一个字是“小”的人，SQL的like '小%'是可以用上`idx_name_age`联合索引的。

![图片](https://mmbiz.qpic.cn/mmbiz_png/sMmr4XOCBzFf5QJ3PsZT6VlERVkFaQGvNiaiaR7w5LicGQ4ulyv4cyCvxS1PWMUKJ91ccibvsCRgrH1LtNCHa8j21w/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

该查询会沿着idx_name_age索引树，找到第一个字是小的索引值，因此依次找到`小军、小伦、小燕、`，分别拿到Id=`600、100、700`，然后回三次表，去找对应的记录。这里面的最左前缀`小`，就是字符串索引的最左M个字符。实际上，

- 这个最左前缀可以是联合索引的最左N个字段。比如组合索引（a,b,c）可以相当于建了（a），（a,b）,(a,b,c)三个索引，大大提高了索引复用能力。
- 最左前缀也可以是字符串索引的最左M个字符。

### 九、索引下推

**「面试官：」** 我们还是居于组合索引 idx_name_age，以下这个SQL执行几次树搜索呢？

```
select * from employee where name like '小%' and age=28 and sex='0';
```

**「解析：」** 这里考察索引下推的知识点，如果是**「Mysql5.6之前」**，在idx_name_age索引树，找出所有名字第一个字是“小”的人，拿到它们的主键id，然后回表找出数据行，再去对比年龄和性别等其他字段。如图：

![图片](https://mmbiz.qpic.cn/mmbiz_png/sMmr4XOCBzFf5QJ3PsZT6VlERVkFaQGvXh87Z9mvt5KElSib5lEIVtueaZpMvribGROeuiciax9FlRybx6NLQJ1rJw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

有些朋友可能觉得奇怪，（name,age)不是联合索引嘛？为什么选出包含“小”字后，不再顺便看下年龄age再回表呢，不是更高效嘛？所以呀，MySQL 5.6 就引入了**「索引下推优化」**，可以在索引遍历过程中，对索引中包含的字段先做判断，直接过滤掉不满足条件的记录，减少回表次数。

因此，MySQL5.6版本之后，选出包含“小”字后，顺表过滤age=28，,所以就只需一次回表。

![		](https://mmbiz.qpic.cn/mmbiz_png/sMmr4XOCBzFf5QJ3PsZT6VlERVkFaQGvLj0vKZQ3JezKaFiaVGTyFy2icZiaDkVwkE8zorNoRbXmwnIfugWtAfI4w/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

### 十、 大表添加索引

**「面试官：」** 如果一张表数据量级是千万级别以上的，那么，给这张表添加索引，你需要怎么做呢？

**「解析：」** 我们需要知道一点，给表添加索引的时候，是会对表加锁的。如果不谨慎操作，有可能出现生产事故的。可以参考以下方法：

- 1.先创建一张跟原表A数据结构相同的新表B。
- 2.在新表B添加需要加上的新索引。
- 3.把原表A数据导到新表B
- 4.rename新表B为原表的表名A，原表A换别的表名；

### 十一、什么是聚簇索引？何时使用聚簇索引与非聚簇索引 

**1.什么是聚簇索引？**

聚簇索引：将数据存储与索引放到了一块，找到索引也就找到了数据

非聚簇索引：将数据存储于索引分开结构，索引结构的叶子节点指向了数据的对应行，myisam通过key_buffer把索引先缓存到内存中，当需要访问数据时（通过索引访问数据），在内存中直接搜索索引，然后通过索引找到磁盘相应数据，这也就是为什么索引不在key buffer命中时，速度慢的原因

**澄清一个概念**：innodb中，在聚簇索引之上创建的索引称之为辅助索引，辅助索引访问数据总是需要二次查找，非聚簇索引都是辅助索引，像复合索引、前缀索引、唯一索引，辅助索引叶子节点存储的不再是行的物理位置，而是主键值

**2.何时使用聚簇索引与非聚簇索引？**



![img](https://pic3.zhimg.com/80/v2-fd11f44ea53d4475e262ee648022731a_720w.jpg)





**3.非聚簇索引一定会回表查询吗？**

不一定，这涉及到查询语句所要求的字段是否全部命中了索引，如果全部命中了索引，那么就不必再进行回表查询。

举个简单的例子，假设我们在员工表的年龄上建立了索引，那么当进行select age from employee where age < 20的查询时，在索引的叶子节点上，已经包含了age信息，不会再次进行回表查询。



### 总结与练习

本文主要讲解了索引的9大关键面试考点，希望对大家有帮助。接下来呢，给大家出一道，有关于我最近业务开发遇到的加索引SQL，看下大家是怎么回答的，有兴趣可以联系我，一起讨论哈~题目如下：

```
select * from A where type ='1' and status ='s' order by create_time desc;
```

假设type有9种类型，区分度还算可以，status的区分度不高（有3种类型），那么你是如何加索引呢？

- 是给type加单索引
- 还是（type，status，create_time）联合索引
- 还是（type，create_time）联合索引呢？