---
title: Express与Koa中间件机制
jd_id: J20-20250511-0113
created: 2025-05-11 01:13
updated: 2025-05-11 01:13
type: note
status: active
schema: v1
tags: [topic/backend/nodejs, topic/backend/express, topic/backend/koa, topic/architecture]
---

# Express 与 Koa 中间件机制对比

## Express 中间件机制

Express 中间件是一个函数，可以访问请求对象（req）、响应对象（res）以及应用程序请求-响应周期中的下一个中间件函数（next）。

### 中间件的基本形式

```javascript
function middleware(req, res, next) {
  // 处理请求
  // ...
  
  // 调用下一个中间件
  next();
}
```

### 中间件的作用

- 执行任何代码
- 修改请求对象和响应对象
- 结束请求-响应周期
- 调用堆栈中的下一个中间件

### 中间件的类型

1. **应用级中间件**：绑定到 `app` 对象
   ```javascript
   app.use(middleware);
   app.get('/route', middleware);
   ```

2. **路由级中间件**：绑定到 `express.Router()` 实例
   ```javascript
   const router = express.Router();
   router.use(middleware);
   ```

3. **错误处理中间件**：有四个参数 (err, req, res, next)
   ```javascript
   app.use((err, req, res, next) => {
     console.error(err.stack);
     res.status(500).send('服务器错误');
   });
   ```

4. **内置中间件**：如 `express.static`、`express.json`、`express.urlencoded`

5. **第三方中间件**：如 `morgan`、`cors`、`helmet` 等

### Express 中间件执行流程

Express 中间件的执行是线性的，按照定义的顺序依次执行：

```
请求 → 中间件1 → 中间件2 → ... → 路由处理函数 → ... → 中间件n → 响应
```

特点：
- 单向流动
- 一旦发送了响应，通常不会再执行后续中间件
- 必须调用 `next()` 才会执行下一个中间件

## 洋葱模型

洋葱模型是一种中间件执行模式，特点是请求和响应都会经过每个中间件，形成一个"进入-退出"的执行流程。

洋葱模型示意图：
```
        ┌────────────────────────────────────┐
        │           中间件 1                  │
        │     ┌────────────────────────┐     │
        │     │       中间件 2          │     │
        │     │    ┌─────────────┐     │     │
        │     │    │   中间件 3    │     │     │
        │     │    │             │     │     │
请求 ──→│─────│────│─────────────│────→│     │──→ 响应
        │     │    │   业务逻辑   │     │     │
        │     │    └─────┬───────┘     │     │
        │     └──────────┼─────────────┘     │
        └────────────────┼──────────────────┘
                         ↓
                    请求响应完成
```

在这个模型中，中间件的执行分为两个阶段：
1. **递进阶段**：从外到内，按定义顺序执行中间件的前半部分
2. **回归阶段**：从内到外，按反向顺序执行中间件的后半部分

## Express 与 Koa 的对比

### 中间件机制对比

**Express**:
- 使用回调函数形式的中间件
- 线性执行模型
- 通过调用 `next()` 传递控制权
- 请求只经过每个中间件一次（正向流动）

```javascript
// Express 中间件示例
app.use((req, res, next) => {
  console.log('进入中间件 1');
  next();
  console.log('离开中间件 1'); // 如果有异步操作，这里可能无法按预期执行
});
```

**Koa**:
- 使用 async/await 的中间件
- 洋葱模型执行
- 通过 await next() 可以暂停当前中间件，等待内层中间件完成
- 请求和响应都会经过每个中间件（正向+反向流动）

```javascript
// Koa 中间件示例
app.use(async (ctx, next) => {
  console.log('进入中间件 1');
  await next();  // 等待内层中间件执行完成
  console.log('离开中间件 1'); // 一定会执行到
});
```

### 错误处理对比

**Express**:
- 使用特殊的错误处理中间件 `(err, req, res, next) => {}`
- 需要显式调用 `next(err)` 来传递错误
- 错误处理相对复杂，尤其在异步代码中

**Koa**:
- 使用 try/catch 和 Promise 处理错误
- 统一的错误处理机制
- 可以在应用层面设置错误处理

```javascript
// Koa 错误处理
app.use(async (ctx, next) => {
  try {
    await next();
  } catch (err) {
    ctx.status = err.status || 500;
    ctx.body = { error: err.message };
    ctx.app.emit('error', err, ctx);
  }
});
```

### API 设计对比

**Express**:
- `req` 和 `res` 分离
- 丰富的路由系统
- 内置了许多功能
- 大量的内置中间件和第三方中间件

**Koa**:
- 统一的 `ctx` 对象，包含 `ctx.request` 和 `ctx.response`
- 更简洁的 API
- 核心更小，更多功能依赖中间件
- 更现代的语法和模式

### 底层实现对比

**Express**:
- 基于 callbacks
- 使用传统的 Node.js 回调风格
- 向后兼容老版本 Node.js

**Koa**:
- 基于 Promises 和 async/await
- 需要较新版本的 Node.js
- 更适合现代异步编程模型

## 总结

1. **Express**:
   - 更成熟，生态更丰富
   - 学习曲线较低
   - 线性中间件模型
   - 适合快速开发和传统项目

2. **Koa**:
   - 设计更现代
   - 洋葱模型中间件执行
   - 更好的错误处理和异步流控制
   - 核心更小，更灵活

两者本质上的区别主要在于中间件的执行模型和对现代 JavaScript 特性的支持程度。Koa 是由 Express 团队开发的，可以看作是 Express 的精神继承者，但采用了更现代的设计理念。

## 相关链接

- [[MOC-Nodejs|Node.js 知识索引]] - Node.js相关知识
- [[../框架/Express基础|Express基础]] - Express框架基础知识
- [[../框架/Koa入门|Koa入门]] - Koa框架入门指南 