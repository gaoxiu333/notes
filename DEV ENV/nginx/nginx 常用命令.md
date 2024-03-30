
## 查看 nginx

```
# 仅查看版本
nginx -v

# 查看nginx配置选项
nginx -V
```

## 启动

```bash
# 通过默认配置重启
nginx

# 指定配置文件
nginx -c [path]
```
## 停止

```bash
# 立即停止
nginx -s stop

# 平滑停止
nginx -s quit

# 或者
kill TERM | INT | QUIT PID
```

## 重启

```bash
# 平滑重启
nginx -s reload
# 或者
kill HUP PID
```

## 平滑升级

```bash
nginx -p newInstallPath
```