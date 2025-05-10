---
title: Node.js学习看板
created: 2024-07-22 12:10
updated: 2024-07-22 12:10
type: note
status: active
schema: v1
tags: [topic/backend/nodejs, topic/learning-board]
---

# Node.js 学习看板

## 📚 待学习

- [ ] Node.js核心模块深入理解
- [ ] 事件循环与异步模型详解
- [ ] Express中间件开发
- [ ] MongoDB高级查询技术
- [ ] GraphQL API设计与实现
- [ ] JWT与OAuth2.0认证体系
- [ ] 微服务架构设计原则
- [ ] Docker容器化部署
- [ ] 单元测试与TDD实践
- [ ] 性能优化与监控
- [ ] WebSocket实时通信
- [ ] 消息队列集成方案

## 🔄 进行中

- [ ] Node.js模块系统详解
  - [x] CommonJS规范
  - [x] ES模块支持
  - [ ] 模块加载机制
  - [ ] 自定义模块实现
- [ ] Express框架开发
  - [x] 路由系统
  - [x] 中间件使用
  - [ ] 错误处理
  - [ ] 项目结构组织
- [ ] 数据库集成实践
  - [x] MongoDB基础连接
  - [ ] MongoDB高级查询
  - [ ] 事务处理
  - [ ] 索引优化

## ✅ 已完成

- [x] Node.js环境搭建与配置
- [x] NPM包管理工具使用
- [x] 基本HTTP服务器开发
- [x] JSON数据处理
- [x] 文件系统操作
- [x] 异步编程基础
- [x] Promise与Async/Await使用
- [x] RESTful API基础

## 📝 学习笔记

### Node.js模块系统
- Node.js模块遵循CommonJS规范
- 使用require()函数导入模块
- 使用module.exports或exports导出模块
- ES模块支持通过package.json的type字段开启

### Express框架
- 中间件是Express的核心概念
- 路由定义遵循HTTP方法+路径+处理函数
- 错误处理中间件有四个参数(err, req, res, next)
- 使用app.use()注册全局中间件

### 异步编程模型
- Node.js擅长I/O密集型应用
- 异步回调是基础模式，但易导致回调地狱
- Promise提供了更优雅的异步处理方式
- Async/Await是目前最优雅的异步编程方案

## 🔗 重要资源

### 官方资源
- [Node.js官方文档](https://nodejs.org/docs/)
- [npm官方仓库](https://www.npmjs.com/)
- [Express官方文档](https://expressjs.com/)

### 社区资源
- Node.js中文社区
- GitHub上的优秀Node.js项目
- Stack Overflow常见问题

### 技术博客
- Node.js官方博客
- Medium上的Node.js专题
- 国内技术社区Node.js专栏

## 📊 学习进度

- 基础知识: 90%
- Web开发: 70%
- 数据库操作: 60%
- API开发: 65%
- 安全实践: 40%
- 测试: 30%
- 部署与运维: 25%
- 微服务: 15%
- 高级主题: 10%

## 📅 近期目标

- [ ] 完成一个完整的RESTful API项目
- [ ] 掌握Express/Koa框架的高级特性
- [ ] 实现基于JWT的身份认证系统
- [ ] 学习Docker容器化部署Node.js应用
- [ ] 编写全面的单元测试

## 📌 资源收藏

### 视频教程
- Node.js从零到部署
- Express框架实战
- MongoDB与Mongoose教程

### 书籍推荐
- 《深入浅出Node.js》
- 《Node.js设计模式》
- 《实战Node.js》

### 开源项目
- Express项目模板
- Node.js最佳实践仓库
- RESTful API示例项目

## 🛠️ 工具箱

- nvm: Node版本管理
- nodemon: 开发环境自动重启
- PM2: 生产环境进程管理
- Postman: API测试工具
- MongoDB Compass: 数据库可视化工具
- VSCode插件: ESLint, Prettier, Debug 