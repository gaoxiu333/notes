---
title: Linux快速指南
created: {{date:YYYY-MM-DD HH:mm}}
updated: {{date:YYYY-MM-DD HH:mm}}
type: note
status: active
schema: v1
tags: [topic/devops, topic/linux, topic/shell, action/reference]
---

# Linux快速指南

## 基本命令

### 文件与目录操作

```bash
# 导航
pwd                 # 打印当前工作目录
cd <directory>      # 切换目录
cd ~                # 进入用户主目录
cd -                # 返回上一个目录

# 列出文件
ls                  # 列出目录内容
ls -l               # 详细列表
ls -la              # 包含隐藏文件
ls -lh              # 人类可读的文件大小

# 文件操作
touch <file>        # 创建空文件
mkdir <directory>   # 创建目录
mkdir -p a/b/c      # 创建嵌套目录
cp <source> <dest>  # 复制文件
cp -r <src> <dest>  # 递归复制目录
mv <source> <dest>  # 移动/重命名
rm <file>           # 删除文件
rm -r <directory>   # 递归删除目录
rm -rf <directory>  # 强制递归删除

# 查看文件内容
cat <file>          # 显示文件内容
less <file>         # 分页查看文件
head -n 10 <file>   # 查看前10行
tail -n 20 <file>   # 查看后20行
tail -f <file>      # 实时查看文件更新
```

### 文件权限

```bash
# 查看权限
ls -l file.txt      # -rw-r--r-- 表示664权限

# 修改权限
chmod 755 file.txt  # 设置为rwxr-xr-x
chmod +x file.txt   # 添加执行权限
chmod -w file.txt   # 移除写权限
chmod u+x,g-w file.txt # 用户添加执行权限，组移除写权限

# 修改所有者
chown user:group file.txt
```

### 查找与搜索

```bash
# 查找文件
find /path -name "*.txt"        # 按名称搜索
find /path -type f -size +10M   # 查找大于10MB的文件
find /path -mtime -7            # 最近7天修改的文件

# 搜索文件内容
grep "pattern" file.txt         # 在文件中搜索
grep -r "pattern" /path         # 递归搜索目录
grep -i "pattern" file.txt      # 忽略大小写
grep -v "pattern" file.txt      # 查找不匹配的行
```

## 进程管理

```bash
# 查看进程
ps aux                # 显示所有进程
top                   # 实时进程监视器
htop                  # 增强版进程监视器

# 控制进程
kill <pid>            # 发送SIGTERM信号
kill -9 <pid>         # 强制终止进程
killall <process-name> # 终止所有匹配的进程
pkill <pattern>       # 按名称模式终止进程

# 后台任务
command &             # 在后台运行命令
jobs                  # 列出后台作业
fg %1                 # 将作业1移到前台
bg %1                 # 将暂停的作业1继续在后台运行
nohup command &       # 在终端关闭后继续运行
```

## 系统信息

```bash
# 系统资源
free -h               # 显示内存使用情况
df -h                 # 显示磁盘使用情况
du -sh <directory>    # 目录大小汇总
lsblk                 # 列出块设备

# 系统信息
uname -a              # 内核和系统信息
cat /etc/os-release   # 发行版信息
uptime                # 系统运行时间和负载
lscpu                 # CPU信息
```

## 网络操作

```bash
# 网络状态
ifconfig              # 网络接口信息
ip addr show          # 现代替代品
netstat -tuln         # 显示监听端口
ss -tuln              # 现代替代品
lsof -i:22            # 查看使用端口22的进程

# 网络测试
ping host             # ICMP连通性测试
traceroute host       # 路由跟踪
curl URL              # 获取网页内容
wget URL              # 下载文件
```

## 用户管理

```bash
# 用户信息
whoami                # 当前用户名
id                    # 用户ID和组信息
who                   # 当前登录用户

# 用户操作
su - username         # 切换用户
sudo command          # 以root权限执行
useradd username      # 添加用户
passwd username       # 设置用户密码
usermod -aG group user # 将用户添加到组
```

## Shell脚本基础

### 基本结构

```bash
#!/bin/bash

# 变量
NAME="Linux"
echo "Hello, $NAME!"

# 接收参数
echo "第一个参数: $1"
echo "所有参数: $@"
echo "参数个数: $#"

# 条件判断
if [ "$1" = "test" ]; then
    echo "测试模式"
elif [ "$1" = "prod" ]; then
    echo "生产模式"
else
    echo "未知模式"
fi

# 循环
for i in {1..5}; do
    echo "数字: $i"
done

# while循环
count=0
while [ $count -lt 5 ]; do
    echo "Count: $count"
    ((count++))
done

# 函数
function sayHello() {
    echo "Hello, $1!"
}

sayHello "World"

# 退出码
exit 0  # 成功
```

### 常用技巧

```bash
# 重定向
command > file        # 重定向输出到文件(覆盖)
command >> file       # 追加输出到文件
command 2> error.log  # 重定向错误输出
command > out.log 2>&1 # 同时重定向标准输出和错误输出

# 管道
command1 | command2   # 将command1的输出传递给command2

# 命令替换
result=$(command)     # 将命令输出存入变量
echo "结果: $(date)"  # 直接在字符串中使用

# 条件执行
command1 && command2  # 如果command1成功，则执行command2
command1 || command2  # 如果command1失败，则执行command2
```

## 常用工具

1. **文本处理**
   - `sed`: 流编辑器，用于文本替换
   - `awk`: 强大的文本分析工具
   - `cut`: 提取文本列
   - `sort`: 排序文本行
   - `uniq`: 报告或忽略重复行

2. **系统监控**
   - `htop`: 交互式进程查看器
   - `iotop`: 监控磁盘I/O
   - `iftop`: 监控网络带宽
   - `ncdu`: 磁盘使用分析器

3. **远程操作**
   - `ssh`: 安全远程登录
   - `scp`: 安全文件复制
   - `rsync`: 高效文件同步

## 相关链接

- [[Linux笔记]] - 更详细的Linux使用笔记
- [[Linux学习笔记]] - Linux系统学习指南
- [[Shell脚本教程]] - 脚本编写详解 