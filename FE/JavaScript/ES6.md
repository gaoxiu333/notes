## ES6  声明变量的6种方法

- var
- function
- let
- const
- import
- class

###  顶层变量	

挂载在window下的变量，`var`、`functiion`声明的变量挂在在window下，`let`、`const`、`class`	声明的全局变量没有挂载在window下，也就是ES6开始全局变量将会和顶层变量脱钩。

```js
var a = 1;
// 如果在 Node 的 REPL 环境，可以写成 global.a
// 或者采用通用方法，写成 this.a
window.a // 1

let b = 1;
window.b // undefined
```

## 解构赋值

```js
// 默认值
let [foo = true] = [];
foo // true 
// 一个已声明变量的解构赋值
let x;
({x} = {x: 1});// 大括号放在行首位被认为代码块，需要放在小括号里
// 数组也可以用对象结构的方式
let arr = [1, 2, 3];
let {0 : first, [arr.length - 1] : last} = arr;
first // 1
last // 3
// 字符串也可以解构赋值
const [a, b, c, d, e] = 'hello';
a // "h"
b // "e"
c // "l"
d // "l"
e // "o"
let {length : len} = 'hello'; // 类数组都有length属性
len // 5
// 数字和布尔值解构赋值：解构赋值过程中等号右边会被转换成对象，数字和布尔值的包装对象都有toString，所以可以结构出toString方法，取值。
let {toString: s} = 123;
s === Number.prototype.toString // true

let {toString: s} = true;
s === Boolean.prototype.toString // true
// null和undefined不能转换成包装对象
let { prop: x } = undefined; // TypeError
let { prop: y } = null; // TypeError

```

