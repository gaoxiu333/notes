---
title: tsconfig-备忘录
jd_id: J00-20250515-1514
created: 2025-05-15 15:14
updated: 2025-05-15 15:14
type: note
status: draft
tags: []
---

# TypeScript 配置 (tsconfig.json) 备忘录

## 社区参考资源

- [TypeScript 官方 tsconfig 参考](https://www.typescriptlang.org/tsconfig)
- [ts-reset: 社区推荐配置](https://github.com/total-typescript/ts-reset)
- [type-fest](https://github.com/sindresorhus/type-fest) - 有用的类型集合
- [typescript-eslint](https://typescript-eslint.io/) - TypeScript 的 ESLint 配置

## 有用的 tsconfig 模板项目

- [tsconfig/bases](https://github.com/tsconfig/bases) - 各种项目类型的推荐基础配置
- [Matt Pocock 的 tsconfig 速查表](https://www.totaltypescript.com/tsconfig-cheat-sheet) - 这是您提供的正确链接

## 最新的 TypeScript 功能

最新的 TypeScript 功能可以在官方博客和发行说明中查看：

- [TypeScript 发行说明](https://devblogs.microsoft.com/typescript/)
- [TypeScript 路线图](https://github.com/microsoft/TypeScript/wiki/Roadmap)

## 基础配置

```json
{
  "compilerOptions": {
    /* 基础选项 */
    "esModuleInterop": true, // 允许 CommonJS 和 ES 模块互操作，简化 import/export 混用
    "skipLibCheck": true, // 跳过所有声明文件（.d.ts）的类型检查，加快编译速度
    "target": "es2022", // 指定编译后 JS 的目标 ECMAScript 版本
    "allowJs": true, // 允许编译 JS 文件（.js）
    "resolveJsonModule": true, // 允许 import JSON 文件为模块
    "moduleDetection": "force", // 强制所有文件都作为模块处理
    "isolatedModules": true, // 每个文件单独作为模块编译，便于与 Babel 等工具集成
    "verbatimModuleSyntax": true, // 精确保留 import/export 语法，强制类型导入用 import type

    /* 严格模式 */
    "strict": true, // 启用所有严格类型检查选项
    "noUncheckedIndexedAccess": true, // 索引访问类型自动加上 | undefined，更安全
    "noImplicitOverride": true, // 子类重写父类方法时必须显式使用 override 关键字

    /* 如果使用 TypeScript 进行转译：*/
    "module": "NodeNext", // 使用 Node.js 的最新模块系统
    "outDir": "dist", // 编译输出目录
    "sourceMap": true, // 生成 source map 文件，便于调试

    /* 如果你在构建一个库：*/
    "declaration": true, // 生成 .d.ts 类型声明文件

    /* 如果你在 monorepo 中构建一个库：*/
    "composite": true, // 支持增量编译，适合大型/多包项目
    "declarationMap": true, // 生成声明文件的 source map，便于调试类型

    /* 如果不使用 TypeScript 进行转译：*/
    "module": "preserve", // 保留源码中的模块语法，不做转换
    "noEmit": true, // 不输出编译结果，仅做类型检查

    /* 如果你的代码运行在 DOM 环境：*/
    "lib": ["es2022", "dom", "dom.iterable"], // 包含 ES2022 和 DOM 相关类型

    /* 如果你的代码不运行在 DOM 环境：*/
    "lib": ["es2022"] // 仅包含 ES2022 类型
  }
}
```

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

## 常见问题与误区

1. **误区：配置越严格越好**

   - 过度严格的配置如`noUnusedLocals`会产生大量警告，干扰开发流程
   - 应根据团队习惯和项目阶段选择适当的严格程度

2. **误区：一种配置适用所有项目**

   - 库项目需要生成声明文件，应用项目则不必
   - 浏览器环境需要 DOM 类型，Node.js 项目则不需要
   - 应根据项目特点定制配置

3. **问题：模块解析错误**

   - 设置`"baseUrl": "."`解决相对路径导入问题
   - 针对不同环境选择正确的`moduleResolution`:
     - Node.js: `"NodeNext"`
     - 打包工具: `"Bundler"`

4. **问题：类型定义文件缺失**

   - 库项目需启用`"declaration": true"`
   - 添加`"types": ["node"]`等选项指定全局类型
   - 使用`@types/*`包添加第三方库的类型

5. **误区：忽略`skipLibCheck"`选项**

   - 大型项目中，检查所有.d.ts 文件会显著增加编译时间
   - 启用该选项可大幅提高开发效率，很少有负面影响

6. **问题：ES 模块与 CommonJS 混用**
   - 设置`"esModuleInterop": true"`简化混用场景
   - 了解`import * as X`和`import X`的区别
   - 正确设置`module`和`moduleResolution`选项

## 推荐资源

- Matt Pocock 的全面 TypeScript 课程：[Total TypeScript](https://www.totaltypescript.com/)
- 官方配置基础项目：[tsconfig/bases](https://github.com/tsconfig/bases)
- Matt Pocock 的配置库：[@total-typescript/tsconfig](https://github.com/total-typescript/tsconfig)
