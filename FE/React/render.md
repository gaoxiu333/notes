# Render 函数

`render` 函数当且仅当下列两种情况才会被调用：

- 组件初始化
- 组件的 `props` 或 `state` 发生变化
  - `props` 在父组件被修改时
  - 父组件重新渲染时 `props` 的引用地址也会变化，导致 `props` 发生变化