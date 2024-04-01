# Pinia

Pinia的设计目的是拥有组合式API的Vue状态管理库，同时支持Vue2和Vue3

### 为什么使用Pinia

* Pinia是Vue的专属状态管理库，可以跨组件或页面共享状态

* 浏览器Devtools支持，可以追踪actions、mutations时间线

* 支持热更新，保持当前State来修改State使页面发生实时变化

* 更好的TypeScript支持

* 支持服务端渲染

### 和Vuex的区别

* mutation 已经被废弃，感觉极其冗余所以废弃

* 原生支持TypeScript

* 模块化由嵌套的方式，改为扁平化管理

* 不再需要命名模块

### Store

* Store是一个保存状态和业务逻辑的尸体，它承载着全局状态。

* 三个核心概念

  * state -> data

  * getter -> computed 

  * action -> methods

* 什么时候使用

  * 可以在整个应用中访问的数据

  * 避免哪些原本可以在组件中保存的本地数据

**定义Store**

* `defineStore`

  * 参数一：必填的唯一id

  * 返回值赋值给一个`useXxx`开头的变量，这个是约定俗成的。

* 两种定义方式

  * 选项式

  * 组合式

    * `ref()` 就是 `state` 属性

    * `computed()` 就是 `getters`

    * `function()` 就是 `actions`

* 使用

  * `storeToRef()`用来解构保持响应式

### APIs

* `defineStore`

* State

  * `$reset()`，组合式中，自己创建！

  * `$patch()`批量修改

  * `$subscribe()`

* Getter

  * 直接返回state

  * 返回Getter->借助`this`

  * 传参

  * 访问其他State->直接在函数体内调用

* Action

  * 比较简单，就想调用方法一样

