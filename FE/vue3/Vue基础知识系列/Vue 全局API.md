# 全局API

在 Vue 3 中，全局和内部 API 都经过了重构，并考虑到了 tree-shaking 的支持，全局 API 现在通过具名导出进行访问。

- `createApp()`
- `version`
- `nextTick()`
- `defineComponent()`
- `defineAsyncComponent()`
- `defineCustomElement()`
- `mergeProps()`
- 

## createApp()

每个 Vue 应用都是通过 `createApp`函数创建一个新的 **应用实例**：

```js
import { createApp } from 'vue'

const app = createApp({  /* 根组件选项 */})
```

#### 参数：

接收两个参数；第一个参数是根组件。第二个参数可选，它是要传递给根组件的 props。

#### 示例

使用一个导入的组件

```js
import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)
```

使用组件模版对象

```html
<div id="app">
  <button @click="count++">{{ count }}</button>
</div>
```

```js
import { createApp } from 'vue'

const app = createApp({
  props: ['username'],
    data() {
      return {
        count: 0
       }
    },
    methods:{},
    computed:{}
  },
  {userName:'Evan'}
)
app.mount('#app') // 手动挂载
```

## defineComponent()

第一个参数是一个组件选项对象。返回值将是该选项对象本身，因为该函数实际上在运行时没有任何操作，仅用于提供类型推导。

#### 示例

定义选项式API组件

```js
import { defineComponent } from 'vue'

const MyComponent = defineComponent({
  data() {
    return { count: 1 }
  },
  methods: {
    increment() {
      this.count++
    }
  }
})
```

定义组合式API组件

```js
import { defineComponent, ref } from 'vue'

const HelloWorld = defineComponent(function HelloWorld() {
  const count = ref(0)
  return { count }
})
```

## defineAsyncComponent()

定义一个异步组件，它在运行时是懒加载的。

#### 示例

```js
import { defineAsyncComponent } from 'vue'
// 动态导入
const AsyncComp = defineAsyncComponent(() =>
  import('./components/MyComponent.vue')
)
// 全局注册异步组件
app.component('MyComponent', defineAsyncComponent(() =>
  import('./components/MyComponent.vue')
))
// 组件局部注册异步组件
export default {
  components: {
    AdminPage: defineAsyncComponent(() =>
      import('./components/AdminPageComponent.vue')
    )
  }
}
// 使用Promise加载
const AsyncComp = defineAsyncComponent(() => {
  return new Promise((resolve, reject) => {
    // ...从服务器获取组件
    resolve(/* 获取到的组件 */)
  })
})
```

其他参数说明：

```js
const AsyncComp = defineAsyncComponent({
  // 加载函数
  loader: () => import('./Foo.vue'),
  // 占位组件：正在加载组件时使用的组件
  loadingComponent: LoadingComponent,
  // 加载失败后展示的组件
  errorComponent: ErrorComponent,
  // 展示加载组件前的延迟时间，默认为 200ms
  delay: 200,
  // 组件加载超时时间，默认值是：Infinity
  timeout: 3000,
  // 默认为true
  suspensible: false,
  /**
   * 错误处理器
   * @param {*} error — 信息错误对象
   * @param {*} retry —  retry是一个函数，它定义了在promise rejects中重新启动的尝试。
   * @param {*} fail — 错误处理结束
   * @param {*} attempts — 重试次数
   */
  onError(error, retry, fail, attempts) {
    if (error.message.match(/fetch/) && attempts <= 3) {
      // 下载错误重复，最多三次。
      retry()
    } else {
      // 注意，retry/fail类似于promise的resolve/reject:
      // 必须有一个调用来继续处理错误。
      fail()
    }
  },
})
```

## defineCustomElement

和`defineComponent`接收的参数相同，返回一个`Web Components`（html原生自定义元素）。

## h()

渲染函数，创建虚拟 DOM 节点 (vnode)。

```js
render() { // 选项式中代替模版的render
  return h('h1', {}, '标题1')
}
```

#### 参数：

接收三个参数：`type`，`props?`和`children?`

**type**

- **类型：** `String | Object | Function`

- **细节：**

  `type`参数是**必须的**。HTML 标记、组件、异步或功能组件的名称。如果您指定一个返回 的函数`null`，则会绘制一条注释。

**props**

- **类型：** `Object`

- **细节：**

  可选参数。具有要在模板中使用的适当属性、输入和事件的对象。

**children**

- **类型：** `String | Array | Object`

- **细节：**

  可选参数。可以是单个文本节点的字符串，多个节点的数组或者是带有插槽的组件对象。

#### 示例：

```js
import { h } from 'vue'
import Foo from './Foo.vue'

// type 为必须的
h('div')
// 第二个参数为props
h('div', { id: 'foo' }) 
// 省略props,第二个参数是 children<String>
h('div', 'hello') 
// 省略props,第二个参数是 children<Array>
h('div', [h('span', 'hello')]) 
// 省略props,第二个参数是 children<Object>
h(Foo, {
  someProp: 'hello',   // 等价于 some-prop="hello"
  onUpdate: () => {}   // 等价于 @update="() => {}"
})


```

## nextTick()

等待下一次 DOM 更新刷新的工具方法，修改一些数据后使用它来等待DOM更新后做一些事情。

> Vue 中更改响应式状态时，最终的 DOM 更新并不是同步生效的，而是由 Vue 将它们缓存在一个队列中，直到下一个“tick”才一起执行。这样是为了确保每个组件无论发生多少状态改变，都仅执行一次更新。

#### 示例：

```vue
<script>
import { nextTick } from 'vue'

export default {
  data() {
    return {
      count: 0
    }
  },
  methods: {
    async increment() {
      this.count++

      // DOM 还未更新
      console.log(document.getElementById('counter').textContent) // 0

      await nextTick()
      // DOM 此时已经更新
      console.log(document.getElementById('counter').textContent) // 1
    }
  }
}
</script>

<template>
  <button id="counter" @click="increment">{{ count }}</button>
</template>
```

## mergeProps()

合并多个 props 对象，稍后出现的同名属性优先；

以下三个有特定的合并方式：

- `class` - 属性的值将被连接起来而不是被覆盖；
- `style` - 属性的值将被连接起来而不是被覆盖；
- `onXxx` - 事件监听器会被合并到一个数组中，也不会被覆盖。

**示例**

合并机制

```js
import { mergeProps } from 'vue'

const one = {
  class: 'foo',
  onClick: handlerA
}

const two = {
  class: { bar: true },
  onClick: handlerB
}

const merged = mergeProps(one, two)
/**
 {
   class: 'foo bar',
   onClick: [handlerA, handlerB]
 }
 */

```

## version

以字符串形式返回 Vue 的安装版本号，这对于可能对不同版本使用不同策略的第三方插件使用。

```js
import { version } from 'vue'

console.log(version)
```



