# Docker

目前只是用Docker完成CI/CD的工作（DevOps）

## 介绍

Docker 包括三个基本概念

- 镜像
- 容器
- 仓库

## 常用命令

``` bash
# 查看空间占用情况 镜像、容器、数据卷
docker system df
# 查看镜像
docker image ls
```

## 使用镜像

```bash
docker pull [选项] [Docker Registr 地址[:端口号]/]仓库名[:标签]
```

示例

```bash
docker pull ubuntu:18.04
docker run -it --rm ubuntu:18.04 bash		# 运行
docker image ls # 列出镜像
docker image rm:[tag]｜[短id]｜[完整id] # 标签：多个标签为移除，单个为删除
```

## 参考

[Docker 从入门到实践](https://yeasy.gitbook.io/docker_practice/)

[Docker 官方文件](https://docs.docker.com/desktop/install/mac-install/)

[Docker 入门](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)