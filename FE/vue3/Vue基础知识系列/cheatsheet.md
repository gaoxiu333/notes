## 使用 vite 创建

快速启动一个 Vue3 项目

```bash
npm init vite-app <project-name>
cd <project-name>
npm install
npm run dev
```

## 模版语法

### 文本插值

```html
<span> {{ msg }} </span>
<span v-text='msg'></span>
```

### 原始 HTML

```html
<span v-html='rawHTML'></span>
```

### 表达式

```html
✅ <span> {{ msg.reverse() }} </span> <!--js表达式可以 -->
❌ <span> {{ let msg = 'hi' }} </span><!--js语句不行 -->
```

## 指令

- `v-if`: 如果为真，则将el放入DOM
- `v-else-if`:  像普通的条件语句一样，添加“else if 区块”；
- ` v-else`:像普通的条件语句一样，添加一个“else 区块”；
- `v-show`: 控制CSS`display`的属性来显示；
- `v-text`: 更新文本内容；
- `v-html`: 使用`innerHTML`更新内容；
- `v-for` : 循环渲染一个对象/数组
- `v-on` or `@`: 监听DOM事件
- `v-bind` or` :`： 动态绑定`attribute`或组件的`prop`
- `v-once` : 只渲染一次，之后有更新也不会重新渲染

### 事件处理

**事件绑定**

```html
<div v-on:click='count'>Increase</div>
<!-- 简写 -->
<div @click='count'>Increase</div>
<!-- 内联事件处理器 -->
<button @click="count++">Add 1</button>
<button @click="increment()">Add 1</button>
<!-- 使用特殊的 $event 变量 -->
<button @click="increment($event)">Add 1</button>
<!-- 使用内联箭头函数 -->
<button @click="(event)=>increment(event)">Add 1</button>
```

**修饰符**

- `.stop` - 阻止冒泡。
- `.prevent` - 阻止默认事件。
- `.once` - 最多触发一次处理函数。
- `.self` - 只监听当前元素本身。

### 列表渲染

```html
<li v-for='(item, index) in items'>
{{ index }} : {{ item }}
</li>
```

### 绑定`v-bind`

### 属性绑定(Attribute)

```html
<div v-bind:id='objectID'>...</div>
<!-- 简写 -->
<div :id='objectID'>...</div>
```

### 表单绑定

```html
<input v-model='email' />
```

**修饰符**

- `.lazy` -使用`change`事件触发更新。
- `.trim` - 去除两端的空格。
- `.number`- 使用`parseFloat`转换为数字

### 样式绑定

```html
<input :class='{error: hasError}' />
<input :style='{margin: space+"px"}' />
```

## 组件

### defineComponent

```js
 export default defineComponent({
   data(){},
   setup(){},
   created(){}
   /* ... */
 })
// __PURE__ 注释 是告诉 webpack 组件可以被 tree-shake
export default /*#__PURE__*/ defineComponent(/* ... */)
```

### 传值（prop）

```html
<custom :msg='s' @someEvent='s = $event'/>
```

### 事件（emit)

```html
<custom :msg='s' @someEvent='s = $event'/>
// custom 组件
<button @click="$emit('someEvent')">click me</button>
```

### 组件双向绑定（v-modal）

```html
// 父组件
<CustomInput v-model="searchText" />
=============================
// CustomInput 组件
<template>
  <input
    :value="modelValue"
    @input="$emit('update:modelValue', $event.target.value)"
  />
</template>
```

### 插槽（solt）

基本使用

```html
<!-- custom -->
<div>
  Hello World
  <slot></slot> <!-- 插槽出口 -->
</div>
==========================
<!-- 父组件 -->
<template>
  <Custom>
     <!-- 插槽内容 -->
  </Custom>
</template>
```

具名插槽

```html
<!-- custom -->
<div>
  <slot name='top' :text="greetingMessage" :count="1"></slot>
  <slot name='bottom'></slot>
  <slot></slot>
</div>
=================================
<!-- 父组件 -->
<Custome>
  <template v-slot:top="{text,count}">
    {{text}}{{count}}     <!-- 作用域插槽 -->
  </template>
  <template #bottom>
    <!-- bottom 插槽的内容 -->
  </template>
   <template #default>
      <!-- default 也可以指定默认插槽 -->
  </template>
</Custome>
```



### 

### 杂项

组件缓存



## 动态组件

```html
<component :is='componentName'/>
<!-- 缓存 -->
<keep-alive>
	<component :is='componentName'/>
</keep-alive>
```

## 组合式API

```js
import { ref, reactive } from 'vue'
import { onMounted,computed } from 'vue'
export default {
  setup(props, context) {
    const val = ref('example')
    const obj = reactive({ count: 0 }) /*响应式数据*/
    const evtHandler = () => {/*...*/} /*事件方法*/
    const b = computed(() => /*...*/)  /*计算属性*/
    onMounted(() => {/*...*/}          /*生命周期*/
    return {
      val, obj, evtHandler
    }
  }
}
```

- 计算属性

  ```js
  setup() {
    const a = ref(1)
    const b = computed(() => a.value * 2)
    return { a, b }
  }
  ```

- 监听

  ```js
  setup() {
    const site = ref('learnvue.co')
    watchEffect(() => {
    	console.log(site.value)
    })
    watch(site,
     () => {
    	console.log(site.value)
    	}
    )
    return { site }
  }
  ```

  

## 选项式API

```js
export default {
  name:''/*显示指定名字，没有指定是会自己推到*/
  components:{/*注册组件*/},
  directives:{/*注册指令*/}
  data() {
    return { count: 1 }
  },
  computed: {/*计算属性*/ },
  created() {/*生命周期*/},
  methods:{/*方法*/},
  watch:{/*监听*/},
  mixins:[],/*官方更推荐组合式API复用逻辑*/
}

```

## 模版引用

定义一个跟模版变量同名的响应式变量

```js
// template
<div ref='example'> Example Div </div>
// script
setup() {
  const example = ref('learnvue.co')
  // DOM挂载完成查看
  onMounted(() => {
  	console.log(example.value)
  })
  return { example }
}
```

## 生命周期

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

> setup比beforeCreate要早

## 组件实例API

- `$forceUpdate()`- 强制该组件重新渲染
- `$nextTick()`- 等待下一次 DOM 更新刷新的工具方法。
- `$emit()`- 触发一个自定义事件

## 响应式API

- 创建响应式数据
  - `ref()`
  - `reactive()`
  - `shallowRef()`
  - `shallowReactive()`
  - `customRef()`
- 判断响应式数据
  - `isRef()`
  - `isReactive()`
  - `isProxy()`
- 响应式工具
  - `undef()`
  - `toRef()`
  - `toRefs()`
  - `toRaw()`
- 当前组件实例
  - `getCurrentInstance()`- 当前组件实例`this`，谨慎使用。
