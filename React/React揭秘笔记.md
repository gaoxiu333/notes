# React 技术揭秘笔记

## 理念篇

- 快速响应

  - 影响快速响应的因素？

    - CPU瓶颈
      - `Q` : 遇到大计算量、设备性能不足 => 掉帧，卡顿
      - `A`：**时间切片** 
    - IO瓶颈：
      - `Q`：网络延迟
      - `A`：`Suspense` 、`useDeferredValue` 、同步更新 => 可中断的异步更新

    

### React 15 架构

- Reconciler（协调器）- 找出变化的组件
- Renderer（渲染器）- 将变化的组件渲染到页面

**协调器**

- 触发更新：`this.setState`、`this.forceUpdate`、`ReactDOM.render`
- 更新原理：递归调用
  - `render` 返回JSX转化为DOM对象（虚拟DOM）
  - 新的DOM和旧的DOM对比
  - 找出本次更新发生变化的DOM
  - 通知Rederer将变化的DOM渲染到页面上

**渲染器**

由于`React`支持跨平台，所以不同平台有不同的**Renderer**

- web端使用的是`react-dom` 
- 还有`react-native` 

> 递归更新缺点：
>
> 1. 组件层级过深，递归时间较长

### React 16 新架构

React 16 之后采用新架构

- Scheduler - 调度器
- Reconciler - 协调器
- Renderer - 渲染器

