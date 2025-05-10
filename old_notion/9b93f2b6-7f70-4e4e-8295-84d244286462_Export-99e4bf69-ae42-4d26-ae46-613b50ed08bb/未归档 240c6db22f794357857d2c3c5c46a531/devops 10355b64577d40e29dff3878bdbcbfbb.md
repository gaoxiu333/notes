# devops

## 使用 Drone

首先需要在 Mac 下使用

参考：https://huanghantao.github.io/2021/05/23/MacOS搭建Drone环境/index.html

- [算是一个入门到手把手教程](https://fix.moe/post/start-drone-ci)
- [github教程](https://dev.to/jimsheldon/run-your-own-drone-ci-4335)

## 插件推荐

- [**drone-scp**](https://github.com/appleboy/drone-scp)
- [**drone-ssh**](https://github.com/appleboy/drone-ssh)

## 步骤

```python
ngrok http 8080

# 更新github auth
https://github.com/settings/applications/2710201
```

[github 配置](https://github.com/settings/applications/2710201)

## docker

```python
version: '3'

services:
    drone-server:
        image: drone/drone:1
        ports:
            - 5000:80
        volumes:
            - /var/lib/drone:/data # SQLite 数据库存储地址
        restart: always
        environment:
            - DRONE_BITBUCKET_CLIENT_ID={{DRONE_BITBUCKET_CLIENT_ID}} # 刚才获取的 Key
            - DRONE_BITBUCKET_CLIENT_SECRET={{DRONE_BITBUCKET_CLIENT_SECRET}} # 刚才获取的 Secret
            - DRONE_RPC_SECRET={{DRONE_RPC_SECRET}} # 可由 openssl rand -hex 16 命令生成
            - DRONE_SERVER_HOST=drone.fix.moe
            - DRONE_SERVER_PROTO=https
            # - DRONE_LOGS_TRACE=true # 日志追踪
```

## 资料

```python
Ov23ligMV6HwW8c7MT7i
239033759475d8b15ab3ff27cc1aaa255e1afec1
```

test

```python
docker run \
  --volume=/var/lib/drone:/data \
  --env=DRONE_GITHUB_CLIENT_ID=Ov23ligMV6HwW8c7MT7i \
  --env=DRONE_GITHUB_CLIENT_SECRET=f8b4c426355764766a7dae635b69ec5576749df5 \
  --env=DRONE_RPC_SECRET=super-duper-secret \
  --env=DRONE_SERVER_HOST=drone.company.com \
  --env=DRONE_SERVER_PROTO=https \
  --publish=80:80 \
  --publish=443:443 \
  --restart=always \
  --detach=true \
  --name=drone \
  drone/drone:2
```

## 问题

- 链接不上socket
    - [参考](https://weinan.io/2023/09/15/docker-macos.html)

## Gitee

```bash
# id
2bf5eef402702489faa6def7e533f98142c2adf4334fae2b590121ab72d006d5
# secret
47d12d4842ddd080d53e91dcb62539947a866190d9670679e4c06447ee8f917a

# 服务器端口
# drone
8100
# drone-runner
3100
```