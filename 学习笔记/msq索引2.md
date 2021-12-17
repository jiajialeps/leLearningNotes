## 什么是索引？

索引是辅助存储引擎高效获取数据的一种数据结构。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4NqBdqx7dXcuCQWHOakJcJIib4gOaG6qtC9ILD3uM3JSzfZbOQEibYnicXZA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

[很多人形象的说索引就是数据的目录，便于存储引擎快速的定位数据。](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

## 索引的分类

[我们经常从以下几个方面对索引进行分类](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

[从 **「数据结构的角度」** 对索引进行分类](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

- [B+tree](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)
- [Hash](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)
- [Full-texts 索引](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

[从 **「物理存储的角度」** 对索引进行分类](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

- [聚簇索引](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)
- [二级索引(辅助索引)](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

[从 **「索引字段特性角度」** 分类](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

- 主键索引
- [唯一索引](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)
- 普通索引
- [前缀索引](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

[从 **「组成索引的字段个数角度」** 分类](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

- [单列索引](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)
- [联合索引（复合索引）](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

### 数据结构角度看索引

下表是 MySQL 常见的存储引擎 InnoDB，MyISAM 和 Memory 分别支持的索引类型

![图片](https://mmbiz.qpic.cn/mmbiz_png/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4Nq049S7V8RyyE0FtzecWYcKvowuicUCia3NyYwSECtxQiczECwfibwmibKTgw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

在实际使用中，InnoDB 作为 MySQL 建表时默认的存储引擎

对上表进行横向查看可以了解到，B+tree 是 MySQL 中被存储引擎采用最多的索引类型。

这里浅尝辄止的谈一下 B+tree 与 Hash 和红黑树的区别。这方面系列面试题和答案全部整理好了，微信搜索互联网架构师，在后台发送：面试，可以在线阅读。

#### B+tree 和 B-tree

> [1970 年，R.Bayer 和 E.Mccreight 提出了一种适用于外查找的平衡多叉树——B-树，磁盘管理系统中的目录管理，以及数据库系统中的索引组织多数采用 B-Tree 这种数据结构。--数据结构 C 语言版第二版 严蔚敏](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

B+tree 是 B-Tree 的一个变种。（哦，对了，B-tree 念 B 树，它不叫 B 减树。。。）

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4NqXI8esnc9de05HicvSd19cuFwWEqxTO4ibmnVsGxt5d97bgmXntxSVF3Q/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

B+tree 只在叶子节点存储数据，而 B-tree 非叶子节点也存储数据，对此处有疑问的可以到下面的连接自己插入数据测试一番。

- B-tree : `https://www.cs.usfca.edu/~galles/visualization/BTree.html`
- B+tree : `https://www.cs.usfca.edu/~galles/visualization/BPlusTree.html`

因此，B+tree 单个节点的数量更小，在相同的磁盘 IO 下能查询更多的节点。

另外 B+tree 叶子节点采用单链表链接适合 MySQL 中常见的基于范围的顺序检索场景，而 B-tree 无法做到这一点。另外，MySQL 系列面试题和答案全部整理好了，微信搜索互联网架构师，在后台发送：2T，可以在线阅读。

#### B+tree 和红黑树

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4NqXI8esnc9de05HicvSd19cuFwWEqxTO4ibmnVsGxt5d97bgmXntxSVF3Q/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

对于有 N 个叶子节点的 B+tree，搜索复杂度为 [**「O(logdN) ,d 是指 degree 是指 B+tree 的度」**](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)，表示节点允许的最大子节点个数为 d 个，在实际的运用中 d 值是大于 100 的，即使数据达到千万级别时候 B+tree 的高度依然维持在 3-4 左右，保证了 3-4 次磁盘 I/O 就能查到目标数据。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4Nq5DCkq9icXGfQ2v1HreQvsHPAlHf5vmJJiazqAhSibOic0FNPtYCGCqu5UQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

从上图中可以看出红黑树是二叉树，节点的子节点个数最多为 2 个，意味着其搜索复杂度为[ **「O(logN)」**](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)，比 B+ 树高出不少，因此红黑树检索到目标数据所需经理的磁盘 I/O 次数更多。

#### B+tree 索引与 Hash 表

范围查询是 MySQL 数据库中常见的场景，而 Hash 表不适合做范围查询，Hash 表更适合做等值查询，另外 Hash 表还存在 Hash 函数选择和 Hash 值冲突等问题。

因为这些原因，B+tree 索引要比 Hash 表索引有更广的适用场景。

### 物理存储角度看索引

MySQL 中的两种常用存储引擎对索引的处理方式差别较大。

#### InnoDB 的索引

首先看一下 InnoDB 存储引擎中的索引，InnoDB 表的索引按照叶子节点存储的是否为完整表数据分为聚簇索引和二级索引。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4NqImUjJ9jW6DUvxauwLj4LrqdZ5IxhkdnjgkY3htNClrp7f2zufSX0OQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

全表数据就是存储在聚簇索引中的。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4NqonpSrINbI5slOdqEvlFBNvFjcxZDTK2oCHKKkWwYLWvRd72KbLrPJw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

聚簇索引以外的其它索引叫做二级索引。



下面结合实际的例子介绍下这两类索引。

```
create table workers
 (
     id    int(11)     not null auto_increment comment '员工工号',
     name  varchar(16) not null comment '员工名字',
     sales int(11) default null comment '员工销售业绩',
     primary key (id)
 ) engine InnoDB
   AUTO_INCREMENT = 10
   default charset = utf8;

 insert into workers(id, name, sales)
 values (1, '江南', 12744);
 insert into workers(id, name, sales)
 values (3, '今何在', 14082);
 insert into workers(id, name, sales)
 values (7, '路明非', 14738);
 insert into workers(id, name, sales)
 values (8, '吕归尘', 7087);
 insert into workers(id, name, sales)
 values (11, '姬野', 8565);
 insert into workers(id, name, sales)
 values (15, '凯撒', 8501);
 insert into workers(id, name, sales)
 values (20, '绘梨衣', 7890);
```

我们现在自己的测试数据库中创建一个包含销售员信息的测试表 workers

包含 id(主键),name,sales 三个字段，指定表的存储引擎为 InnoDB。

然后插入 8 条数据

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4NqCcVhVudZeGwtt4MdSAyhVcwcocRuLqJicRzGkQbR8npyL3AywicoKnLg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

这个例子当中，workers 表的聚簇索引建立在字段 id 上

为了准确模拟，我们先把主键 id 插入 b+tree 得到下图

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4Nqk4M1FqxHbibvckg8MdDbcIk3RwPicB57fDzcBeEibKrbro3YDDd5364ew/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

然后在此图基础上，我画出了高清版。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4Nq3cdatxKy4ZZnP3k228VBAIm5q1s11UibicwAHmyKXhh5wOqviagbHYd1w/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

从图中可以看到，聚簇索引的每个叶子节点存储了一行完整的表数据，叶子节点间采用单向链表按 id 列递增连接，可以方便的进行顺序检索。

InnoDB 表要求必须有聚簇索引，默认在主键字段上建立聚簇索引，在没有主键字段的情况下，表的第一个 NOT NULL 的唯一索引将被建立为聚簇索引，在前两者都没有的情况下，InnoDB 将自动生成一个隐式自增 id 列并在此列上创建聚簇索引。

接着来看二级索引。

还以刚才的 workers 表为例

我们在 name 字段上添加二级索引 index_name

```
alter table workers add index index_name(name);
```



![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4Nqt4IVlargA9qMJtfhBTfdQpH9Mtnrib4JRZayPD4C3AIpwJBwjleuyWw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

同样我们画出了二级索引 index_name 的 B+tree 示意图

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4Nqk5QDMAFnFg0icr4B3Ynt5pmhYNXvaVmuTBkNyEicroLficM1zSy2VEAcw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

图中可以看出二级索引的叶子节点并不存储一行完整的表数据，而是存储了聚簇索引所在列的值，也就是workers 表中的 id 列的值。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4Nq3cdatxKy4ZZnP3k228VBAIm5q1s11UibicwAHmyKXhh5wOqviagbHYd1w/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4Nqk5QDMAFnFg0icr4B3Ynt5pmhYNXvaVmuTBkNyEicroLficM1zSy2VEAcw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)





这两张示意图中 B+tree 的度设置为了 3 ，这也主要是为了方便演示。

实际的 B+tree 索引中，树的度通常会大于 100。

说了聚簇索引和二级索引 肯定要提到「**回表查询**」。

由于二级索引的叶子节点不存储完整的表数据，所以当通过二级索引查询到聚簇索引的列值后，还需要回到局促索引也就是表数据本身进一步获取数据。

分享资料：[2T架构师学习资料干货分享](http://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

比如说我们要在 workers 表中查询 名叫吕归尘的人

```
select * from workers where name='吕归尘';
```

这条 SQL 通过 name='吕归尘'的条件

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4NqNZuoYVLC65Sm7L2doqQ4kRxMgG04dnkVGWE9fvSDnmQYWHHUYvsgPA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



在二级索引 index_name 中查询到主键 id=8 ，接着带着 id=8 这个条件

进一步回到聚簇索引查询以后才能获取到完整的数据，很显然回表需要额外的 B+tree 搜索过程，必然增大查询耗时。

需要注意的是通过二级索引查询时，回表不是必须的过程，当 Query 的所有字段在二级索引中就能找到时，就不需要回表，MySQL 称此时的二级索引为覆盖索引或称触发了 **「索引覆盖」**。

```
select id,name from workers where name='吕归尘';
```

这句 SQL 只查询了 id，和 name，二级索引就已经包含了 Query 所以需要的所有字段，就无需回表查询。

```
explain select id,name from workers where name='吕归尘';
```

使用 explain 查看此条 SQL 的执行计划

![图片](https://mmbiz.qpic.cn/mmbiz_png/TNUwKhV0JpTDcua6Infg8X2eYFTuEhhE6Riaqd6I3NvM8RIeE5Tiabe5cGsCUGMBrMylQf5xdsicP4whPztibWFRLQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

[执行计划的 Extra 字段中出现了 Using where;Using index 表明查询触发了索引 index_name 的索引覆盖，且对索引做了 where 筛选，这里不需要回表。](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

下面做对比，查询一下没有索引的

```
explain select id,name,sales from workers where name='吕归尘';
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/TNUwKhV0JpTDcua6Infg8X2eYFTuEhhEBp2HzgLUmcYtE2PuJvMjbm7WduibBsW4cW0J6QOweOcNv1r81sNXtXA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

Extra 为 `Using Index Condition` 表示会先条件过滤索引，过滤完索引后找到所有符合索引条件的数据行，随后用 WHERE 子句中的其他条件去过滤这些数据行。Index Condition Pushdown (ICP)是 MySQL 5.6 以上版本中的新特性，是一种在`存储引擎层`使用索引过滤数据的一种优化方式。ICP 开启时的执行计划含有 Using index condition 标示 ，表示优化器使用了 ICP 对数据访问进行优化。

如果你对此感兴趣去查阅对应的官方文档和技术博客。

这次我们简化来理解，不考虑 ICP 对数据访问的优化，当关闭 ICP 时，Index 仅仅是 data access 的一种访问方式，存储引擎通过索引回表获取的数据会传递到 MySQL Server 层进行 WHERE 条件过滤。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4NqjPzJ692fbaYzyiaicygpZZG6cP4Mdy5WHKFKW18Jrm7Dvl47efIzPeibQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

Extra 为 `Using where` 只是提醒我们 MySQL 将用 where 子句来过滤结果集。这个一般发生在 MySQL 服务器，而不是存储引擎层。一般发生在不能走索引扫描的情况下或者走索引扫描，但是有些查询条件不在索引当中的情况下。

这里表明没有触发索引覆盖，进行回表查询。

#### MyISAM 的索引

说完了 InnoDB 的索引，接下来我们来看 MyISAM 的索引

以 MyISAM 存储引擎存储的表不存在聚簇索引。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4Nqrmib3iakLrxkBNQXoHdXPbS2LaLCBHHNRalQl1TBWUGDqnh2KltcyW0g/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

MyISAM 表中的主键索引和非主键索引的结构是一样的，从上图中我们可以看到

他们的叶子节点是不存储表数据的，节点中存放的是表数据的地址，所以 MyISAM 表可以没有主键。

MyISAM 表的数据和索引是分开的，是单独存放的。

MyISAM 表中的主键索引和非主键索引的区别仅在于主键索引 B+tree 上的 key 必须符合主键的限制，

非主键索引 B+tree 上的 key 只要符合相应字段的特性就可以了。

### 索引字段特性角度看索引

**「主键索引」**

- [建立在主键字段上的索引](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)
- [一张表最多只有一个主键索引](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)
- [索引列值不允许为 null](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)
- [通常在创建表的时候一起创建](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

[**「唯一索引」**](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

- [建立在 UNIQUE 字段上的索引就是唯一索引](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)
- [一张表可以有多个唯一索引，索引列值允许为 null](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

[我们演示创建索引](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

```
create table persons
 (
     id   int(11) not null auto_increment comment '主键id',
     eno  int(11) comment '工号',
     eid  int(11) comment '身份证号',
     veid int(11) comment '虚拟身份证号',
     name varchar(16) comment '名字',
     primary key (id) comment '主键索引',
     UNIQUE key (eno) comment 'eno唯一索引',
     UNIQUE key (eid) comment 'eid唯一索引'
 ) engine = InnoDB
   auto_increment = 1000
   default charset = utf8;
 alter table persons
     add unique index index_veid (veid) comment 'veid唯一索引';
```

[通过 `show index from persons`;命令我们看到已经成功创建了三个唯一索引。](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4Nq7lPBorK16Snt5GgnebbkVjicCg8pLte1layQ7PzN1rwUD5I503sRmAg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

#### [普通索引](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

[主键索引和唯一索引对字段的要求是要求字段为主键或 unique 字段，](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

[而那些建立在普通字段上的索引叫做普通索引，既不要求字段为主键也不要求字段为 unique。](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

另外，关注公众号互联网架构师，在后台回复：面试，可以获取我整理的 MySQL 系列面试题和答案，非常齐全。

#### [前缀索引](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

[前缀索引是指对字符类型字段的前几个字符或对二进制类型字段的前几个 bytes 建立的索引，而不是在整个字段上建索引。](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

[例如，可以对 persons 表中的 name(varchar(16))字段 中 name 的前 5 个字符建立索引。](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

```
create index index_name on persons (name(5)) comment '前缀索引';
show index from persons;
```

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4NqVXUL67NJ3RZficeP1xy0OGvkao8JX07cwlLXCqmI5L3ScndpMRwMKQw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

[前缀索引可以建立在类型为](https://mp.weixin.qq.com/s?__biz=MzI2MTIzMzY3Mw==&mid=2247487508&idx=1&sn=78cf235aa9ba5f988c6922ca98f8bfd6&chksm=ea5cdd72dd2b54647cf55b4a73dcafa69fc7228205ad39ecc98fe57b39cdecb21c238c6d6cb6&scene=21#wechat_redirect)

- char
- varchar
- binary
- varbinary

的列上，可以大大减少索引占用的存储空间，也能提升索引的查询效率。

### 索引列的个数角度看索引

- 建立在单个列上的索引为单列索引

  

- - 上文演示的都是单列索引

- 建立在多列上的称为联合索引（复合索引）

演示一下联合索引`create index index_id_name on workers(id,name) comment '组合索引';`这条语句在我们演示表 workers 中建立 id，name 这两个字段的联合索引。借助 show index 命令查看索引的详细信息 操作后结果如下：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4NqEoPCGCyzXib305ue5s50ibKIMv7lrTVTdNBAHsfsbtNrEZkVcQLc9yZA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



虽然详细信息当中列出了两条关于联合索引的条目，但并不表示联合索引是建立了多个索引，联合索引是一个索引结构，这两个条目表示的是组合索引中字段的具体信息，按建立索引时的书写顺序排序。



同样我们来看下联合索引的 B+tree 示意图

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9mQQWOf4KRIsYJvGP4MRo9Jf98qQJ4NqFS36xR42ibo4F8ojajgquOwRVQSEyxIlOicgoRc2uibo8AqJg0axChA9w/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

从图中看到组合索引的非叶子节点保存了两个字段的值作为 B+tree 的 key 值，当 B+tree 上插入数据时，先按字段 id 比较，在 id 相同的情况下按 name 字段比较。