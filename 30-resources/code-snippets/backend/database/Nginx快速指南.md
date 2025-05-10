---
title: Nginx快速指南
created: {{date:YYYY-MM-DD HH:mm}}
updated: {{date:YYYY-MM-DD HH:mm}}
type: note
status: active
schema: v1
tags: [topic/backend, topic/devops, topic/webserver, topic/nginx, action/reference]
---

# Nginx快速指南

## 基本概念

Nginx(发音为"engine x")是一个高性能的HTTP和反向代理服务器，也是一个IMAP/POP3/SMTP代理服务器。其特点是占用内存少，并发能力强。

主要用途：
- Web服务器
- 反向代理服务器
- 负载均衡器
- HTTP缓存

## 安装与基本命令

### 安装

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nginx

# CentOS/RHEL
sudo yum install epel-release
sudo yum install nginx

# macOS
brew install nginx
```

### 基本命令

```bash
# 启动Nginx
sudo systemctl start nginx    # 系统服务方式
sudo nginx                    # 直接启动

# 停止Nginx
sudo systemctl stop nginx     # 系统服务方式
sudo nginx -s stop            # 快速停止
sudo nginx -s quit            # 优雅停止(等待请求完成)

# 重新加载配置
sudo systemctl reload nginx   # 系统服务方式
sudo nginx -s reload          # 直接重载

# 测试配置文件语法
sudo nginx -t

# 查看Nginx版本
nginx -v
```

## 配置文件结构

Nginx配置文件的主要结构：

```
main        # 全局配置
├── events  # 连接处理
├── http    # HTTP服务器配置
│   ├── server        # 虚拟主机配置
│   │   ├── location  # 路径配置
│   │   └── location
│   └── server
└── stream  # TCP/UDP服务器配置
```

配置文件位置：
- `/etc/nginx/nginx.conf` (主配置文件)
- `/etc/nginx/conf.d/*.conf` (包含的配置文件)
- `/etc/nginx/sites-available/` 和 `/etc/nginx/sites-enabled/` (虚拟主机配置)

## 基本配置示例

### 静态内容服务器

```nginx
server {
    listen 80;
    server_name example.com www.example.com;
    
    root /var/www/html;
    index index.html index.htm;
    
    location / {
        try_files $uri $uri/ =404;
    }
}
```

### 反向代理

```nginx
server {
    listen 80;
    server_name example.com;
    
    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

### 负载均衡

```nginx
upstream backend {
    server backend1.example.com;
    server backend2.example.com;
    server backend3.example.com;
}

server {
    listen 80;
    server_name example.com;
    
    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### HTTPS配置

```nginx
server {
    listen 443 ssl;
    server_name example.com;
    
    ssl_certificate /etc/nginx/ssl/example.com.crt;
    ssl_certificate_key /etc/nginx/ssl/example.com.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    
    location / {
        root /var/www/html;
        index index.html;
    }
}

# HTTP重定向到HTTPS
server {
    listen 80;
    server_name example.com;
    return 301 https://$host$request_uri;
}
```

## 常用配置指令

### HTTP服务器配置

```nginx
http {
    # 基本设置
    include mime.types;                    # 包含MIME类型配置
    default_type application/octet-stream; # 默认MIME类型
    sendfile on;                           # 启用sendfile
    keepalive_timeout 65;                  # 保持连接超时
    gzip on;                               # 启用gzip压缩
    
    # 缓冲区设置
    client_body_buffer_size 10K;
    client_header_buffer_size 1k;
    client_max_body_size 8m;               # 最大上传文件大小
    
    # 超时设置
    client_body_timeout 12;
    client_header_timeout 12;
    send_timeout 10;
}
```

### 服务器块配置

```nginx
server {
    listen 80;                     # 监听端口
    server_name example.com;       # 服务器名
    root /var/www/html;            # 根目录
    
    # 日志配置
    access_log /var/log/nginx/example.access.log;
    error_log /var/log/nginx/example.error.log;
    
    # 默认页
    index index.html index.htm;
}
```

### Location块配置

```nginx
location / {
    # 基本匹配
    root /var/www/html;     # 文档根目录
    index index.html;       # 默认索引文件
    try_files $uri $uri/ /index.html; # 查找文件顺序
}

location ~* \.(jpg|jpeg|png|gif)$ {
    # 正则匹配示例（所有图片文件）
    expires 30d;            # 设置缓存过期
}

location /api/ {
    # 前缀匹配
    proxy_pass http://backend;
    proxy_set_header Host $host;
}

# 精确匹配
location = /favicon.ico {
    log_not_found off;
    access_log off;
}
```

## 安全配置

### 基础安全设置

```nginx
server {
    # 隐藏版本信息
    server_tokens off;
    
    # 添加安全头
    add_header X-Content-Type-Options nosniff;
    add_header X-Frame-Options SAMEORIGIN;
    add_header X-XSS-Protection "1; mode=block";
    
    # HTTPS安全头
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
}
```

### 限制请求

```nginx
# 在http块中
limit_req_zone $binary_remote_addr zone=one:10m rate=1r/s;

server {
    # 在server或location块中应用
    location /login {
        limit_req zone=one burst=5;
    }
}
```

### 访问限制

```nginx
# 基于IP的访问控制
location /admin {
    allow 192.168.1.0/24;
    deny all;
}

# 基本认证
location /private {
    auth_basic "Restricted Area";
    auth_basic_user_file /etc/nginx/.htpasswd;
}
```

## 性能优化

### 缓存配置

```nginx
# 设置缓存区
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m inactive=60m;

server {
    # 启用缓存
    location / {
        proxy_cache my_cache;
        proxy_cache_valid 200 302 10m;
        proxy_cache_valid 404 1m;
        proxy_pass http://backend;
    }
}
```

### 静态文件优化

```nginx
location ~* \.(css|js|jpg|jpeg|png|gif)$ {
    expires 30d;
    add_header Cache-Control "public, no-transform";
    access_log off;
    log_not_found off;
}
```

### worker进程优化

```nginx
# 在main块中
worker_processes auto;  # 自动设置为CPU核心数
worker_rlimit_nofile 65535;  # 每个worker的最大文件描述符

events {
    worker_connections 4096;  # 每个worker的最大连接数
    multi_accept on;  # 同时接受多个连接
    use epoll;  # Linux上使用epoll事件模型
}
```

## 常见问题排查

1. **配置文件错误**
   - 使用`nginx -t`测试配置文件语法
   - 检查错误日志`/var/log/nginx/error.log`

2. **权限问题**
   - 检查网站根目录和文件的所有权与权限
   - 为Nginx用户(通常是www-data或nginx)提供适当访问权限

3. **代理连接问题**
   - 确保后端服务在运行并且可访问
   - 检查proxy_pass参数是否正确
   - 查看错误日志中的连接拒绝消息

4. **性能问题**
   - 启用访问日志的请求时间记录
   - 使用`ngxtop`或其他工具分析访问日志
   - 检查服务器资源使用情况(CPU, 内存, I/O)

## 相关链接

- [[Nginx参考]] - 更详细的Nginx使用文档
- [[反向代理配置]] - 高级代理设置和技巧
- [[Web服务器对比]] - Nginx与其他服务器的对比 