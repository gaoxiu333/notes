---
title: MOC-React核心原理
jd_id: J30-20250511-0126
created: 2025-05-11 01:26
updated: 2025-05-11 01:26
type: moc
status: active
schema: v1
tags: [topic/frontend/react, topic/moc]
---

# React核心原理索引

本MOC收集和整理React核心原理相关的知识、实现细节和最佳实践，便于系统学习和面试准备。

## 设计理念

React的核心设计理念包括声明式编程、组件化、单向数据流。本MOC主要围绕这些理念下的实现机制展开。

## 核心原理

### 虚拟DOM

- [[核心原理/01-虚拟DOM实现与原理|虚拟DOM实现与原理]] - 详解虚拟DOM的工作原理、Diffing算法和优化策略

### Fiber架构

- [[核心原理/02-Fiber架构与调度机制|Fiber架构与调度机制]] - 深入理解React Fiber架构、工作原理和时间切片调度

### Hooks机制

- [[核心原理/03-Hooks内存模型与闭包|Hooks内存模型与闭包]] - 探索React Hooks的实现原理、闭包陷阱及解决方案  

### 并发模式

- [[核心原理/04-并发模式与服务端组件|并发模式与服务端组件]] - 解析React并发特性与服务端组件的原理与使用

### 性能优化

- [[核心原理/05-React性能优化策略|React性能优化策略]] - React应用性能优化的工具、模式与最佳实践

## 学习资源

- [React官方文档](https://react.dev/) - React最新官方文档
- [React Working Group讨论](https://github.com/reactwg/react-18) - React团队关于新特性的讨论
- [Dan Abramov的博客](https://overreacted.io/) - React核心团队成员深度技术博客

## 相关链接

- [[../React 项目最佳实践|React项目最佳实践]] - React项目开发的实践指南
- [[../React 的学习参考资源|React学习资源]] - 更多React学习资源
- [[../../../code-snippets/frontend/javascript/React代码片段|React代码片段]] - 常用React代码片段 