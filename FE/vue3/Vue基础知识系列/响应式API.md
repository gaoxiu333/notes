# 响应式API

选项式 API 会用 `data` 选项来声明组件的响应式状态；

组合式 API 需要用到`reactive()`、`ref()`等函数创建响应式数据。

## `reactive()`

创建一个响应式对象或数组。

**描述：**

- 基于`ES6 Proxy`实现，对响应数据对象属性的访问与更改操作。
- 默认创建深层响应式数据，会影响所有嵌套的属性。

```js
import { reactive } from 'vue'

const state = reactive({ count: 0 })
```

**局限性：**

- 仅对对象类型有效，对基础类型无效；
- 需要保持引用，不能重新被赋值；
- 响应式对象属性不能赋值给本地变量，会失去响应式：

```js
const state = reactive({ count: 0 })

// 失去响应性连接
let n = state.count

// count 也和 state.count 失去了响应性连接
let { count } = state

// state.count 赋值给函数参数，失去响应
callSomeFunction(state.count)
```

## `ref()`

创建可以使用任何值类型的响应式数据。

**描述：**

- 返回的响应式数据会包装在`.value`属性里
- **基本类型**使用`defineProperty`劫持，实现响应式数据
- **引用类型**内部调用`reactive`转换为响应式数据

```js
const count = ref(0)

console.log(count) // { value: 0 }
console.log(count.value) // 0

count.value++
console.log(count.value) // 1
```

**.value解包**

`ref()`创建的响应式数据，需要访问`.value`属性，有以下几个场景会自动解包，不需要`.value`

- 在`<template>`模版作为顶层属性时；
- 在`<template>`模版中不是顶层属性：
  - 在文本插值语法中（即一个 `{{ }}` 符号）
  - 在`JavaScript`表达式中**不会解包**
- 在响应式对象中，作为响应式对象的一个属性值时，并且相互关联
  - 数组和`Map`类型的对象除外
- 作为`watch`的监听源时

在`<template>`中

```vue
<script setup>
import { ref } from 'vue'

const count = ref(0)
const object = { foo: ref(1) }

function increment() {
  count.value++
}
</script>

<template>
  <button @click="increment">
    {{ count }} <!--【自动解包】 无需 .value -->
  </button>
	<span>{{ object.foo }}</span><!--【自动解包】 -->
	<span>{{ object.foo + 1 }}</span><!--【不能自动解包】 -->
</template>

```

作为响应式对象属性

```js
const count = ref(0)
const state = reactive({
  count
})
//【自动解包】 无需 .value
console.log(state.count) // 0 

state.count = 1
console.log(count.value) // 1

const books = reactive([ref('Vue 3 Guide')])
//【不能自动解包】 这里需要 .value
console.log(books[0].value)

```

## `ref()` VS `reactive()`

ref既然可以创建所有类型的影响式数据，为什么还有reactive？

- `reactive()`访问属性时，不需要`.value`
- `reactive()`适合将一组相关联的状态集合，避免`.value`造成的心智负担
- `ref()`更加灵活，可以定所有类型的响应式数据

结合以上几点，到底该如何取舍，我觉得取决于编程习惯。

## `computed()`

接收一个`getter`函数，并且返回一个响应式 ref 对象

- 和`ref`创建的响应式数据一样，通过`.value`访问响应式数据
- 只有当`getter`函数内的响应式依赖更新时，计算属性才会重新执行；

创建一个只读计算属性：

```js
const count = ref(1)
const plusOne = computed(() => count.value + 1)

console.log(plusOne.value) // 2

plusOne.value++ // 错误

```

创建一个可写的计算属性：

```js
const count = ref(1)
const plusOne = computed(
{
  get: () => count.value + 1,
  set: (val) => {
    count.value = val - 1
  }
},
{
  onTrack(e) {
    // 被追踪为依赖时触发（被访问读取时）
  },
  onTrigger(e) {
    // 当被更改时触发（被设置新的值）
  }
)

plusOne.value = 1
console.log(count.value) // 0
```

## `watch()`

在每次响应式状态发生变化时触发回调函数：

**描述：**

- 可以监听一个返回函数
- 可以监听一个响应式对象
- 或者是以上两种类型的合成数组

**参数：**

接收三个参数：`source`,`callback`,`options`

- source： 响应式数据或者返回函数
- callback：回调函数
- options：一个可选的配置项目
  - **`immediate`**：在侦听器创建时立即触发回调。第一次调用时旧值是 `undefined`。
  - **`deep`**：如果源是对象，强制深层遍历，以便在深层级变更时触发回调。
  - **`flush`**： 调整回调函数的刷新时机；默认`pre`将会使侦听器延迟到组件渲染之后再执行。
  - **`onTrack / onTrigger`**：调试侦听器的依赖。


> 注意：
>
> - 监听源是一个对象时；默认开始深层监听
> - 监听源是一个返回函数时，需要显示的加上`deep:true`进行深层监听

监听一个简单类型的值

