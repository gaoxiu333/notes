## 简介

**Docker** 使用 `Google` 公司推出的 [Go 语言](https://golang.org/) 进行开发实现，**Docker** 在容器的基础上，进行了进一步的封装，从文件系统、网络互联到进程隔离等等，极大的简化了容器的创建和维护。使得 `Docker` 技术比虚拟机技术更为轻便、快捷。
## 安装

Docker 分为 CE 和 EE 两大版本。CE 即社区版（免费，支持周期 7 个月），EE 即企业版，强调安全，付费使用，支持周期 24 个月。 Docker CE 分为 stable、test 和 nightly 三个更新频道。 官方网站上有各种环境下的 安装指南，这里主要介绍 Docker CE 在 Linux 、Windows 10 和 macOS 上的安装。

### 版本的选择

**docker-io、docker-ce、docker-ee的区别**
- docker-io （Docker-engine）是以前早期的版本，版本号是 1.* , 最新版是 1.13。
- docker-ce 是社区版 它包含了CLI客户端、后台进程/服务以及API。用户像以前以同样的方式获取。
- docker-ee 是企业版 增加了额外的支付产品和技术支持
- 这些修改并不影响Docker Compose以及Docker Machine
- docker-ce 和docker-ee 的版本号规则是基于YY.MM来的 使用基于月份的发行版本，17.03 的第一版就指向17.03.0，如果有bug/安全修复需要发布，那么将会指向17.03.1等等。
- Edge 和 Stable
    - Edge版本每月发布，提供一个月支持。
    - Stable版本每季度发布，提供4个月支持。
    - 可以通过Docker EE订阅 延长Stable版本支持以及补丁修复。

> 有人说docker.io 是早期的版本。但是当你安装 docker.io 然后查看版本会发现，docker.io 的版本可能是比 docker-ce 高的。所以 说 docker.io 是旧版本是不对的，事实上：
> - docker-ce 是 docker 官方维护的
> - docker.io 是 Debian 团队维护的
> - docker.io 采用 apt 的方式管理依赖
> - docker-ce 用 go 的方式管理依赖，会自己管理所有的依赖。
> - [参考来源](https://www.baifachuan.com/posts/134f8b8b.html)

Docker Desktop 和 Docker Engine

Mac 或者 Win 通常安装 Docker Desktop，而 Ubuntu 通常安装的 Docker Engine

### Ubuntu 安装

- dokcer.io 安装
```bash
apt install docker.io
```
- docker.ce 安装
```
# 如果有旧版记得卸载
apt-get remove docker \
        docker-engine \
        docker.io \
        containerd \
        runc
        
# apt 安装
apt-get update
# 由于安装源使用HTTPS，首先需要添加 HTTPS 传输的软件包以及 CA 证书
apt-get install \
	    apt-transport-https \
	    ca-certificates \
	    curl \
	    gnupg-agent \
	    software-properties-common
# 添加软件源的 GPG 密钥
# mirrors 为国内源
curl -fsSL https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu/gpg | apt-key add -
# 官方源
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

# 向 source.list 添加 Docker 软件源 以下是国内源
# stable 稳定版，test为测试版，nightly为每日构建版
add-apt-repository \
    "deb [arch=amd64] https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu \
    $(lsb_release -cs) \
    stable"
# 官方源
add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"
# 安装
apt-get update
apt-get install docker-ce

```
- 使用脚本自动安装
```bash
$ curl -fsSL get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh --mirror Aliyun
# $ sudo sh get-docker.sh --mirror AzureChinaCloud
```
### Mac /  Win 安装

[官方安装文档](https://docs.docker.com/get-docker/)


## Docker 使用

### 启动开机自启

```bash
$ sudo systemctl enable docker
$ sudo systemctl start docker
```

### 建立 docker 用户组

```bash
groupadd docker # 建立 docker 组
usermod -aG docker $USER 将当前用户加入 docker 组
usermod -aG docker dockerUser # 将用户名为 dockerUser 的用户添加到 docker 组
gpasswd -d dockerUser docker # 从用户组中移除
```

### 测试 docker 是否正确安装

``` bash
docker run hello-world
```

### [镜像加速](http://docker.baoshu.red/install/mirror.html)
## 常用命令

```bash
# 启动docker
systemctl start docker
# 停止docker
systemctl stop docker
# 查看docker服务状态
systemctl status docker
# 设置docker开机自启动
systemctl enable docker
# 删除未运行的容器
docker rm `docker ps -aq`
# 删除所有镜像
docker rmi $(docker images -q)
```

## 参考

[Docker — 北京图灵学院](http://docker.baoshu.red/)
[Docker 从入门到实践](https://yeasy.gitbook.io/docker_practice/)
[Docker 官方文件](https://docs.docker.com/desktop/install/mac-install/)
[Docker 入门](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)