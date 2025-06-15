---
title: TypeScript配置指南
jd_id: J10-20250519-1523
created: 2025-05-19 15:23
updated: 2025-06-15 19:46
type: guide
status: active
tags: [topic/typescript, topic/config, topic/frontend, action/config]
---

# ⚙️ TypeScript 配置备忘录

> [!info]
> 本文聚焦于 TypeScript 项目配置的实用方案，适合查阅和快速定位常见场景下的最佳实践。

## 目录

- [⚙️ TypeScript 配置备忘录](#️-typescript-配置备忘录)
  - [目录](#目录)
  - [核心配置速查表](#核心配置速查表)
  - [典型场景配置方案](#典型场景配置方案)
    - [1. 前端项目（Vite/Webpack）](#1-前端项目vitewebpack)
    - [2. Node.js 项目](#2-nodejs-项目)
    - [3. 库开发](#3-库开发)
    - [4. 配置合并技巧](#4-配置合并技巧)
  - [进阶与最佳实践](#进阶与最佳实践)
  - [常见问题与排查技巧](#常见问题与排查技巧)
  - [优质资源推荐](#优质资源推荐)

---

## 核心配置速查表

| 配置项                    | 推荐值  | 说明/场景                    |
| ------------------------- | ------- | ---------------------------- |
| strict                    | true    | 开启严格类型检查             |
| noEmit                    | true    | 仅类型检查，交由打包工具转译 |
| module                    | ESNext  | 前端项目/库开发              |
| moduleResolution          | Bundler | Vite/Webpack 等现代前端      |
| target                    | es2022  | 现代浏览器/Node.js           |
| lib                       | ["dom"] | 前端需加 dom                 |
| moduleDetection           | force   | 强制所有文件为模块           |
| isolatedModules           | true    | 单文件编译，配合 Babel       |
| allowJs/resolveJsonModule | true    | 允许导入 JS/JSON 文件        |
| esModuleInterop           | true    | 推荐所有项目开启             |

**典型用例**
`esModuleInterop` 它控制 TypeScript 如何处理 CommonJS 模块（比如 require() 导入）与 ES Module 的互操作

```ts
import moment from "moment"; // ❌ 报错：Property 'default' does not exist

// 必须这样写
import * as moment from "moment";

// 开启后 esModuleInterop 后
import moment from "moment"; // ✅ 可以直接这样写
```

---

## 典型场景配置方案

### 1. 前端项目（Vite/Webpack）

```json
{
  "compilerOptions": {
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "noEmit": true,
    "strict": true
  }
}
```

> [!tip]
> 只做类型检查，转译交给打包工具。

### 2. Node.js 项目

```json
{
  "extends": "@tsconfig/node22/tsconfig.json"
}
```

> [!info]
> 推荐直接继承官方 Node 版本预设，省心省力。

### 3. 库开发

```json
{
  "compilerOptions": {
    "declaration": true,
    "emitDeclarationOnly": true,
    "outDir": "dist/types"
  }
}
```

> [!example]
> 生成类型声明文件，便于他人引用。

### 4. 配置合并技巧

TypeScript 5.0 支持多配置继承：

```json
{
  "extends": [
    "@tsconfig/strictest/tsconfig.json",
    "@tsconfig/node18/tsconfig.json"
  ]
}
```

> [!tip]
> 灵活组合不同预设，避免手动合并。

---

## 进阶与最佳实践

- 启用 `noUncheckedIndexedAccess` 提升安全性
- 使用 `verbatimModuleSyntax` 精确控制类型导入
- 配置 `baseUrl` 和 `paths` 实现路径别名
- 设置合适的 `target`，根据运行环境选择
- 对库项目添加 `declaration`，生成类型定义文件

---

## 常见问题与排查技巧

- `moduleResolution` 默认值不确定？
  > 运行 `tsc --showConfig` 查看实际生效配置
- 配置冲突、类型丢失等常见坑
- Node.js 项目 ESModule 与 Commonjs 互转，需关注 `package.json`、`tsconfig.json`、`eslint.config.ts` 配合

---

## 优质资源推荐

- [TypeScript 官方 tsconfig 参考](https://www.typescriptlang.org/tsconfig)
- [tsconfig/bases](https://github.com/tsconfig/bases)
- [@total-typescript/tsconfig](https://github.com/total-typescript/tsconfig)
- [ts-reset](https://github.com/total-typescript/ts-reset)
- [type-fest](https://github.com/sindresorhus/type-fest)
- [Total TypeScript](https://www.totaltypescript.com/)
- [TypeScript 发行说明](https://devblogs.microsoft.com/typescript/)
- [TypeScript 路线图](https://github.com/microsoft/TypeScript/wiki/Roadmap)
- [typescript-eslint](https://typescript-eslint.io/)

---

> [!summary]
> 本文持续更新，欢迎补充与指正！

---

[[00-MOC-React技术栈|返回 React 技术栈 MOC]]
