# React 内置 API 参考

> 来源：https://react.dev/reference/react/apis

除了 [Hooks](https://react.dev/reference/react) 和 [Components](https://react.dev/reference/react/components) 之外，`react` 包还导出了一些其他用于定义组件的 API。本文列出了所有现代 React API。

## 核心 API

- [`createContext`](https://react.dev/reference/react/createContext) - 让你定义并向子组件提供 context。与 [`useContext`](https://react.dev/reference/react/useContext) 配合使用。

- [`forwardRef`](https://react.dev/reference/react/forwardRef) - 让你的组件将 DOM 节点作为 ref 暴露给父组件。与 [`useRef`](https://react.dev/reference/react/useRef) 配合使用。

- [`lazy`](https://react.dev/reference/react/lazy) - 让你延迟加载组件的代码，直到它第一次被渲染。

- [`memo`](https://react.dev/reference/react/memo) - 让你的组件在 props 相同时跳过重新渲染。与 [`useMemo`](https://react.dev/reference/react/useMemo) 和 [`useCallback`](https://react.dev/reference/react/useCallback) 配合使用。

- [`startTransition`](https://react.dev/reference/react/startTransition) - 让你将状态更新标记为非紧急。类似于 [`useTransition`](https://react.dev/reference/react/useTransition)。

- [`act`](https://react.dev/reference/react/act) - 让你在测试中包装渲染和交互，以确保在进行断言之前已处理更新。

## Resource APIs

*Resources* 可以被组件访问，而无需将它们作为状态的一部分。例如，组件可以从 Promise 中读取消息，或从 context 中读取样式信息。

要从 resource 中读取值，使用以下 API：

- [`use`](https://react.dev/reference/react/use) - 让你从 resource（如 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) 或 [context](https://react.dev/learn/passing-data-deeply-with-context)）中读取值。

```js
function MessageComponent({ messagePromise }) {
  const message = use(messagePromise);
  const theme = use(ThemeContext);
  // ...
}
