---
title: Node.js文档
created: 2024-07-22 11:15
updated: 2024-07-22 11:15
type: note
status: draft
schema: v1
tags: [topic/backend/nodejs, topic/dev-environment, action/reference]
---

# Node.js 文档参考

## 基础知识

### 安装与环境配置
- 从[官方网站](https://nodejs.org/)下载并安装Node.js
- 使用nvm管理多个Node.js版本
  ```bash
  # 安装nvm
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
  
  # 安装特定版本的Node.js
  nvm install 18.17.1
  
  # 切换Node.js版本
  nvm use 16.20.2
  ```
- 配置npm源
  ```bash
  # 设置淘宝镜像源
  npm config set registry https://registry.npmmirror.com
  ```

### 核心模块
- **fs**：文件系统操作
- **path**：路径处理
- **http/https**：HTTP服务器和客户端
- **url**：URL解析
- **events**：事件处理
- **stream**：流处理
- **util**：实用工具

## 包管理

### NPM 基本命令
```bash
# 初始化项目
npm init

# 安装依赖
npm install <package-name>

# 安装开发依赖
npm install <package-name> --save-dev

# 全局安装
npm install -g <package-name>

# 更新依赖
npm update

# 卸载依赖
npm uninstall <package-name>
```

### Package.json 关键字段
- **dependencies**：生产环境依赖
- **devDependencies**：开发环境依赖
- **scripts**：自定义脚本命令
- **engines**：指定Node.js版本要求
- **main**：指定入口文件
- **type**：指定模块类型(commonjs/module)

## 异步编程

### 回调函数
```javascript
fs.readFile('file.txt', 'utf8', (err, data) => {
  if (err) {
    console.error('读取文件失败:', err);
    return;
  }
  console.log('文件内容:', data);
});
```

### Promise
```javascript
const fsPromises = require('fs').promises;

fsPromises.readFile('file.txt', 'utf8')
  .then(data => {
    console.log('文件内容:', data);
  })
  .catch(err => {
    console.error('读取文件失败:', err);
  });
```

### Async/Await
```javascript
const fsPromises = require('fs').promises;

async function readFileContent() {
  try {
    const data = await fsPromises.readFile('file.txt', 'utf8');
    console.log('文件内容:', data);
  } catch (err) {
    console.error('读取文件失败:', err);
  }
}

readFileContent();
```

## Web开发

### HTTP服务器
```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello, World!\n');
});

const port = 3000;
server.listen(port, () => {
  console.log(`服务器运行在 http://localhost:${port}/`);
});
```

### Express框架
```javascript
const express = require('express');
const app = express();
const port = 3000;

// 中间件
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// 路由
app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.post('/api/data', (req, res) => {
  const data = req.body;
  // 处理数据...
  res.json({ success: true, data });
});

// 启动服务器
app.listen(port, () => {
  console.log(`应用运行在 http://localhost:${port}`);
});
```

## 数据库集成

### MongoDB (使用Mongoose)
```javascript
const mongoose = require('mongoose');

// 连接数据库
mongoose.connect('mongodb://localhost:27017/myapp', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

// 定义模型
const userSchema = new mongoose.Schema({
  name: String,
  email: { type: String, required: true, unique: true },
  age: Number,
  createdAt: { type: Date, default: Date.now }
});

const User = mongoose.model('User', userSchema);

// 使用模型
async function createUser() {
  try {
    const user = new User({
      name: '张三',
      email: 'zhangsan@example.com',
      age: 30
    });
    
    const result = await user.save();
    console.log('用户已创建:', result);
  } catch (err) {
    console.error('创建用户失败:', err);
  }
}
```

### MySQL (使用mysql2)
```javascript
const mysql = require('mysql2/promise');

async function connectDB() {
  try {
    // 创建连接池
    const pool = mysql.createPool({
      host: 'localhost',
      user: 'root',
      password: 'password',
      database: 'myapp',
      waitForConnections: true,
      connectionLimit: 10,
      queueLimit: 0
    });

    // 执行查询
    const [rows, fields] = await pool.execute('SELECT * FROM users WHERE id = ?', [1]);
    console.log('查询结果:', rows);
  } catch (err) {
    console.error('数据库操作失败:', err);
  }
}
```

## 部署与生产环境

### PM2进程管理
```bash
# 安装PM2
npm install -g pm2

# 启动应用
pm2 start app.js --name "my-app"

# 查看应用状态
pm2 status

# 查看日志
pm2 logs

# 重启应用
pm2 restart "my-app"

# 停止应用
pm2 stop "my-app"

# 自动重启配置
pm2 startup
pm2 save
```

### 环境变量管理
```javascript
// 使用dotenv加载.env文件
require('dotenv').config();

// 访问环境变量
const port = process.env.PORT || 3000;
const dbUrl = process.env.DB_URL;
```

## 性能优化

### 常见性能问题
- 内存泄漏
- 回调地狱
- 阻塞操作
- 未处理的Promise异常

### 性能监控工具
- **node-clinic**：性能分析工具套件
- **node --inspect**：使用Chrome DevTools调试
- **New Relic/DataDog**：生产环境监控

## 参考资源
- [Node.js官方文档](https://nodejs.org/docs/latest/api/)
- [Express文档](https://expressjs.com/)
- [Node.js最佳实践](https://github.com/goldbergyoni/nodebestpractices)
- [Node.js设计模式](https://github.com/nodejs/node-addon-api)

## 待扩展内容
- Node.js微服务架构
- GraphQL API开发
- 身份认证与安全最佳实践
- WebSocket与实时通信
- 单元测试与集成测试 