
## Mac 打包的镜像在 ubuntu 上无法使用

使用 buildx 指定环境打包

```bash
docker buildx build -t gaoxiu/rsshub:latest --platform=linux/amd64 
```

## 查看 docker 日志

```bash
 docker logs --tail 50 --follow --timestamps rss_rsshub_1
```

## 查看 docker 运行状态

```bash
docker-compose ps -a
```

## docker-compose 执行报错

```bash
# 如果报 HTTPConnection.request() got an unexpected keyword argument 'chunked'
pip list |grep request
pip install requests==2.28.0
```