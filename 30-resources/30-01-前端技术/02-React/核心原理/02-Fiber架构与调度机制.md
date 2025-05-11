---
title: Fiber架构与调度机制
jd_id: J30-20250511-0130
created: 2025-05-11 01:30
updated: 2025-05-11 01:30
type: note
status: active
schema: v1
tags: [topic/frontend/react, topic/frontend/fiber, topic/interview]
---

# Fiber架构与调度机制

## Fiber架构简介

Fiber是React 16引入的架构，它重新实现了React的核心算法，从基于栈的递归模型改为基于链表的迭代模型，使得渲染过程可以被中断和恢复，为异步渲染奠定了基础。

### 引入Fiber的背景

在React 16之前，React使用递归的方式创建虚拟DOM，递归过程不能中断，一旦开始必须走完整个流程。当组件树很大时，会导致以下问题：

1. **长任务阻塞**：JavaScript是单线程的，长时间的计算会阻塞主线程，导致界面卡顿
2. **无法中断和恢复**：一旦开始渲染，不能中断以处理更高优先级的任务
3. **无法细粒度地控制渲染优先级**：不能优先处理用户交互等高优先级任务

## Fiber的数据结构

Fiber是一种特殊的数据结构，它可以看作是对React元素的表示，每个Fiber节点对应一个组件。

### Fiber节点的主要属性

```javascript
{
  // 实例相关
  type: 'div', // 标识节点类型
  key: null,    // 唯一标识，用于reconciliation
  stateNode: null, // 指向实例节点（如DOM节点、组件实例）
  
  // Fiber节点关系
  return: Fiber,  // 指向父Fiber节点
  child: Fiber,   // 指向第一个子Fiber节点
  sibling: Fiber, // 指向兄弟Fiber节点
  
  // Effect相关
  effectTag: 'PLACEMENT', // 指示需要执行的DOM操作类型
  nextEffect: Fiber,      // 指向下一个需要处理Effect的Fiber节点
  firstEffect: Fiber,     // 指向第一个需要处理Effect的子Fiber节点
  lastEffect: Fiber,      // 指向最后一个需要处理Effect的子Fiber节点
  
  // 工作相关
  pendingProps: {},    // 新的待处理props
  memoizedProps: {},   // 已处理的props
  memoizedState: {},   // 组件状态
  updateQueue: {},     // 更新队列
  
  // 调度相关
  expirationTime: 0,   // 过期时间，用于优先级调度
  alternate: Fiber     // 指向"另一棵树"的对应节点
}
```

### 双缓存Fiber树

React维护两棵Fiber树：

1. **current树**：当前屏幕上显示的内容对应的Fiber树
2. **workInProgress树**：正在内存中构建的新Fiber树

当workInProgress树构建完成后，React会通过一个简单的指针切换，将workInProgress树变为current树，这个过程称为"commit"。

## Fiber的工作循环(工作流程)

Fiber将渲染过程分为两个阶段：

### 1. Render/Reconciliation阶段（可中断）

这个阶段执行的任务包括：

- 更新state和props
- 调用生命周期方法
- 找出DOM变化
- 调用渲染函数
- 构建workInProgress树

这个阶段是**异步**的，可以被中断和恢复，不会直接进行DOM操作。

```javascript
// 伪代码展示Fiber的工作循环
function workLoop(deadline) {
  let shouldYield = false;
  while (nextUnitOfWork && !shouldYield) {
    // 执行当前工作单元
    nextUnitOfWork = performUnitOfWork(nextUnitOfWork);
    // 检查是否需要让出控制权
    shouldYield = deadline.timeRemaining() < 1;
  }
  
  // 如果所有工作完成，提交更改
  if (!nextUnitOfWork && workInProgressRoot) {
    commitRoot();
  }
  
  // 安排下一次执行
  requestIdleCallback(workLoop);
}
```

### 2. Commit阶段（不可中断）

这个阶段执行的任务包括：

- 更新DOM
- 调用componentDidMount/componentDidUpdate等生命周期方法
- 执行所有useEffect/useLayoutEffect

这个阶段是**同步**的，一旦开始就必须完成所有工作，不能被中断。

## 调度机制详解

Fiber架构引入了优先级调度机制，使React能够：

1. **中断渲染**：将渲染工作分解为小单元
2. **为任务分配优先级**：先处理高优先级任务，如用户交互
3. **重用已完成的工作**：通过双缓存机制，不浪费已完成的工作
4. **丢弃不再需要的工作**：如果数据再次更新，可以丢弃处理中的过时工作

### 优先级分类

React内部实现了多种不同的优先级类型：

- **Immediate(-1)**：需要同步执行的任务
- **UserBlocking(250ms)**：用户交互的任务，如点击按钮
- **Normal(5s)**：普通任务，如网络请求
- **Low(10s)**：优先级较低的任务，如数据分析
- **Idle(无穷大)**：可闲置的任务，如预加载

### 调度器（Scheduler）

Scheduler是React的一个核心包，负责管理任务的优先级和执行时机。它实现了自己的时间切片机制，替代了浏览器的requestIdleCallback，确保跨浏览器兼容性。

```javascript
// 示例：如何使用scheduler
import { unstable_scheduleCallback, unstable_NormalPriority } from 'scheduler';

// 调度一个普通优先级的回调
unstable_scheduleCallback(
  unstable_NormalPriority,
  () => {
    console.log('This is a normal priority task');
  }
);
```

## Concurrent Mode（并发模式）

并发模式是基于Fiber架构的一个新功能，它使React能够：

1. 并发渲染多个版本的UI
2. 基于优先级中断和恢复渲染过程
3. 在后台准备新UI而不阻塞主线程
4. 丢弃不再需要的渲染

### useTransition和useDeferredValue

React 18提供了两个新Hook，它们利用了并发渲染的特性：

```javascript
// useTransition：标记低优先级状态更新
const [isPending, startTransition] = useTransition();

// 低优先级更新，可以被中断
startTransition(() => {
  setCount(count + 1);
});

// useDeferredValue：获取值的延迟版本
const deferredValue = useDeferredValue(value);
```

## 面试常见问题

1. **为什么React需要引入Fiber架构？**
   - 解决长时间同步渲染导致的页面卡顿问题
   - 支持异步渲染，实现可中断的渲染流程
   - 为并发模式提供基础架构支持

2. **Fiber架构如何解决性能问题？**
   - 将渲染工作分解为小单元，可以分时间片处理
   - 引入优先级机制，优先处理重要任务
   - 支持工作中断和恢复，提高响应性

3. **Fiber的双缓存机制是什么？**
   - 维护两棵树：current树和workInProgress树
   - 在内存中构建完整的workInProgress树
   - 构建完成后一次性提交到DOM，减少DOM操作

4. **什么是React的时间切片？**
   - 将渲染工作拆分成多个小任务
   - 在浏览器空闲时执行这些任务
   - 可以让出控制权处理用户交互等高优先级任务

## 相关链接

- [[../MOC-React核心原理|React核心原理]] - React核心原理索引
- [[01-虚拟DOM实现与原理|虚拟DOM实现与原理]] - 虚拟DOM的基础
- [[04-并发模式与服务端组件|并发模式与服务端组件]] - 更多并发模式相关内容 