```js
const state = reactive({ count: 0 })
watch(
  () => state.count, // 不能直接监听 state.count
  (count, prevCount) => {
    /* ... */
  }
)
// 或者
const count = ref(0)
watch(count, (count, prevCount) => {
  /* ... */
})
```

监听一个引用类型

```js
const state = reactive({ count: 0 })
// 直接监听，默认开启深层监听
watch(state,   (newValue, oldValue) => {
    // 注意：`newValue` 此处和 `oldValue` 是相等的
 })
// 需要显示 指定 deep:true 开启深层监听
watch(
  () => state,
  (newValue, oldValue) => {
    // newValue === oldValue
  },
  { deep: true }
)
```

停止监听和清理副作用

```js
const stop = watch(id, async (newId, oldId, onCleanup) => {
  const { response, cancel } = doAsyncWork(newId)
  // 当 `id` 变化时，`cancel` 将被调用，
  // 取消之前的未完成的请求
  onCleanup(cancel)
  data.value = await response
})
// 当已不再需要该侦听器时：
stop()
```

## `watchEffect()`

立即执行副作用函数（回调函数），副作用函数内依赖放生变化时，重新执行。

**描述：**

- 不需要指定监听源
- 和`computed()`类似，依赖修改时立即执行。
- 不能对比变化前后对值，需要的对比的话建议使用`watch()`指明监听源

```js
//watchEffect 定义时会立即执行，回调内定义的响应数据发生变化也会执行。
watchEffect(()=>{
    const x1 = sum.value
    const x2 = person.age
    console.log('watchEffect配置的回调执行了')
})
```

## `watchPostEffect()`

`watchEffect()`使用 `flush: 'post'` 选项时的别名；将会使侦听器延迟到组件渲染之后再执行。

## `watchSyncEffect()`

`watchEffect()`使用 `flush: 'sync'` 选项时的别名；响应式依赖发生改变时立即触发侦听器。

## `customRef()`

创建一个自定义的 响应式数据，显式声明对其依赖追踪和更新触发的控制方式。

**示例**

创建一个防抖 ref，即只在最近一次 set 调用后的一段固定间隔后再调用：

```js
import { customRef } from 'vue'

export function useDebouncedRef(value, delay = 200) {
  let timeout
  return customRef((track, trigger) => {
    return {
      get() {
        track()
        return value
      },
      set(newValue) {
        clearTimeout(timeout)
        timeout = setTimeout(() => {
          value = newValue
          trigger()
        }, delay)
      }
    }
  })
}
```

## `toRaw()`

根据一个 Vue 创建的代理返回其原始对象；可以返回一下代理对象对应的原始对象：

- `reactive()`
- `readonly()`
- `shallowReactive()`
- `shallowReadonly()`

```js
const foo = {}
const reactiveFoo = reactive(foo)

console.log(toRaw(reactiveFoo) === foo) // true
```

## `unref()`

如果参数是 ref，则返回内部值，否则返回参数本身。这是 `val = isRef(val) ? val.value : val` 计算的一个语法糖。

```js
const count = ref(1)
count.value === unref(count) // true
```

## `toRef()`

基于一个响应式对象，创建一个关联的响应式数据。改变新创建的响应式数据，会影响原来的响应式对象。

```js
const state = reactive({
  foo: 1,
  bar: 2
})

const fooRef = toRef(state, 'foo')

// 更改该 ref 会更新源属性
fooRef.value++
console.log(state.foo) // 2

// 更改源属性也会更新该 ref
state.foo++
console.log(fooRef.value) // 3
```

## `toRefs()`

将一个响应式对象转换为一个普通对象，普通对象的属性都通过`toRef()`创建响应式数据关联源数据。

```js
function useFeatureX() {
  const state = reactive({
    foo: 1,
    bar: 2
  })

  // 在返回时都转为 ref
  return toRefs(state)
}

// 可以解构而不会失去响应性
const { foo, bar } = useFeatureX()
```

## `其他响应式API`

- `shallowRef()`：`ref()`的浅层作用形式。
- `shallowReactive()`：`reactive()`的浅层作用形式。
- `readonly()`：返回一个原值的只读代理。
- `shallowReadonly()`：`readonly()`的浅层作用形式。
- `triggerRef()`：强制触发依赖于一个浅层响应数据的副作用。
- `markRaw()`：将一个对象标记为不可被转为代理。返回该对象本身。
- `effectScope()`：创建一个响应式作用域。
- `getCurrentScope()`：获取当前活跃的作用域。
- `onScopeDispose()`：相关的 effect 作用域停止时会调用这个回调函数，通常用在hooks中，每个组件也可以被认为是 effect 作用域，组件被注销，作用域被停止。
- `isRef()`：检查值是否是一个ref
- `isProxy()`：检查是否是一个代理对象。
- `isProxy()`：检查是否由`reactive()`或`shallowReactive()`创建。
- `isReadonly()`：检查是否由`readonly()`、`shallowReadonly()`或没有`set`的`computed`

