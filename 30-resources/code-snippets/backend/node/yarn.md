---
title: yarn
created: 2024-04-22 11:45
updated: 2024-04-22 11:45
type: resource
status: active
schema: v1
tags: [source/notion, topic/backend/nodejs, topic/devops/package-manager, lang/javascript]
---

# yarn

## 版本

- `latest` / `berry` / `stable` -> 最新的稳定版本(`>=2.0.0`)
- `canary` -> 稳定版的下一个版本金丝雀版本(`>=2.0.0`)
- `classic` -> 经典版本(`^0.x || ^1.x`)

> 最新版本4.x建议node>18

## 安装

官方推荐的首选安装方式

```
corepack enable # 安装的似乎是yarn 1.2.x
yarn set version berry   # 使用最新的yarn 4.x
corepack prepare yarn@1.22.22 --activate # 使用 1.22
yarn init -2 # 初始化项目
```

## 初始化

```
yarn init
yarn init -2  # 使用yarn 2 初始化
yarn init -w # 初始化，并将其定义为工作空间根目录。

# 特别的: 添加ts并使用VSCode
yarn add --dev typescript
yarn dlx @yarnpkg/sdks vscode
```

## 清理缓存

```
# 清除本地所有缓存
yarn cache clean
# 只清除 .yarn 目录中的缓存
yarn cache clean --mirror

# 终极：删除所有缓存文件
yarn cache clean --all
```

## monorepo

### 基本操作

```
# 初始化子项目
yarn packages/my-new-lib init

单个项目添加依赖
yarn workspace components add -D react
```

### **混用**`PnP`+`node_modules`

1. 创建项目

2. `.yarnrc.yml`在monorepo 根目录的main 中为此路径添加 PnP 忽略模式：

3. 最后 `yarn installpnpIgnorePatterns`

### yarn 中的工作流

- `yarn workspace foucs` - 当你只想安装某个子工作区的依赖时可能会用到（官网这点教程写的特别简单）
- `yarn workspaces foreach`统一或者并行运行各个项目内`pacage.json`中的`script`命令

## 可能用到的配置

- 如果你想使用经典的`node-modules`

- 如果出现幽灵依赖问题

## 补充

### yarn4出现解决了什么问题？

- pnpm通过软/硬链接来指向最终依赖包
- pnpm通过提升软件包来优化`node_modules`大小，导致出现幽灵依赖
- yarn 保留了所有包及其依赖项的列表
- yarn 的错误提示更加完整（自称）
- 零安装 - 缓存依赖想，切换分支的时候，可以保证项目正常运行

### 哪些项目不能使用yarn？

- React Native
- Expo
- 依赖Flow 的项目

它们需要`node_modules`所以不适用yarn

## 总结

最新版本的`yarn`在本地开发很不优化，如果是js的依赖，没办法看到源文件的定义。