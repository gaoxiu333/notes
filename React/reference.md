# React 参考文档

> 来源：https://react.dev/reference/react

本文档提供了 React 的详细参考信息。如果你是 React 新手，建议先访问 [Learn](https://react.dev/learn) 部分。

React 参考文档分为以下几个功能子部分：

## React 核心

提供 React 的编程功能特性：

- [Hooks](https://react.dev/reference/react/hooks) - 在组件中使用不同的 React 特性
- [Components](https://react.dev/reference/react/components) - 可在 JSX 中使用的内置组件
- [APIs](https://react.dev/reference/react/apis) - 用于定义组件的 API
- [Directives](https://react.dev/reference/rsc/directives) - 为兼容 React Server Components 的打包工具提供指令

## React DOM 

React-dom 包含仅支持 Web 应用程序（在浏览器 DOM 环境中运行）的功能。这部分分为以下几个方面：

- [Hooks](https://react.dev/reference/react-dom/hooks) - 用于在浏览器 DOM 环境中运行的 Web 应用程序的 Hooks
- [Components](https://react.dev/reference/react-dom/components) - React 支持所有浏览器内置的 HTML 和 SVG 组件
- [APIs](https://react.dev/reference/react-dom) - react-dom 包含仅在 Web 应用程序中支持的方法
- [Client APIs](https://react.dev/reference/react-dom/client) - react-dom/client API 允许你在客户端（浏览器中）渲染 React 组件
- [Server APIs](https://react.dev/reference/react-dom/server) - react-dom/server API 允许你在服务器端将 React 组件渲染为 HTML

## React 规则

React 有其独特的范式或规则，用于以易于理解的方式表达模式，并产出高质量的应用程序：

- [Components and Hooks must be pure](https://react.dev/reference/rules/components-and-hooks-must-be-pure) - 纯函数使你的代码更容易理解和调试，并允许 React 自动正确地优化你的组件和 hooks
- [React calls Components and Hooks](https://react.dev/reference/rules/react-calls-components-and-hooks) - React 负责在必要时渲染组件和 hooks，以优化用户体验
- [Rules of Hooks](https://react.dev/reference/rules/rules-of-hooks) - Hooks 使用 JavaScript 函数定义，但它们代表一种特殊类型的可重用 UI 逻辑，对它们的调用位置有限制

## 旧版 API

- [Legacy APIs](https://react.dev/reference/react/legacy) - 从 react 包导出，但不推荐在新代码中使用的 API
