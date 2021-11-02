## 1.什么是微服务？

单个轻量级服务一般为一个单独微服务，微服务讲究的是 专注某个功能的实现，比如登录系统只专注于用户登录方面功能的实现，讲究的是职责单一，开箱即用，可以独立运行。微服务架构系统是一个分布式的系统，按照业务进行划分服务单元模块，解决单个系统的不足，满足越来越复杂的业务需求。

马丁福勒（Martin Fowler）：就目前而言，对于微服务业界并没有一个统一的、标准的定义。但通常而言，微服务架构是一种架构模式或者说是架构风格，它提倡将单一应用程序划分成一组小的服务。每个服务运行在其独立的自己的进程中服务之间相互配合、相互协调，为用户提供最终价值。服务之间采用轻量级通信。每个服务都围绕具体业务进行构建，并能够独立部署到生产环境等。另外应尽量避免统一的、集中的服务管理机制。

通俗的来讲：

> 微服务就是一个独立的职责单一的服务应用程序。在 intellij idea 工具里面就是用maven开发的一个个独立的module，具体就是使用springboot 开发的一个小的模块，处理单一专业的业务逻辑，一个模块只做一个事情。

微服务强调的是服务大小，关注的是某一个点，具体解决某一个问题/落地对应的一个服务应用，可以看做是idea 里面一个 module。

比如你去医院：你的牙齿不舒服，那么你就去牙科。你的头疼，那么你就去脑科。一个个的科室，就是一个微服务，一个功能就是一个服务。

业界大牛 马丁福勒（Martin Fowler）讲解 ：

> https://martinfowler.com/bliki/

看不懂英文，这里有中文博客翻译的：

> https://blog.csdn.net/u013970991/article/details/53333921

