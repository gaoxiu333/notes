---
title: Docker快速指南
created: {{date:YYYY-MM-DD HH:mm}}
updated: {{date:YYYY-MM-DD HH:mm}}
type: note
status: active
schema: v1
tags: [topic/devops, topic/docker, topic/container, action/reference]
---

# Docker快速指南

## 核心概念

- **镜像(Image)**：只读模板，包含创建容器的指令
- **容器(Container)**：镜像的运行实例，相互隔离
- **仓库(Repository)**：存储和分发镜像的服务

## 基本命令

### 镜像管理
```bash
# 拉取镜像
docker pull <image>

# 列出镜像
docker images

# 删除镜像
docker rmi <image>

# 构建镜像
docker build -t <name:tag> .
```

### 容器管理
```bash
# 创建并启动容器
docker run <options> <image>

# 常用选项
-d          # 后台运行
-p 8080:80  # 端口映射（主机:容器）
-v /host:/container  # 卷挂载
--name myapp  # 指定容器名称
-e VAR=value  # 环境变量
--network my-net  # 指定网络

# 查看容器
docker ps      # 运行中的容器
docker ps -a   # 所有容器

# 容器操作
docker start/stop/restart <container>  # 启动/停止/重启容器
docker rm <container>                  # 删除容器
docker logs <container>                # 查看日志
docker exec -it <container> <command>  # 在容器中执行命令
```

## Dockerfile

```dockerfile
# 基础镜像
FROM node:18-alpine

# 工作目录
WORKDIR /app

# 复制文件
COPY package*.json ./
COPY . .

# 执行命令
RUN npm install
RUN npm run build

# 暴露端口
EXPOSE 3000

# 启动命令
CMD ["node", "dist/index.js"]
```

## Docker Compose

Docker Compose用于定义和运行多容器Docker应用。

### docker-compose.yml示例

```yaml
version: '3'

services:
  webapp:
    build: ./webapp
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
    depends_on:
      - db
      
  db:
    image: postgres:14
    volumes:
      - db-data:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=example
      - POSTGRES_USER=myapp
      
volumes:
  db-data:
```

### 常用命令

```bash
# 启动服务
docker-compose up -d

# 停止服务
docker-compose down

# 查看服务状态
docker-compose ps

# 查看日志
docker-compose logs
```

## 常见问题解决

1. **容器权限问题**
   - 使用`--user`参数：`docker run --user 1000:1000 image`
   - 在Dockerfile中设置用户：`USER node`

2. **网络连接问题**
   - 创建自定义网络：`docker network create my-net`
   - 将容器加入网络：`docker run --network my-net image`

3. **数据持久化**
   - 使用命名卷：`docker run -v mydata:/app/data image`
   - 绑定挂载：`docker run -v $(pwd)/data:/app/data image`

4. **容器资源限制**
   - 限制内存：`docker run --memory=512m image`
   - 限制CPU：`docker run --cpus=0.5 image`

## 最佳实践

1. **使用多阶段构建减小镜像大小**
2. **优化层缓存提高构建速度**
3. **不在容器中运行应用为root用户**
4. **使用.dockerignore排除不需要的文件**
5. **使用环境变量进行配置**
6. **利用健康检查确保服务可用性**

## 相关链接

- [[Docker-compose使用]] - 更详细的Docker Compose指南
- [[Docker基本使用]] - Docker基础详解
- [[Docker使用问题]] - 常见问题排查与解决 