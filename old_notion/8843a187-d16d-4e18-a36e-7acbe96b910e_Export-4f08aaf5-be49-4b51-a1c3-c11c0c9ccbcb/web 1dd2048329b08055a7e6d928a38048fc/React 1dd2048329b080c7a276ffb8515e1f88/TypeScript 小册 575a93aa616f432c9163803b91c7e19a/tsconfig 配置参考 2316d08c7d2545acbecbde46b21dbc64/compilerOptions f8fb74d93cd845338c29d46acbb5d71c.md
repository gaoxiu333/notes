# compilerOptions

编译器选项

## 基本配置

以下配置适合所有项目：

```json
{
  "compilerOptions": {
    "esModuleInterop": true,
    "skipLibCheck": true,
    "target": "es2022",
    "allowJs": true,
    "resolveJsonModule": true,
    "moduleDetection": "force",
    "isolatedModules": true,
    "verbatimModuleSyntax": true
  }
}
```

- `esModuleInterop` - 修复 CommonJS 和 ES 模块之间的一些界限
- `skipLibCheck` - 跳过检查 .d.ts 文件，提升检查性能
- `target` - 转为 JavaScript 的版本
- `allowJs` - 允许 JS
- `resolveJsonModule` - 允许 JSON
- `moduleDetection` - 强制 TypeScript 将所有文件视为模块有助于避免 '[**cannot redeclare block-scoped variable**](https://www.totaltypescript.com/cannot-redeclare-block-scoped-variable)' 错误
- `isolatedModules` - 阻止一些 TS 功能？？？？？？？？
- `verbatimModuleSyntax` - 强制使用 **`import type`** 和 **`export type`** ，可预测并减少不必要的导入

## 严格

适合 TS 中严格性选项

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true
  }
```

- `strict` - 启用所有严格类型检查
- `noUncheckedIndexedAccess` - 防止运行时错误，组织未检查数组或者对象时访问该数组或对象
- `noImplicitOverride` - 使用 `override` 关键字 ？？？？？

## 转译

以下配置在使用 `tsc` 转译代码时有用

```json
{
  "compilerOptions": {
    "module": "NodeNext",
    "outDir": "dist"
  }
}
```

- `module` - 告诉 TypeScript 使用什么模块的语法，推荐 `NodeNext` ，同时隐含 `moduleResolution: NodeNext`
- `outDir` - 编译后的 JavaScript 存放位置

## 构建 Library

```json
{
  "compilerOptions": {
    "declaration": true
  }
}
```

- `declaration` - 生成 `.d.ts` 文件

## Monorepo 中构建 Library

```json
{
  "compilerOptions": {
    "declaration": true,
    "composite": true,
    "sourceMap": true,
    "declarationMap": true
  }
}
```

- `composite` - 生成 `.tsbuildinfo` 文件，告诉 ts 这个项目是 monorepo 的一部分，有助于加快构建速度
- `soureMap` - 生成源码映射
- `declarationMap` - 生成声明映射，可以使用 `go-to-definition` 跳转到源码

## 不使用 TSC 转译

如果不使用 `tsc` 转译代码，只是使用 TypeScript 作为 linter，以下选项可能是需要的

```json
{
  "compilerOptions": {
    "module": "preserve",
    "noEmit": true
  }
}
```

- `module` - `preserve` 选项最接近模仿捆绑程序处理模块的方式，并且隐含`moduleResolution:Bunder`
- `noEmit` - 阻止 TypeScript 生成任何文件

## 如果需要 DOM

```json
{
  "compilerOptions": {
    "lib": ["es2022", "dom", "dom.iterable"]
  }
}
```

- `lib` - 告诉 TypeScript 包含哪些内置类型
    - `es2022` 是js版本最好的选择
    - `dom` 提供 `document` 和 `window` ，单不包括迭代器（由于历史原因？）
    - `dom.iterable` 单独提供迭代器的支持