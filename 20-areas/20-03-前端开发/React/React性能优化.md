---
title: React性能优化
jd_id: J00-20250512-0006
created: 2025-05-12 00:06
updated: 2025-05-12 00:06
type: note
status: draft
tags: []
---

# React 组件重渲染优化策略

## 关键概念

React 的重渲染是性能瓶颈的常见来源。识别和避免不必要的重渲染是提升性能的核心。

## 识别重渲染问题

### 诊断工具

- React DevTools Profiler - 确定哪些组件在重渲染
- `why-did-you-render` 库 - 追踪意外重渲染
- Chrome Performance 面板 - 测量渲染时间

### 识别模式

1. **Props 变更频繁** - 每次父组件渲染传递新引用
2. **Context 滥用** - 高频更新的值放在 Context
3. **State 设计不当** - 细粒度控制不足

## 优化策略层次

从简单到复杂，按需应用：

### 1. 组件设计优化

- **状态局部化** - 将状态下移到最小需要它的组件
- **组件拆分** - 将静态和动态内容分离为不同组件
- **子组件提升** - 使用 children 传递静态内容

```jsx
// 优化前
function ParentWithData() {
  const [data, setData] = useState(fetchData());
  return (
    <div>
      <ExpensiveHeader title="Dashboard" />
      <DataDisplay data={data} />
    </div>
  );
}

// 优化后
function Parent() {
  return (
    <div>
      <ExpensiveHeader title="Dashboard" />
      <DataContainer />
    </div>
  );
}

function DataContainer() {
  const [data, setData] = useState(fetchData());
  return <DataDisplay data={data} />;
}
```

2. 记忆化技术

React.memo - 组件级缓存
useMemo - 计算结果缓存
useCallback - 函数引用缓存

3. 引用稳定性技术

对象展平 - 避免传递嵌套对象
ID传递 - 传递ID而非整个对象
Selector模式 - 从store提取最小所需数据

4. 渲染优化技术

虚拟化列表 - 只渲染可见项
延迟加载 - 使用React.lazy和Suspense
批量更新 - 合并多个状态更新

实战案例分析
重型仪表盘性能优化
优化前问题:

50+组件同时渲染
每秒多次数据更新
图表重计算导致卡顿

优化步骤详解:

使用Performance Profiler确定瓶颈
应用记忆化策略减少重计算
实现时间切片更新数据
结果：渲染时间从230ms降至45ms

避坑指南

过度优化 - 提前优化是万恶之源
记忆化误用 - 比较成本高于计算成本
依赖数组错误 - 遗漏依赖导致过期数据

相关知识

[[React渲染机制深度解析]] - Fiber架构详解
[[状态管理与重渲染关系]] - 不同状态管理的重渲染影响
[[React组件设计原则]] - 从设计角度减少重渲染