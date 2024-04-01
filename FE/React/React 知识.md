## 开发环境

### 构建

- Vite

- Nextjs

### 编辑器配置

- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) - 自动格式化代码

### 开发者工具

React Developer Tools

- [**Chrome**](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en)

- [**Firefox**](https://addons.mozilla.org/en-US/firefox/addon/react-devtools/)

- [**Edge**](https://microsoftedge.microsoft.com/addons/detail/react-developer-tools/gpphkfbcpidddadnkolkpfckpihlkkil)

## JSX

### 什么是JSX

- JavaScript XML的缩写，是JavaScript的语法拓展，用于在JavaScript代码中声明UI元素

- 在React中，本质上JSX只是`React.createElement`提供的一种语法糖

## 特点

- 增强组件的可读性

- 可以使用JavaScript表达式

### 原理

- JSX在后续中会被转换为嵌套调用，使用`React.createElement()`

### 语法规则

- **单一跟元素：**最外层必须只能有一个元素

- **首字母大写：**小写字会被认为不是React组件

- **标签必须闭合：**关闭所有标签，所有标签都需要有闭合标签

- **小驼峰命名法：**DOM属性，标签属性使用小驼峰命名法，除非用到了保留字

- `{}`可以书写JavaScript表达式

### 注意

- `class => className`

- `for => htmlFor`

- checked

- `checked`

- `defaultChecked`

- `dangerousySetInnerHTML` :原生`innerHTML`

- JavaScript 表达式必须用大括号

- 內联样式必须使用对象

- 多行JSX必须用括号括起来

## 组件

### 类组件

- 类组件通过继承`React.Component`类创建

- 具有自己的状态（state）和生命周期方法

- 类组件使用`render()`方法来返回要想渲染的UI结构

### 函数组件

- 函数组件是纯函数，接受`props`作为参数并返回JSX元素

- 函数组件没有自己的状态或生命周期，但是可以使用React Hooks来管理状态和其他React特性

- 必要条件

- 必须显式返回`null`或`React.Element`

- 接受一个可选的`props`作为参数

- 首字母必须大写

他们的共同特点是，都需要使用大驼峰命名法，不然不会被React识别会React组件。

- 类组件

- 函数组件

- 组件优化

- `React.memo`

- `PureComponent`

- `<Fragment>`

### 组件抽象

- 状态组件

- 无状态组件 - 只负责接收props，渲染DOM，没有State

- 有状态组件 - 包含State，生命周期等

- 容器组件

- 提取获取数据和处理数据的逻辑

- 降低耦合性

- 高阶组件 - 借鉴高阶函数，返回组件的函数

- 渲染回调组件 - 将渲染逻辑委托给子组件，其实就是调用`children`方法，原来可以调用的！

- 受控组件

- 受React状态更新的组件

- 非受控组件

- 由DOM元素本身来管理，通过Ref来获取表单元素的值。

## 状态管理和单向数据流

- `useState`

- `useReducer`

- [增加交互：](https://react.dev/learn/adding-interactivity)查看state运行原理

- [APIs 文档](https://react.dev/reference/react/hooks)：直接查看用法

### APIs 速记

- useState

- 初始化

- `值`、`纯函数` (调用)

- `纯函数`(不调用)

- state - 状态变量

- 管理状态的数据

- setState 函数

- 仅更新下次渲染的状态变量

- 通过`Object.is`比较新旧值是否相等，相等则跳过重新渲染组件及其子组件

- 批量更新状态

- 严格模式下会调用两次更新函数

- 在同一个代码块内多次连续调用，请使用纯函数的方式调用，不然只生效一次

- 阅读[更新状态中的对象](https://react.dev/learn/updating-objects-in-state)和[更新状态中的数组](https://react.dev/learn/updating-arrays-in-state)以了解更多信息。

- [批量更新](https://react.dev/learn/queueing-a-series-of-state-updates)

- 如何处理多个状态更新

- 对同一状态多次更新

- 状态快照

- 设置状态不会更改现有渲染中的变量，但会请求新的渲染。

- React 在事件处理程序完成运行后处理状态更新。这称为批处理。

- 要在一个事件中多次更新某个状态，可以使用`setNumber(n => n + 1)`updater 函数。

-  更新对象

- 浅拷贝，如：拓展运算符

- 使用Immer

- 更新数组

- 拓展运算符或者Immer

- 添加

- `concat`、`[...arr]`

- 删除

- `filter`、`slice`

- 替换

- `map`

### 原理

#### 渲染

简单表述React原理：React通过事件触发渲染，然后渲染组件，最后提交给DOM

- 响应事件

- 状态

- 渲染并提交

- 初始渲染

- 通过调用`createRoot`然后通过`render`方法调用完成。

- 触发：app启动时，React调用根组件

- 提交：React 调用`appendChild()`更新DOM

- 状态更新引起的渲染

- 触发：调用状态更新触发渲染的函数组件

- 以上过程是递归的，直至嵌套的所有组件都完成

- 通过diff，只对更改进行渲染

- 渲染特点

- 渲染的方式为递归

- 直至嵌套的所有组件都完成

- 优化：[解决顶层组件的性能问题](https://legacy.reactjs.org/docs/optimizing-performance.html) - 但不要过早优化

> 总结：React 更新DOM经过三个步骤，首先是触发事件，然后调用Render函数，也就是React自己的渲染，最后提交给DOM，进行浏览器绘制。 - Trigger - Render - Commit

### 代码示例

更新state的两种用法

```
const [state,setState] = useState()
// nextState:直接传递你想要的状态值
setState('state') 
// nextState: 纯函数，参数为当前state，返回下一个状态
setState((currentState)=>currentState+1) 
```

#### 常见问题

1. 设置状态如何触发重新渲染?

- 调用`setState`

- 当React检测到状态变化时，React会重新调用组件的`render`方法，根据新的状态生成更新后的UI

1. 状态何时以及如何更新?

- 状态在事件处理程序、生命周期、或者effect hook中调用`setState`

- 状态更新时，React在当前渲染周期结束后，以异步的方式批量更新组件的状态

- 这样做可以提高性能，避免不必要的重复渲染

1. 为什么状态在设置后没有立即更新?

- React采用异步更新状态的机制，调用`setState`后会将状态更新放入队列中

- 在适当的时机批量更新状态（通常是当前渲染周期结束后），并触发重新渲染

1. 事件处理程序如何访问状态的“快照”?

- 通过闭包来访问状态的快照

- 确保事件处理程序始终使用更新之前的状态值，并且避免一些常见的陷阱，提高性能

1. 什么是批量处理？

- React 会等到事件处理程序中的所有代码都运行完毕后才处理状态更新；

- 这使得更新多个状态不会触发太多重新渲染

- 同时事件处理程序执行完之前，UI不会更新

- 这种行为成为批量更新。

## API

### 内置 Components

- `<Fragment>`

- `<Profiler>`

- `<StrictMode>`

- `<Suspense>`

> 参考：[Built-in React Components](https://react.dev/reference/react/components)

### 内置API

- `createContext`

- `forwardRef`

- `lazy`

- `memo`

- `startTransition`

> 参考：[Built-in React APIs](https://react.dev/reference/react/apis)

### 内置 hooks

常用的hooks

- `useState`

- `useEffect`

- `useContext`

- `useReducer`

- `useCallback`

- `useMemo`

- `useRef`

- `useLayoutEffect`

> 更多参考：[Built-in React Hooks](https://react.dev/reference/react/hooks)

### React DOM API

- `createPartal`

- `flushSync`

- 其他：

- `react-dom/client`

- `react-dom/server`

> 参考：[React DOM API](https://react.dev/reference/react-dom)

- [React 参考概述](https://react.dev/reference/react)

## 常见问题

- `useState`批量更新

- `useCallback`和`useMemo` 的区别是什么？

- `useEffect`和`useLayoutEffect`的区别是什么？

- 严格模式

- [帮助你发现意外的杂质。](https://react.dev/reference/react/useState#my-initializer-or-updater-function-runs-twice)

react如何触发更新的

diff算法是什么

需要源码么

批量更新又是什么



## DOM 操作

- `useRef`

### APIs

- useRef

- 记住某些信息，但是不希望触发重新渲染时使用

- 引用DOM

- 引用不希望触发渲染的值

- ref 回调

- `forwardRef` 访问子组件的DOM

- `flushSync` - state更新后强制刷新DOM，使手动操作DOM可以和State保持一致

- 常用于滚动到新元素，新元素获取焦点等

### 代码示例

- ref 回调

```jsx
import { useRef } from 'react';

export default function CatFriends() {
  const itemsRef = useRef(null);

  function scrollToId(itemId) {
    const map = getMap();
    const node = map.get(itemId);
    node.scrollIntoView({
      behavior: 'smooth',
      block: 'nearest',
      inline: 'center'
    });
  }

  function getMap() {
    if (!itemsRef.current) {
      // Initialize the Map on first usage.
      itemsRef.current = new Map();
    }
    return itemsRef.current;
  }

  return (
    <>
      <nav>
        <button onClick={() => scrollToId(0)}>
          Tom
        </button>
        <button onClick={() => scrollToId(5)}>
          Maru
        </button>
        <button onClick={() => scrollToId(9)}>
          Jellylorum
        </button>
      </nav>
      <div>
        <ul>
          {catList.map(cat => (
            <li
              key={cat.id}
              ref={(node) => {
                const map = getMap();
                if (node) {
                  map.set(cat.id, node);
                } else {
                  map.delete(cat.id);
                }
              }}
            >
              <img
                src={cat.imageUrl}
                alt={'Cat #' + cat.id}
              />
            </li>
          ))}
        </ul>
      </div>
    </>
  );
}

const catList = [];
for (let i = 0; i < 10; i++) {
  catList.push({
    id: i,
    imageUrl: 'https://placekitten.com/250/200?image=' + i
  });
}
```

## 生命周期和Effect

- `useEffect`

### APIs

- 生命周期

- 组件生命周期包含安装、更新和卸载

- `Effect`

- 开始同步、停止同步

- 每次渲染都会导致`Effect`执行

- 可以设置依赖项，如果依赖改变，才会执行

- 空依赖，只有在组件挂载时执行一次

- 严格模式

- 严格模式会执行两次

- 是为了保证副作用有清理操作

- 获取数据

- 不能服务端渲染加载数据

- 更多的网络请求会导致网络瀑布

- 不能与加载或者缓存数据

- 使用`React Query`、`useSwr`、`React Router` 获取数据

- 可以避免网络瀑布逻辑，避免重复请求，添加缓存等

## Hooks

- React 16.8.0 引入的权限概念

- 定义：允许在函数组件内定义某些机制

- 自定义hooks，轻松共享复用逻辑

- 监听浏览器事件，比如`resize`，鼠标滚动等

- 共享状态逻辑（业务逻辑）

### 常用Hooks

- 基础hooks

- `useState`

- `useEffect`

- `useContext`

- 附加hooks

- `useReducer`

- `useCallback`

- `useMemo`

- `useRef`

- `useImperativeHandle`

- `useLayoutEffect`

- `useDebugValue`

- `use`

- `useAccountInfo`

- `useDocumentInfo`

> 附加hooks可以覆盖边缘情况，以及处理某些优化

### ESlint

- `eslint-plugin-react-hooks`遵循一些规则，防止遇到意外的错误行为

- 规则

- 只能在函数组件中使用，类组件现在也可以了，现在的规则应该是只可以在React组件内使用

- 只能在组件的顶层使用，不能在循环等代码块中使用

- 允许在hook内部使用

## 事件处理程序

- 如何传递事件处理程序

- `stopPropagation`

- `preventDefault`

### 事件处理程序和本机事件API之间的差异

- React 事件使用**驼峰命名**法定义

- `SyntheticEvent` React合成时间可能会被重置为`null`

- 合成时间对象是短暂的，不久后就会失效，这是处于性能原因

- `event.persist()`推荐写法，组织React将合成事件重置为`null`

### 概念

- 合成事件

- React 基于W3C规范，实现了一套事件机制，包括时间注册、事件合成、事件冒泡、事件派发。

- 事件委派

- React 事件代理机制：事件处理函数并不会绑定到真实的DOM节点上，而是把所有事件绑定到结构的最外层，使用一个**统一的事件监听器**，通过维护一个映射，来处理事件函数。

- 自动绑定

## 条件渲染和列表

- 条件

- `if`

- `&&`

- `三元运算符`

- 列表

- `map()`

- `key`

## ES5 +

- `let/cont/var`

- `()=>{}`

- `String`

- `string.includes(value)`

- `string.startsWith(value)`

- `string.endsWith(value)`

- `Array`

- `Array.of(3) // [3]`

- `Array.of(1,2,3) // [1,2,3]`

- `Array.from('Example') // ['E','x',...]`

- `Array.isArray(arr)`

- `[].find()`

- `[].findIndex()`

- `[].includes()`

- `Object`

- `Object.assign()`

- `Object.entries()`

- `Object.keys()`

- `Object.values()`

- `Object.freeze()`

- `Class`

- `constructor`

- `extends`

- `super`

- `解构赋值`

- `拓展运算符`

- `Modules`

- 命名导出 - `export const name`

- 默认导出 - `export default`

- `Promise`

- `async await`

## 元素/渲染

### 元素

- React 元素是React应用程序的最小构建块

- 由`React.createElement()`创建的不可变更对象

- React创建用户界面是声明式方式

- 优点：只需要描述状态和如何呈现内容

- 可读性和简单性比较高，不容易出错

### 组件

- 可以重复使用，隔离且独立

## CSS和样式

- 內联样式

- CSS Modules

- `classnames`

- CSS-in-JS

- `styled-components`

- `emotion`

- `styled-jsx`

## 高阶组件HOC

- 组件作为函数参数和返回值

- 源自高阶函数

- 可以更好的封装通用逻辑

- 比如 高阶组件可以从布局组件中提取逻辑

- Functions as a Child

- Render-Props

- 轻量级高阶组件

- 比高阶组件更加灵活和可读

### 实现高阶组件的方法

- 属性代理

- 反向继承