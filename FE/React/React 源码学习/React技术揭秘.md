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

    

### React15 架构

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



> 递归更新缺点：
>
> 1. 组件层级过深，递归时间较长

### 新架构

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

## Fiber 心智模型

- 代数效应 - 函数式编程概念，用于讲副作用从函数调用中分离。

