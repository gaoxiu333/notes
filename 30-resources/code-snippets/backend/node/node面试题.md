---
title: node面试题
created: 2025-02-16 14:54
updated: 2025-02-17 02:05
type: resource
status: active
schema: v1
tags: [source/notion, topic/backend/nodejs, lang/javascript]
---

# Node面试题

### 说一下 express 中间件、洋葱模型，以及和koa有什么不同

- 参考：https://blog.xav1er.com/p/middleware-of-koa-and-express/
- **koa** 严格按照洋葱模型
- **express** 也算是洋葱模型，但是在进入阶段结束后数据就发给了客户端，回溯阶段并不能对数据进行再次处理。

洋葱模型

1. 每个中间件分两个阶段

```bash
   ┌──────────────────────┐
   │  Middleware 1 (进入)  │
   ├──────────────────────┤
   │  Middleware 2 (进入)  │
   ├──────────────────────┤
   │       Route Handler  │
   ├──────────────────────┤
   │  Middleware 2 (退出)  │
   ├──────────────────────┤
   │  Middleware 1 (退出)  │
   └──────────────────────┘
``` 