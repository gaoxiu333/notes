---
title: Drone简明指南
created: {{date:YYYY-MM-DD HH:mm}}
updated: {{date:YYYY-MM-DD HH:mm}}
type: note
status: active
schema: v1
tags: [topic/devops, topic/ci-cd, topic/drone, topic/automation, action/reference]
---

# Drone简明指南

## 基本概念

Drone是一个基于容器的持续集成/持续部署(CI/CD)平台，使用YAML配置文件定义和自动化软件开发流程。

主要特点：
- **容器原生**: 每个构建步骤在独立容器中运行
- **声明式配置**: 通过YAML文件定义整个流程
- **插件生态系统**: 丰富的插件支持各种集成
- **可扩展性**: 支持分布式执行，可水平扩展
- **多平台支持**: 可与GitHub, GitLab, Bitbucket等集成

## 安装配置

### 服务器安装

#### Docker部署 (推荐)

```bash
# 创建共享密钥
openssl rand -hex 16

# 启动Drone服务器
docker run \
  --volume=/var/lib/drone:/data \
  --env=DRONE_GITHUB_CLIENT_ID=your-github-client-id \
  --env=DRONE_GITHUB_CLIENT_SECRET=your-github-client-secret \
  --env=DRONE_RPC_SECRET=your-shared-secret \
  --env=DRONE_SERVER_HOST=drone.example.com \
  --env=DRONE_SERVER_PROTO=https \
  --publish=80:80 \
  --publish=443:443 \
  --restart=always \
  --name=drone \
  drone/drone:latest
```

#### Runner安装

```bash
# 启动Drone Runner
docker run \
  --volume=/var/run/docker.sock:/var/run/docker.sock \
  --env=DRONE_RPC_HOST=drone.example.com \
  --env=DRONE_RPC_PROTO=https \
  --env=DRONE_RPC_SECRET=your-shared-secret \
  --env=DRONE_RUNNER_CAPACITY=2 \
  --env=DRONE_RUNNER_NAME=my-runner \
  --restart=always \
  --name=drone-runner \
  drone/drone-runner-docker:latest
```

### 配置OAuth

Drone需要配置OAuth以便与代码托管服务进行身份验证：

1. 在GitHub/GitLab/Bitbucket中创建OAuth应用
2. 授权回调URL设置为 `https://drone.example.com/login`
3. 获取Client ID和Client Secret
4. 将这些凭据配置到Drone服务器环境变量中

## 配置文件

Drone使用`.drone.yml`文件定义CI/CD流程，该文件位于代码库的根目录。

### 基本结构

```yaml
kind: pipeline
type: docker
name: default

steps:
  - name: build
    image: node:14
    commands:
      - npm install
      - npm run build

  - name: test
    image: node:14
    commands:
      - npm run test

  - name: deploy
    image: plugins/s3
    settings:
      bucket: my-bucket
      access_key:
        from_secret: aws_access_key_id
      secret_key:
        from_secret: aws_secret_access_key
      source: dist/**/*
      target: /
```

### 核心概念

#### 流水线(Pipeline)

定义一组步骤的执行环境：

```yaml
kind: pipeline
type: docker  # 或 kubernetes, exec等
name: build-test
```

#### 步骤(Steps)

定义流水线中的各个任务：

```yaml
steps:
  - name: greeting
    image: alpine
    commands:
      - echo hello world
```

#### 触发器(Triggers)

控制何时执行流水线：

```yaml
trigger:
  branch:
    - main
    - develop
  event:
    - push
    - pull_request
```

#### 服务(Services)

为流水线提供辅助服务：

```yaml
services:
  - name: database
    image: postgres:12
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
```

#### 秘密(Secrets)

安全存储敏感信息：

```yaml
steps:
  - name: publish
    image: plugins/docker
    settings:
      username:
        from_secret: docker_username
      password:
        from_secret: docker_password
```

## 常见工作流

### 基本CI工作流

```yaml
kind: pipeline
type: docker
name: build-test

steps:
  - name: install
    image: node:14
    commands:
      - npm install

  - name: lint
    image: node:14
    commands:
      - npm run lint
    depends_on:
      - install

  - name: test
    image: node:14
    commands:
      - npm run test
    depends_on:
      - install
```

### 多阶段构建和部署

