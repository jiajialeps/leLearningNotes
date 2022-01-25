# 1.概述

### 1.1 生态

- Lambda 表达式
- 函数式接口
- 方法引用 / 构造器引用
- Stream API
- 接口中的默认方法 / 静态方法
- 新时间日期 API
- 其他新特性

### 1.2 新特性

- 速度更快
- 代码更少
- 强大的 Stream API
- 便于并行
- 最大化减少空指针异常 Optional (Kotlin ?)

### 1.3 温故而知新

- Hashmap 底层结构/原理 老话题不再阐述 …
- 并发hashmap …
- Java虚拟机 …
- Java内存模型 …

# 2. Lambda

### 2.1 匿名函数

> Lambda是一个匿名函数，可以理解为一段可以传递的代码（将代码像数据一样传递）；可以写出更简洁、更灵活的代码；作为一种更紧凑的代码风格，是Java语言表达能力得到提升。

### 2.2 匿名内部类

```JAVA
@Test
public void test01(){
    //匿名内部类
    Comparator<Integer> comparator = new Comparator<Integer>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            return Integer.compare(o1,o2);
        }

        @Override
        public boolean equals(Object obj) {
            return false;
        }
    };
    //调用
    TreeSet<Integer> set = new TreeSet<>(comparator);
}
```

### 2.3 Lambda

```java
语法格式一 : 无参数，无返回值
() -> System.out.println("Hello Lambda!");

语法格式二 : 有一个参数，并且无返回值
(x) -> System.out.println(x)

语法格式三 : 若只有一个参数，小括号可以省略不写
x -> System.out.println(x)

Consumer<String> con = (x) -> System. out .println(x);
con.accept( "啦啦啦，我是卖报的小行家" );

语法格式四 : 有两个以上的参数，有返回值，并且 Lambda 体中有多条语句
Comparator <Integer> com = (x, y) -> {
    System.out.println("函数式接口");
    return Integer.compare(x, y);
};

语法格式五 : 若 Lambda 体中只有一条语句， return 和 大括号都可以省略不写
Comparator <Integer> com = (x, y) -> Integer.compare(x, y);

语法格式六 : Lambda 表达式的参数列表的数据类型可以省略不写，因为JVM编译器通过上下文推断出，数据类型，即“类型推断”
(Integer x, Integer y) -> Integer.compare(x, y);
注 : Lambda 表达式中的参数类型都是由编译器推断得出的。 Lambda 表达式中无需指定类型，程序依然可以编译，这是因为 javac 根据程序的上下文，在后台推断出了参数的类型。 Lambda 表达式的类型依赖于上下文环境，是由编译器推断出来的。这就是所谓的 “类型推断”
```



```JAVA
@Test
public void test02(){
    // Lambda 表达式
    Comparator<Integer> comparator = (a, b) -> Integer.compare(a, b);

    TreeSet<Integer> set = new TreeSet<>(comparator);
}
```

演变过程：

- 垃圾代码 --> 策略模式 --> 匿名内部类 --> Lambda表达式

基础语法：

- 操作符：->
- 左侧：参数列表
- 右侧：执行代码块 / Lambda 体

口诀：

- 写死小括号，拷贝右箭头，落地大括号
- 左右遇一括号省
- 左侧推断类型省

语法格式：

无参数，无返回值：() -> sout

例如 Runnable接口：

```JAVA
public class Test02 {
    int num = 10; //jdk 1.7以前 必须final修饰
    
    @Test
    public void test01(){
        //匿名内部类
        new Runnable() {
            @Override
            public void run() {
                //在局部类中引用同级局部变量
                //只读
                System.out.println("Hello World" + num);
            }
        };
    }

    @Test
    public void test02(){
        //语法糖
         Runnable runnable = () -> {
             System.out.println("Hello Lambda");
         };
    }
}
```

有一个参数，无返回值

```JAVA
@Test
public void test03(){
    Consumer<String> consumer = (a) -> System.out.println(a);
    consumer.accept("我觉得还行！");
}
```

有一个参数，无返回值 （小括号可以省略不写）

```JAVA
@Test
public void test03(){
    Consumer<String> consumer = a -> System.out.println(a);
    consumer.accept("我觉得还行！");
}
```

有两个及以上的参数，有返回值，并且 Lambda 体中有多条语句

```JAVA
@Test
public void test04(){
    Comparator<Integer> comparator = (a, b) -> {
        System.out.println("比较接口");
        return Integer.compare(a, b);
    };
}
```

有两个及以上的参数，有返回值，并且 Lambda 体中只有1条语句 （大括号 与 return 都可以省略不写）

```JAVA
@Test
public void test04(){
    Comparator<Integer> comparator = (a, b) -> Integer.compare(a, b);
}
```

- Lambda 表达式 参数的数据类型可以省略不写 Jvm可以自动进行 “类型推断” 函数式接口：
- 接口中只有一个抽象方法的接口 @FunctionalIterface 测试：
- 定义一个函数式接口：

```JAVA
@FunctionalInterface
public interface MyFun {

    Integer count(Integer a, Integer b);
}
```

用一下：

```JAVA
@Test
public void test05(){
    MyFun myFun1 = (a, b) -> a + b;
    MyFun myFun2 = (a, b) -> a - b;
    MyFun myFun3 = (a, b) -> a * b;
    MyFun myFun4 = (a, b) -> a / b;
}
```

再用一下：

```JAVA
public Integer operation(Integer a, Integer b, MyFun myFun){
    return myFun.count(a, b);
}

@Test
public void test06(){
    Integer result = operation(1, 2, (x, y) -> x + y);
    System.out.println(result);
}
```

### 2.4 案例

**案例一：**调用 Collections.sort() 方法，通过定制排序 比较两个 Employee (先按照年龄比，年龄相同按照姓名比)，使用 Lambda 表达式作为参数传递

- 定义实体类

  ```JAVA
  @Data
  @NoArgsConstructor
  @AllArgsConstructor
  public class Employee {
    private Integer id;
    private String name;
    private Integer age;
    private Double salary;
  }
  ```

- 定义 List 传入数据

  ```JAVA
  List<Employee> emps = Arrays.asList(
    new Employee(101, "Z3", 19, 9999.99),
    new Employee(102, "L4", 20, 7777.77),
    new Employee(103, "W5", 35, 6666.66),
    new Employee(104, "Tom", 44, 1111.11),
    new Employee(105, "Jerry", 60, 4444.44)
  );
  ```

- @Test

  ```JAVA
  @Test
  public void test01(){
    Collections.sort(emps, (e1, e2) -> {
        if (e1.getAge() == e2.getAge()){
            return e1.getName().compareTo(e2.getName());
        } else {
            return Integer.compare(e1.getAge(), e2.getAge());
        }
    });
  
    for (Employee emp : emps) {
        System.out.println(emp);
    }
  }
  ```

