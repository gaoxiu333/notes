---
title: Mock数据配置指南
jd_id: J10-20250528-1403
created: 2025-05-28 14:03
updated: 2025-05-28 14:03
type: guide
status: active
tags: [topic/mock, topic/msw, topic/testing, action/config]
---

# 🔄 Mock 数据配置指南

## MSW 介绍

使用 MSW 模拟数据，可以方便地模拟各种网络请求

> [!warning]
>
> **MSW 在与 nextjs 不兼容**
> **注意区分环境，通常有以下几种环境**
>
> - nodejs 环境
> - browser 环境
> - 测试环境

## 初始化配置

```
npx msw init ./public --save
```
