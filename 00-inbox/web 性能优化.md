---
title: web 性能优化
jd_id: J00-20250511-1138
created: 2025-05-11 11:38
updated: 2025-05-11 11:38
type: note
status: draft
tags: []
---

# web 性能优化

## 概述

简要描述本笔记的主要内容和目的。

## 内容
**html 解析过程**

> 当解析器发现非阻塞资源，例如一张图片，浏览器会请求这些资源并且继续解析。当遇到一个 CSS 文件时，解析也可以继续进行，但是对于 `<script>` 标签（特别是没有 [`async`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/async_function) 或者 `defer` 属性的）会阻塞渲染并停止 HTML 的解析
> 

注意点：

1. css 也会阻塞，不会影响html继续解析，但是会阻塞渲染，HTML 的解析和 CSS 的请求是可以并行进行的，等待css解析完成后渲染页面，**同时也会阻塞 JS（js需要等待查询元素CSS属性）**
2. script 也会阻塞，并且会阻塞 HTML 的解析

**预加载扫描器？**

1. 与HTML解析并行：浏览器开始解析 HTML 文档时，预加载扫描器会同时启动
2. 预加载扫描器会扫描 HTML 文档中 `<link>`, `<script>`, `<img>` 等标签，查找资源文件的引用。
3. 预加载扫描器发现资源后，会立即发起网络请求下载这些资源（同解析HTML 并行）

TODO: https://web.dev/learn/performance/understanding-the-critical-path?authuser=1&hl=zh-cn#what_resources_are_on_the_critical_rendering_path

还没看完，一会儿地铁上看一下。

## 链接与参考

参考来源：web.dev

- [以用户为中心的性能指标](https://web.dev/articles/user-centric-performance-metrics?authuser=1&hl=zh-cn#important-metrics)
- [Core Web Vitals](https://web.dev/articles/vitals?authuser=1&hl=zh-cn)

## CSS

- [CSS 异步加载](https://www.filamentgroup.com/lab/load-css-simpler/)（旧的兼容方案）
- 新属性： [`blocking=render` 属性](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#blocking-attributes)

## 待办事项

- 用来经常回顾和加深理解

 

