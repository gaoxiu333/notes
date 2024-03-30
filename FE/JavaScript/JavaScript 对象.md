# JavaScript 对象

- 对象创建
- 对象继承
- 对象枚举（遍历）



### 对象遍历

* [`for..in`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/for...in) 

  * 包含：自有可枚举、原型可枚举

  * 不包含：Symbol、不可枚举

* [`Object.hasOwnProperty()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwnProperty)

* [`Object.propertyIsEnumerable()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/propertyIsEnumerable)

* [`Object.getOwnPropertyNames()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyNames) - 返回一个数组

  * 包含：自有属性、自有不可枚举

  * 不包含：Symbol、原型属性

* `Object.getOwnPropertySymbols()`

  * 包含：Symbol

  * 不包含：除了Symbol，其他都不包含

* [`Object.keys()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)、`Object.values()`、`Object.entries()`

  * 包含：自有可枚举

  * 不包含：Symbol、不可枚举、原型属性

* [`Object.getOwnPropertyDescriptors()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyDescriptors)

* `Reflect.ownKeys()`

  * 包含：自身属性、自身不可枚举属性、Symbol

  * 不包含：原型属性

## 创建对象

###### 创建新对象

- 对象初始化器

- 使用构造函数

- 使用`Object.create`
  - 指定原型

  - `null` 指定无原型

- 使用`Object.defineProperty`

> 更多参考：[使用不同的方法来创建对象和改变原型链](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Inheritance_and_the_prototype_chain#使用不同的方法来创建对象和改变原型链)

```js


// 1. 对象初始化器/字面量
let obj1 = {a:1}
// 2. 构造函数
function Foo(){
    this.name = 'aa'
}
let obj2 = new Foo()
//3. Object.create// 可以指定原型，或者null没有原型
let obj3 = Object.create(Foo)
```



###### 对象描述符

`Object.defineProperty`精确的添加或修改对象上的属性；

- `configurable` - 属性是否可配置，默认`false`

- `enumerable`

- 数据描述符

- `value`

- `writable`

- 访问器描述符

- `get`

- `set`

> 数据描述符和访问器描述符，通常是二选一，只有一个生效。

###### 枚举对象属性

- `for..in`  访问对象及其原型链中所有的可枚举属性

- `Object.keys()`、`Object.values()`、`Object.entries()` 返回对象自身所可枚举属性，不包含原型中的属性

- `Object.getOwnPropertyNames()` 返回对象自身所有属性，包含不可枚举，不包含原型

- `Object.getOwnPropertySymbols()` 返回自身的Symbol，其他的都不返回

- `Reflect.ownKeys()` 返回自身所有属性，包含不可枚举以及Symbol

###### 判断属性

- `Object.propertyIsEnumerable()`  是否可枚举

- `Object.hasOwnProperty()` 是否是自身属性

- `Object.hasOwn()` 用来取代`Object.hasOwnProperty()`

###### 其他有用的

- `Object.getOwnPropertyDescriptors()`

###### 参考

- [MDN 参考 Object.defineProperty()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)

## 基于原型链的继承

- [MDN 继承与原型链](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Inheritance_and_the_prototype_chain#基于原型链的继承) 的笔记

- 对象原型：`[[Prototype]]` 、`{ __proto__: ... }`(注意不能直接这么访问，访问已经被遗弃)
- 构造函数创建的每一个实例都会自动将构造函数的 [`prototype`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype) 属性作为其 `[[Prototype]]`
- `Object.create`
- 

### 原型链

JavaScript 只有一种结构：对象。每个对象（object）都有一个私有属性指向另一个名为**原型**（prototype）的对象。原型对象也有一个自己的原型，层层向上直到一个对象的原型为 `null`。根据定义，`null` 没有原型，并作为这个**原型链**（prototype chain）中的最后一个环节

### 原型

- **ECMAScript 标准：**符号 `someObject.[[Prototype]]` 用于标识 `someObject` 的原型

- **访问和设置：**[`Object.getPrototypeOf()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf)[、](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf)[`Object.setPrototypeOf()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf)

- **__proto__访问器**：是非标准的，但是现在仍然被浏览器引擎实现。

- **注意：**不应与函数的 `func.prototype` 属性混淆，这一点比较难以理解，忘记请看

### 构造函数与原型

- [**prototype：**](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype)通过构造函数创建的每一个实例都会自动将构造函数的 [`prototype`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype) 属性作为其 `[[Prototype]]`

- **constructor：**它引用了构造函数本身，这允许我们在任何实例中访问原始构造函数。

### 性能

原型链上较深层的属性的查找时间可能会对性能产生负面影响，这在性能至关重要的代码中可能会非常明显。此外，尝试访问不存在的属性始终会遍历整个原型链。

### 其他

- 判断：使用 [`hasOwnProperty`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwnProperty) 或 [`Object.hasOwn`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwn) 方法

### 参考

- Function() 构造函数

- Function.prototype.prototype

## ES6+ 新特性

- Proxy

- Reflect

- Promise



