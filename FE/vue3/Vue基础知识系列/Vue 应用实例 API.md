# 应用实例 API

Vue 2.x 所有全局更改 Vue 行为的 API 都已移至使用新的`createApp`

## mount()

用`innerHTML`应用程序根组件的呈现模板替换指定的 DOM 元素。

#### 参数：

- `{Element | string} rootContainer`

参数可以是一个实际的 DOM 元素或一个 CSS 选择器 (使用第一个匹配到的元素)。返回根组件的实例。

```js
import { createApp } from 'vue'
const app = createApp(/* ... */)

app.mount('#app')

// 也可以挂载到一个实际的 DOM 元素。
app.mount(document.body.firstChild)
```



## unmount()

卸载一个已挂载的应用实例。卸载一个应用会触发该应用组件树内所有组件的卸载生命周期钩子。



## use()

安装 Vue.js 插件。传递对象时，它必须包含一个`install`。 如果传递了函数，则将其视为`install`安装插件的方法。

如果多次调用同一个插件的`install`方法，只会安装一次。

#### 参数：

- `{Object | Function}`

  第一个可以是包含`install`的对象，或者是一个函数，会被看作`install`安装插件的方法。

- `...options (可选)`

  第二个参数是可以选的，将会作为`install`的参数。

```js
import { createApp } from 'vue'
import MyPlugin from './plugins/MyPlugin'

const app = createApp({})

app.use(MyPlugin)
app.mount('#app')
```

## components()

注册或获取全局组件。

#### 参数：

- `{string} name`
- `{Function | Object} definition (可选参数)`

#### 示例

```js
import { createApp } from 'vue'
import MyComponent from './App.vue'


const app = createApp({})

// 支持链式调用
app
  .component('my-component', {/* 组件模版对象 */})
	.component('my-component', MyComponent)

//一个参数： get 一个已注册的组件，如果有的话
const MyComponent = app.component('my-component')
```

## directive()

注册或获取全局指令。

#### 参数：

- `{string} name`
- `{Function | Object} definition (可选参数)`

#### 示例

简写形式只有两个钩子`mounted`，`updated`；通常情况下，指令仅需要这两钩子就够啦！

```js
  // 简写形式
app.directive('color', (el, binding) => {
  // 回调函数会在 `mounted` 和 `updated` 时都调用
  el.style.color = binding.value
})
```

完整的钩子：

```js
const app = createApp({})

// 使 v-focus 在所有组件中都可用
app.directive('focus', {
  // 在绑定元素的 attribute 前或事件监听器应用前调用
  created(el, binding, vnode, prevVnode) {},
  // 在元素被插入到 DOM 前调用
  beforeMount(el, binding, vnode, prevVnode) {},
  // 在绑定元素的父组件及他自己的所有子节点都挂载完成后调用
  mounted(el, binding, vnode, prevVnode) {},
  // 绑定元素的父组件更新前调用
  beforeUpdate(el, binding, vnode, prevVnode) {},
  // 在绑定元素的父组件及他自己的所有子节点都更新后调用
  updated(el, binding, vnode, prevVnode) {},
  // 绑定元素的父组件卸载前调用
  beforeUnmount(el, binding, vnode, prevVnode) {},
  // 绑定元素的父组件卸载后调用
  unmounted(el, binding, vnode, prevVnode) {}
})

```

## provide()

全局注入，所有子组件都可以访问到。

- 全局注入通常用在插件开发上；

#### 参数：

- `{string | Symbol} key`
- `value`

```js
import { createApp } from 'vue'

const app = createApp({
  inject: ['user'],
  template: `
    <div>
      {{ user }}
    </div>
  `
})

app.provide('user', 'administrator')
```

##  mixin()

可以为整个 Vue 应用程序全局添加一个 mixin。**Vue3 已经不再推荐**，推荐`组合式函数`替代。

```js
const app = Vue.createApp({
  myOption: 'hello!'
})

// 所有子组件实例都会 mixin 一个 created 钩子
app.mixin({
  created() {
    const myOption = this.$options.myOption
    if (myOption) {
      console.log(myOption)
    }
  }
})

app.mount('#mixins-global') // => "hello!"
```

## config

每个 Vue 应用程序都会公开一个对象`config`，其中包含该应用程序的配置设置：

```js
const app = createApp({})

console.log(app.config)
```

在安装应用程序之前，您可以更改下面列出的属性。

- `errorHandler` - 指定捕获错误处理函数
- `warnHandler` - 指定Vue 的运行时警告处理函数
- `performance` - 性能追踪
- `compilerOptions` - 配置运行时编译器的选项
- `globalProperties` - 注册全局属性对象
- `optionMergeStrategies` - 自定义组件选项的合并策略

#### globalProperties

- **类型：** `[key: string]: any`

- **默认：** `{}`

- **用法：**

  ```js
  app.config.globalProperties.foo = 'bar'
  
  app.component('child-component', {
    mounted() {
      console.log(this.foo) // 'bar'
    }
  })
  ```

  `Vue.prototype`这种方法取代了Vue 2.x 中的扩展：

  ```js
  // Vue2.x
  Vue.prototype.$http = () => {}
  
  // Vue3
  const app = createApp({})
  app.config.globalProperties.$http = () => {}
  ```

  



