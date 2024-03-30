# 组合API

实例代码实用单文件组件语法

## Setup

一个组件选项，它是 Composition API 的起点，在创建组件**之前**`props`、解析输入参数之后执行。

- **参数：**
  - `props`- 输入参数
  - `context` - setup上下文对象；其实也只能访问`attrs`、`slots`、`emit`、`expose`
  
- **例子：**
  
  - 返回一个对象
  
    ```js
    export default {
      setup(props, { attrs, slots, emit, expose }) {
        const count = ref(0)
        const increment = () => ++count.value
       
        retrun {count,increment}
      }
    }
    ```
  
  - 返回一个渲染函数
  
    ```js
    import { h, ref } from 'vue'
    
    export default {
      setup(props, { expose }) {
        const count = ref(0)
        const increment = () => ++count.value
        
    	  // 有选择地暴露局部状态
        expose({
          increment
        })
    
        return () => h('div', count.value)
      }
    }
    ```
  
    > 注意：
    >
    > - 如果返回一个渲染函数，将无法返回其他属性；
    > - 如果需要声明属性以便可以从外部访问它们，例如，通过`ref`父级访问它们，那么您可以使用`expose`

## 生命周期

通过显式导入的函数注册生命周期挂钩`onX`：

```js
import { onMounted, onUpdated, onUnmounted } from 'vue'

export default {
  setup() {
    onMounted(() => {
      console.log('挂载后!')
    })
    onUpdated(() => {
      console.log('更新后!')
    })
    onUnmounted(() => {
      console.log('卸载后!')
    })
  }
}
```

**Options API 和 Composition API 钩子的对应关系**

- `beforeCreate`-> 使用`setup()`

- `created`-> 使用`setup()`
- `beforeMount`->`onBeforeMount`
- `mounted`->`onMounted`
- `beforeUpdate`->`onBeforeUpdate`
- `updated`->`onUpdated`
- `beforeUnmount`->`onBeforeUnmount`
- `unmounted`->`onUnmounted`
- `errorCaptured`->`onErrorCaptured`
- `renderTracked`->`onRenderTracked`
- `renderTriggered`->`onRenderTriggered`
- `activated`->`onActivated`
- `deactivated`->`onDeactivated`

> 注意：setup() 执行早于  beforeCreate；在创建组件**之前**`props`、解析输入参数之后执行。

## Provide / Inject

`provide`和函数`inject`提供依赖注入能力

**注入**:

```js
<script setup>
import { ref, provide } from 'vue'

// 提供静态值
provide('foo', 'bar')

// 提供响应式的值
const count = ref(0)
provide('count', count)

// 提供时将 Symbol 作为 key
const s = Symbol() // 应该定义在外部，这里是为了方便示例
provide(s, count)
</script>
```

**使用：**

```js
<script setup>
import { inject } from 'vue'
import { fooSymbol } from './injectionSymbols'

// 注入值的默认方式
const foo = inject('foo')

// 注入响应式的值
const count = inject('count')

// 通过 Symbol 类型的 key 注入
const s = Symbol() // 应该定义在外部，这里是为了方便示例
const foo2 = inject(s)

// 注入一个值，若为空则使用提供的默认值
const bar = inject('foo', 'default value')

// 注入一个值，若为空则使用提供的工厂函数
const baz = inject('foo', () => new Map())

// 注入时为了表明提供的默认值是个函数，需要传入第三个参数
const fn = inject('function', () => {}, false)
</script>
```

## 响应式