**案例二：**声明函数式接口，接口中声明抽象方法，String getValue(String str); 声明类 TestLambda，类中编写方法使用接口作为参数，将一个字符串转换成大写，并作为方法的返回值；再将一个字符串的第二个和第四个索引位置进行截取字串

**案例三：**声明一个带两个泛型的函数式接口，泛型类型为<T, R> T 为参数，R 为返回值；接口中声明对应的抽象方法；在 TestLambda 类中声明方法，使用接口作为参数，计算两个 Long 类型参数的和；在计算两个 Long 类型参数的乘积

# 3. 函数式接口

Java内置四大核心函数式接口：

| 函数式接口                | 参数类型 | 返回类型 | 用途                                                         |
| ------------------------- | -------- | -------- | ------------------------------------------------------------ |
| Consumer 消费型接口       | T        | void     | 对类型为T的对象应用操作：void accept(T t)                    |
| Supplier 提供型接口       | 无       | T        | 返回类型为T的对象：T get()                                   |
| Function<T, R> 函数型接口 | T        | R        | 对类型为T的对象应用操作，并返回结果为R类型的对象：R apply(T t) |
| Predicate 断言型接口      | T        | boolean  | 确定类型为T的对象是否满足某约束，并返回boolean值：boolean test(T t) |

### 3.1 消费型接口

```java
@Test
public void test01(){
    //Consumer
    Consumer<Integer> consumer = (x) -> System.out.println("消费型接口" + x);
    //test
    consumer.accept(100);
}
```

### 3.2 提供型接口

```java
@Test
public void test02(){
    List<Integer> list = new ArrayList<>();
    List<Integer> integers = Arrays.asList(1,2,3); 
    list.addAll(integers);
    //Supplier<T>
    Supplier<Integer> supplier = () -> (int)(Math.random() * 10);
    list.add(supplier.get());
    System.out.println(supplier);
    for (Integer integer : list) {
        System.out.println(integer);
    }
}
```

### 3.3 函数型接口

```
@Test
public void test03(){
    //Function<T, R>
    String oldStr = "abc123456xyz";
    Function<String, String> function = (s) -> s.substring(1, s.length()-1);
    //test
    System.out.println(function.apply(oldStr));
}
```

### 3.4 断言型接口

```
@Test
public void test04(){
    //Predicate<T>
    Integer age = 35;
    Predicate<Integer> predicate = (i) -> i >= 35;
    if (predicate.test(age)){
        System.out.println("你该退休了");
    } else {
        System.out.println("我觉得还OK啦");
    }
}
```

### 3.5 其他接口

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200518225311406.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTIyNTU5NQ==,size_16,color_FFFFFF,t_70#pic_center)



# 4.引用

### 4.1 方法引用

**定义：**若 Lambda 表达式体中的内容已有方法实现，则我们可以使用“方法引用”

语法格式：

- 对象 :: 实例方法
- 类 :: 静态方法
- 类 :: 实例方法

对象::实例方法

```
@Test
public void test01(){
    PrintStream ps = System.out;
    Consumer<String> con1 = (s) -> ps.println(s);
    con1.accept("aaa");

    Consumer<String> con2 = ps::println;
    con2.accept("bbb");
}
```

**注意：**Lambda 表达实体中调用方法的参数列表、返回类型必须和函数式接口中抽象方法保持一致

类::静态方法

```
@Test
public void test02(){
    Comparator<Integer> com1 = (x, y) -> Integer.compare(x, y);
    System.out.println(com1.compare(1, 2));

    Comparator<Integer> com2 = Integer::compare;
    System.out.println(com2.compare(2, 1));
}
```

类::实例方法

```
@Test
public void test03(){
    BiPredicate<String, String> bp1 = (x, y) -> x.equals(y);
    System.out.println(bp1.test("a","b"));

    BiPredicate<String, String> bp2 = String::equals;
    System.out.println(bp2.test("c","c"));
}
```

**条件：**Lambda 参数列表中的第一个参数是方法的调用者，第二个参数是方法的参数时，才能使用 ClassName :: Method

### 4.2 构造器引用

格式：

- ClassName :: new

  ```
  @Test
  public void test04(){
    Supplier<List> sup1 = () -> new ArrayList();
  
    Supplier<List> sup2 = ArrayList::new;
  }
  ```

**注意：**需要调用的构造器的参数列表要与函数时接口中抽象方法的参数列表保持一致

### 4.3 数组引用

语法：

Type :: new;

# 5. Stream API

### 5.1 创建

什么是 Stream?

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200518225358689.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTIyNTU5NQ==,size_16,color_FFFFFF,t_70#pic_center)

Stream的操作步骤：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200518225430446.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTIyNTU5NQ==,size_16,color_FFFFFF,t_70#pic_center)

创建流：（的几种方法如下）

```JAVA
  /**
* 创建流
*/
@Test
public void test01(){
    /**
    * 1.集合流
    *  - Collection.stream() 穿行流
    *  - Collection.parallelStream() 并行流
    */
    List<String> list = new ArrayList<>();
    Stream<String> stream1 = list.stream();

    //2.数组流
    //Arrays.stream(array)
    String[] strings = new String[10];
    Stream<String> stream2 = Arrays.stream(strings);

    //3.Stream 静态方法
    //Stream.of(...)
    Stream<Integer> stream3 = Stream.of(1, 2, 3);

    //4.无限流
    //4.1迭代
    Stream<Integer> stream4 = Stream.iterate(0, (i) -> ++i+i++);
    stream4.forEach(System.out::println);
     // stream4.limit(5).forEach(System.out::println); //使用limit可以选出无限流的其中五个

    //4.2 生成
    Stream.generate(() -> Math.random())
        // .limit(5)  //使用limit可以选出无限流的其中五个
        .forEach(System.out::println);
}
```

### 5.2 筛选与切片

中间操作：

- filter：接收 Lambda ，从流中排除某些元素
- limit：截断流，使其元素不超过给定数量
- skip(n)：跳过元素，返回一个舍弃了前n个元素的流；若流中元素不足n个，则返回一个空流；与 limit(n) 互补
- distinct：筛选，通过流所生成的 hashCode() 与 equals() 去除重复元素 (调用此方法时要重写hashCode() 与 equals()才行)

```JAVA
List<Employee> emps = Arrays.asList(
    new Employee(101, "Z3", 19, 9999.99),
    new Employee(102, "L4", 20, 7777.77),
    new Employee(103, "W5", 35, 6666.66),
    new Employee(104, "Tom", 44, 1111.11),
    new Employee(105, "Jerry", 60, 4444.44)
);

@Test
public void test01(){
    emps.stream()
        .filter((x) -> x.getAge() > 35)
        .limit(3) //短路？达到满足不再内部迭代
        .distinct()
        .skip(1)
        .forEach(System.out::println);

}
```

