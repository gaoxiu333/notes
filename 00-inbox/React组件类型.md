---
title: React组件类型
jd_id: J00-20250615-1922
created: 2025-06-15 19:22
updated: 2025-06-15 19:22
type: note
status: draft
tags: []
---

# React 组件类型

## 概述

了解各种 React 组件类型之间的细微差别对于做出明智的使用决策至关重要。

---

## `React.FC` VS `React.ElementType`

- `React.FC` 仅表示函数组件。
  > [!info]  
  > 在 React 18 之前，`React.FC` 包含隐式 `children` 属性，现在已经移除，却没多少人使用了。

```tsx
interface Props {
  title: string;
  children?: React.ReactNode;
}
// 使用 React.FC 定义函数组件
const ComWithFC: React.FC<Props> = ({ children }) => {
  return <div>{children}</div>;
};
// 类型推断
const ComWithoutFC = ({ children }: Props) => {
  return <div>{children}</div>;
};
```

- `React.ElementType` 适用于需要让组件支持自定义渲染标签或组件（如 `as` prop）的场景，让组件更灵活、可复用。
  > [!info]
  > 使用 `React.ElementType` 时，建议配合 `...rest` 透传 props，并注意类型安全（如为 `as` 指定合适的 props 类型约束）。

```tsx
type ButtonProps = {
  as?: React.ElementType;
  children: React.ReactNode;
};

const Button: React.FC<ButtonProps> = ({
  as: Component = 'button',
  children,
  ...rest
}) => {
  return <Component {...rest}>{children}</Component>;
};

// 用法
<Button>默认按钮</Button>
<Button as="a" href="#">链接按钮</Button>
<Button as={MyCustomComponent}>自定义组件</Button>
```

---

## `React.ReactNode` VS `React.ReactElement` VS `JSX.Element`

- `React.ReactElement`：表示具体的 React 元素，包括原生 HTML 标签、React 组件。
- `React.ReactNode`：更包容，除了 `React.ReactElement`，还包括数字、字符串、布尔值、null、undefined。
- `JSX.Element`：等价于 `React.ReactElement<any, any>`，是 JSX 的类型，而 `React.ReactElement` 是 React 的类型。

---

> [!tip]
> 建议在实际开发中优先使用类型推断，减少冗余类型声明。
