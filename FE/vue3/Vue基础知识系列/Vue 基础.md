## Vue 实例

- [createApp()](https://cn.vuejs.org/api/application.html#createapp)

创建一个应用实例，需要一个挂载的DOM元素。之后通过操作实例来初始化和挂载Vue，同时也可以定制化Vue应用实例。

## Vue 模版语法

Vue 使用基于 HTML 的模板语法，可以在模板中使用插值表达式、指令等来实现数据绑定和逻辑控制；能够声明式地将组件实例呈现到DOM上

- 底层转化为JavaScript代码

- 也就是虚拟DOM

- 也可以手写渲染函数

### 文本插值

- `{{...}}`

- `v-text`

- `v-html`

### JavaScript 表达式

- 仅支持表达式

- 支持函数调用

- [有限的全局对象列表](https://github.com/vuejs/core/blob/main/packages/shared/src/globalsAllowList.ts#L3)

### 绑定属性

- `v-bind`

- 简写`:`

### 指令

- `v-for`

- `v-if`

- `v-slot`

- `v-model`

- ...

### 事件绑定

- `v-on`

- `@`

- 修饰符

- `.stop` - 阻止冒泡

- `.prevent` - 阻止默认事件

- `.self` - 只处理自身

- `.capture` - 

- `.once` - 只触发一次

- `.passive` - 立即发生，并且防止包含阻止默认事件

> 修饰符可以组合使用，并且不同顺序的组合效果不同。

### 表单-双向绑定

- `v-model`

- 修饰符

- `v-model.lazy`

- `v-model.number`

- `v-model.trim`

### 内置元素

- `<componet>`

- 用于动态组件

- `<slot>`

- 插槽

- `<template>`

- 占位符

### Attributes

- 透传

- key

- ref

- is

**属性透传**

- 概念：当一个组件以单个根元素渲染时，组件的属性会自动穿透到根元素上

- 注意：`class`、`style`属性会自动合并

- 访问：`$attrs`、`useAttrs()`

- 手动继承：`v-bind:$attrs`

- 禁用：`defineOptions({inheritAttrs:false})`

**key**

对于Vue来说，key有助于性能优化，Vue始终销毁key已经不存在的元素，可以利用这一点可以做一些事件：

- 在适当的时候触发组件的生命周期（强制刷新）

- 触发过渡

**ref**

DOM元素或者子组件的引用；

## Vue 生命周期

- `beforCreate`

- `created`

- `beforeMount`

- `mounted`

- `beforeUpdate`

- `updated`

- `beforeDestroy`

- `destroyed`

- 父子组件执行顺序

- `parent beforeCreate`=>`parent created`=>`parent beforeMount`=> `child beforeCreate`=> `child created`=> `child beforeMount`=> `child mounted` => `parent mounted`

- `parent beforeDestroy`=> `child beforeDestroy`=>`child destroyed`=>`parent destroyed`

- 总体上是，父组件先创建，然后准备挂载父组件，这个时候子组件开始创建并且挂载，子组件挂载完之后挂载父组件。

- 卸载的思路也不多，父组件开始准备卸载，然后子组件先卸载，最后才是父组件完成卸载。

- 更新

## 组件

### 内置组件

- [](https://cn.vuejs.org/api/built-in-components.html#transition)

- [](https://cn.vuejs.org/api/built-in-components.html#transitiongroup)

- [](https://cn.vuejs.org/api/built-in-components.html#keepalive)

- [](https://cn.vuejs.org/api/built-in-components.html#teleport)

- [](https://cn.vuejs.org/api/built-in-components.html#suspense)

### 组件基础

- 定义组件

- 动态组件

- 异步组件

- 组件通信

- props

- 插槽

- Attributes

- 依赖注入

#### 定义组件

- [SFC语法定义](https://cn.vuejs.org/api/sfc-spec.html)

- `*.vue` 文件

- 由三种顶层语言块构成：`<template>`、`<script>` 和 `<style>`，以及一些其他的自定义块

- 选项式 API

- 组合式API

- `<script setup>`

- 注册组件

- 全局注册

- 局部注册

#### 动态组件

- **语法:** 

- `<commponent :is='...'>`

- **API**

- [](https://cn.vuejs.org/api/built-in-special-elements.html#component)

- [is](https://cn.vuejs.org/api/built-in-special-attributes.html#is)

- [](https://cn.vuejs.org/api/built-in-components.html#keepalive)

#### 异步组件

- `defineAsyncComponent`

- `import()`

- [更多配置，比如：加载和错误状态](https://cn.vuejs.org/api/general.html#defineasynccomponent)

> \- `defineAsyncComponent` - 接受一个Promise - `import()`- ES模块动态导入返回一个Promise - 刚好适配

#### 组件通信

- Props、Events、$emit、$parent、$children、Provide/Inject、Vuex 等）

- `provide/inject`

- 可以跨越组件层级

- 可以传递普通变量，也可以传递响应式数据

- Props

- `camelCase` 小驼峰

- `defineProps`

- 特性

- 单向数据流

- 父组件更新，新状态向下流往子组件，不会逆向传递，也就是不能在子组件中修改

#### 插槽

- 具名：`v-slot:header`、`#header`

- 动态具名：`v-slot:[header]`、`#[header]`

- [作用域插槽](https://cn.vuejs.org/guide/components/slots.html#scoped-slots) 

- 通过插槽传值

- 通过`#item="{解构}"`简写解构赋值的方式更方便

#### Attributes

属性透传

- 概念：当一个组件以单个根元素渲染时，组件的属性会自动穿透到根元素上

- 注意：`class`、`style`属性会自动合并

- 访问：`$attrs`、`useAttrs()`

- 手动继承：`v-bind:$attrs`

- 禁用：`defineOptions({inheritAttrs:false})`

## Composition API

Composition API 提供了一组函数，可以让开发者按功能逻辑来组织代码，而不是按照选项对象的顺序；`setup`函数是核心，它在组件实例创建之前调用，可以在setup中定义一些列组件的状态，计算属性，方法和生命周期钩子。

- `reactive()`创建响应式对象

- `ref()`创建普通引用类型数据

- `computed()`创建计算属性

- `watch()`监听响应式数据的变化

- `onMounted()`、`onUpdated()`、`onUnmounted()`生命周期钩子

- `toRefs()`、`toRef()`、`watchEffect()`辅助函数

### composition API 和选项式的区别

- 代码组织方式、

- vue2：组件逻辑通过一个选项对象来组织

- vue3：组件逻辑在setup函数中定义

- 逻辑复用和组合

- vue2：复用逻辑主要借助mixins等方式，但是无法定位逻辑所在组件

- vue3：更加灵活，可以将相关逻辑放在一起，以函数的形式进行组合复用，提高了代码的可读性和可维护性

- 可读性和可维护性

- TypeScript 支持

## 响应式系统

### 响应式核心

**创建**

- `ref()`

- `reactive()`

- `shallowRef()`

- `shallowReactive()`

**监听**

- `computed()`

- `watch()`

- `watchEffect()`

**工具**

- `isRef()`

- `isReactive()`

- `isProxy()`

- `unref()`

- `toRef()`

- `toValue()`

- `toRefs()`

## 插件

插件是一种给Vue添加全局功能的工具代码。简单来说，就是给**Vue实例**添加全局属性、变量或者方法。

### 编写一个插件

- 插件是一个对象

- 对象必须拥有`install`方法

**示例**

```
// plugins/example.js
export default{
  install:(app,options)=>{
    // 插件逻辑
    // app.config.globalPreperties 
  }
}
```

### 作用

- 拓展Vue实例全局属性

- `app.config.globalProperties`

- [配合TypeScript拓展全局属性](https://cn.vuejs.org/guide/typescript/options-api.html#augmenting-global-properties)

- 注册全局组件和全局指令

- `app.component()`

- `app.directive()`

- 注册全局供应

- `app.provide()`