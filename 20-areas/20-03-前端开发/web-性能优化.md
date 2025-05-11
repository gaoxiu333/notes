---
title: Web性能优化
jd_id: J20.03.0001
created: 2025-05-11 11:38
updated: 2025-05-11 13:01
type: note
status: active
tags: [topic/frontend/performance, topic/web]
---

# Web性能优化

## 概述

本笔记汇总了Web性能优化的关键知识点和最佳实践，包括关键渲染路径、资源加载优化、性能指标等内容。

## 浏览器渲染流程

**HTML 解析过程**

> 当解析器发现非阻塞资源，例如一张图片，浏览器会请求这些资源并且继续解析。当遇到一个 CSS 文件时，解析也可以继续进行，但是对于 `<script>` 标签（特别是没有 [`async`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/async_function) 或者 `defer` 属性的）会阻塞渲染并停止 HTML 的解析
> 

注意点：

1. CSS 也会阻塞，不会影响HTML继续解析，但是会阻塞渲染，HTML 的解析和 CSS 的请求是可以并行进行的，等待CSS解析完成后渲染页面，**同时也会阻塞 JS（JS需要等待查询元素CSS属性）**
2. Script 也会阻塞，并且会阻塞 HTML 的解析

**预加载扫描器**

1. 与HTML解析并行：浏览器开始解析 HTML 文档时，预加载扫描器会同时启动
2. 预加载扫描器会扫描 HTML 文档中 `<link>`, `<script>`, `<img>` 等标签，查找资源文件的引用
3. 预加载扫描器发现资源后，会立即发起网络请求下载这些资源（同解析HTML 并行）

更多内容参见：https://web.dev/learn/performance/understanding-the-critical-path?authuser=1&hl=zh-cn#what_resources_are_on_the_critical_rendering_path

## 性能指标

### 核心指标

- **LCP (Largest Contentful Paint)**: 最大内容绘制，测量加载性能
- **FID (First Input Delay)**: 首次输入延迟，测量交互性
- **CLS (Cumulative Layout Shift)**: 累积布局偏移，测量视觉稳定性

### 其他重要指标

- **TTFB (Time to First Byte)**: 首字节时间
- **FCP (First Contentful Paint)**: 首次内容绘制
- **TTI (Time to Interactive)**: 可交互时间

## 资源加载优化

### CSS优化

- [CSS 异步加载](https://www.filamentgroup.com/lab/load-css-simpler/)（旧的兼容方案）
- 新属性：[`blocking=render` 属性](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#blocking-attributes)
- 关键CSS内联
- CSS分割与懒加载

### JavaScript优化

- 使用 `async` 和 `defer` 属性
- 代码分割
- Tree Shaking
- 路由级懒加载

### 图片优化

- 使用现代图片格式（WebP, AVIF）
- 响应式图片（srcset, sizes）
- 懒加载

## 链接与参考

参考来源：web.dev

- [以用户为中心的性能指标](https://web.dev/articles/user-centric-performance-metrics?authuser=1&hl=zh-cn#important-metrics)
- [Core Web Vitals](https://web.dev/articles/vitals?authuser=1&hl=zh-cn)

## 待办事项

- [ ] 完善关键渲染路径内容
- [ ] 添加实际优化案例
- [ ] 整理性能测量工具列表 