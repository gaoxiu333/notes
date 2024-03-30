# React JSX

**JSX 是类 XML 语法的 ECMAScript 扩展**，完美地利用了 JavaScript 自带的语法和特性，并使用大家熟悉的 HTML 语法来创建虚拟元素。

####  原理

DOM 元素包含的信息其实只有三个：

- 标签名 `tagName`
- 属性 `props`
- 子元素 `children`

基于以上，可以使用 JavaScript 对象来描述所有能用 HTML 表示的 UI 信息；

React 把 JavaScript 的语法拓展了一下，让 JS 支持在 JS 里编写 HTML 标签结构的语法：

- 编译的过程会把类 HTML 的 JSX 结构转换成 JavaScript 的对象结构
- 是结构更加清晰
- 书写也方便很多

#### 语法

- 元素类型
  - 自定义组件**首字母必须大写**
  - **首字母小写**意味着是原生 HTML 标签
- 标签必须闭合
- 字符串转义
  - 可以防止部分 XSS 注入攻击
  - 导致部分字符需要转义
    - 借助 `dangerouslySetInnerHTML` 避免转义
    - 使用数组组装 `<div>{['cc ', <span>©</span>, ' 2015']}</div>`
    - 使用 UTF-8 或 Unicode 等
- 特殊属性
  - `class ` => `className`
  - `innerHTML` => `dangerouslySetInnerHTML`
  - `for` => `htmlfor`