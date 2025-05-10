---
title: Node调试指南
created: 2024-07-22 13:10
updated: 2024-07-22 13:10
type: note
status: active
schema: v1
tags: [topic/backend/nodejs, topic/dev-environment, topic/debugging]
---

# Node.js 调试指南

## 基本调试方法

### 使用console

最简单的调试方法是使用`console`方法输出信息：

```javascript
// 常规日志
console.log("变量值:", value);

// 警告信息
console.warn("警告信息");

// 错误信息
console.error("错误信息:", error);

// 信息分组
console.group("组名称");
console.log("组内信息1");
console.log("组内信息2");
console.groupEnd();

// 输出对象完整结构
console.dir(obj, { depth: null, colors: true });

// 计时
console.time("操作");
// 执行操作...
console.timeEnd("操作"); // 显示操作耗时

// 输出调用栈
console.trace("调用栈跟踪");

// 条件日志
console.assert(condition, "条件为false时输出此消息");

// 表格输出
console.table([
  { name: "张三", age: 23 },
  { name: "李四", age: 24 }
]);
```

### 使用util.inspect

```javascript
const util = require('util');

// 深层次检查对象
console.log(util.inspect(complexObject, {
  showHidden: true,  // 显示不可枚举属性
  depth: null,       // 无限递归深度
  colors: true       // 彩色输出
}));
```

## Node.js内置调试器

### 使用inspector协议

从Node.js 6.3.0开始，Node.js支持基于Chrome DevTools Protocol的调试：

```bash
# 启动调试
node --inspect server.js

# 在应用启动时自动打开DevTools
node --inspect-brk server.js
```

### 在Chrome中调试

1. 在Chrome浏览器中打开: `chrome://inspect`
2. 点击"Open dedicated DevTools for Node"
3. 或在"Remote Target"下点击"inspect"链接

### 在VS Code中调试

1. 创建`.vscode/launch.json`文件：

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "启动程序",
      "skipFiles": [
        "<node_internals>/**"
      ],
      "program": "${workspaceFolder}/index.js",
      "outFiles": [
        "${workspaceFolder}/**/*.js"
      ]
    }
  ]
}
```

2. 设置断点并按F5启动调试

### 命令行调试

```bash
# 启动内置调试器
node inspect server.js

# 常用命令
# c - 继续执行
# n - 执行下一步
# s - 步入函数
# o - 步出函数
# repl - 在当前上下文中执行代码
```

## 高级调试技巧

### 使用断点

```javascript
// 源码中的调试语句，执行到此行时会自动启动调试器
debugger;

// 条件断点，仅在特定条件下触发
if (someCondition) {
  debugger;
}
```

### 使用性能分析工具

#### 内存快照

```bash
# 启用inspector
node --inspect server.js
```

1. 在Chrome DevTools的Memory标签中
2. 选择"Take heap snapshot"
3. 点击"Take snapshot"
4. 分析内存使用情况，查找内存泄漏

#### CPU分析

```bash
# 启用inspector
node --inspect server.js
```

1. 在Chrome DevTools的Performance标签中
2. 点击"Record"
3. 执行要分析的操作
4. 点击"Stop"
5. 分析CPU使用情况

### 使用第三方调试工具

#### ndb

Google开发的增强型Node.js调试器：

```bash
# 安装
npm i -g ndb

# 启动调试
ndb server.js
```

#### node-clinic

Node.js性能分析工具套件：

```bash
# 安装
npm i -g clinic

# 使用Doctor检测性能问题
clinic doctor -- node server.js

# 使用Bubbleprof分析异步操作
clinic bubbleprof -- node server.js

# 使用Flame生成火焰图
clinic flame -- node server.js
```

## 特定环境调试

### 调试异步代码

```javascript
async function someAsyncFunction() {
  try {
    const result = await someOperation();
    console.log('操作结果:', result);
  } catch (error) {
    console.error('异步操作错误:', error);
    // 详细错误信息
    console.error('错误栈:', error.stack);
    console.error('错误原因:', error.cause);
  }
}
```

### 调试Promise

```javascript
// 未捕获的Promise拒绝处理
process.on('unhandledRejection', (reason, promise) => {
  console.error('未处理的Promise拒绝:', reason);
});

// 使用catch捕获Promise错误
somePromise()
  .then(result => {
    console.log('Promise结果:', result);
  })
  .catch(error => {
    console.error('Promise错误:', error);
  });
```

### 远程调试

```bash
# 允许远程调试连接（危险：仅在安全网络中使用）
node --inspect=0.0.0.0:9229 server.js
```

连接到远程调试器：

1. 通过SSH隧道将远程端口映射到本地
   ```bash
   ssh -L 9221:localhost:9229 user@remote-host
   ```

2. 在本地Chrome中访问: `chrome://inspect`

### 调试Docker容器中的Node.js

Dockerfile配置：

