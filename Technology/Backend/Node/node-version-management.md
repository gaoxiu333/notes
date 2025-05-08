---
title: "Node.js版本管理与开发环境"
date: 2024-07-15
updated: 2024-07-15
tags: 
  - type/reference
  - subject/backend/node
status: active
---

# Node.js版本管理与开发环境

本文档介绍Node.js开发环境的搭建和版本管理工具的使用。

## FNM (Fast Node Manager)

FNM是一个快速的Node.js版本管理器，使用Rust编写，性能优异。

### 安装与基本使用

```bash
# 安装FNM
brew install fnm

# 安装最新LTS版本的Node.js
fnm install --lts

# 设置默认Node.js版本
fnm default 18.17.1

# 查看已安装的Node.js版本
fnm ls
```

### 项目特定版本

```bash
# 为当前项目使用特定版本
fnm use 16
```

## PNPM包管理器

PNPM是一个快速、节省磁盘空间的包管理器，通过硬链接共享依赖，提高安装速度。

### 启用与安装

```bash
# 启用Corepack (Node.js 16.9.0+自带)
corepack enable

# 准备并激活最新版PNPM
corepack prepare pnpm@latest --activate

# 使用最新版PNPM
corepack use pnpm@latest
```

### 常用命令

```bash
# 安装依赖
pnpm install

# 添加依赖
pnpm add <package>

# 添加开发依赖
pnpm add -D <package>
```

## 推荐配置

- 使用`.nvmrc`或`.node-version`文件指定项目Node.js版本
- 配置`.npmrc`文件设置PNPM行为
- 结合使用`volta`或`fnm`进行版本管理

## 参考资源

- [FNM官方文档](https://github.com/Schniz/fnm)
- [PNPM官方文档](https://pnpm.io/) 