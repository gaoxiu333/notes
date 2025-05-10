# tsconfig & react

## React 官方文档解释如何使用 TypeScript

参考链接：[使用 TypeScript](https://react.dev/learn/typescript) 

 React 官方文档解释如何使用 TypeScript，它包含了一些基础的类型使用和类型包推荐，比如：

- `@types/react`
- `@types/react-dom`
- [常见类型代码仓库参考](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/react/index.d.ts)
- [DOM 事件类型参考](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/b580df54c0819ec9df62b0835a315dd48b8594a9/types/react/index.d.ts#L1247C1-L1373)
    - 如果找不到，使用事件类型的基类型：[`React.SyntheticEvent`](tsconfig%20&%20react%20c89d138b06064fd3ab0f86ac1f1fc176.md)
- 关于 `chrildren`
    - `React.ReactNode`  - 当子组件作为 JSX 类型传递时
    - `React.ReactElement` - JSX 只能是 HTML 元素
- 关于 `style`
    - `React.CSSProperties` - 包含所有 CSS 属性的联合类型

## TypeScript 文档中的 tsx 部分

这部分说明了如何将 tsx 语法转换成普通的js，这里是参考链接：[tsconfig tsx](https://www.typescriptlang.org/tsconfig/#jsx)

## Vite 中的 tsx

vite 中主要是依赖 **`@vitejs/plugin-react`**  插件，该插件利用 jsx-runtime，当然还有一些其他的一些配置，详情请看插件介绍。

这里为了支持 jsx-runtime，所以tsconfig中配置的 `"jsx": "react-jsx"` 意思就是将 tsx 文件转换成 jsx 文件交给 jsx-runtime。