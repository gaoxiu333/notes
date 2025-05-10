# Composition API

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