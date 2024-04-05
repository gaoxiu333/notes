# Node 堆栈

- PM2
- ts-node



## Script

- `postinstall` -install后立即执行



## PM2

守护进程

### 安装

```bash
npm i pm2 -g
```

## 运行一个应用

```bash
pm2 start app.js
pm2 restart app
pm2 reload __
pm2 stop __
pm2 delete __

```

## 查看状态

```bash
pm2 ls|status
pm2 logs
```

