# Vue3 基础

## 单文件组件SFC

Vue 的单文件组件 (即 `*.vue` 文件，英文 Single-File Component，简称 **SFC**)，使我们能够将一个 Vue 组件的模板、逻辑与样式封装在单个文件中；

每一个 `*.vue` 文件都由三种顶层语言块构成：`<template>`、`<script>` 和 `<style>`

### `<template>`:

- 每个 `*.vue` 文件最多可以包含一个顶层 `<template>` 块。

- `Fragment`: 碎片化节点， `template` 中只允许有多个根节点（Vue2只允许一个根节点）。

- 文本插值：`<span>Message: {{ msg }}</span>`

- 指令：

  - `v-bind`: 【缩写`:` 或者 `.` (当使用 `.prop` 修饰符)】动态的绑定一个或多个 attribute，也可以是组件的 prop。
  - `v-on`:【缩写`@`】给元素绑定事件监听器。

- 内置特殊元素

  - `<component>`: 用于渲染动态组件的"元组件";要实际渲染的实际组件由`is`决定。
  - `<slot>`: 表示模板中的插槽内容出口。
  - `<template>`: 
    1. 用在单文件组件的顶层;
    2. 作为占位符，使用`v-if`、`v-for`、`v-solt`等指令（因为同一个元素只能使用一个指令）。

- 内置Attributes

  - `key`:比较新旧节点列表时用于识别 vnode；当`key`变更时会强制替换元素，并不会复用（Vue进行了优化，渲染时通常会尽可能的复用相同类型的元素）。

    - 触发组件声明周期
    - 触发过渡动画

  - `ref`： 用于注册元素或子组件的引用。

  - `is`:  用于绑定动态组件，可以使用`vue:`前缀绑替换原生组件。

    ```html
    <!-- my-row-component 自定义组件会将 tr元素替换掉 -->
    <table>
      <tr is="vue:my-row-component"></tr>
    </table>
    ```

### `<script>`:

- 只能有一个`<script setup> `和`<script>`块

- `<script>` 和`<script setup> `可以组合使用

- 普通的 `<script>` 在有这些需要的情况下或许会被使用到：

  - 声明无法在 `<script setup>` 中声明的选项，例如 `inheritAttrs` 或插件的自定义选项。
  - 声明模块的具名导出 (named exports)。
  - 运行只需要在模块作用域执行一次的副作用，或是创建单例对象。
  
  ```vue
  <script>
  // 普通 <script>, 在模块作用域下执行 (仅一次,可以理解为只有在组件注册时执行？)
  runSideEffectOnce()
  
  // 声明额外的选项
  export default {
    inheritAttrs: false,
    customOptions: {}
  }
  </script>
  
  <script setup>
  // 在 setup() 作用域中执行 (对每个实例皆如此)
  </script>
  
  ```
  
  
  

### `<style>`:

- 每个 `*.vue` 文件可以包含多个 `<style>` 标签。

- `scoped`: 使用 `scoped` 后，父组件的样式将不会渗透到子组件中；
- 有三个伪类以应对不同的场景：
  - `:deep()`: 穿透影响子组件样式，在父组件中修改子组件样式时很有用；
  - `:slotted()`:插槽选择器，明确地将插槽内容作为选择器的目标，修改插槽内元素的样式；
  - `:global()`: 全局选择器，在`scoped`内定义全局样式，不受作用域影响。
- `v-bind()`：支持在style中动态绑定

```vue
<script setup>
const theme = reactive({
  color: 'red'
})
</script>
<style scoped>
p {
  color: v-bind('theme.color');   /*  v-bind 绑定  */
}
  /* 全局  */
:global(.red) {}
  /* 插槽 */
:slotted(div) {}
 /* 深度选择器 */
.a :deep(.b) {}
</style>
```

## setup

`setup()` 钩子是在组件中使用组合式 API 的入口。

- setup是一个函数
- 组件的数据、方法、生命周期等均在setup函数中配置。
- setup有两种返回值：
  1. `return`一个对象，对象属性会暴露给模板和其他的选项式 API 钩子
  2. `return`一个渲染函数，此渲染函数会代替`<template>`模版。
- `setup(props,context)`有两个参数：
  1. 参数一：`props`组件的传值
  2. 参数二：`context`执行上下文，类似选项式组件中的`this`

## `<script setup>`

### 为什么要用`<script setup>`?

- 更少的样板内容，更简洁的代码。
- 能够使用纯 TypeScript 声明 props 和自定义事件。
- 更好的运行时性能 (其模板会被编译成同一作用域内的渲染函数，避免了渲染上下文代理对象)。
- 更好的 IDE 类型推导性能 (减少了语言服务器从代码中抽取类型的工作)。

### 内置属性？

- `defineProps`: 用来声明`props`
- `defineEmits`：用来声明`emits`
- `defineExpose`：组件中要暴露出去的属性和方法，父组件通过模版引用访问暴露出来的属性和方法。

### 生命周期

- Vue3.0中可以继续使用Vue2.x中的生命周期钩子，但有有两个被更名：

  - `beforeDestroy`改名为 `beforeUnmount`
  - `destroyed`改名为 `unmounted`

