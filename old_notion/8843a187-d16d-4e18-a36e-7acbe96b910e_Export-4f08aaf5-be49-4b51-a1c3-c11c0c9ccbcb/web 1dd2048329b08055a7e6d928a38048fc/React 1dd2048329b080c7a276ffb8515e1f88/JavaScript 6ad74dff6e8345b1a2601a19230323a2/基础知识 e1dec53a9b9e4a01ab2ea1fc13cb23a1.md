# 基础知识

# 基础知识

### 

涵盖JavaScript的基础知识，以及JavaScript的语言特点。

### JavaScript 语言特点

- **解释执行：**JavaScript是一种解释型语言，不需要提前编译成字节码或者机器语言，而是由引擎在运行时解释执行
- **动态类型：**变量的类型在运行时根据赋值的值确定，所以变量是没有类型的，只有值才有类型
- **弱类型语言：**对数据类型的转换很灵活，可以自动进行隐式转换
- **基于原型的继承：**采用原型链的方式实现对象之间的继承关系，通过原型链实现对象的共享属性和方法
- **事件驱动和异步编程：**支持事件驱动的编程模型，在用户与页面交互时可以触发各种事件，并且可以使用回调函数实现异步编程
- **函数式编程：**支持函数作为一等公民，可以作为参数或者返回值给其他函数，使得JavaScript具有函数式编程的特性，如：高阶函数，闭包等
- **跨平台：**可以在各种平台上运行，如：浏览器、服务器、移动端设备等。

### 基础语法

- **表达式与运算符**（包括了赋值、比较、算数、位运算、逻辑、字符串、三元，等等。）
    - [MDN 表达式和运算符](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators)
- **控制流程语句（条件语句、循环语句）**[JavaScript 参考](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference)
    - [MDN 循环与迭代](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Loops_and_iteration)

### 数据结构和类型

- **特点：** 动态和弱类型
- **数据类型**：原始类型（字符串、数字、布尔值、null、undefined、Symbol）、对象类型
- **类型转换**：显式转换、隐式转换、强制类型转换
- [MDN JavaScript 数据类型和数据结构](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Data_structures#object)

### 变量和作用域

- **var、let、const**三种变量声明方式可以很好的体现这门语言变量的作用域、以及作用域链
- **闭包：**由于闭包的特点，闭包在很长一段时间，一直在模仿let的特点，封闭的空间内创建自己的作用域。
- 函数作用域
- **其他参考或者理解：**等待补充，比如从原理层面来解释

### **基于原型的继承机制**

### 严格模式

1. 严格模式通过**抛出错误**来消除了一些原有**静默错误**。
2. 严格模式修复了一些导致 JavaScript 引擎难以执行优化的缺陷：有时候，相同的代码，严格模式可以比非严格模式下**运行得更快**。
3. 严格模式**禁用了**在 ECMAScript 的未来版本中可能会定义的一些语法。

### 基本内存模型

### **错误处理机制**（[`throw`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/throw)、[`try...catch`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/try...catch)，以及创建用户自定义[错误](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Error)类型的能力）