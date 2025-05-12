# React生态系统

## React核心
- [[React渲染机制深度解析]] - 调和算法与Fiber架构
- [[Hooks内部实现与最佳实践]] - Hooks工作原理详解
- [[状态管理策略]] - 从Context到状态管理库
- [[React性能优化完全指南]] - 有效的性能优化策略

## 生态组件
- [[React Router深入]] - 路由实现与高级技巧
- [[React状态管理解析]] - Redux/Zustand/Jotai/Recoil对比
- [[React表单解决方案]] - 复杂表单处理策略
- [[React查询方案]] - SWR/React-Query数据获取

## 架构模式
- [[React应用架构模式]] - 大型应用组织策略
- [[组件设计原则]] - 可维护组件API设计
- [[数据流设计模式]] - 单向数据流与状态管理
- [[React性能架构]] - 性能优先的架构决策

## 新一代React
- [[React Server Components]] - RSC工作原理与实践
- [[React并发模式]] - 并发特性与应用
- [[React挂起与流式渲染]] - Suspense最佳实践
- [[React生态未来展望]] - React新特性与方向


# MOC-React生态

## React核心概念
- [[React组件模型详解]] - 类组件与函数组件完整对比
- [[React渲染机制与调和过程]] - 虚拟DOM与Fiber架构
- [[React生命周期完全指南]] - 各阶段钩子及最佳实践
- [[React状态管理基础]] - useState与类组件state对比
- [[React Context API深度应用]] - 上下文机制与性能考量
- [[React事件系统]] - 合成事件与原生事件交互

## React Hooks深度
- [[React Hooks工作原理]] - Hooks内部实现机制
- [[useState与useReducer最佳实践]] - 状态逻辑组织模式
- [[useEffect完全指南]] - 依赖数组、清理与常见陷阱
- [[useCallback与useMemo性能优化]] - 引用稳定性保障
- [[自定义Hooks设计模式]] - 逻辑复用与组合模式
- [[React Hooks测试策略]] - 钩子函数的有效测试方法
- [[useContext性能优化模式]] - Context消费者优化策略
- [[useRef高级应用场景]] - DOM引用与持久化数据存储

## 状态管理生态
- [[React状态管理方案对比]] - Redux/Zustand/Jotai/Recoil
- [[Redux架构与最佳实践]] - 单向数据流完整实现
- [[Redux中间件机制详解]] - 中间件原理与自定义实现
- [[Redux Toolkit现代实践]] - 简化Redux的最佳实践
- [[React Query数据获取策略]] - 服务端状态管理最佳实践
- [[Zustand轻量状态方案]] - 简单高效的状态管理
- [[Recoil原子化状态管理]] - 基于原子模型的状态方案
- [[Context + useReducer模式]] - 轻量级Redux替代方案

## React性能优化
- [[React组件渲染优化指南]] - 避免不必要渲染
- [[React.memo与shouldComponentUpdate]] - 组件级缓存策略
- [[React代码分割最佳实践]] - 路由级与组件级代码分割
- [[React列表渲染优化]] - 大数据列表高效渲染策略
- [[React DevTools性能分析]] - 使用开发工具诊断性能问题
- [[React并发渲染模式]] - Concurrent Mode实践指南
- [[useTransition与useDeferredValue]] - 优先级控制API应用
- [[React长任务优化策略]] - 避免主线程阻塞的方法

## 组件设计与模式
- [[React组件设计原则]] - 可维护组件设计指南
- [[React组件组合模式]] - 优于继承的组合设计
- [[React高阶组件(HOC)模式]] - HOC设计与应用场景
- [[Render Props设计模式]] - 渲染属性模式最佳实践
- [[React复合组件模式]] - Compound Components实现
- [[受控与非受控组件]] - 两种表单组件设计对比
- [[React错误边界设计]] - 优雅降级与错误处理
- [[React组件懒加载策略]] - Suspense与延迟加载

## 路由与导航
- [[React Router完全指南]] - v6路由库深度应用
- [[React Router数据管理]] - 路由与状态数据集成
- [[嵌套路由最佳实践]] - 复杂应用路由结构设计
- [[React Router授权控制]] - 基于角色的路由访问控制
- [[动态路由与代码分割]] - 按路由优化加载策略
- [[React路由状态持久化]] - 会话导航状态保持
- [[TanStack Router探索]] - 类型安全路由方案尝试
- [[单页应用与SEO]] - SPA路由的搜索引擎优化

## 服务端渲染与SSG
- [[Next.js应用架构]] - 服务端渲染框架全解析
- [[Next.js数据获取策略]] - SSR/SSG/ISR数据加载模式
- [[React Server Components]] - RSC工作原理与最佳实践
- [[服务端状态同构方案]] - 客户端服务端状态一致性
- [[静态站点生成优化]] - Next.js与Gatsby SSG策略
- [[增量静态生成(ISR)]] - 动静结合的渲染策略
- [[Edge渲染模式]] - 边缘计算渲染方案
- [[Streaming SSR]] - 流式服务端渲染技术

## React测试策略
- [[React测试库最佳实践]] - 组件测试基础与进阶
- [[React单元测试设计]] - 可测试组件的设计原则
- [[React集成测试策略]] - 组件交互与集成测试
- [[React Mock服务测试]] - API依赖的模拟测试
- [[React E2E测试方案]] - 端到端测试实现策略
- [[React性能测试方法]] - 性能回归测试实践
- [[测试驱动开发React]] - TDD在React开发中的应用
- [[Storybook驱动开发]] - 组件文档与可视化测试

## 样式与UI集成
- [[React样式方案对比]] - CSS-in-JS/CSS Modules/Tailwind
- [[Styled-components深入]] - CSS-in-JS主流方案
- [[Tailwind CSS与React集成]] - 原子化CSS最佳实践
- [[React中的CSS Modules]] - 模块化CSS实现细节
- [[主题系统设计与实现]] - 多主题支持与动态主题
- [[组件库集成策略]] - Material-UI/Ant Design最佳实践
- [[动态样式与动画]] - React应用中的动效实现
- [[React中的样式架构]] - 大型应用CSS组织方案

## React生态工具
- [[Create React App替代方案]] - Vite/Next.js/自定义配置
- [[React开发环境优化]] - 开发体验与工具效率提升
- [[React DevTools高级调试]] - 高效调试React应用
- [[状态调试与可视化]] - Redux DevTools与状态跟踪
- [[类型安全React开发]] - TypeScript与React最佳实践
- [[React文档生成工具]] - API文档与组件文档自动化
- [[React性能监控方案]] - 生产环境性能跟踪
- [[可视化构建工具]] - 低代码平台与React集成

## 高级与实验特性
- [[React 19新特性展望]] - 最新React版本变化与影响
- [[React并发特性应用]] - Suspense与Concurrent模式
- [[服务端组件与客户端组件]] - React组件新模型
- [[React编译优化探索]] - 编译时优化与运行时优化
- [[React Native与React共享]] - 跨平台代码共享策略
- [[React新一代状态管理]] - Signals与细粒度更新
- [[React与WebAssembly集成]] - WASM性能提升方案
- [[React未来发展趋势]] - 官方路线图与社区动向