- Vue3.0也提供了 Composition API 形式的生命周期钩子，与Vue2.x中钩子对应关系如下（部分）：

  - `beforeCreate`======>`setup()`

  - `created`==========>`setup()`

  - `beforeMount` ======>`onBeforeMount`

  - `mounted`==========>`onMounted`

  - `beforeUpdate`======>`onBeforeUpdate`

  - `updated` ==========>`onUpdated`

  - `beforeUnmount` ====>`onBeforeUnmount`

  - `unmounted` ========>`onUnmounted`

  - `errorCaptured` ====> `onErrorCaptured`

    

> 注意：setup比beforeCreate还早；<script setup> 中的代码会在每次组件实例被创建的时候执行。

### 响应式数据

#### `ref()`

- 接受基本类型，也可以是引用类型；返回响应式数据的引用对象（reference对象，简称ref对象）；
- 基本类型基于`defineProperty`原理，内部源码用的是class的get和set;
- 引用类型在内部借用`reactive()`；
- 使用时通过`.value`访问响应式数据；

#### `reactive()`

- 只接受对象，返回一个对象的响应式代理（proxy对象）；
- reactive定义的响应式数据是“深层次的”，嵌套属性同样是响应式的；
- 内部基于 ES6 的 Proxy 实现，通过代理对象操作源对象内部数据进行操作；

#### `reactive`对比`ref`

- 从定义数据角度对比：
  - ref用来定义：**基本类型数据**。
  - reactive用来定义：**对象（或数组）类型数据**。
  - 备注：ref也可以用来定义**对象（或数组）类型数据**, 它内部会自动通过`reactive`转为**代理对象**。
- 从原理角度对比：
  - ref通过`Object.defineProperty()`的`get`与`set`来实现响应式（数据劫持）。
  - reactive通过使用**Proxy**来实现响应式（数据劫持）, 并通过**Reflect**操作**源对象**内部的数据。
- 从使用角度对比：
  - ref定义的数据：操作数据**需要**`.value`，**可以重新赋值**，重新赋之后依然保持响应。
  - reactive定义的数据：操作数据与读取数据：**均不需要**`.value`；**不能重新赋值**，只能修改属性。

#### 浅响应

- `shallowRef`
- `shallowReactive`
- `shallowReadonly`

#### computed函数

与Vue2配置一样

- 只有`get`没有`set`时返回一个只读的响应式ref对象；
- 既有`get`也有`set`会创建一个可写的 ref 对象，可以用在`v-modal`指令上。

```vue
<script setup>
  const count = ref(1)
  const plusOne = computed({
    get: () => count.value + 1,
    set: (val) => {
      count.value = val - 1
    }
  })

  plusOne.value = 1
  console.log(count.value) // 0
</script>
```



#### watch函数

侦听一个或多个响应式数据源，并在数据源变化时调用所给的回调函数。

- 监听一个getter函数
- 监听一个reactive
- 监听一个ref

```vue
<script setup>
 // 侦听一个 getter 函数：
const state = reactive({ count: 0 })
watch(
  () => state.count,
  (count, prevCount) => { /* ... */},
  {
    immediate：true,// 默认：false, 定义时立即执行
    deep:true,//   默认：false，开启深度监听
    flush:'pre' | 'post' | 'sync', // 默认：pre,回调的触发时机:数据变更后，DOM更新前｜DOM更新后｜异步
  }
)
// 侦听一个 ref：
const count = ref(0)
watch(count, (count, prevCount) => {/* ... */})
// 监听多个源，参数是一个数组
watch([fooRef, barRef], ([foo, bar], [prevFoo, prevBar]) => {/* ... */})

</script>
```

#### watchEffect

立即执行函数，并在依赖更改时重新执行；依赖收集和响应式追踪和`computed`很像。

- vs`watch`:watch需要指明监听的响应式数据，监听的那个响应式数据修改时才会执行。
  - watch能明确监听哪一个值发生变化时执行；
  - watch能访问前一个值和当前值
- vs`computed`:都不需要指明响应式数据，函数体内有的响应数据都会被监听；
  - computed需要return一个值；
  - watch不需要return任何值；

```vue
<script setup>
//watchEffect 定义时会立即执行，回调内定义的响应数据发生变化也会执行。
watchEffect(()=>{
    const x1 = sum.value
    const x2 = person.age
    console.log('watchEffect配置的回调执行了')
})
</script>
```



## Hooks

- 什么是钩子（Hooks）呢？
  - 以函数形式抽离一些**可复用的方法**像钩子一样挂着，随时可以引入和调用，实现**高内聚低耦合**的目标；
  - Vue叫“组合式函数”(Composables) ，是一个利用 Vue 的组合式 API 来封装和复用**有状态逻辑**的函数。

- 命名约定
  - 组合式函数约定用驼峰命名法命名，并以“use”作为开头。
- 返回值使用ref，返回值被解构是可以保持响应。
  - 如果习惯`reactive`可以用`toRefs`转换为ref
- https://juejin.cn/post/6892017198450081800

## 组件

- 普通组件特性
- 异步组件
- 内置组件
  - Suspense
  - KeepAlive
  - Teleport
  - Transition
  - 

