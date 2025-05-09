---
title: "Node.js环境设置"
date: 2024-07-18
tags: 
  - type/guide
  - subject/backend
  - topic/nodejs
  - tool/nvm
status: active
---

# Node.js环境设置

> **注意**: 此文件内容与 [[node-version-management|Node.js版本管理]] 有部分重叠，未来可能合并。

## fnm

```bash
# 安装
brew install fnm

fnm install --lts # 安装最新LTS版本

# 设置默认版本
fnm default 18.17.1

# 查看版本
fnm ls
```

## pnpm

```bash
corepack enable
corepack prepare pnpm@latest --activate # 存疑，不知道是否需要
corepack use pnpm@latest
``` 