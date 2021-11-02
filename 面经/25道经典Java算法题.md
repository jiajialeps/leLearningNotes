## 【程序1:兔子增生问题】

题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？   

```java
//这是一个菲波拉契数列问题

public class test01 {
    public static void main(String[] args) {
        int f1=1,f2=1,f;
        int M=30;
        System.out.println(1);
        System.out.println(2);
        for(int i=3;i<M;i++) {
            f=f2;
            f2=f1+f2;
            f1=f;
            System.out.println(f2);
        }
    }

}
```



## 【程序2：素数问题】

题目：判断101-200之间有多少个素数，并输出所有素数。 
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除， 则表明此数不是素数，反之是素数。

 ```java
public class test02 {
    public static void main(String[] args) {
        int count=0;
        for(int i=101;i<200;i+=2) {
            boolean flag=true;
            for(int j=2;j<=Math.sqrt(i);j++) {
                if(i%j==0) {
                    flag=false;
                    break;
                }
            }
            if(flag==true) {
                count++;
                System.out.println(i);
            }
        }
        System.out.println(count);
    }

}
 ```



## 【程序3:水仙花问题】


题目：打印出所有的 "水仙花数 "，所谓 "水仙花数 "是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个 "水仙花数 "，因为153=1的三次方＋5的三次方＋3的三次方。

 ```java
public class test03 {
    public static void main(String[] args) {
        int a,b,c;
        for(int i=101;i<1000;i++) {
            a=i%10;
            b=i/10%10;
            c=i/100;
            if(a*a*a+b*b*b+c*c*c==i)
                System.out.println(i);
        }
    }
} 
 ```





## 【程序4:正整数分解质因数】

题目：将一个正整数分解质因数。例如：输入90,打印出90=233*5。   
程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：   


