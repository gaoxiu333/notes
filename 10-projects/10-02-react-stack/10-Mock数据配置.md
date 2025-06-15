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
> **注意区分环境，每种环境可能基于使用方式，配置略有不同，通常有以下几种环境：**
>
> - nodejs 环境
> - browser 环境
> - 测试环境

## 初始化配置

```
npx msw init ./public --save
```

## 问题

**1. 本地开发环境使用 Cookie 时，mock 接口出现 500 的问题**

注意: MSW 不会自己清楚已有的 Cookie，需要手动清除

参考: [issues/2401](https://github.com/mswjs/msw/issues/2401)

**2. 使用 Nestjs 时，没办法跑在浏览器环境**

MSW 目前不支持 Nestjs 的浏览器环境，需要另外使用 Nodejs 环境，稍微麻烦些，目前官方没有好的办法，官方的态度是等待 Nestjs 支持。