#  docker概述
>   概 述
>   ![请添加图片描述](https://img-blog.csdnimg.cn/ea2af4ef470847cfbf12a52e84789087.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_14,color_FFFFFF,t_70,g_se,x_16)





docker是go语言开发的

-   docker官方文档：

https://docs.docker.com/get-started/

- docker hub:   

  https://hub.docker.com/

Docker的思想就如它的logo一样：
    docker就是大鲸鱼，而每个镜像container就是对应的集装箱。



> 那么docker的核心思想是什么呢？答案就是——隔离！！
>
> 通过隔离机制，既可以保障每个"集装箱里面的东西"是互不影响的，也可以将服务器的资源压榨到最大程度。



#  docker能干嘛？

docker的 出 现 改 变 了 什 么 ？
![请添加图片描述](https://img-blog.csdnimg.cn/f2e4efb92c974cffab42992333c8ea76.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_20,color_FFFFFF,t_70,g_se,x_16)


#  docker与VM有啥区别？

与 虚 拟 机 的 区 别

 ![请添加图片描述](https://img-blog.csdnimg.cn/c58c5c3116664b088eb53bd190a9b489.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_20,color_FFFFFF,t_70,g_se,x_16)


#  安装docker

安 装 前 的 准 备 阶 段 **—— **卸 载 老 版 本

>   官方安装步骤：https://docs.docker.com/get-started/overview/




>  sudo yum remove docker \
>
>  docker-client \
>
>  docker-client-latest \      
>
>  docker-common \
>
>  docker-latest \
>
>  docker-latest-logrotate \   
>
>  ocker-logrotate \
>
>  docker-engine



 ![请添加图片描述](https://img-blog.csdnimg.cn/3f86dd00c57a4701b1d0ee54c33e56be.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_20,color_FFFFFF,t_70,g_se,x_16)

使 用 仓 库 进 行 安 装

>   sudo yum install -y yum-utils

![请添加图片描述](https://img-blog.csdnimg.cn/803e7ba001354f87ae9b4743e7472ba6.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_20,color_FFFFFF,t_70,g_se,x_16)


>   sudo yum-config-manager \
>
>   --add-repo \
>
>   https://download.docker.com/linux/centos/docker-ce.repo

![请添加图片描述](https://img-blog.csdnimg.cn/26303ef212d74cdebaa0c2e2c9324933.jpg)


安 装 d o c k e r 引 擎

>   sudo yum install docker-ce docker-ce-cli containerd.io

![请添加图片描述](https://img-blog.csdnimg.cn/08ad0475edcd4145bb15d70c332b7a92.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_20,color_FFFFFF,t_70,g_se,x_16)


启动docker

>   sudo systemctl start docker


![请添加图片描述](https://img-blog.csdnimg.cn/29bd2830ff5f4818b2dc1316b6f6ef3b.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_20,color_FFFFFF,t_70,g_se,x_16)


验 证 d o c k e r 引 擎 是 否 安 装 完 毕 sudo docker run hello-world


d o c k e r 启 动 相 关 指 令

```shell
# 查看下载的镜像列表

docker images

# 重新加载docker

sudo systemctl daemon-reload

# 重启docker

sudo systemctl restart docker  # 配置docker国内镜像地址（加快镜像下载速度）

sudo mkdir -p /etc/docker

sudo tee /etc/docker/daemon.json <<-'EOF'

{

"registry-mirrors":

["https://aa25jngun.mirror.aliyuncs.com"]

}

EOF

sudo systemctl daemon-reload sudo systemctl restart docker
```



#  docker基础命令

>   可 以 通 过 官 网 查 看 相 关 命 令

>   官网文档链接：

>   https://docs.docker.com/reference/

![请添加图片描述](https://img-blog.csdnimg.cn/9bceadc16a18465fb4257857bc448f7a.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_20,color_FFFFFF,t_70,g_se,x_16)


常 用 基 础 命 令

![在这里插入图片描述](https://img-blog.csdnimg.cn/63233baf230d4f83bc09892d3dd7cafa.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_20,color_FFFFFF,t_70,g_se,x_16)

#  docker镜像命令

常 用 镜 像 命 令

![在这里插入图片描述](https://img-blog.csdnimg.cn/552e8cd01529428ba5f67445860d6faf.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_20,color_FFFFFF,t_70,g_se,x_16)



#  docker容器命令

常 用 容 器 命 令


![请添加图片描述](https://img-blog.csdnimg.cn/05dc0b43f0bd434abcb646eda2dc1102.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_15,color_FFFFFF,t_70,g_se,x_16)

![请添加图片描述](https://img-blog.csdnimg.cn/9934b18f0274468693e888c533f72d14.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_20,color_FFFFFF,t_70,g_se,x_16)



D o c k e r 命 令 大 全  


#  docker镜像原理

什 么 是 镜 像

>   镜像是一种轻量级、可执行的独立软件包。包含代码、运行时、库、环境变量和配置文件。所有应用，直接打包docker镜像，就可以直接跑起来。

>   获得镜像的方式：

* 1.从远程仓库下载
* 2.通过传输拷贝方式获得

* 3.自己通过DockerFile制作镜像



镜 像 拉 取

![请添加图片描述](https://img-blog.csdnimg.cn/76357340c8c540bd94d780132ea1dfe1.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_20,color_FFFFFF,t_70,g_se,x_16)


>   我们下载的时候，看到的一层层下载，这个就是联合文件系统——UnionFS。
>
>   联合文件系统是一种分层、轻量级、高性能的文件系统。它支持对文件系统的修改作为一次提交来一层层的叠加。
>
>   联合文件系统是Docker镜像的基础。

联 合 文 件 系 统

![请添加图片描述](https://img-blog.csdnimg.cn/e8d9659aca8f4f9b80f7b9618014a47a.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_20,color_FFFFFF,t_70,g_se,x_16)


镜 像 加 载 原 理

![请添加图片描述](https://img-blog.csdnimg.cn/6c7e4bc38b614e05901a09a6fdfe9938.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_20,color_FFFFFF,t_70,g_se,x_16)


提 交 镜 像

>   \# 提交容器，成为一个新的副本。
>
>   docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]] 

![请添加图片描述](https://img-blog.csdnimg.cn/7d518cbb6f5d445f9085fc84b18f9653.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_20,color_FFFFFF,t_70,g_se,x_16)

#  容器数据卷

什 么 是 容 器 数 据 卷

>   如前面介绍的，docker是将应用和环境进行了打包。那么如果删掉容器的话，数据也会同时被删除掉。那么，如果我们有数据持久化的需求，或者容器之间数据共享的需求，那么就用到了容器数据卷。

![请添加图片描述](https://img-blog.csdnimg.cn/006036252c814059a0a15a2f9e6d47a9.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_20,color_FFFFFF,t_70,g_se,x_16)


挂 载 操 作

>   \# 执行挂载（把本机路径/home/muse/test，挂在到centos容器的/bin/bash目录下）
>
>   docker run -it -v /home/muse/test:/home centos /bin/bash




>   \# 查看挂载内容（上面run的容器id就是da6268d8ac0a）
>
>   docker inspect da6268d8ac0a

![请添加图片描述](https://img-blog.csdnimg.cn/fb0d11af3a1648f0b23cb667265577ce.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_20,color_FFFFFF,t_70,g_se,x_16)

具 名 挂 载 与 匿 名 挂 载

- 匿名挂载

  通过-v 指定容器内路径

  docker run -d -P --name nginx1 -v :/etc/nginx nginx
 ![请添加图片描述](https://img-blog.csdnimg.cn/254e3c1063c74b62b5359578546f7c1e.jpg)


- 具名挂载（常用方式）

  通过-v 卷名:容器内路径，指定具名挂载

  docker run -d -P --name nginx2 -v nginx2:/etc/nginx nginx
![请添加图片描述](https://img-blog.csdnimg.cn/60a21b88641d4777aa8f59eaff6936c2.jpg)


挂 载 常 用 相 关 命 令

- 查看挂载列表

  docker volume ls
![请添加图片描述](https://img-blog.csdnimg.cn/dd18eda6dd4340919ce7155642356b05.jpg)



- 查看挂载信息

  docker volume inspect [VOLUME]

![请添加图片描述](https://img-blog.csdnimg.cn/fa62edff2a974d1fb18d1cbeb0f7c582.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_20,color_FFFFFF,t_70,g_se,x_16)


数 据 卷 容 器

![请添加图片描述](https://img-blog.csdnimg.cn/a1b0ee945d5c4345a2b990d7c5163477.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5L2z5L2z5LmQMjUwMw==,size_20,color_FFFFFF,t_70,g_se,x_16)


>   我们发现，删除了museCentOS03之后，museCentOS02里的muse01目录下依然有a.txt文件，这就表明了， museCentOS01\~museCentOS03这三个容器中a.txt文件是互相同步复制备份的。而并不是同享了某个目录，大家都去查看一个备份。

#  DockerFile初探

编 写 一 个 简 单 的 D o c k e r F i le

- 在/home/muse下构造dockerfiles文件夹和dockerfile01文件

- 编写DockerFile（命令大写）

  FROM centos

  VOLUME ["muse01","muse02"]

  CMD echo "------finish------"   CMD /bin/bash

- 构造镜像

  docker build -f /home/muse/dockerfiles/dockerfile01 -t muse/centos:1.0 .

- 启动自己构建的镜像（通过docker images查询出IMAGE ID为eb78333356a6 ）
  docker run -it eb78333356a6 /bin/bash