Stream的中间操作：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200518225456187.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTIyNTU5NQ==,size_16,color_FFFFFF,t_70#pic_center)

- 内部迭代：迭代操作由 Stream API 完成
- 外部迭代：我们通过迭代器完成

### 5.3 映射

- map：接收 Lambda ，将元素转换为其他形式或提取信息；接受一个函数作为参数，该函数会被应用到每个元素上，并将其映射成一个新的元素
- flatMap：接收一个函数作为参数，将流中每一个值都换成另一个流，然后把所有流重新连接成一个流

map：

```JAVA
@Test
public void test02(){
    List<String> list = Arrays.asList("a", "b", "c");
    list.stream()
        .map((str) -> str.toUpperCase())
        .forEach(System.out::println);
}
```

flatMap：

```java
public Stream<Character> filterCharacter(String str){
    List<Character> list = new ArrayList<>();
    for (char c : str.toCharArray()) {
        list.add(c);
    }

    return list.stream();
}

@Test
public void test03(){
    List<String> list = Arrays.asList("a", "b", "c");
    Test02 test02 = new Test02();
    list.stream()
        .flatMap(test02::filterCharacter)
        .forEach(System.out::println);
}
```

### 5.4 排序

- sorted()：自然排序
- sorted(Comparator c)：定制排序

Comparable：自然排序

```java
@Test
public void test04(){
    List<Integer> list = Arrays.asList(1,2,3,4,5);
    list.stream()
        .sorted() //comparaTo()	
        .forEach(System.out::println);
}
```

Comparator：定制排序

```java
@Test
public void test05(){
    emps.stream()
        .sorted((e1, e2) -> { //compara()
            if (e1.getAge().equals(e2.getAge())){
                return e1.getName().compareTo(e2.getName());
            } else {
                return e1.getAge().compareTo(e2.getAge());
            }
        })
        .forEach(System.out::println);
}
```

### 5.5 查找 / 匹配

终止操作：

- allMatch：检查是否匹配所有元素
- anyMatch：检查是否至少匹配一个元素
- noneMatch：检查是否没有匹配所有元素
- findFirst：返回第一个元素
- findAny：返回当前流中的任意元素
- count：返回流中元素的总个数
- max：返回流中最大值
- min：返回流中最小值

```java
public enum Status {
    FREE, BUSY, VOCATION;
}

@Test
public void test01(){
    List<Status> list = Arrays.asList(Status.FREE, Status.BUSY, Status.VOCATION);

    boolean flag1 = list.stream()
        .allMatch((s) -> s.equals(Status.BUSY));
    System.out.println(flag1);

    boolean flag2 = list.stream()
        .anyMatch((s) -> s.equals(Status.BUSY));
    System.out.println(flag2);

    boolean flag3 = list.stream()
        .noneMatch((s) -> s.equals(Status.BUSY));
    System.out.println(flag3);

    // 避免空指针异常
    Optional<Status> op1 = list.stream()
        .findFirst();
    // 如果Optional为空 找一个替代的对象
    Status s1 = op1.orElse(Status.BUSY);
    System.out.println(s1);

    Optional<Status> op2 = list.stream()
        .findAny();
    System.out.println(op2);

    long count = list.stream()
        .count();
    System.out.println(count);
}
```

### 5.6 归约 / 收集

- 归约：reduce(T identity, BinaryOperator) / reduce(BinaryOperator) 可以将流中的数据反复结合起来，得到一个值
- 收集：collect 将流转换成其他形式；接收一个 Collector 接口的实现，用于给流中元素做汇总的方法

reduce：

```java
/**
* Java：
*  - reduce：需提供默认值（初始值）
* Kotlin：
*  - fold：不需要默认值（初始值）
*  - reduce：需提供默认值（初始值）
*/
@Test
public void test01(){
    List<Integer> list = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9);
    Integer integer = list.stream()
        .reduce(0, (x, y) -> x + y);
    System.out.println(integer);
}
```

collect：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200518225526879.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTIyNTU5NQ==,size_16,color_FFFFFF,t_70#pic_center)

```java
List<Employee> emps = Arrays.asList(
  new Employee(101, "Z3", 19, 9999.99),
  new Employee(102, "L4", 20, 7777.77),
  new Employee(103, "W5", 35, 6666.66),
  new Employee(104, "Tom", 44, 1111.11),
  new Employee(105, "Jerry", 60, 4444.44)
);

@Test
public void test02(){
  //放入List
  List<String> list = emps.stream()
      .map(Employee::getName)
      .collect(Collectors.toList()); 
  list.forEach(System.out::println);
  
  //放入Set
  Set<String> set = emps.stream()
      .map(Employee::getName)
      .collect(Collectors.toSet());
  set.forEach(System.out::println);

  //放入LinkedHashSet
  LinkedHashSet<String> linkedHashSet = emps.stream()
      .map(Employee::getName)
      .collect(Collectors.toCollection(LinkedHashSet::new));
  linkedHashSet.forEach(System.out::println);
}

@Test
public void test03(){
  //总数
  Long count = emps.stream()
      .collect(Collectors.counting());
  System.out.println(count);

  //平均值
  Double avg = emps.stream()
      .collect(Collectors.averagingDouble(Employee::getSalary));
  System.out.println(avg);

  //总和
  Double sum = emps.stream()
      .collect(Collectors.summingDouble(Employee::getSalary));
  System.out.println(sum);

  //最大值
  Optional<Employee> max = emps.stream()
      .collect(Collectors.maxBy((e1, e2) -> Double.compare(e1.getSalary(), e2.getSalary())));
  System.out.println(max.get());

  //最小值
  Optional<Double> min = emps.stream()
      .map(Employee::getSalary)
      .collect(Collectors.minBy(Double::compare));
  System.out.println(min.get());
}

@Test
public void test04(){
  //分组
  Map<Integer, List<Employee>> map = emps.stream()
      .collect(Collectors.groupingBy(Employee::getId));
  System.out.println(map);

  //多级分组
  Map<Integer, Map<String, List<Employee>>> mapMap = emps.stream()
      .collect(Collectors.groupingBy(Employee::getId, Collectors.groupingBy((e) -> {
          if (e.getAge() > 35) {
              return "开除";
          } else {
              return "继续加班";
          }
      })));
  System.out.println(mapMap);
  
  //分区
  Map<Boolean, List<Employee>> listMap = emps.stream()
      .collect(Collectors.partitioningBy((e) -> e.getSalary() > 4321));
  System.out.println(listMap);
}

@Test
public void test05(){
  //总结
  DoubleSummaryStatistics dss = emps.stream()
      .collect(Collectors.summarizingDouble(Employee::getSalary));
  System.out.println(dss.getMax());
  System.out.println(dss.getMin());
  System.out.println(dss.getSum());
  System.out.println(dss.getCount());
  System.out.println(dss.getAverage());
  
  //连接
  String str = emps.stream()
      .map(Employee::getName)
      .collect(Collectors.joining("-")); //可传入分隔符
  System.out.println(str);
}
```

