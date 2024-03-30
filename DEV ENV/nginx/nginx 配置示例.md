
## 配置 web 服务器

```bash
# 用户和工作进程
user nginx;
worker_processes auto;

# 基本工作目录和日志文件
pid /var/run/nginx.pid;
error_log /var/log/nginx/error.log;
access_log /var/log/nginx/access.log;

# 设置Nginx进程的最大打开文件数
worker_rlimit_nofile 10240;

# 全局事件块
events {
    worker_connections 1024;
    use epoll;
}

# HTTP部分
http {
    # 基本设置
    include mime.types;
    default_type application/octet-stream;
    sendfile on;
    keepalive_timeout 65;

    # Gzip压缩
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

    # 服务器块（虚拟主机配置）
    server {
        listen 80;
        server_name example.com www.example.com;

        # 重定向HTTP到HTTPS
        location / {
            return 301 https://$host$request_uri;
        }
    }

    # HTTPS服务器块
    server {
        listen 443 ssl;
        server_name example.com www.example.com;

        # SSL证书和密钥文件
        ssl_certificate /etc/nginx/ssl/fullchain.pem;
        ssl_certificate_key /etc/nginx/ssl/privkey.pem;
        
        # 安全性设置
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_prefer_server_ciphers off;
        ssl_ciphers 'TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384';
        ssl_session_cache shared:SSL:10m;
        ssl_session_timeout 10m;
        ssl_session_tickets off;
        ssl_stapling on;
        ssl_stapling_verify on;

        # 网站根目录
        root /var/www/html;

        # 访问日志和错误日志
        access_log /var/log/nginx/access_ssl.log;
        error_log /var/log/nginx/error_ssl.log;

        # 静态文件缓存
        location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
            expires 7d;
        }

        # 代理到后端应用
        location /api/ {
            proxy_pass http://backend_server;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }

        # 其他Nginx配置（如反向代理、负载均衡等）根据需要添加
    }

    # 其他服务器块（根据需要添加）
}

```