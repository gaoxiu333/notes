# 源码学习-react-reconciler包

### **掌握 Fiber 架构和协调过程**

负责在虚拟DOM与真实DOM之间建立映射关系，它的核心目标是高效的更新 UI

- **目标**：理解 React 的核心协调算法（Diffing 过程、Fiber 架构）。
- **关键点**：
    - Fiber 节点的数据结构（`alternate`、`effectTag`、`updateQueue` 等）。
    - 协调过程的工作循环（`beginWork`/`completeWork`）。
    - 副作用（Effects）链表和提交阶段（Render 和 Commit 分离）。
    - 双缓冲机制和更新批处理。
- **为什么此时学**：
    - 这是 React 最复杂的部分，需结合调度器和核心 API 的知识。
- **理解**
    - 实现了协调算法，也就是Fiber架构的核心。协调器负责组件的更新调度，虚拟DOM的diff算法，以及将变化应用到实际的渲染环境，协调器需要与scheduler包协作，安排任务的优先级和执行时机。

## API

**源码**

- 出口：[packages/react-reconciler/src/ReactFiberReconciler.js](https://github.com/facebook/react/blob/v18.2.0/packages/react-reconciler/src/ReactFiberReconciler.js)

**提供的核心方法：**

- 容器管理
    - **`createContainer`**：创建根容器（新旧协调器入口）
    - **`createHydrationContainer`**：服务端渲染（SSR）激活容器
    - **`updateContainer`**：触发容器更新（调度更新的核心入口）
    - **`getPublicRootInstance`**：获取根节点实例
- 更新调度控制
    - **`batchedUpdates`**：批量更新（合并多个 setState）
    - **`deferredUpdates`**：延迟更新（低优先级任务）
    - **`discreteUpdates`**：离散更新（高优先级用户交互）
    - **`flushSync`**：强制同步刷新（穿透优先级直接更新）
    - **`flushControlled`**：受控更新冲刷（用于 Suspense 等场景）
    - **`runWithPriority`**：动态调整更新优先级
- Hydration 水合机制
    - **`attempt*Hydration` 系列**：
        - `attemptSynchronousHydration`（同步激活）
        - `attemptDiscreteHydration`（离散优先级激活）
        - `attemptContinuousHydration`（连续激活）
        - `attemptHydrationAtCurrentPriority`（当前优先级激活）
- DOM 实例操作
    - **`findHostInstance*` 系列**：
        - `findHostInstance`：查找宿主 DOM 节点
        - `findHostInstanceWithNoPortals`：忽略 Portal 的节点查找
        - `findHostInstanceWithWarning`：带警告的查找（开发模式）
    - **`createPortal`**：创建跨 DOM 层级的 Portal 节点
- 副作用处理和错误处理
    - **`flushPassiveEffects`**：刷新被动效果（处理 useEffect）
    - **`shouldError`/`shouldSuspend`**：错误边界控制（决定组件是否抛出错误/挂起
- 渲染状态控制
    - **`isAlreadyRendering`**：检测当前是否处于渲染流程中
    - **`getCurrentUpdatePriority`**：获取当前更新优先级
- 开发者工具集成
    - **`injectIntoDevTools`**：注入自定义渲染器到 React DevTools

**架构意义**

- 虚拟 DOM 差异计算（Diff算法）
- 更新任务调度（与 Scheduler 交互）
- 渲染流程控制（同步/异步/批量更新）
- 跨平台渲染基础-通过抽象借口支持DOM/Native等不同渲染器

**协调组件数的调度**

- 生成新的 Fiber 树
- 渲染阶段
- 提交阶段
- 任务切片供 scheduler 控制
- [优先级的官方解读](https://github.com/facebook/react/tree/v18.2.0/packages/react-reconciler#getcurrenteventpriority)
    - 离散事件
    - 连续事件
    - 其他事件

## 留下的疑问

### 核心工作流程

- Render 阶段（调和阶段）
- Commit 阶段（提交阶段）
- Layout 阶段（布局阶段）

### 核心方法

**Render 阶段**

- `beginWork`
- `completeWork`

**Commit 阶段**

- `commitBefroeMutationEffects`
- `commitMutationEffects`
- `commitLayoutEffects`

### Fiber

`fiber` 是最小单元

```jsx
{
  tag,                // 节点类型 (FunctionComponent, ClassComponent, HostComponent 等)
  key,                // 唯一标识
  type,               // 节点具体类型，如组件函数、HTML 元素类型
  stateNode,          // 与当前 Fiber 关联的实例或 DOM 节点
  child,              // 子节点 Fiber
  sibling,            // 兄弟节点 Fiber
  return,             // 父节点 Fiber
  alternate,          // 当前 Fiber 的旧版本
  updateQueue,        // 保存节点状态更新的队列
  memoizedProps,      // 节点最新的 props
  memoizedState,      // 节点最新的 state
  flags,              // 标记当前节点需要执行的更新操作
}
```

- 分别指向兄弟和子元素
- 双缓存机制
- 更新队列
- 副作用
- 优先级调度

### 总结

- 核心流程
    - Render 阶段：计算 fiber 树的更新
    - Commit 阶段：将更新应用到真实 DOM
- 关键机制
    - Fiber 数据结构，支持细粒度控制和高效更新
    - Lane 模型，改进优先级管理，支持并发渲染
- 模块整合
    - 配合 scheduler 提供调度能力
    - 使用 flags 和 updateQueue 管理状态和副作用

## 问题

怎么做到的不阻塞，哪些任务使用的是立即执行异步，哪些使用的是不重要的异步，哪些可以可中断，哪些不能可中断？