```yaml
kind: pipeline
type: docker
name: complete-workflow

steps:
  # 构建阶段
  - name: build
    image: node:14
    commands:
      - npm install
      - npm run build

  # 测试阶段
  - name: test
    image: node:14
    commands:
      - npm run test
    depends_on:
      - build

  # 部署阶段
  - name: deploy
    image: plugins/s3
    settings:
      bucket: my-bucket
      access_key:
        from_secret: aws_access_key_id
      secret_key:
        from_secret: aws_secret_access_key
      source: dist/**/*
      target: /
    depends_on:
      - test
    when:
      branch:
        - main
```

### 并行执行

```yaml
kind: pipeline
type: docker
name: parallel-workflow

steps:
  - name: install
    image: node:14
    commands:
      - npm install

  - name: test-unit
    image: node:14
    commands:
      - npm run test:unit
    depends_on:
      - install

  - name: test-integration
    image: node:14
    commands:
      - npm run test:integration
    depends_on:
      - install

  - name: deploy
    image: plugins/s3
    settings:
      bucket: my-bucket
    depends_on:
      - test-unit
      - test-integration
```

## 高级功能

### 条件执行

```yaml
steps:
  - name: deploy-production
    image: plugins/s3
    settings:
      bucket: production
    when:
      branch:
        - main
      event:
        - tag
```

### 矩阵构建

```yaml
steps:
  - name: test
    image: node:${NODE_VERSION}
    commands:
      - npm install
      - npm test

matrix:
  include:
    - NODE_VERSION: 12
    - NODE_VERSION: 14
    - NODE_VERSION: 16
```

### 管道间依赖

```yaml
# 第一个管道
kind: pipeline
type: docker
name: build

steps:
  - name: build
    image: golang
    commands:
      - go build

---
# 第二个管道
kind: pipeline
type: docker
name: test

steps:
  - name: test
    image: golang
    commands:
      - go test

depends_on:
  - build
```

## 常用插件

### Docker构建与发布

```yaml
steps:
  - name: docker
    image: plugins/docker
    settings:
      repo: octocat/hello-world
      tags: latest
      username:
        from_secret: docker_username
      password:
        from_secret: docker_password
```

### Kubernetes部署

```yaml
steps:
  - name: deploy
    image: plugins/kubernetes
    settings:
      kubernetes_server:
        from_secret: kubernetes_server
      kubernetes_token:
        from_secret: kubernetes_token
      kubernetes_cert:
        from_secret: kubernetes_cert
      namespace: default
      deployment: app
      container: app
      repo: octocat/hello-world
      tag: latest
```

### 通知

```yaml
steps:
  - name: slack
    image: plugins/slack
    settings:
      webhook:
        from_secret: slack_webhook
      channel: builds
      template: >
        Build {{build.number}} finished with status {{build.status}}
```

## 最佳实践

1. **使用官方插件**: 优先使用官方维护的插件，确保安全性和稳定性

2. **管理秘密**: 敏感信息应存储为秘密而非明文

3. **容器版本固定**: 使用具体版本标签而非`latest`标签

4. **优化构建速度**:
   - 使用缓存机制减少重复工作
   - 并行执行无依赖的步骤
   - 避免不必要的依赖安装

5. **清晰组织配置文件**:
   - 使用有意义的步骤名称
   - 为复杂流水线添加注释
   - 长配置考虑分割为多个流水线

6. **定义明确的依赖关系**: 使用`depends_on`确保步骤按正确顺序执行

7. **有条件执行步骤**: 使用`when`条件避免不必要的任务执行

## 故障排除

### 常见问题

1. **构建卡在克隆仓库阶段**
   - 检查仓库权限设置
   - 验证Drone服务器网络连接

2. **插件报错**
   - 检查插件文档确认配置参数
   - 验证秘密是否正确设置

3. **步骤运行超时**
   - 为长时间运行的步骤增加超时设置
   - 考虑优化构建流程

4. **构建失败但无明确错误**
   - 增加调试命令查看环境状态
   - 检查是否有资源限制问题

### 调试技巧

```yaml
steps:
  - name: debug
    image: alpine
    commands:
      - env
      - ls -la
      - cat /etc/os-release
```

## 相关链接

- [[CI/CD基本概念]] - 持续集成/持续部署基本原理
- [[Docker快速指南]] - Docker基础知识(Drone基于Docker)
- [[Git工作流]] - 与CI/CD集成的Git工作流
- [[自动化测试]] - 测试自动化最佳实践 