```dockerfile
FROM node:16

WORKDIR /app
COPY . .
RUN npm install

# 暴露调试端口
EXPOSE 9229

# 启用调试
CMD ["node", "--inspect=0.0.0.0:9229", "server.js"]
```

docker-compose.yml配置：

```yaml
version: '3'
services:
  app:
    build: .
    ports:
      - "3000:3000"
      - "9229:9229"
```

## 生产环境调试

### 日志记录最佳实践

使用结构化日志框架，如winston或pino：

```javascript
// 使用winston
const winston = require('winston');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' })
  ]
});

if (process.env.NODE_ENV !== 'production') {
  logger.add(new winston.transports.Console({
    format: winston.format.combine(
      winston.format.colorize(),
      winston.format.simple()
    )
  }));
}

// 使用logger
logger.info('信息级别日志', { user: 'user123', action: 'login' });
logger.error('错误级别日志', { error: err, stack: err.stack });
```

### 错误处理与监控

全局未捕获异常处理：

```javascript
// 处理未捕获的异常
process.on('uncaughtException', (error) => {
  console.error('未捕获的异常:', error);
  // 记录错误并通知监控系统
  recordErrorToMonitoringSystem(error);
  // 优雅关闭应用
  gracefulShutdown();
});

// 处理未处理的Promise拒绝
process.on('unhandledRejection', (reason, promise) => {
  console.error('未处理的Promise拒绝:', reason);
  // 记录错误并通知监控系统
  recordErrorToMonitoringSystem(reason);
});
```

### 使用APM工具

应用性能监控(APM)工具：

- **New Relic**: 全栈监控解决方案
- **Datadog**: 基础设施和应用监控
- **AppDynamics**: 企业级APM解决方案
- **Elastic APM**: 开源APM解决方案

示例（Elastic APM）：

```javascript
// 引入APM代理，必须在应用代码最前面
const apm = require('elastic-apm-node').start({
  serviceName: 'my-service-name',
  secretToken: 'xxxx',
  serverUrl: 'http://localhost:8200'
});

const express = require('express');
const app = express();

app.get('/', function (req, res) {
  // 自定义事务
  const span = apm.startSpan('获取用户数据');
  getUserData()
    .then(data => {
      // 结束事务
      span.end();
      res.send(data);
    })
    .catch(err => {
      // 捕获并报告错误
      apm.captureError(err);
      span.end();
      res.status(500).send('错误');
    });
});
```

## 调试常见问题

### 内存泄漏

识别内存泄漏：

1. 监控内存使用：
   ```javascript
   // 每10秒报告内存使用情况
   setInterval(() => {
     const memoryUsage = process.memoryUsage();
     console.log(`内存使用: ${Math.round(memoryUsage.heapUsed / 1024 / 1024)} MB`);
   }, 10000);
   ```

2. 堆快照分析：
   - 使用Chrome DevTools的Memory标签
   - 比较多个快照，查找增长的对象

常见内存泄漏原因：
- 闭包引用
- 事件监听器未移除
- 缓存无限增长
- 全局变量累积
- 循环引用

### 性能瓶颈

找出性能瓶颈：

```javascript
// 简单的代码段性能测试
console.time('操作');
// 执行操作...
console.timeEnd('操作');

// 更详细的性能分析
const { PerformanceObserver, performance } = require('perf_hooks');

// 创建性能观察器
const obs = new PerformanceObserver((items) => {
  items.getEntries().forEach((entry) => {
    console.log(`${entry.name}: ${entry.duration}ms`);
  });
});
obs.observe({ entryTypes: ['measure'] });

// 标记开始点
performance.mark('A-start');
// 执行操作...
// 标记结束点
performance.mark('A-end');
// 测量两个点之间的性能
performance.measure('A to B', 'A-start', 'A-end');
```

### 调试Express应用

使用debug模块：

```bash
# 启用Express调试日志
DEBUG=express:* node app.js

# 更多细粒度控制
DEBUG=express:router,express:application node app.js
```

使用middleware调试请求：

```javascript
// 添加请求调试中间件
app.use((req, res, next) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
  console.log('请求头:', req.headers);
  console.log('请求体:', req.body);
  
  // 捕获响应
  const oldSend = res.send;
  res.send = function(data) {
    console.log('响应体:', data);
    return oldSend.apply(res, arguments);
  };
  
  next();
});
```

## 延伸阅读

- [Node.js调试指南](https://nodejs.org/en/docs/guides/debugging-getting-started/)
- [Chrome DevTools协议](https://chromedevtools.github.io/devtools-protocol/)
- [Node.js调试的最佳实践](https://blog.risingstack.com/node-js-logging-tutorial/)
- [使用ndb进行Node.js调试](https://github.com/GoogleChromeLabs/ndb)
- [Node.js性能调优指南](https://github.com/davidmarkclements/node-performance-workshop) 