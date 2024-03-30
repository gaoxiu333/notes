Docker 包括三个基本概念

- 镜像（`Image`）
- 容器（`Container`）
- 仓库（`Repository`）

理解了这三个概念，就理解了 Docker 的整个生命周期。

## 镜像

Docker 镜像是一个特殊的文件系统，除了提供容器运行时所需要的程序、库、资源、配置文件外，还包含了一些为运行时准备的一些配置参数，比如：匿名卷、环境变量、用户等。镜像不包含任何动态数据，其内容在构建之后也不会被改变。

### 分层储存

镜像构建时，会一层层构建，前一层是后一层的基础，每一层构建完就不会再发生改变，每一层的任何改变只影响当前层，比如：删除前一层文件的操作，实际不是真多删除，而是在当前层标记该文件已删除，最终容器运行时，虽然看不见该文件，实际上该文件会一直跟随镜像。

> 每一层尽量只包含该层需要添加的东西，任何额外的东西应该在该层构建结束前清理掉。


## 容器

镜像和容器的关系，就像是面向对象程序设计中类和实例的关系；镜像是静态的定义，容器是镜像运行时的实体，容器可以被创建、启动、停止、删除、暂停等。

容器的实质是进程，容器可以拥有自己的 root 文件系统，自己的网络配置，自己的进程空间

容器和镜像一样也使用分层存储，容器运行时，以镜像为基础层，在上面创建容器存储层，容器存储层同容器的生存周期一样，容器关闭时，存储层也将消失；

容器存储层应该保持无状态化，所有的文件吸入操作，都应该使用**数据卷**。

> 容器的生命周期？？

## 仓库

镜像构建完成后，如果需要在其他服务器上使用这个镜像，可以将镜像存储在仓库中。

[Docker Hub](https://hub.docker.com/) - Docker 官方的仓库
[Quay.io](https://quay.io/repository/) - Red Hat 仓库
[Google Container Registry](https://cloud.google.com/container-registry/) - Google 提供的仓库，Kubernetes 使用这个仓库

### 国内访问

国内访问官方仓库会比较慢，可以使用镜像服务加速器`Registry Mirror`，有以下几个知名加速器。

- [阿里云加速器](https://cr.console.aliyun.com/#/accelerator)
- [DaoCloud 加速器](https://www.daocloud.io/mirror#accelerator-doc)
- [网易云镜像服务](https://c.163.com/hub#/m/library/)
- [DaoCloud 镜像市场](https://hub.daocloud.io/)
- [阿里云镜像库](https://cr.console.aliyun.com/)

### 私有 Docker Registry

TODO