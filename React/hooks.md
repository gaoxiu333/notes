# React Hooks 参考文档

> 来源：https://react.dev/reference/react/hooks

*Hooks* 让你能在组件中使用不同的 React 特性。你可以使用内置 Hooks，也可以组合它们来构建自己的 Hooks。

## State Hooks

*State* 让组件能够["记住"信息，比如用户输入](https://react.dev/learn/state-a-components-memory)。例如，表单组件可以使用 state 存储输入值，图片画廊组件可以使用 state 存储选中的图片索引。

可以使用以下 Hooks 来为组件添加 state：

- [`useState`](https://react.dev/reference/react/useState) - 声明一个可以直接更新的 state 变量
- [`useReducer`](https://react.dev/reference/react/useReducer) - 声明一个 state 变量，更新逻辑在 [reducer 函数](https://react.dev/learn/extracting-state-logic-into-a-reducer)中

```js
function ImageGallery() {
  const [index, setIndex] = useState(0);
  // ...
}
```

## Context Hooks

*Context* 让组件能够[接收来自远处父组件的信息，而无需通过 props 传递](https://react.dev/learn/passing-props-to-a-component)。例如，你的应用顶层组件可以将当前的 UI 主题传递给下面的所有组件，无论多深。

- [`useContext`](https://react.dev/reference/react/useContext) - 读取并订阅 context

```js
function Button() {
  const theme = useContext(ThemeContext);
  // ...
}
```

## Ref Hooks

*Refs* 让组件能够[持有一些不用于渲染的信息](https://react.dev/learn/referencing-values-with-refs)，比如 DOM 节点或者超时 ID。与 state 不同，更新 ref 不会重新渲染你的组件。Refs 是 React 范式的"逃生舱"。当你需要与非 React 系统（如浏览器内置 API）工作时，它们很有用。

- [`useRef`](https://react.dev/reference/react/useRef) - 声明一个 ref。你可以在其中保存任何值，但最常用于保存 DOM 节点
- [`useImperativeHandle`](https://react.dev/reference/react/useImperativeHandle) - 让你自定义组件暴露的 ref。这很少使用

```js
function Form() {
  const inputRef = useRef(null);
  // ...
}
```

## Effect Hooks

*Effects* 让组件能够[连接并同步到外部系统](https://react.dev/learn/synchronizing-with-effects)。这包括处理网络、浏览器 DOM、动画、使用不同 UI 库编写的小部件以及其他非 React 代码。

- [`useEffect`](https://react.dev/reference/react/useEffect) - 将组件连接到外部系统

```js
function ChatRoom({ roomId }) {
  useEffect(() => {
    const connection = createConnection(roomId);
    connection.connect();
    return () => connection.disconnect();
  }, [roomId]);
  // ...
}
```

Effects 是 React 范式的"逃生舱"。不要使用 Effects 来编排应用程序的数据流。如果你没有与外部系统交互，[你可能不需要 Effect](https://react.dev/learn/you-might-not-need-an-effect)。

useEffect 有两个较少使用的变体，它们在时机上有所不同：

- [`useLayoutEffect`](https://react.dev/reference/react/useLayoutEffect) - 在浏览器重绘屏幕之前触发。你可以在这里测量布局
- [`useInsertionEffect`](https://react.dev/reference/react/useInsertionEffect) - 在 React 对 DOM 进行更改之前触发。库可以在这里插入动态 CSS

## Performance Hooks

优化重新渲染性能的常见方法是跳过不必要的工作。例如，你可以告诉 React 重用缓存的计算结果，或者在数据自上次渲染以来没有更改的情况下跳过重新渲染。

要跳过计算和不必要的重新渲染，使用以下 Hooks：

- [`useMemo`](https://react.dev/reference/react/useMemo) - 缓存昂贵计算的结果
- [`useCallback`](https://react.dev/reference/react/useCallback) - 在将函数定义传递给优化的组件之前缓存它

```js
function TodoList({ todos, tab, theme }) {
  const visibleTodos = useMemo(() => filterTodos(todos, tab), [todos, tab]);
  // ...
}
```

有时，你无法跳过重新渲染，因为屏幕确实需要更新。在这种情况下，你可以通过将阻塞更新（必须同步，如在输入框中输入）与非阻塞更新（不需要阻塞用户界面，如更新图表）分开来提高性能。

要优化渲染优先级，使用以下 Hooks：

- [`useTransition`](https://react.dev/reference/react/useTransition) - 将状态转换标记为非阻塞，并允许其他更新中断它
- [`useDeferredValue`](https://react.dev/reference/react/useDeferredValue) - 延迟更新 UI 的非关键部分，让其他部分先更新

## 其他 Hooks

这些 Hooks 主要对库作者有用，在应用程序代码中不常使用：

- [`useDebugValue`](https://react.dev/reference/react/useDebugValue) - 自定义 React DevTools 显示的自定义 Hook 标签
- [`useId`](https://react.dev/reference/react/useId) - 让组件关联一个唯一 ID。通常用于可访问性 API
- [`useSyncExternalStore`](https://react.dev/reference/react/useSyncExternalStore) - 让组件订阅外部存储
- [`useActionState`](https://react.dev/reference/react/useActionState) - 允许你管理 actions 的状态

## 自定义 Hooks

你也可以[定义自己的自定义 Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks#extracting-your-own-custom-hook-from-a-component) 作为 JavaScript 函数。