(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。   

(2)如果n <> k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。 

(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。

```java
import java.util.Scanner;
public class test04 {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        int n=input.nextInt();
        int k=2;
        while(n>=k) {
            if(n==k) {
                System.out.println(k);
                break;
            }else if (n%k==0) {
                System.out.println(k);
                n=n/k;
            }else {
                k++;
            }
        }
    }

}
```



## 【程序5：成绩分配问题】


题目：利用条件运算符的嵌套来完成此题：学习成绩> =90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

 



```java
import java.util.Scanner;
public class test05 {
public static void main(String[] args) {
 
    Scanner input=new Scanner(System.in);
 
    int score=input.nextInt();
 
    char grade=score>=90?'A':score>=60?'B':'C';
 
    System.out.println(grade);
}
}
```


三目运算符

```shell
1、三目运算符 (表达式1)?(表达式2):(表达式3)，计算方法是这样的：表达式1是一个逻辑表达式，如果其值为true，则整个表达式的值为表达式2的值，否则为表达式3的值
2、例子：int i = (5 > 3) ? (5 + 3) : (5 - 3);结果为i = 8.因为5 > 3为true，所以i = 5 + 3.
3、根据三目运算符的从右到左的结合性，我是这样划分的
year > a.year ? 1 : (year < a.year ? -1 : (month > a.month ? 1 : (month < a.month ? -1 : (day > a.day ? 1 : (day < a.day ? -1 : 0)))));
所以应该从最右边的那个表达式开始计算，结果应该是1、0、-1中的一个值。
```





## 【程序6:大公约数和最小公倍数】

题目：输入两个正整数m和n，求其最大公约数和最小公倍数。   /*在循环中，只要除数不等于0，用较大数除以较小的数，将小的一个数作为下一轮循环的大数，取得的余数作为下一轮循环的较小的数，如此循环直到较小的数的值为0，返回较大的数，此数即为最大公约数，最小公倍数为两数之积除以最大公约数。 

```java
import java.util.Scanner;public class test06 {
 
    public static void main(String[] args) {
 
        Scanner input =new Scanner(System.in);
 
        int a=input.nextInt();
 
        int b=input.nextInt();
 
 
        test06 test=new test06();
 
        int i = test.gongyinshu(a, b);
 
 
        System.out.println("最小公因数"+i);
 
        System.out.println("最大公倍数"+a*b/i);
 
    }
 
    public int gongyinshu(int a,int b) {
 
        if(a<b) {
 
            int t=b;
 
            b=a;
 
            a=t;
 
        }
 
        while(b!=0) {
 
            if(a==b)
 
                return a;
 
            int x=b;
 
            b=a%b;
 
            a=x;
 
        }
 
        return a;
 
    }
}
```





## 【程序7:统计英文字母、空格、数字个数】

题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

```java
import java.util.Scanner;
public class test07 {
    public static void main(String[] args) {
        int abccount=0;
        int spacecount=0;
        int numcount=0;
        int othercount=0;
 
        Scanner input=new Scanner(System.in);
        String toString=input.nextLine();
        char [] ch=toString.toCharArray();
 
        for(int i=0;i<ch.length;i++) {
            if(Character.isLetter(ch[i])) {
                abccount++;
            }else if(Character.isDigit(ch[i])) {
                numcount++;
            }else if(Character.isSpaceChar(ch[i])){
                spacecount++;
            }else {
                othercount++;
            }
        }
        System.out.println(abccount);
        System.out.println(spacecount);
        System.out.println(numcount);
        System.out.println(othercount);
    }
}
```





## 【程序8:数字相加问题】


题目：求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。

 ```java
import java.util.Scanner;
public class test08 {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        int a=input.nextInt();
        int n=input.nextInt();
 
        int sum=0,b=0;
        for(int i=0;i<n;i++) {
            b+=a;
            sum+=b;
            a=a*10;
        }
        System.out.println(sum);
    }
 
}
 ```



## 【程序9:完数问题】

题目：一个数如果恰好等于它的因子之和，这个数就称为 "完数 "。例如6=1＋2＋3.编程     找出1000以内的所有完数。

```java
public class test09 {

	public static void main(String[] args) {

		for (int i = 1; i <= 1000; i++) {

			int t = 0;

			for (int j = 1; j <= i / 2; j++) {

				if (i % j == 0) {

					t += j;

				}

			}

			if (t == i) {

				System.out.println(i);

			}

		}

	}
}
```






【程序10】


题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在 第10次落地时，共经过多少米？第10次反弹多高？

 ```java
public class test10 {
 
    public static void main(String[] args) {
 
        double h=100;
 
        double s=100;
 
        for(int i=1;i<=10;i++) {
 
            h=h/2;
 
            s=s+2*h;
 
        }
 
        System.out.println(s);
 
        System.out.println(h);
}
}
 ```




【程序11】

题目：有1、2、3、4四个数字，能组成多少个互不相同且一个数字中无重复数字的三位数？并把他们都输入。    

```java
public class test11 {

	/**
	 * 题目：有1、2、3、4四个数字，能组成多少个互不相同且一个数字中无重复数字的三位数？并把他们都输入
	 * 
	 * @param args
	 */
	public static void main(String[] args) {
		int count = 0;
		for (int i = 1; i <= 4; i++) {
			for (int k = 1; k <= 4; k++) {
				for (int j = 1; j <= 4; j++) {
					if (i != k && k != j && i != j) {
						count++;
						System.out.println(i * 100 + j * 10 + k);
					}

				}

			}

		}
		System.out.println(count);

	}
```




【程序12】

 

题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润，求应发放奖金总数？   

```java
test12 {
 
public static void main(String[] args) {
 
        Scanner input =new Scanner(System.in);
 
        double x=input.nextDouble();
 
        double y=0;
 
 
        if(x>0&&x<=10) {
 
        y=x*0.1;
 
        }else if (x>10&&x<=20) {
 
        y=10*0.1+(x-10)*0.075;
 
        }else if (x>20&&x<=40) {
 
        y=10*0.1+10*0.075+(x-20)*0.05;
 
        }else if (x>40&&x<=60) {
 
        y=10*0.1+10*0.075+20*0.05+(x-40)*0.03;
 
        } else if (x>60&&x<=100) {
 
        y=10*0.1+10*0.075+20*0.05+20*0.03+(x-60)*0.015;
 
        }else if (x>100) {
 
        y=10*0.1+10*0.075+20*0.05+20*0.03+40*0.015+(x-100)*0.01;
 
        }
 
        System.out.println(y);
 
    }
    }
```



【程序13】


题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

 ```java
public class test13 {
public static void main(String[] args) {
for(int i=-100;i<10000;i++) {
if(Math.sqrt(i+100)%1==0&&Math.sqrt(i+268)%1==0) {
System.out.println(i);
}
}
}
}
 ```




【程序14】


题目：输入某年某月某日，判断这一天是这一年的第几天？

 ```java
import java.util.*;public class lianxi14 {public static void main(String[] args) {     int year, month, day;     int days = 0;     int d = 0;     int e;     input fymd = new input();     do {     e = 0;     System.out.print("输入年：");     year =fymd.input();     System.out.print("输入月：");     month = fymd.input();     System.out.print("输入天：");     day = fymd.input();     if (year < 0 || month < 0 || month > 12 ||day < 0 || day > 31) {     System.out.println("输入错误，请重新输入！");     e=1 ;     }     }while( e==1);
 
    for (int i=1; i <month; i++) {
        switch (i) {
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                days = 31;
                break;
            case 4:
            case 6:
            case 9:
            case 11:
                days = 30;
                break;
            case 2:
                if ((year % 400 == 0) || (year % 4 == 0&& year % 100 != 0)) {
                    days = 29;
                } else {
                    days = 28;
                }
                break;
        }
        d += days;
    }
    System.out.println(year + "-" + month +"-" + day + "是这年的第" +(d+day) + "天。");
}
}
class input{
    public int input() {
        int value = 0;
        Scanner s = new Scanner(System.in);
        value = s.nextInt();
        return value;
    }
}
 ```




【程序15】


题目：输入三个整数x,y,z，请把这三个数由小到大输出。

```java
import java.util.Scanner;
public class test15 {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        int x=input.nextInt();
        int y=input.nextInt();
        int z=input.nextInt();
 
        int t=0;
        if(x>y) {
            t=x;
            x=y;
            y=t;
        }
        if(y>z) {
            t=z;
            z=y;
            y=t;
        }
        if(x>y) {
            t=x;
            x=y;
            y=t;
        }
        System.out.println(x+""+y+""+z);
    }
 
}
```




【程序16】


题目：输出9*9口诀。

```java
public class test16 {
 
    public static void main(String[] args) {
 
        for(int i=1;i<10;i++){
 
            for(int j=1;j<=i;j++) {
 
                System.out.print(i+"*"+j+"="+i*j);
 
                System.out.print(" ");
 
            }
 
            System.out.println("");
 
        }
 
    }
}
```




【程序17】


题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个     第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下     的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。

```java
public class test17 {
 
    public static void main(String[] args) {
 
        int x=1;
 
        for(int i=10;i>1;i--) {
 
            x=(x+1)*2;
 
        }
 
        System.out.println(x);
 
    }
}
```




【程序18】


题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

```java
public class test18 {
 
    public static void main(String[] args) {
 
        for(char i='x';i<='z';i++) {
 
            for (char j='x';j<='z';j++) {
 
                if(i!=j) {
 
                    for(char k='x';k<='z';k++) {
 
                        if(i!=k&&j!=k) {
 
                            if(i!='x'&&j!='x'&&j!='z') {
 
                                System.out.println("a:"+i+"
b:"+j+"
c:"+k);
 
                            }
 
                        }
 
                    }
 
                }
 
            }
 
        }
 
    }}
```





【程序19】


题目：打印出图案（菱形）   

```java
public class lianxi19 {
public static void main(String[] args) {
    int H = 7, W = 7;//高和宽必须是相等的奇数
    for(int i=0; i<(H+1) / 2; i++) {
     for(int j=0; j<W/2-i; j++) {
      System.out.print(" ");
 
    }
     for(int k=1; k<(i+1)*2; k++) {
      System.out.print('*');
     }
     System.out.println();
    }
    for(int i=1; i<=H/2; i++) {
     for(int j=1; j<=i; j++) {
      System.out.print(" ");
     }
     for(int k=1; k<=W-2*i; k++) {
      System.out.print('*');
     }
     System.out.println();
    }
}
}
```






【程序20】


题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和。

```java
public class test20 {
public static void main(String[] args) {
double sum=0,ver=2;
for(int i=1;i<=10;i++) {
sum+=ver/i;
ver+=i;
}
System.out.println(sum);
}
 
}
```






【程序21】


题目：求1+2!+3!+…+20!的和

```java
public class test21 {
 
public static void main(String[] args) {
 
long sum=0,ver=1;
 
for(int i=1;i<=20;i++) {
 
ver=ver*i;
 
sum+=ver;
 
}
 
System.out.println(sum);
 
}}
```






【程序22】


题目：利用递归方法求5!。

```java
public class test22 {
public static void main(String[] args) {
System.out.println(fac(5));
}
public static int fac(int i) {
if(i==1) return 1;
else {
return i*fac(i-1);
}
}
 
}
```






【程序23】


题目：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？

 

```java
public class test23 {
    public static void main(String[] args) {
        int age=10;
        for(int i=2;i<=5;i++) {
            age+=2;
        }
        System.out.println( age);
    }
 
}
```






【程序24】


题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。   
//使用了长整型最多输入18位



```java
import java.util.Scanner;
public class test24 {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        String toString=input.nextLine();
        char[] num=toString.toCharArray();
        System.out.println(num.length);
        for(int i=num.length;i>0;i--) {
            System.out.print(num[i-1]);
        }
    }
 
}
```




【程序25】


题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。



```java
import java.util.Scanner;public class test25 {
 
    public static void main(String[] args) {
 
        Scanner input =new Scanner(System.in);
 
        int numtest=input.nextInt();
 
        System.out.println(ver(numtest));
 
 
    }
 
    public static boolean ver(int num) {
 
        if(num<0||(num!=0&&num%10==0))
 
            return false;
 
        int ver=0;
 
        while(num>ver) {
 
            ver=ver*10+num%10;
 
            num=num/10;
 
        }
 
        return(num==ver||num==ver/10);
 
    }
}
```

