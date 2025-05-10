# TypeScript 声明文件

# TypeScript 声明文件

草稿

- 工程能力
- 框架继承
- ES语法
- TSConfig
- Node API

### 类型检查指令

使用注释忽略TS全局配置

```tsx
// 忽略下一行代码的类型检查// @ts-ignore// 只有下一行类型报错时忽略下一行类型检查，否则不能使用（更人性化的@ts-ignore）// @ts-expect-error// eslint 禁用下一行类型检查/* eslint-disable-next-line */// eslint 放在文件首行，禁用整个文件类型检查/* eslint-disable */// tsc 禁用检查// @ts-nocheck
```

### 类型声明

### 语法

- `declare module`
- `declare namespace`
- `declare`
- 类型声明和类型标注的区别是什么？
- 非代码文件？JSON?
- js文件？
- 全局变量或者改写全局变量

**不支持TS的npm包**

```tsx
// .d.tsdeclare module 'pkg' {
  const handler:()=>boolean}
// main.tsimport foo from 'pkg'const res = foo.handler()
```

**对代码文件导入**

- `.md`、`.css`、`.module.css`、`.png`等文件

markdown文件

```tsx
// d.tsdeclare module "*.d" {
  const raw:string;  export default raw
}
// main.tsimport raw from './note.md'const content = raw.replace('',...)
```

**修改全局变量**

- 使用`interface`声明类型时，如果有多个同名类型，则**自动合并**

```tsx
// .d.tsinterface Window { // 将于工具类中的Window接口自动合并  someKey:any}
```

### 三斜线指令

- 类似ts的配置文件
    - 它可以定制当前文件编译配置
    - 也可以在没有模块化时，自己引入依赖
- 它的作用是声明当前文件依赖的其他类型声明
- 必须放在文件的顶部才能生效

### 其他问题

- React 中不引入React，就能使用是怎么做到的?
    - `allowUmdGlobalAccess`
    - TS 配置，开启后，React作为全局变量

```tsx
export = React;export as namespace React; // React 将作为全局变量，不需要导入declare namespace React {
  // 省略了不必要的类型标注  function useState<S>(initialState): [];}
```

1