![更新流程](https://react.iamkasong.com/img/process.png)

> Reconciler 内部采用Fiber架构
>
> Scheduler和Reconciler是可中断的：
>
> 1. 有其他更高优先级任务时
> 2. 当前帧没有剩余时间

## Fiber 架构

这一段几乎就是 Fiber架构 文章中的内容，跟React技术揭秘无关

参考文章：[React Fiber Architecture（Fiber架构）](https://github.com/acdlite/react-fiber-architecture)

### 先决条件

- **React组件、元素和实例**
  
  - `Component` 
    - 是`class` 或者`function`声明的组件
    - 以`props`作为输入，元素树作为输出
  - `Element` 
    - 元素是一个简单的对象，它是不可变对象，也就是一旦创建就不会改变
    - React组件或者HTML元素的对象描述
  - `Instance` 
    - React处理的组件的引用
- **协调算法**
  
  - 旧版
    - 动机：为了有效跟新DOM，遍历新DOM和旧DOM对比更新的部分，算法复杂度为`O(n 3 )`
    - React 解决方案：启发式`O(n) ` 
      1. 不同类型的根元素，会从头开始构建新树
      2. 相同类型的DOM元素，更新属性
      3. 相同类型的组件，实例保持不变，更新props
      4. 递归子元素对比差异
      5. 使用key来标识一个元素，决定元素是重新生成还是copy一份
- **React 基本理论概念**

  - React理念包含：解决方案、增量步骤、算法优化、遗留代码、调试工具等
  - 纯函数 - 相同输入给出相同的输出
  - 抽象 - 抽象可重用部分，来复用
  - Composition(组合) - 将两个或者多个抽象组合成一个新的抽象
  - 状态 -  使用**不可变更数据模型**作为服务数据/业务逻辑状态
  - 记忆化 - 使用相同的值，不必再重复执行，创建一个函数的记忆版本来跟踪最后一个参数和最后一个结果
  - 列表 - 
  - 延续 - 减少样板代码，比如使用柯里化
  - StateMap - 提取和传递状态的逻辑转移到低级函数
  - MemoizationMap - 通过组合函数传递记忆缓存
  - 代数效应 - 分离副作用

- **React 设计原则**

  - 组合
  - 稳定

  - 实用大于优雅

  - 调度+响应式

### Fiber 架构正文

- *reconciliation*
  - React 使用算法将一棵树和另一棵树进行比较，以确定哪一部分需要更改。
- *update*
  - 用于渲染React应用程序，通常是`setState`更新导致的重新渲染

> React 的核心是重新渲染，但是重新渲染整个应用程序代价过高，所以React做了优化，这些优化的大部分是成为**协调**过程的一部分

### 协调和渲染

协调和渲染是分开的，以支持，**协调器**负责计算树的哪些部分已更改，然后**渲染器**使用该信息来实际更新渲染的应用程序；同时渲染器可以分为ReactDOM和React Native等渲染器。

### 调度

- seceduling - 确定何时执行工作的过程
- work - 任何必须执行的计算，通常指的`setState` 更新的结果。

### Scheduling（调度）

- 调度 - 确定何时执行工作的过程
- 工作 - 任何必须执行的计算，通常指的`setState` 更新的结果。

> 关键点
>
> - 在UI中，没有必要立即应用每个更新
> - 不同类型的更新具有不同的优先级，比如动画更新需要比数据存储更新更快的完成

#### Fiber

Fiber的目标主要是能够使React利用调度：

- 暂停工作稍后再回来重新执行
- 为不同类型的工作分配优先级
- 可以重用以前完成的工作
- 如果不再需要则终止工作

> 如果需完成以上的目标，需要尽可能的将任务分成颗粒度足够细的小任务。
>
> - 如果小任务是每个函数
> - 那么Fiber就是调用堆栈的重新实现

**实现细节**

将工作分解为多个单元，也就是最小单元，然后手动处理这些小单元，就像是处理函数调用堆栈一样。

- type&key
  - 以确定Fiber是否可以重复使用
- child&sibling
  - 描述Filber的递归结构
- pendingProps和memoizedProps
  - `pendingProps`在其执行开始时设置
  - `memoizedProps`在执行结束时设置。
  - pendingProps等于memoizedProps时，表示可以复用，不需要再执行一次计算
- pendingWorkPriority
  - 定义优先级
- alternate 
  - fiber 的实现细节
  
    - flush - 刷新到屏幕上
    - Work-in-progress - 尚未完成的fiber
  
    > 一个组件实例包含：当前的、已刷新的、正在进行的fiber

Fiber架构思想结束

## Fiber 的实现原理

fiber节点可以构成fiber树，那么fiber树和页面呈现的DOM树有什么关系，React又是如何更新DOM到呢？

- fiber结构
- 静态的数据结构
- 动态的工作单元

## Fiber 的工作原理

- 双缓存
  - 定义：在内存中构建并直接替换的技术叫做双缓存
  - 作用：React 使用双缓存来完成Fiber树的构建与替换--对应着DOM树的创建与更新

> 每当状态更新都会产生 workInProgress Fiber 树，当workInProgress构建完，current指向workInprogress，交给Renderer渲染到页面上。

fiber渲染分两种情况：

- 初始化时
- 状态更新时

<img src="/Users/xiu/code/notes/assets/fiber-brief-intro-dark.png" alt="img" style="zoom:80%;" />

---

**Fiber**

- **目标：**提高动画、布局和手势等领域的适用性。

- **增量渲染：**能将渲染工作分割成块，分布在多个帧上。
- **关键功能：**更新时暂停、中止或重用工作的能力；新的并发原语，给不同的更新分配优先级。

- 参考文章：[React Fiber Architecture（Fiber架构）](https://github.com/acdlite/react-fiber-architecture)
- 代数效应 - 函数式编程概念，用于将副作用从函数调用中分离，使函数关注点保持纯粹。
  - 应用：`React 纯函数`、`Hooks` 
- `Fiber` 的核心思想

## TODO

- [React 设计原则](https://facebook.github.io/react/contributing/design-principles.html)- 特别注意调度部分。它很好地解释了React Fiber 的*原因*。需要细读

- 调度程序如何找到下一个要执行的工作单元。
- 如何通过 Fiber 树跟踪和传播优先级。
- 调度程序如何知道何时暂停和恢复工作。
- 如何刷新工作并将其标记为完成。
- 副作用（例如生命周期方法）如何工作。
- 协程是什么以及如何使用它来实现上下文和布局等功能。