参考：[【120期】面试官：谈谈什么是微服务？](http://mp.weixin.qq.com/s?__biz=MzIyNDU2ODA4OQ==&mid=2247484794&idx=1&sn=a8b0b863ca3e86f34f407bc7cca0c405&chksm=e80db30cdf7a3a1a8e668fd328f8fea0b3b2f4218edb656f41bb8f9a4521a135b24dbc8f9a49&scene=21#wechat_redirect)

## 2.微服务之间如何独立通讯的?

同步通信：dobbo通过 RPC 远程过程调用、springcloud通过 REST  接口json调用 等。

异步：消息队列，如：RabbitMq、ActiveM、Kafka 等。

## 3.SpringCloud 和 Dubbo 有哪些区别?

首先，他们都是分布式管理框架。

dubbo 是二进制传输，占用带宽会少一点。SpringCloud是http 传输，带宽会多一点，同时使用http协议一般会使用JSON报文，消耗会更大。

dubbo 开发难度较大，所依赖的 jar 包有很多问题大型工程无法解决。SpringCloud 对第三方的继承可以一键式生成，天然集成。

SpringCloud 接口协议约定比较松散，需要强有力的行政措施来限制接口无序升级。

最大的区别:

**Spring Cloud抛弃了Dubbo 的RPC通信，采用的是基于HTTP的REST方式。**

严格来说，这两种方式各有优劣。虽然在一定程度上来说，后者牺牲了服务调用的性能，但也避免了上面提到的原生RPC带来的问题。而且REST相比RPC更为灵活，服务提供方和调用方的依赖只依靠一纸契约，不存在代码级别的强依赖，这在强调快速演化的微服务环境下，显得更为合适。

![图片](https://mmbiz.qpic.cn/mmbiz_png/8KKrHK5ic6XB4UytSaRiaQiaMLQMiapTP0Nyic8FJGcial6VUlwS3zgVOk1gicTmHAPAuGa2jRdgFHTTzpIFmWVO9FL8Q/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 4.SpringBoot 和 SpringCloud 之间关系？

SpringBoot：专注于快速方便的开发单个个体微服务（关注微观）；SpringCloud：关注全局的微服务协调治理框架，将SpringBoot开发的一个个单体微服务组合并管理起来（关注宏观）；

SpringBoot可以离开SpringCloud独立使用，但是SpringCloud不可以离开SpringBoot，属于依赖关系。

参考：

> https://blog.csdn.net/qq_41497111/article/details/91042405

## 5.什么是熔断？什么是服务降级？

**服务熔断**
服务熔断的作用类似于我们家用的保险丝，当某服务出现不可用或响应超时的情况时，为了防止整个系统出现雪崩，暂时停止对该服务的调用。

**服务降级**
服务降级是从整个系统的负荷情况出发和考虑的，对某些负荷会比较高的情况，为了预防某些功能（业务场景）出现负荷过载或者响应慢的情况，在其内部暂时舍弃对一些非核心的接口和数据的请求，而直接返回一个提前准备好的fallback（退路）错误处理信息。这样，虽然提供的是一个有损的服务，但却保证了整个系统的稳定性和可用性。

**熔断VS降级**
相同点：

目标一致 都是从可用性和可靠性出发，为了防止系统崩溃；

用户体验类似 最终都让用户体验到的是某些功能暂时不可用；

不同点：

触发原因不同 服务熔断一般是某个服务（下游服务）故障引起，而服务降级一般是从整体负荷考虑； 

**Hystrix简介**


Hystrix：英 [hɪst'rɪks] 美 [hɪst'rɪks] ，翻译过来是“豪猪”的意思。 在分布式环境中，不可避免地会出现某些依赖的服务发生故障的情况。Hystrix是这样的一个库，它通过添加容许时延和容错逻辑来帮助你控制这些分布式服务之间的交互。Hystrix通过隔离服务之间的访问点，阻止跨服务的级联故障，并提供了退路选项，所有这些都可以提高系统的整体弹性。


## 6.微服务的优缺点是什么？说下你在项目中碰到的坑。

优点：松耦合，聚焦单一业务功能，无关开发语言，团队规模降低。在开发中，不需要了解多有业务，只专注于当前功能，便利集中，功能小而精。微服务一个功能受损，对其他功能影响并不是太大，可以快速定位问题。微服务只专注于当前业务逻辑代码，不会和 html、css 或其他界面进行混合。可以灵活搭配技术，独立性比较舒服。

缺点：随着服务数量增加，管理复杂，部署复杂，服务器需要增多，服务通信和调用压力增大，运维工程师压力增大，人力资源增多，系统依赖增强，数据一致性，性能监控。

## 7.eureka和zookeeper都可以提供服务注册与发现的功能，请说说两个的区别？



1.CAP 理论的不可能三角**

![img](https://pic3.zhimg.com/80/v2-e6b9d06542ea240216b7bcd51512b086_720w.jpg)

- 一致性（Consistency）
- 可用性（Availability）
- 分区容错性（Partition tolerance）

在分布式系统中，是不存在同时满足一致性 Consistency、可用性 Availability和分区容错性 Partition Tolerance三者的。

**一句话总结：一致性、可用性和分区容错在分布式事务中不可兼得。**

在绝大多数的场景，都需要牺牲强一致性来换取系统的高可用性，系统往往只需要保证最终一致性。

这也是是后来发展出的BASE理论的基础。

- zookeeper 是CP原则，强一致性和分区容错性。
- eureka 是AP 原则 可用性和分区容错性。
- zookeeper当主节点故障时，zk会在剩余节点重新选择主节点，耗时过长，虽然最终能够恢复，但是选取主节点期间会导致服务不可用，这是不能容忍的。
- eureka各个节点是平等的，一个节点挂掉，其他节点仍会正常保证服务。

## 8.你所知道微服务的技术栈有哪些？列举一二。

## ![1](https://mmbiz.qpic.cn/mmbiz_png/8KKrHK5ic6XB4UytSaRiaQiaMLQMiapTP0NyboMyMvnYMDbvLiaicQWyO2G4FCrMaZevcBrbCX1awerjdL23egicBQmTg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1) 

## 9.什么是微服务架构？ 

在前面你理解什么是微服务，那么对于微服务架构基本上就已经理解了。

微服务架构 就是 对微服务进行管理整合应用的。微服务架构 依赖于 微服务，是在微服务基础之上的。

例如：上面已经列举了什么是微服务。在医院里，每一个科室都是一个独立的微服务，那么 这个医院 就是 一个大型的微服务架构，就类似 院长 可以 对下面的 科室进行管理。微服务架构主要就是这种功能。





## 10.Eureka工作原理

Eureka : 就是服务注册中心(可以是一个集群),对外暴露自己地址;

提供者 : 启动后向Eureka注册自己信息(地址,提供什么服务)

消费者 : 向Eureka 订阅服务,Eureka会将对应服务的服务列表发送给消费者,并且定期更新

心跳(续约): 提供者定期通过http方式向Eureka刷新自己的状态

 

 **什么是服务注册**

服务提供者在启动时,会向EurekaServer发起一次请求,将自己注册到Eureka注册中心中去

 **什么是服务续约**

在注册服务完成以后,服务提供者会维持一个心跳(每30s定时向EurekaServer 分发起请求)告诉EurekaServer "我还活着"

 **什么是失效剔除**

有时候,我们的服务提供方并不一定是正常下线,可能是内存溢出,网络故障等原因导致服务无法正常工作.EurekaServer会将这些失效的服务剔除服务列表.因此它会开启一个定时任务.每隔60秒会对失效的服务进行一次剔除

**什么是自我保护**

当服务未按时进行心跳续约时,在生产环境下,因为网络原因,此时就把服务从服务列表中剔除并不妥当,因为服务也有可能未宕机.Eureka就会把当前实例的注册信息保护起来,不允剔除.这种方式在生产环境下很有效,保证了大多数服务依然可用

**如果我们不适用Eureka注册中心的情况下,分布式服务必然面临的问题有哪些?**

 服务管理 : 

​      ----如何自动注册和发现服务.

​      ----如何实现服务状态的监管.

​      ----如何实现动态路由,从而实现负载均衡.

服务如何实现负载均衡

服务如何解决容灾问题

服务如何实现统一配置

//简述什么是CAP,并说明Eureka包含CAP中的哪些?

CAP理论:一个分布式系统不可能同时满足C (一致性),A(可用性),P(分区容错性).由于分区容错性P在分布式系统中是必须要保证的,因此我们只能从A和C中进行权衡.

Eureka 遵守 AP

Eureka各个节点都是平等的,几个节点挂掉不会影响正常节点的工作,神域的节点依然可以提供注册和查询服务.

而Eureka的客户端在向某个Eureka 注册或查询是如果发现连接失败,则会自动切换至其他节点

只要有一台Eureka还在,就能保证注册服务可用(保证可用性),只不过查的信息可能不最新的不保证强一致性).



## 11. 对比常用的注册中心

Consul、zookeeper、etcd、eureka、Nacos

| **Feature**              | **Consul**               | **Zookeeper**         | **Etcd**          | **Eureka**                   | **Nacos**                                                    |
| ------------------------ | ------------------------ | --------------------- | ----------------- | ---------------------------- | ------------------------------------------------------------ |
| **服务健康检查**         | 服务状态，内存，硬盘等   | (弱)长连接，keepalive | 连接心跳          | 可配支持                     | 传输层 (PING 或 TCP)和应用层 (如 HTTP、MySQL、用户自定义）的健康检查 |
| **多数据中心**           | 支持                     | —                     | —                 | —                            | 支持                                                         |
| **kv存储服务**           | 支持                     | 支持                  | 支持              | —                            | 支持                                                         |
| **一致性**               | Raft                     | Paxos                 | Raft              | —                            | Raft                                                         |
| **CAP定理**              | CP                       | CP                    | CP                | AP                           | CP: 配置中心AP: 注册中心                                     |
| **使用接口(多语言能力)** | 支持http和dns            | 客户端                | http/grpc         | http（sidecar）              | Nacos 支持基于 DNS 和基于 RPC 的服务发现。服务提供者使用 原生SDK、OpenAPI、或一个独立的Agent |
| **watch支持**            | 全量/支持long polling    | 支持                  | 支持 long polling | 支持 long polling/大部分增量 | 支持 long polling/大部分增量                                 |
| **自身监控**             | metrics                  | —                     | metrics           | metrics                      |                                                              |
| **安全**                 | acl /https               | acl                   | https支持（弱）   | —                            | acl                                                          |
| **Spring Cloud集成**     | 已支持                   | 已支持                | 已支持            | 已支持                       | 已支持                                                       |
| **备注**                 | 可以作为eureka的替代使用 |                       |                   | 2.0不在更新                  | 1. 支持dubbo 2. spring-cloud-alibaba支持                     |

**总结**

springcloud中实现的注册中心

1. 当项目数量少于1000时， 可以考虑 eureka 1.x ； 2.0版本官方不在维护

2. 使用最新的可以考虑使用 Consul， 使用Raft实现一致性的同时， 尽量保证可用， 支持 k8s

3. 使用dubbo， 可以使用 zookeeper、 nacos，  推荐使用 nacos

4. nacos是阿里来源的集配置中心和注册中心与一体的， 新版本 AP 支持性能良好， 天然支持 dubbo

               在 spring-cloud-alibaba 项目中， 很好的实现配置中心和注册中心

              支持 k8s、spring 系列、 docker 和 多注册中心的同步

              2.0 规划 屏蔽 同步 k8s 和 spring 管理的差异、 支持 istio

5. 新项目可以使用 nacos

## 12、服务注册和发现是什么意思？Spring Cloud如何实现？

当我们开始一个项目时，我们通常在属性文件中进行所有的配置。随着越来越多的服务开发和部署，添加和修改这些属性变得更加复杂。有些服务可能会下降，而某些位置可能会发生变化。手动更改属性可能会产生问题。 Nacos服务注册和发现可以在这种情况下提供帮助。由于所有服务都在Eureka服务器上注册并通过调用Nacos服务器完成查找，因此无需处理服务地点的任何更改和处理。

## 什么是Nacos?



英文全称Dynamic Naming and Configuration Service，Na为naming/nameServer即注册中心,co为configuration即注册中心，service是指该注册/配置中心都是以服务为核心。

![1](https://img-blog.csdnimg.cn/20210330130214541.png)



## Nacos注册中心原理

![1](https://img-blog.csdnimg.cn/20210330224113162.png)



	服务提供者、服务消费者、服务发现组件这三者之间的关系大致如下

1、微服务在启动时，将自己的网络地址等信息注册到服务发现组件(nacos server)中，服务发现组件会存储这些信息。

2、各个微服务与服务发现组件使用一定机制通信（例如在一定的时间内发送心跳包）。服务发现组件若发现与某微服务实例通信正常则保持注册状态(up在线状态)、若长时间无法与某微服务实例通信，就会自动注销（即：删除）该实例。

3、服务消费者可从服务发现组件查询服务提供者的网络地址，并使用该地址调用服务提供者的接口。

4、当微服务网络地址发生变更（例如实例增减或者IP端口发生变化等）时，会重新注册到服务发现组件。





## Nacos注册中心使用【Nacos-Client客户端】

（1）pom文件加依赖:alibaba-nacos-discovery

```
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
</dependency>

```

（2）启动类加注解

```
//Nacos服务端【早期版本需要加注解，现在0.0.9版本后已不是必须的】
@EnableDiscoveryClient

```

（3）在对应的微服务的yml配置文件【服务名称和nacos server 地址】

```
spring:
  cloud:
    nacos:
      discovery:
        #指定nacos server的地址，不需要写http
        server-addr: localhost:8848 
```

## Nacos配置中心使用【Nacos-Server服务端】

1）加依赖–alibaba-nacos-config

```
<!--nacos-config nacos管理配置的依赖-->
<dependency>
	<groupId>org.springframework.cloud</groupId>
	<artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>
</dependency>

```

2）加配置，新增bootstrap.yml文件配置，配置属性如下

```
spring:
  cloud:
    nacos:
      config:
        server-addr: 127.0.0.1:8848 #这里的server-addr用作配置管理
        file-extension: yaml
  application:
    name: user-server
  profiles: # profiles区分多环境配置
    active: dev #切换配置文件，如dev、test、pro等环境

```

3）配置中心包含：配置管理、服务管理(微服务管理)、命名空间、集群管理

![1](https://img-blog.csdnimg.cn/20210330230349149.png)



4）通过配置更改动态刷新参数–@RefreshScope注解
普通application参数在配置中心直接配置皆可，如果需要可以动态刷新的配置，需要在相应类上加上@RefreshScope注解,示例如下，当在nacos配置中心更改配置后，方法getId的值也会刷新。

```

@RefreshScope
public class IdEntity {
    @Value("${id}")
    private int id;
    public int getId(){
        return this.id;
}
```



## 8.Feign介绍

Feign是Netfilx开源的声明式HTTP客户端，Feign是一个http请求调用的轻量级框架，可以以Java接口注解的方式调用Http请求。Spring Cloud引入 Feign并且集成了Ribbon实现客户端负载均衡调用。

## 9.Feign调用原理

Feign远程调用，核心就是通过一系列的封装和处理，将以JAVA注解的方式定义的远程调用API接口，最终转换成HTTP的请求形式，然后将HTTP的请求的响应结果，解码成JAVA Bean，放回给调用者。

基于重试器发送HTTP请求：Feign 内置了一个重试器，当HTTP请求出现IO异常时，Feign会有一个最大尝试次数发送请求。
 

## 10.Feign调用原理

（1）加依赖–openfeign

```
 <!--feign依赖、服务通信-->
<dependency>
	<groupId>org.springframework.cloud</groupId>
	<artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>

```

（2）启动类加注解

```
@EnableFeignClients//feign注解
```

（3）请求接口的类加FeignClient注解：

```
@FeignClient(value="article-server")
```

## 11.Feign使用中遇到的相关问题

（1）使用feign客户端调用其他微服务时，发送POST请求时，对象信息没有传递成功。关键在于加上注解：@RequestBody
（2）使用feign客户端调用其他微服务时，报错超时：e=feign.RetryableException: Read timed out executing POST



```
ribbon.ReadTimeout=60000
ribbon.ConnectTimeout=60000

```

## 12.什么是服务熔断？什么是服务降级？

熔断机制是应对雪崩效应的一种微服务链路保护机制。当某个微服务不可用或者响应时间太长时，会进行服务降级，进而熔断该节点微服务的调用，快速返回“错误”的响应信息。当检测到该节点微服务调用响应正常后恢复调用链路。在SpringCloud框架里熔断机制通过Hystrix实现，Hystrix会监控微服务间调用的状况，当失败的调用到一定阈值，缺省是5秒内调用20次，如果失败，就会启动熔断机制。

服务降级，一般是从整体负荷考虑。就是当某个服务熔断之后，服务器将不再被调用，此时客户端可以自己准备一个本地的fallback回调，返回一个缺省值。这样做，虽然水平下降，但好歹可用，比直接挂掉强。

## 13.什么是服务雪崩效应?

雪崩效应是在大型互联网项目中，当某个服务发生宕机时，调用这个服务的其他服务也会发生宕机，大型项目的微服务之间的调用是互通的，这样就会将服务的不可用逐步扩大到各个其他服务中，从而使整个项目的服务宕机崩溃。

## 14.@LoadBalanced注解的作用

开启客户端负载均衡。

## 15. Nginx与Ribbon的区别

Nginx是反向代理同时可以实现负载均衡，nginx拦截客户端请求采用负载均衡策略根据upstream配置进行转发，相当于请求通过nginx服务器进行转发。Ribbon是客户端负载均衡，从注册中心读取目标服务器信息，然后客户端采用轮询策略对服务直接访问，全程在客户端操作。



## 16.Ribbon底层实现原理

Ribbon使用discoveryClient从注册中心读取目标服务信息，对同一接口请求进行计数，使用%取余算法获取目标服务集群索引，返回获取到的目标服务信息。



## 17.Ribbon负载均衡算法

IRule是以下七种负载均衡算法的父接口



https://img-blog.csdnimg.cn/20210330231828514.png



说明：



https://img-blog.csdnimg.cn/20210330231859370.png



RoundRobinRule： 默认轮询的方式
RandomRule： 随机方式
WeightedResponseTimeRule： 根据响应时间来分配权重的方式，响应的越快，分配的值越大。
BestAvailableRule： 选择并发量最小的方式
RetryRule： 在一个配置时间段内当选择server不成功，则一直尝试使用subRule的方式选择一个可用的server
ZoneAvoidanceRule： 根据性能和可用性来选择。
AvailabilityFilteringRule： 过滤掉那些因为一直连接失败的被标记为circuit tripped的后端server，并过滤掉那些高并发的的后端server（active connections 超过配置的阈值）

## 18.分布式事务产生的背景？

在传统的单体项目中，多个不同的业务逻辑使用的都是同一个数据源，使用的都是同一个事务管理器，所以不会存在事务问题。
在分布式或者微服务架构中，每个服务都有自己的数据源，使用不同事务管理器，如果A服务去调用B服务，B服务执行失败了，A服务的事务和B服务的事务都会回滚，这时候是不存在事务问题的，但是如果A服务B服务执行成功之后出现异常，A服务的事务会回滚，但是B服务的事务不会回滚，此时就存在分布式事务问题。
	 

## 19.seata是什么

Seata是阿里巴巴退出的一款用来解决分布式事务问题的框架，他经过天猫双十一的考验，很有可能成为解决分布式事务问题的主流框架

## 20.seata术语

Seata分为三个模块，分别是TM、RM和TC(简写)。
TC(transaction Coordinator)，代表seata服务器，seata是一个spring boot的jar包。
TM(transaction Manager)事务管理器。
RM(Resource Manager) 代表每个数据库。
Seata还用了一个XID，代表了一个分布式事务，相当于dubbo中的Request ID。

## 21.seata流程

TM向TC注册全局事务，并生成全局唯一的XID。
RM向TC注册分支事务，并将其纳入该XID对应的全局事务范围。
RM向TC汇报资源的准备状态。
TC汇总所有事务参与者的执行状态，决定分布式事务是全部提交还是全部回滚。
TC通知所有RM提交/回滚事务。



https://img-blog.csdnimg.cn/20210330233119612.png



## 22.seata流程相亲版

张学霸（TM）跟导师(TC)提议，为卢学霸安排对象，卢学霸生成了一个相亲id。
女神（RM）向tc注册了资料，卢学霸在他的相亲id中接收到了推送。
女神向卢学霸汇报自己的资料。
TC汇总所有女神的资料，让卢学霸决定是否去参加相亲。
TC向卢学霸汇报相亲结果。

## 23.Seata分布式事务框架实现原理？

Seata有三个组成部分：事务协调器TC：协调者、事务管理器TM：发起方、资源管理器RM：参与方
（1）发起方会向协调者申请一个全局事务id，并保存到ThreadLocal中（为什么要保存到ThreadLocal中？弱引用，线程之间不会发生数据冲突）
（2）Seata数据源代理发起方和参与方的数据源，将前置镜像和后置镜像写入到undo_log表中，方便后期回滚使用
（3）发起方获取全局事务id，通过改写Feign客户端请求头传入全局事务id。
（4）参与方从请求头中获取全局事务id保存到ThreadLocal中，并把该分支注册到SeataServer中。
（5）如果没有出现异常，发起方会通知协调者，协调者通知所有分支，通过全局事务id和本地事务id删除undo_log数据，如果出现异常，通过undo_log逆向生成sql语句并执行，然后删除undo_log语句。如果处理业务逻辑代码超时，也会回滚。



## 24.SpringBoot如何整合Seata?

一般情况下，学一个知识不需要去学API，学的主要是思想，API会发生变化，思想几乎是不会变的
第一步：引入依赖
第二步：bin下的file文件和registry文件放入到每个项目中，并修改，分组名称要保持一致
第三步：yml配置seata
第四步：引入DataSourceProxy配置文件
第五步：添加核心主机@GlobalTransaction注解

## 25.常见的分布式事务解决方案？

1、使用MQ
2、使用LCN
3、使用Seata
4、2PC、3PC