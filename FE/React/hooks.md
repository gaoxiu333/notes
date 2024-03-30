# React Hooks

Hook 是 React 16.8 的新增特性。它可以让你在不编写 class 的情况下使用 state 以及其他的 React 特性。

#### State Hooks 数据驱动

- [useState](https://react.dev/reference/react/useState)  - 返回一个 state，以及更新 state 的函数
- [useReducer](https://react.dev/reference/react/useReducer) -  返回当前的 state 以及与其配套的 `dispatch` 方法
- `useSyncExternalStore` - concurrent 模式下，订阅外部数据源
- `useDeferroredValue` - concurrent 模式下，更新状态滞后

#### Context Hooks 上下文

- [useContext](https://react.dev/reference/react/useContext)  - 接收一个 context 对象，并返回该 context 的当前值。

#### Ref Hooks 静态变量

- [useRef](https://react.dev/reference/react/useRef) - 获取元素或者组件实例。
- [useImperativeHandle](https://react.dev/reference/react/useImperativeHandle) - 定义 React 组件暴露出来的 API ，需要配合 `forwardRef`

#### Effect Hooks 执行副作用

- [useEffect](https://react.dev/reference/react/useEffect) - DOM 变更之后调用，此时可以读取最新的DOM
- `useLayoutEffect` - DOM 更显之前同步执行
- `useInetionEffect` - 处理 CSS-in-JS 问题

#### Performance Hooks - 性能

- [useMemo](https://react.dev/reference/react/useMemo) - 记住计算结果，并缓存，之后依赖改变才重新计算，有助于避免在每次渲染时都进行高开销的计算
- [useCallback](https://react.dev/reference/react/useCallback) -  简化 useMemo 操作
- `useTransition` - concurrent 模式下，将不重要的计算挂起执行避免卡顿

#### Other Hooks 其他

- [useDebugValue](https://react.dev/reference/react/useDebugValue) - Devtool Debug
- [useId](https://react.dev/reference/react/useId) - 生成唯一 ID