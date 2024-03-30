# React 内置组件

React 提供了一些内置的组件，你可以在 JSX 中使用它们。

- `<Fragment>` - 也可以写作 `<>...</>`，让你可以将多个 JSX 节点组合在一起。
- `<Profiler>` -  查看React 树的渲染性能。
- `<Suspense>` - React 的 Loading 组件
- `<StrictMode>` - React  严格模式，开发环境默认开启

## `<Fragment>`

通常通过`<>...</>`语法使用，可以作为包裹节点，渲染后在DOM中不存在，节省DOM节点

```jsx
function APP(){
  return <>
  	<h1>标题</h1>
  	<p>内容</p>
  <>
}
```

在 Fragment 上使用 key，这个时候不能使用简写 `<>...</>`

```js
import { Fragment } from 'react';
function Blog() {
  return posts.map(post =>
    <Fragment key={post.id}>
      <PostTitle title={post.title} />
      <PostBody body={post.body} />
    </Fragment>
  );
}
```

## `<StrictMode>`

开发模式 默认开启严格模式

特点：

- 组件每次渲染后都会再重复一次。
- Effects 在重新渲染后也会重新执行。
- 检查是否使用了已经废弃的 API

```jsx
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';

const root = createRoot(document.getElementById('root'));
root.render(
  <StrictMode>
    <App />
  </StrictMode>
);
```

> 包裹跟组件意味着全局使用严格模式，也可以单独包裹某个组件，针对组件开启严格模式 。

## `<Suspense>`

可以在组件挂起时，显示 loading

```jsx
<Suspense fallback={<Loading />}>
  <Albums />
</Suspense>
```

> **只有启用了 Suspense 的数据源才会激活 Suspense 组件。**他们包括：
>
> - 使用支持 Suspense 的框架（如[Relay](https://relay.dev/docs/guided-tour/rendering/loading-states/)和[Next.js）获取数据](https://nextjs.org/docs/advanced-features/react-18)
> - 延迟加载组件代码[`lazy`](https://react.dev/reference/react/lazy)
>
> Suspense**不会**检测何时在 Effect 或事件处理程序中获取数据。
>
> 总结就是，需要支持才行。

原理？？

https://juejin.cn/post/6844903789959315470