### 5.7 案例

**案例一：**给定一个数字列表，如何返回一个由每个数的平方构成的列表呢？(如：给定【1，2，3，4，5】，返回【1，4，9，16，25】)

```java
@Test
public void test01(){
    List<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
    list.stream()
        .map((x) -> x * x)
        .forEach(System.out::println);
}
```

**案例二：**怎样使用 map 和 reduce 数一数流中有多少个 Employee 呢？

```java
List<Employee> emps = Arrays.asList(
    new Employee(101, "Z3", 19, 9999.99),
    new Employee(102, "L4", 20, 7777.77),
    new Employee(103, "W5", 35, 6666.66),
    new Employee(104, "Tom", 44, 1111.11),
    new Employee(105, "Jerry", 60, 4444.44)
);

@Test
public void test02(){
    Optional<Integer> result = emps.stream()
        .map((e) -> 1)
        .reduce(Integer::sum);
    System.out.println(result.get());
```

### 5.8 并行流

- 并行流：就是把一个内容分成几个数据块，并用不同的线程分别处理每个数据块的流
- Java 8 中将并行进行了优化，我们可以很容易的对数据进行操作；Stream API 可以声明性地通过 parallel() 与 sequential() 在并行流与串行流之间切换

Fork / Join 框架：

![在这里插入图片描述](https://img-blog.csdnimg.cn/2020051822555569.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTIyNTU5NQ==,size_16,color_FFFFFF,t_70#pic_center)

Fork / Join 框架与传统线程池的区别：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200518225613845.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTIyNTU5NQ==,size_16,color_FFFFFF,t_70#pic_center)

Fork / Join 实现：

```java
public class ForkJoinCalculate extends RecursiveTask<Long> {

  private static final long serialVersionUID = 1234567890L;

  private long start;
  private long end;

  private static final long THRESHPLD = 10000;

  public ForkJoinCalculate(long start, long end) {
      this.start = start;
      this.end = end;
  }

  @Override
  protected Long compute() {
      long length = end - start;

      if (length <= THRESHPLD) {
          long sum = 0;
          for (long i = start; i <= end; i++) {
              sum += i;
          }
      } else {
          long middle = (start + end) / 2;

          ForkJoinCalculate left = new ForkJoinCalculate(start, end);
          left.fork(); //拆分子任务 压入线程队列

          ForkJoinCalculate right = new ForkJoinCalculate(middle + 1, end);
          right.fork();

          return left.join() + right.join();
      }

      return null;
  }
}

public class TestForkJoin {

  /**
   * ForkJoin 框架
   */
  @Test
  public void test01(){
      Instant start = Instant.now();

      ForkJoinPool pool = new ForkJoinPool();
      ForkJoinCalculate task = new ForkJoinCalculate(0, 100000000L);

      Long sum = pool.invoke(task);
      System.out.println(sum);

      Instant end = Instant.now();
      System.out.println(Duration.between(start, end).getNano());
  }

  /**
   * 普通 for循环
   */
  @Test
  public void test02(){
      Instant start = Instant.now();

      Long sum = 0L;
      for (long i = 0; i < 100000000L; i++) {
          sum += i;
      }

      Instant end = Instant.now();
      System.out.println(Duration.between(start, end).getNano());
  }
}
```

Java 8 并行流 / 串行流：

```java
@Test
public void test03(){
  //串行流(单线程)：切换为并行流 parallel()
  //并行流：切换为串行流 sequential()
  LongStream.rangeClosed(0, 100000000L)
      .parallel() //底层：ForkJoin
      .reduce(0, Long::sum);

}
```





【重要】在并行处理情况下，传入给Reduce等方法的集合类，需要是线程安全的，否则执行结果会与预期结果不一样。感兴趣的可以尝试下。具体使用见回复，文章内容中示例未进行修改

### 5.9 Stream的Reduce及Collect方法详解

**0. 涉及知识**

大部分涉及到的知识在http://blog.csdn.net/icarusliu/article/details/79495534中已经进行了介绍，还有几个新的类在下面将会涉及到，先行理解：

**0.1 BiFunction**

它是一个函数式接口，包含的函数式方法定义如下：

```java
R apply(T t, U u);
```

可见它与Function不同点在于它接收两个输入返回一个输出； 而Function接收一个输入返回一个输出。
注意它的两个输入、一个输出的类型可以是不一样的。

**0.2 BinaryOperator**

它实际上就是继承自BiFunction的一个接口；我们看下它的定义：

```java
public interface BinaryOperator<T> extends BiFunction<T,T,T>
```

上面已经分析了，BiFunction的三个参数可以是一样的也可以不一样；而BinaryOperator就直接限定了其三个参数必须是一样的；
因此BinaryOperator与BiFunction的区别就在这。
它表示的就是两个相同类型的输入经过计算后产生一个同类型的输出。

**0.3 BiConsumer**

也是一个函数式接口，它的定义如下：



```java
public interface BiConsumer<T, U> {
/**
 * Performs this operation on the given arguments.
 *
 * @param t the first input argument
 * @param u the second input argument
 */
void accept(T t, U u);
}
```


可见它就是一个两个输入参数的Consumer的变种。计算没有返回值。

**1. Reduce**

Reduce中文含义为：减少、缩小；而Stream中的Reduce方法干的正是这样的活：根据一定的规则将Stream中的元素进行计算后返回一个唯一的值。
它有三个变种，输入参数分别是一个参数、二个参数以及三个参数；

**1.1 一个参数的Reduce**

定义如下：

```java
Optional<T> reduce(BinaryOperator<T> accumulator)
```

假设Stream中的元素a[0]/a[1]/a[2]…a[n - 1]，它表达的计算含义，使用Java代码来表述如下： 

```java
T result = a[0];  
for (int i = 1; i < n; i++) {
	result = accumulator.apply(result, a[i]);  
}
return result;  
```



也就是说，a[0]与a[1]进行二合运算，结果与a[2]做二合运算，一直到最后与a[n-1]做二合运算。

可见，reduce在求和、求最大最小值等方面都可以很方便的实现，代码如下，注意其返回的结果是一个Optional对象：

```java
Stream<Integer> s = Stream.of(1, 2, 3, 4, 5, 6);
/**
 * 求和，也可以写成Lambda语法：
 * Integer sum = s.reduce((a, b) -> a + b).get();
 */
Integer sum = s.reduce(new BinaryOperator<Integer>() {
	@Override
	public Integer apply(Integer integer, Integer integer2) {
		return integer + integer2;
	}
}).get();

/**
 * 求最大值，也可以写成Lambda语法：
 * Integer max = s.reduce((a, b) -> a >= b ? a : b).get();
 */
Integer max = s.reduce(new BinaryOperator<Integer>() {
	@Override
	public Integer apply(Integer integer, Integer integer2) {
		return integer >= integer2 ? integer : integer2;
	}
}).get(); 
```

当然可做的事情更多，如将一系列数中的正数求和、将序列中满足某个条件的数一起做某些计算等。

**1.2 两个参数的Reduce**

其定义如下：

```java
T reduce(T identity, BinaryOperator<T> accumulator)
```

相对于一个参数的方法来说，它多了一个T类型的参数；实际上就相当于需要计算的值在Stream的基础上多了一个初始化的值。
同理，当对n个元素的数组进行运算时，其表达的含义如下：

```java
T result = identity; 
for (int i = 0; i < n; i++) {
	result = accumulator.apply(result, a[i]);  
}
return result;  
```

注意区分与一个参数的Reduce方法的不同：它多了一个初始化的值，因此计算的顺序是identity与a[0]进行二合运算，结果与a[1]再进行二合运算，最终与a[n-1]进行二合运算。
因此它与一参数时的应用场景类似，不同点是它使用在可能需要某些初始化值的场景中。

使用示例，如要将一个String类型的Stream中的所有元素连接到一起并在最前面添加[value]后返回：

```java
Stream<String> s = Stream.of("test", "t1", "t2", "teeeee", "aaaa", "taaa");
/**
 * 以下结果将会是：　[value]testt1t2teeeeeaaaataaa
 * 也可以使用Lambda语法：
 * System.out.println(s.reduce("[value]", (s1, s2) -> s1.concat(s2)));
 */
System.out.println(s.reduce("[value]", new BinaryOperator<String>() {
	@Override
	public String apply(String s, String s2) {
		return s.concat(s2);
	}
})); 
```

> 输出：

```
[value]testt1t2teeeeeaaaataaa
```





**1.3 三个参数的Reduce**

三个参数时是最难以理解的。
先来看其定义：

```java
<U> U reduce(U identity,
                 BiFunction<U, ? super T, U> accumulator,
                 BinaryOperator<U> combiner)
```

分析下它的三个参数：

* identity: 一个初始化的值；这个初始化的值其类型是泛型U，与Reduce方法返回的类型一致；注意此时Stream中元素的类型是T，与U可以不一样也可以一样，这样的话操作空间就大了；不管Stream中存储的元素是什么类型，U都可以是任何类型，如U可以是一些基本数据类型的包装类型Integer、Long等；或者是String，又或者是一些集合类型ArrayList等；后面会说到这些用法。
* accumulator: 其类型是BiFunction，输入是U与T两个类型的数据，而返回的是U类型；也就是说返回的类型与输入的第一个参数类型是一样的，而输入的第二个参数类型与Stream中元素类型是一样的。
* combiner: 其类型是BinaryOperator，支持的是对U类型的对象进行操作；

第三个参数combiner主要是使用在并行计算的场景下；如果Stream是非并行时，第三个参数实际上是不生效的。

因此针对这个方法的分析需要分并行与非并行两个场景。



**1.3.1 非并行**

如果Stream是非并行的，combiner不生效；
其计算过程与两个参数时的Reduce基本是一致的。
如Stream中包含了N个元素，其计算过程使用Java代码表述如下：

```java
<U> U reduce(U identity,
                 BiFunction<U, ? super T, U> accumulator,
                 BinaryOperator<U> combiner)
```



这个含义与1.2中的含义基本是一样的——除了类型上，Result的类型是U，而Element的类型是T！如果U与T一样，那么与1.2就是完全一样的；
就是因为不一样，就存在很多种用法了。如假设U的类型是ArrayList，那么可以将Stream中所有元素添加到ArrayList中再返回了，如下示例：

```java
/**
 * 以下reduce生成的List将会是[aa, ab, c, ad]
 * Lambda语法：
 *  System.out.println(s1.reduce(new ArrayList<String>(), (r, t) -> {r.add(t); return r; }, (r1, r2) -> r1));
 */
Stream<String> s1 = Stream.of("aa", "ab", "c", "ad");
System.out.println(s1.reduce(new ArrayList<String>(),
		new BiFunction<ArrayList<String>, String, ArrayList<String>>() {
			@Override
			public ArrayList<String> apply(ArrayList<String> u, String s) {
				u.add(s);
				return u;
			}
		}, new BinaryOperator<ArrayList<String>>() {
			@Override
			public ArrayList<String> apply(ArrayList<String> strings, ArrayList<String> strings2) {
				return strings;
			}
		}));
```

输出：

```
[aa, ab, c, ad]
```



也可以进行元素过滤，即模拟Stream中的Filter函数：

```java
/**
 * 模拟Filter查找其中含有字母a的所有元素，打印结果将是aa ab ad
 * lambda语法：
 * s1.reduce(new ArrayList<String>(), (r, t) -> {if (predicate.test(t)) r.add(t);  return r; },
		(r1, r2) -> r1).stream().forEach(System.out::println);
 */
Stream<String> s1 = Stream.of("aa", "ab", "c", "ad");
Predicate<String> predicate = t -> t.contains("a");
s1.reduce(new ArrayList<String>(), new BiFunction<ArrayList<String>, String, ArrayList<String>>() {
			@Override
			public ArrayList<String> apply(ArrayList<String> strings, String s) {
				if (predicate.test(s)) strings.add(s);
				return strings;
			}
		},
		new BinaryOperator<ArrayList<String>>() {
			@Override
			public ArrayList<String> apply(ArrayList<String> strings, ArrayList<String> strings2) {
				return strings;  
			}
		}).stream().forEach(System.out::println);
```

注意由于是非并行的，第三个参数实际上没有什么意义，可以指定r1或者r2为其返回值，甚至可以指定null为返回值。

**1.3.2 并行**

当Stream是并行时，第三个参数就有意义了，它会将不同线程计算的结果调用combiner做汇总后返回。
注意由于采用了并行计算，前两个参数与非并行时也有了差异！
举个简单点的例子，计算4+1+2+3的结果，其中4是初始值：

```java
/**
 * lambda语法：
 * System.out.println(Stream.of(1, 2, 3).parallel().reduce(4, (s1, s2) -> s1 + s2
 , (s1, s2) -> s1 + s2));
 **/
System.out.println(Stream.of(1, 2, 3).parallel().reduce(4, new BiFunction<Integer, Integer, Integer>() {
			@Override
			public Integer apply(Integer integer, Integer integer2) {
				return integer + integer2;
			}
		}
		, new BinaryOperator<Integer>() {
			@Override
			public Integer apply(Integer integer, Integer integer2) {
				return integer + integer2;
			}
		}));
```



并行时的计算结果是18，而非并行时的计算结果是10！
为什么会这样？
先分析下非并行时的计算过程；第一步计算4 + 1 = 5，第二步是5 + 2 = 7，第三步是7 + 3 = 10。按1.3.1中所述来理解没有什么疑问。
那问题就是非并行的情况与理解有不一致的地方了！
先分析下它可能是通过什么方式来并行的？按非并行的方式来看它是分了三步的，每一步都要依赖前一步的运算结果！那应该是没有办法进行并行计算的啊！可实际上现在并行计算出了结果并且关键其结果与非并行时是不一致的！
那要不就是理解上有问题，要不就是这种方式在并行计算上存在BUG。
暂且认为其不存在BUG，先来看下它是怎么样出这个结果的。猜测初始值4是存储在一个变量result中的；并行计算时，线程之间没有影响，因此每个线程在调用第二个参数BiFunction进行计算时，直接都是使用result值当其第一个参数（由于Stream计算的延迟性，在调用最终方法前，都不会进行实际的运算，因此每个线程取到的result值都是原始的4），因此计算过程现在是这样的：

线程1：1 + 4 = 5；

线程2：2 + 4 = 6；

线程3：3 + 4 = 7；

Combiner函数： 5 + 6 + 7 = 18！
通过多种情况的测试，其结果都符合上述推测！

如以下示例：

```java
/**
 * lambda语法：
 * System.out.println(Stream.of(1, 2, 3).parallel().reduce(4, (s1, s2) -> s1 + s2
 , (s1, s2) -> s1 * s2));
 */
System.out.println(Stream.of(1, 2, 3).parallel().reduce(4, new BiFunction<Integer, Integer, Integer>() {
			@Override
			public Integer apply(Integer integer, Integer integer2) {
				return integer + integer2;
			}
		}
		, new BinaryOperator<Integer>() {
			@Override
			public Integer apply(Integer integer, Integer integer2) {
				return integer * integer2;
			}
		}));
```



以上示例输出的结果是210！
它表示的是，使用4与1、2、3中的所有元素按(s1,s2) -> s1 + s2(accumulator)的方式进行第一次计算，得到结果序列4+1, 4+2, 4+3，即5、6、7；然后将5、6、7按combiner即(s1, s2) -> s1 * s2的方式进行汇总，也就是5 * 6 * 7 = 210。
使用函数表示就是：(4+1) * (4+2) * (4+3) = 210;

reduce的这种写法可以与以下写法结果相等（但过程是不一样的，三个参数时会进行并行处理）：

```java
System.out.println(Stream.of(1, 2, 3).map(n -> n + 4).reduce((s1, s2) -> s1 * s2));
```

这种方式有助于理解并行三个参数时的场景，实际上就是第一步使用accumulator进行转换（它的两个输入参数一个是identity, 一个是序列中的每一个元素），由N个元素得到N个结果；第二步是使用combiner对第一步的N个结果做汇总。

但这里需要注意的是，如果第一个参数的类型是ArrayList等对象而非基本数据类型的包装类或者String，第三个函数的处理上可能容易引起误解，如以下示例：

```java
/**
 * 模拟Filter查找其中含有字母a的所有元素，打印结果将是aa ab ad
 * lambda语法：
 * s1.parallel().reduce(new ArrayList<String>(), (r, t) -> {if (predicate.test(t)) r.add(t);  return r; },
 (r1, r2) -> {System.out.println(r1==r2); return r2; }).stream().forEach(System.out::println);
 */
Stream<String> s1 = Stream.of("aa", "ab", "c", "ad");
Predicate<String> predicate = t -> t.contains("a");
s1.parallel().reduce(new ArrayList<String>(), new BiFunction<ArrayList<String>, String, ArrayList<String>>() {
			@Override
			public ArrayList<String> apply(ArrayList<String> strings, String s) {
				if (predicate.test(s)) {
					strings.add(s);
				}

				return strings;
			}
		},
		new BinaryOperator<ArrayList<String>>() {
			@Override
			public ArrayList<String> apply(ArrayList<String> strings, ArrayList<String> strings2) {
				System.out.println(strings == strings2);
				return strings;
			}
		}).stream().forEach(System.out::println);
```

其中System.out.println(r1==r2)这句打印的结果是什么呢？经过运行后发现是True！
为什么会这样？这是因为每次第二个参数也就是accumulator返回的都是第一个参数中New的ArrayList对象！因此combiner中传入的永远都会是这个对象，这样r1与r2就必然是同一样对象！
因此如果按理解的，combiner是将不同线程操作的结果汇总起来，那么一般情况下上述代码就会这样写(lambda)：

```java
Stream<String> s1 = Stream.of("aa", "ab", "c", "ad");

//模拟Filter查找其中含有字母a的所有元素，由于使用了r1.addAll(r2)，其打印结果将不会是预期的aa ab ad
Predicate<String> predicate = t -> t.contains("a");
s1.parallel().reduce(new ArrayList<String>(), (r, t) -> {if (predicate.test(t)) r.add(t);  return r; },
		(r1, r2) -> {r1.addAll(r2); return r1; }).stream().forEach(System.out::println);
```

这个时候出来的结果与预期的结果就完全不一样了，要多了很多元素！

**3.1.2.7 collect**

collect含义与Reduce有点相似；
先看其定义：

```java
<R> R collect(Supplier<R> supplier,
			  BiConsumer<R, ? super T> accumulator,
			  BiConsumer<R, R> combiner);
```

仍旧先分析其参数（参考其JavaDoc）：

supplier：动态的提供初始化的值；创建一个可变的结果容器（JAVADOC）；对于并行计算，这个方法可能被调用多次，每次返回一个新的对象；
accumulator：类型为BiConsumer，注意这个接口是没有返回值的；它必须将一个元素放入结果容器中（JAVADOC）。
combiner：类型也是BiConsumer，因此也没有返回值。它与三参数的Reduce类型，只是在并行计算时汇总不同线程计算的结果。它的输入是两个结果容器，必须将第二个结果容器中的值全部放入第一个结果容器中（JAVADOC）。
可见Collect与分并行与非并行两种情况。
下面对并行情况进行分析。
直接使用上面Reduce模拟Filter的示例进行演示(使用lambda语法）：

```java
/**
 * 模拟Filter查找其中含有字母a的所有元素，打印结果将是aa ab ad
 */
Stream<String> s1 = Stream.of("aa", "ab", "c", "ad");
Predicate<String> predicate = t -> t.contains("a");
System.out.println(s1.parallel().collect(() -> new ArrayList<String>(),
		(array, s) -> {if (predicate.test(s)) array.add(s); },
		(array1, array2) -> array1.addAll(array2)));
```

根据以上分析，这边理解起来就很容易了：每个线程都创建了一个结果容器ArrayList，假设每个线程处理一个元素，那么处理的结果将会是[aa],[ab],[],[ad]四个结果容器（ArrayList）；最终再调用第三个BiConsumer参数将结果全部Put到第一个List中，因此返回结果就是打印的结果了。

JAVADOC中也在强调结果容器（result container)这个，那是否除集合类型，其结果R也可以是其它类型呢？
先看基本类型，由于BiConsumer不会有返回值，如果是基本数据类型或者String，在BiConsumer中加工后的结果都无法在这个函数外体现，因此是没有意义的。
那其它非集合类型的Java对象呢？如果对象中包含有集合类型的属性，也是可以处理的；否则，处理上也没有任何意义，combiner对象使用一个Java对象来更新另外一个对象？至少目前我没有想到这个有哪些应用场景。它不同Reduce，Reduce在Java对象上是有应用场景的，就因为Reduce即使是并行情况下，也不会创建多个初始化对象，combiner接收的两个参数永远是同一个对象，如假设人有很多条参加会议的记录，这些记录没有在人本身对象里面存储而在另外一个对象中；人本身对象中只有一个属性是最早参加会议时间，那就可以使用reduce来对这个属性进行更新。当然这个示例不够完美，它能使用其它更快的方式实现，但至少通过Reduce是能够实现这一类型的功能的。

 



# 6. Optional

**定义：**Optional 类 (java.util.Optional) 是一个容器类，代表一个值存在或不存在，原来用 null 表示一个值不存在，现在用 Optional 可以更好的表达这个概念；并且可以避免空指针异常

常用方法：

- Optional.of(T t)：创建一个 Optional 实例
- Optional.empty(T t)：创建一个空的 Optional 实例
- Optional.ofNullable(T t)：若 t 不为 null，创建 Optional 实例，否则空实例
- isPresent()：判断是否包含某值
- orElse(T t)：如果调用对象包含值，返回该值，否则返回 t
- orElseGet(Supplier s)：如果调用对象包含值，返回该值，否则返回 s 获取的值
- map(Function f)：如果有值对其处理，并返回处理后的 Optional，否则返回 Optional.empty()
- flatmap(Function mapper)：与 map 相似，要求返回值必须是 Optional

Optional.of(T t)：

```java
@Test
public void test01(){
    Optional<Employee> op = Optional.of(new Employee());
    Employee employee = op.get();
}
```

Optional.empty(T t)：

```java
@Test
public void test02(){
    Optional<Employee> op = Optional.empty();
    Employee employee = op.get();
}
```

Optional.ofNullable(T t)：

```java
@Test
public void test03(){
    Optional<Employee> op = Optional.ofNullable(new Employee());
    Employee employee = op.get();
}
```

isPresent()：

```java
@Test
public void test03(){
    Optional<Employee> op = Optional.ofNullable(new Employee());
    if (op.isPresent()) {
        Employee employee = op.get();
    }
}
```

不再一一例举…

# 7. 接口

### 7.1 默认方法

```java
public interface MyFun {

    default String getName(){
        return "libo";
    }

    default Integer getAge(){
        return 22;
    }
}
```

类优先原则：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200518225652926.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTIyNTU5NQ==,size_16,color_FFFFFF,t_70#pic_center)

### 7.2 静态方法

```
public interface MyFun {

    static void getAddr(){
        System.out.println("addr");
    }

    static String Hello(){
        return "Hello World";
    }
}
```

# 8. Date / Time API

### 8.1 安全问题

传统的日期格式化：

```java
@Test
public void test01(){
    SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

    Callable<Date> task = () -> sdf.parse("20200517");

    ExecutorService pool = Executors.newFixedThreadPool(10);

    ArrayList<Future<Date>> result = new ArrayList<>();
    for (int i = 0; i < 10; i++) {
        result.add(pool.submit(task));
    }

    for (Future<Date> future : result) {
        try {
            System.out.println(future.get());
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
    }
    
    pool.shutdown();
}
```

加锁：

```java
public class DateFormatThreadLocal {
    private static final ThreadLocal<DateFormat> df = ThreadLocal.withInitial(() -> new SimpleDateFormat("yyyy-MM-dd HH:mm:ss"));

    public static Date convert(String source) throws ParseException{
        return df.get().parse(source);
    }
}

@Test
public void test02(){
    Callable<Date> task = () -> DateFormatThreadLocal.convert("20200517");

    ExecutorService pool = Executors.newFixedThreadPool(10);

    ArrayList<Future<Date>> result = new ArrayList<>();
    for (int i = 0; i < 10; i++) {
        result.add(pool.submit(task));
    }

    for (Future<Date> future : result) {
        try {
            System.out.println(future.get());
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
    }

    pool.shutdown();
}
```

DateTimeFormatter：

```java
@Test
public void test03(){
    DateTimeFormatter dtf = DateTimeFormatter.ISO_LOCAL_DATE;

    Callable<LocalDate> task = () -> LocalDate.parse("20200517",dtf);

    ExecutorService pool = Executors.newFixedThreadPool(10);

    ArrayList<Future<LocalDate>> result = new ArrayList<>();
    for (int i = 0; i < 10; i++) {
        result.add(pool.submit(task));
    }

    for (Future<LocalDate> future : result) {
        try {
            System.out.println(future.get());
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
    }

    pool.shutdown();
}
```

### 8.2 本地时间 / 日期

ISO 标准：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200518225724271.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTIyNTU5NQ==,size_16,color_FFFFFF,t_70#pic_center)

常用方法：

| 方法名                                                       | 返回值类型           | 解释                                                         |
| ------------------------------------------------------------ | -------------------- | ------------------------------------------------------------ |
| now( )                                                       | static LocalDateTime | 从默认时区的系统时钟获取当前日期                             |
| of(int year, int month, int dayOfMonth, int hour, int minute, int second) | static LocalDateTime | 从年，月，日，小时，分钟和秒获得 LocalDateTime的实例，将纳秒设置为零 |
| plus(long amountToAdd, TemporalUnit unit)                    | LocalDateTime        | 返回此日期时间的副本，并添加指定的数量                       |
| get(TemporalField field)                                     | int                  | 从此日期时间获取指定字段的值为 int                           |

@Test：

```java
@Test
public void test01(){
  //获取当前时间日期 now
  LocalDateTime ldt1 = LocalDateTime.now();
  System.out.println(ldt1);

  //指定时间日期 of
  LocalDateTime ldt2 = LocalDateTime.of(2020, 05, 17, 16, 24, 33);
  System.out.println(ldt2);

  //加 plus
  LocalDateTime ldt3 = ldt2.plusYears(2);
  System.out.println(ldt3);

  //减 minus
  LocalDateTime ldt4 = ldt2.minusMonths(3);
  System.out.println(ldt4);

  //获取指定的你年月日时分秒... get
  System.out.println(ldt2.getDayOfYear());
  System.out.println(ldt2.getHour());
  System.out.println(ldt2.getSecond());
}
```

LocalDate / LocalTime 不再一一例举…

### 8.3 时间戳

Instant：以 Unix 元年 1970-01-01 00:00:00 到某个时间之间的毫秒值

@Test：

```java
@Test
public void test02(){
    // 默认获取 UTC 时区 (UTC：世界协调时间)
    Instant ins1 = Instant.now();
    System.out.println(ins1);

    //带偏移量的时间日期 (如：UTC + 8)
    OffsetDateTime odt1 = ins1.atOffset(ZoneOffset.ofHours(8));
    System.out.println(odt1);

    //转换成对应的毫秒值
    long milli1 = ins1.toEpochMilli();
    System.out.println(milli1);

    //构建时间戳
    Instant ins2 = Instant.ofEpochSecond(60);
    System.out.println(ins2);
}
```

### 8.4 时间 / 日期 差

- Duration：计算两个时间之间的间隔
- Period：计算两个日期之间的间隔

@Test：

```java
@Test
public void test03(){
    //计算两个时间之间的间隔 between
    Instant ins1 = Instant.now();
    try {
        Thread.sleep(1000);
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
    Instant ins2 = Instant.now();
    Duration dura1 = Duration.between(ins1, ins2);
    System.out.println(dura1.getSeconds());
    System.out.println(dura1.toMillis());
}

@Test
public void test04(){
    LocalDate ld1 = LocalDate.of(2016, 9, 1);
    LocalDate ld2 = LocalDate.now();
    Period period = Period.between(ld1, ld2);  // ISO 标准
    System.out.println(period.getYears());
    System.out.println(period.toTotalMonths());
}
```

### 8.5 时间校正器

操纵日期：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200518225752314.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTIyNTU5NQ==,size_16,color_FFFFFF,t_70#pic_center)

@Test：

```java
@Test
public void test01(){
    //TemporalAdjusters：时间校正器
    LocalDateTime ldt1 = LocalDateTime.now();
    System.out.println(ldt1);

    //指定日期时间中的 年 月 日 ...
    LocalDateTime ldt2 = ldt1.withDayOfMonth(10);
    System.out.println(ldt2);

    //指定时间校正器
    LocalDateTime ldt3 = ldt1.with(TemporalAdjusters.next(DayOfWeek.SUNDAY));
    System.out.println(ldt3);

    //自定义时间校正器
    LocalDateTime ldt5 = ldt1.with((ta) -> {
        LocalDateTime ldt4 = (LocalDateTime) ta;
        DayOfWeek dow1 = ldt4.getDayOfWeek();
        if (dow1.equals(DayOfWeek.FRIDAY)) {
            return ldt4.plusDays(3);
        } else if (dow1.equals(DayOfWeek.SATURDAY)) {
            return ldt4.plusDays(2);
        } else {
            return ldt4.plusDays(1);
        }
    });
    System.out.println(ldt5);
}
```

### 8.6 格式化

- DateTimeFormatter：格式化时间 / 日期

  ```java
  @Test
  public void test01(){
   //默认格式化
   DateTimeFormatter dtf1 = DateTimeFormatter.ISO_DATE_TIME;
   LocalDateTime ldt1 = LocalDateTime.now();
   String str1 = ldt1.format(dtf1);
   System.out.println(str1);
  
   //自定义格式化 ofPattern
   DateTimeFormatter dtf2 = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
   LocalDateTime ldt2 = LocalDateTime.now();
   String str2 = ldt2.format(dtf2);
   System.out.println(str2);
  
   //解析
   LocalDateTime newDate = ldt1.parse(str1, dtf1);
   System.out.println(newDate);
  }
  ```

  ### 8.7 时区

- ZonedDate

- ZonedTime

- ZonedDateTime @Test：

```java
@Test
public void test02(){
    //查看支持的时区
    Set<String> set = ZoneId.getAvailableZoneIds();
    set.forEach(System.out::println);

    //指定时区
    LocalDateTime ldt1 = LocalDateTime.now(ZoneId.of("Europe/Tallinn"));
    System.out.println(ldt1);

    //在已构建好的日期时间上指定时区
    LocalDateTime ldt2 = LocalDateTime.now(ZoneId.of("Europe/Tallinn"));
    ZonedDateTime zdt1 = ldt2.atZone(ZoneId.of("Europe/Tallinn"));
    System.out.println(zdt1);
}
```

一些转换：

```java
@Test
public void test03(){
    // Date 转 LocalDateTime 
    Date date = new Date();
    Instant instant = date.toInstant();
    ZoneId zoneId = ZoneId.systemDefault();
    LocalDateTime localDateTime = instant.atZone(zoneId).toLocalDateTime();

    // LocalDateTime 转 Date
    LocalDateTime localDateTime = LocalDateTime.now();
    ZoneId zoneId = ZoneId.systemDefault();
    ZonedDateTime zdt = localDateTime.atZone(zoneId);
    Date date = Date.from(zdt.toInstant());
    
    // 原则：利用 时间戳Instant
}
```

# 9. 注解

### 9.1 重复注解

定义注解：

```java
@Repeatable(MyAnnotations.class) //指定容器类
@Target({ElementType.TYPE, ElementType.METHOD,  ElementType.FIELD})
@Retention(RetentionPolicy.RUNTIME)
public @interface MyAnnotation {

    String value() default "Java 8";
}
```

定义容器：

```java
@Target({ElementType.TYPE, ElementType.METHOD,  ElementType.FIELD})
@Retention(RetentionPolicy.RUNTIME)
public @interface MyAnnotations {

    MyAnnotation[] value();
}
```

@Test：

```java
public class Test01 {

    //重复注解
    @Test
    @MyAnnotation("Hello")
    @MyAnnotation("World")
    public void test01() throws NoSuchMethodException {
        Class<Test01> clazz = Test01.class;
        Method test01 = clazz.getMethod("test01");
        MyAnnotation[] mas = test01.getAnnotationsByType(MyAnnotation.class);
        for (MyAnnotation ma : mas) {
            System.out.println(ma.value());
        }
    }
}
```

### 9.2 类型注解

Java 8 新增注解：新增ElementType.TYPE_USE 和ElementType.TYPE_PARAMETER（在Target上）