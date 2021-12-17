

java新特性

#### 案例分析：简化查询代码逻辑

```java
List<Employee> emps = Arrays.asList(
			new Employee(101, "张三", 18, 9999.99),
			new Employee(102, "李四", 59, 6666.66),
			new Employee(103, "王五", 28, 3333.33),
			new Employee(104, "赵六", 8, 7777.77),
			new Employee(105, "田七", 38, 5555.55)
	);

	//需求：获取公司中年龄小于 35 的员工信息
	public List<Employee> filterEmployeeAge(List<Employee> emps){
		List<Employee> list = new ArrayList<>();
		
		for (Employee emp : emps) {
			if(emp.getAge() <= 35){
				list.add(emp);
			}
		}
		
		return list;
	}
	
	@Test
	public void test3(){
		List<Employee> list = filterEmployeeAge(emps);
		
		for (Employee employee : list) {
			System.out.println(employee);
		}
	}
	
	//需求：获取公司中工资大于 5000 的员工信息
	public List<Employee> filterEmployeeSalary(List<Employee> emps){
		List<Employee> list = new ArrayList<>();
		
		for (Employee emp : emps) {
			if(emp.getSalary() >= 5000){
				list.add(emp);
			}
		}
		
		return list;
	}
```



优化

```java


//优化方式一：策略设计模式
public List<Employee> filterEmployee(List<Employee> emps, MyPredicate<Employee> mp){
	List<Employee> list = new ArrayList<>();
	
	for (Employee employee : emps) {
		if(mp.test(employee)){
			list.add(employee);
		}
	}
	
	return list;
}

@Test
public void test4(){
	List<Employee> list = filterEmployee(emps, new FilterEmployeeForAge());
	for (Employee employee : list) {
		System.out.println(employee);
	}
	
	System.out.println("------------------------------------------");
	
	List<Employee> list2 = filterEmployee(emps, new FilterEmployeeForSalary());
	for (Employee employee : list2) {
		System.out.println(employee);
	}
}

//优化方式二：匿名内部类
@Test
public void test5(){
	List<Employee> list = filterEmployee(emps, new MyPredicate<Employee>() {
		@Override
		public boolean test(Employee t) {
			return t.getId() <= 103;
		}
	});
	
	for (Employee employee : list) {
		System.out.println(employee);
	}
}

//优化方式三：Lambda 表达式
@Test
public void test6(){
	List<Employee> list = filterEmployee(emps, (e) -> e.getAge() <= 35);
	list.forEach(System.out::println);
	
	System.out.println("------------------------------------------");
	
	List<Employee> list2 = filterEmployee(emps, (e) -> e.getSalary() >= 5000);
	list2.forEach(System.out::println);
}

//优化方式四：Stream API
@Test
public void test7(){
	emps.stream()
		.filter((e) -> e.getAge() <= 35)
		.forEach(System.out::println);
	
	System.out.println("----------------------------------------------");
	
	emps.stream()
		.map(Employee::getName)
		.limit(3)
		.sorted()
		.forEach(System.out::println);
}
```
# 一、Lambda 表达式

```java
package com.atguigu.java8;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Consumer;

import org.junit.Test;

/*
 * 一、Lambda 表达式的基础语法：Java8中引入了一个新的操作符 "->" 该操作符称为箭头操作符或 Lambda 操作符
 * 						    箭头操作符将 Lambda 表达式拆分成两部分：
 * 
 * 左侧：Lambda 表达式的参数列表
 * 右侧：Lambda 表达式中所需执行的功能， 即 Lambda 体
 * 
 *
 * 
 * 语法格式二：有一个参数，并且无返回值
 * 		(x) -> System.out.println(x)   eg:test1()
 * 
 * 语法格式三：若只有一个参数，小括号可以省略不写
 * 		x -> System.out.println(x)
 * 
 * 语法格式四：有两个以上的参数，有返回值，并且 Lambda 体中有多条语句,
 *		Comparator<Integer> com = (x, y) -> {
 *			System.out.println("函数式接口");
 *			return Integer.compare(x, y);
 *		};
 *注：多条语句必须用{} 
 *
 * 语法格式五：若 Lambda 体中只有一条语句， return 和 大括号都可以省略不写
 * 		Comparator<Integer> com = (x, y) -> Integer.compare(x, y);
 * 
 * 语法格式六：Lambda 表达式的参数列表的数据类型可以省略不写，因为JVM编译器通过上下文推断出，数据类型，即“类型推断”
 * 		(Integer x, Integer y) -> Integer.compare(x, y);
 * 
 * 上联：左右遇一括号省
 * 下联：左侧推断类型省
 * 横批：能省则省
 * 
 * 二、Lambda 表达式需要“函数式接口”的支持
 * 函数式接口：接口中只有一个抽象方法的接口，称为函数式接口。 可以使用注解 @FunctionalInterface 修饰
 * 			 可以检查是否是函数式接口
 */
public class TestLambda2 {
	
	@Test
	public void test1(){
		int num = 0;//jdk 1.7 前，必须是 final
		
		Runnable r = new Runnable() {
			@Override
			public void run() {
				System.out.println("Hello World!" + num);
			}
		};
		
		r.run();
		
		System.out.println("-------------------------------");
		
        
		Runnable r1 = () -> System.out.println("Hello Lambda!");
		r1.run();
	}
	
	@Test
	public void test2(){
		Consumer<String> con = x -> System.out.println(x);
		con.accept("我大尚硅谷威武！");
	}
	
	@Test
	public void test3(){
		Comparator<Integer> com = (x, y) -> {
			System.out.println("函数式接口");
			return Integer.compare(x, y);
		};
	}
	
	@Test
	public void test4(){
		Comparator<Integer> com = (x, y) -> Integer.compare(x, y);
	}
	
	@Test
	public void test5(){
//		String[] strs;
//		strs = {"aaa", "bbb", "ccc"};
		
		List<String> list = new ArrayList<>();
		
		show(new HashMap<>());
	}

	public void show(Map<String, Integer> map){
		
	}
	
	//需求：对一个数进行运算
	@Test
	public void test6(){
		Integer num = operation(100, (x) -> x * x);
		System.out.println(num);
		
		System.out.println(operation(200, (y) -> y + 200));
	}
	
	public Integer operation(Integer num, MyFun mf){
		return mf.getValue(num);
	}
}

```



