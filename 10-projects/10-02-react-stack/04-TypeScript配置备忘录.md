---
title: 04-TypeScript配置备忘录
jd_id: J10-20250519-1523
created: 2025-05-19 15:23
updated: 2025-05-28 16:17
type: guide
status: active
tags: [topic/typescript, topic/config, topic/frontend, action/config]
---

# 🔧 06-TypeScript配置备忘录

## 初始化和基础配置模版

- [tsconfig/bases](https://github.com/tsconfig/bases) - 各种项目类型的推荐基础配置
- [Matt Pocock 的 tsconfig 速查表](https://www.totaltypescript.com/tsconfig-cheat-sheet) - 这是您提供的正确链接

> `tsconfig/bases` 记录有官方推荐的模版，可以简单参考，tsconfig 速查表给出了最佳实践的配置，添加了个人理解，回避官方文档全面些。

## 社区参考资源

- [TypeScript 官方 tsconfig 参考](https://www.typescriptlang.org/tsconfig) - 官方配置文档
- [tsconfig/bases](https://github.com/tsconfig/bases) - 官方推荐的各类项目基础配置
- [@total-typescript/tsconfig](https://github.com/total-typescript/tsconfig) - Matt Pocock 的配置库
- [ts-reset](https://github.com/total-typescript/ts-reset) - TypeScript 的"CSS 重置"，改进常见 JavaScript API 的类型
- [type-fest](https://github.com/sindresorhus/type-fest) - 有用的类型集合
- [Total TypeScript](https://www.totaltypescript.com/) - Matt Pocock 的全面 TypeScript 课程

## TypeScript Lint

- [typescript-eslint](https://typescript-eslint.io/) - TypeScript 的 ESLint 配置

## 最新的 TypeScript 功能

最新的 TypeScript 功能可以在官方博客和发行说明中查看：

- [TypeScript 发行说明](https://devblogs.microsoft.com/typescript/)
- [TypeScript 路线图](https://github.com/microsoft/TypeScript/wiki/Roadmap)

## 关键配置

**noEmit** · _仅类型检查_

- 值: `true`
- 作用: 不生成 JS 文件，仅执行类型检查
- 适用: Vite/Webpack 等打包工具环境

**target** · _输出版本_

- 值: `es2022`
- 作用: 决定生成的 JavaScript 代码版本
- 适用: 现代浏览器与 Node.js 项目

**lib** · _类型库_

- 值: 前端项目需添加 `dom`
- 作用: 提供类型定义范围
- 适用: 根据项目环境选择

**moduleResolution** · _模块解析策略_

- 现代前端: `bundler`
- Node.js: `nodenext`
- 传统项目: `node`
- 作用: 控制模块的查找和解析方式

**moduleDetection** · _模块检测_

- 值: `force`
- 作用: 强制将所有文件视为模块
- 优势: 避免全局命名空间污染

**isolatedModules** · _隔离编译_

- 值: `true`
- 作用: 启用单文件编译模式
- 适用: 与 Babel 等转译工具配合使用时

**module** · _模块系统_

- Node.js: `nodenext`
- 前端项目: `preserve`/`esnext`
- 作用: 指定生成的模块代码类型

**allowJs/resolveJsonModule** · _文件导入_

- 值: `true`
- 作用: 允许导入 JS/JSON 文件
- 适用: 需混合使用不同文件类型时

**esModuleInterop** · _模块兼容_
值: true
作用: 允许 CommonJS 和 ES Module 互操作，简化 import/export 混用
适用: 推荐所有项目开启，尤其是需引入 CommonJS 包时（如 import express from 'express'）

## 不同环境的选择

### 1. 使用 TypeScript 进行转译（生成 JavaScript 文件）

当您直接使用 tsc 编译器生成 JavaScript 时，需要配置输出相关选项：

```json
{
  "compilerOptions": {
    "module": "NodeNext", // 使用Node.js的最新模块解析规则
    "outDir": "dist", // 输出到dist目录，保持源码目录干净
    "sourceMap": true // 生成源映射，便于调试编译后的代码
  }
}
```

### 2. 使用外部打包工具（Vite、Webpack 等）

当使用 Vite、Webpack 等打包工具时，TypeScript 只需负责类型检查，转译由打包工具处理：

```json
{
  "compilerOptions": {
    "moduleResolution": "Bundler", // 使用打包工具的模块解析策略
    "module": "ESNext", // 保留ES模块语法，交给打包工具处理
    "noEmit": true // 不输出文件，只做类型检查
  }
}
```

### 3. 针对 Node.js 项目

Node.js 项目有特定的环境需求，可以直接使用官方针对不同 Node 版本优化的配置：

```json
{
  "extends": "@tsconfig/node22/tsconfig.json" // 为Node.js 22适配的优化配置
}
```

## 配置合并技巧

TypeScript 5.0 引入了多配置继承功能，可以组合不同的基础配置以满足复杂需求：

```json
{
  "extends": [
    "@tsconfig/strictest/tsconfig.json", // 最严格的类型检查
    "@tsconfig/node18/tsconfig.json" // Node.js 18环境优化
  ]
}
```

这种方式避免了手动合并配置的复杂性，可以灵活组合不同的预设配置。

## 实用配置建议

1. **使用`"strict": true"`**

   - 开启全面的类型检查，捕获更多潜在问题
   - 新项目建议从一开始就启用，避免未来技术债务

2. **添加`"noUncheckedIndexedAccess": true"`**

   - 使数组和对象索引访问更安全，会自动添加`| undefined`类型
   - 避免常见的"可能是 undefined"错误

3. **添加`"verbatimModuleSyntax": true"`**

   - 精确控制类型导入，减少生成的 JavaScript 代码量
   - 强制正确使用`import type`语法

4. **设置合适的`target"`**

   - 根据运行环境选择目标 ES 版本，影响语法特性和兼容性
   - 现代应用通常可以选择较新版本，获取更多特性

5. **对库项目添加`"declaration": true"`**

   - 生成类型定义文件，使您的库可以被其他 TypeScript 项目引用
   - 提高库的使用体验和类型安全性

6. **添加`"baseUrl": "."`**
   - 简化模块导入路径，支持非相对路径导入
   - 与`paths`配合使用，创建路径别名

## 推荐资源

- Matt Pocock 的全面 TypeScript 课程：[Total TypeScript](https://www.totaltypescript.com/)
- 官方配置基础项目：[tsconfig/bases](https://github.com/tsconfig/bases)
- Matt Pocock 的配置库：[@total-typescript/tsconfig](https://github.com/total-typescript/tsconfig)
