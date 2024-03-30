# javascript 语言基础

## 语言特性

-   动态类型，弱类型
-   基于原型的类继承
-   函数是一等公民
    -   函数也是 Object
    -   高阶函数
    -   函数没有重载
-   单线程，非阻塞（EventLoop 队列）
-   高级语言，JIT（Just-In-Time）编译

> 语言特性学习路径：
> 从多个角度开始，会有不同的理解，比如：从V8编译原理开始学习，或者单纯的从语言特性开始学习。另一个角度是ES6的变量声明？

## 动态和弱类型

对于各种语言类型可参考下图：

![img](https://blog.poetries.top/img/static/gitee/2019/11/2.png)

**动态：**JavaScript 中的变量与任何特定值类型没有任何关联，并且任何变量都可以分配（重新分配）所有类型的值；（声明后还可以重新分配其他类型的变量）

**弱类型：**意味着当操作涉及不匹配的类型是否，它将允许隐式类型转换，而不是抛出一个错误。（在动态执行的时候允许隐士转换）

## 数据类型

###  js基础类型

**基本类型有七种**：`null`,`undefined`,`boolean`,`number`,`string`,`symbol`,`bigint`	

- `Symbol`代表独一无二的值，通常用来定义对象的唯一属性名。

- `BigInt`表示任意大小的整数。

  除了 [`null`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/null) 和 [`undefined`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/undefined)，所有原始类型都有它们相应的对象包装类型，这为处理原始值提供可用的方法。

  | 类型                                                         | `typeof` 返回值 | 对象包装器                                                   |
  | :----------------------------------------------------------- | :-------------- | :----------------------------------------------------------- |
  | [Null](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Data_structures#null_类型) | `"object"`      | N/A                                                          |
  | [Undefined](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Data_structures#undefined_类型) | `"undefined"`   | N/A                                                          |
  | [Boolean](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Data_structures#boolean_类型) | `"boolean"`     | [`Boolean`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Boolean) |
  | [Number](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Data_structures#number_类型) | `"number"`      | [`Number`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Number) |
  | [BigInt](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Data_structures#bigint_类型) | `"bigint"`      | [`BigInt`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/BigInt) |
  | [String](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Data_structures#string_类型) | `"string"`      | [`String`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String) |
  | [Symbol](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Data_structures#symbol_类型) | `"symbol"`      | [`Symbol`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Symbol) |

> 除了 [`null`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/null)，所有原始类型都可以使用 [`typeof`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/typeof) 运算符测试。`typeof null` 返回 `"object"`，因此必须使用 `=== null` 来测试 `null`。

### `undefined`和`null`

从概念上讲，`undefined` 表示没有任何*值*，`null` 表示没有任何*对象*（这也可以构成 [`typeof null === "object"` 的接口](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/typeof#typeof_null)）。当某些东西没有值时，该语言通常默认为 `undefined`：

- 没有值（`return;`）的 [`return`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/return) 语句，隐式返回 `undefined`。
- 访问不存在的[对象](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object)属性（`obj.iDontExist`），返回 `undefined`。
- 变量声明时没有初始化（`let x;`），隐式初始化为 `undefined`。
- 许多如 [`Array.prototype.find()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/find) 和 [`Map.prototype.get()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Map/get) 的方法，当没有发现元素时，返回 `undefined`。

`null` 在核心语言中使用频率少得多。最重要的地方是[原型链的末端](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)——其次是与原型交互的方法，如 [`Object.getPrototypeOf()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf)、[`Object.create()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/create) 等，接受或返回 `null` 而不是 `undefined`。

`null` 是一个[关键字](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Lexical_grammar#关键字)，但是 `undefined` 是一个普通的[标识符](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Lexical_grammar#identifiers)，恰好是一个全局属性。在实践中，这两个差异很小，因为 `undefined` 不应该被重新定义或者遮蔽。

**引用数据类型：**`Object`

- 普通对象`Object`
- 数组对象`Array`
- 正则对象`RegExp`
- 日期对象`Date`
- 数学函数`Math`
- 函数对象`Function`

## 类型转换

**强制转换**

- `Number()`

  ```js
  Number(324) // 324
  Number('324') // 324
  Number('324abc') // NaN
  Number('') // 0
  Number(true) // 1
  Number(false) // 0
  Number(undefined) // NaN
  Number(null) // 0
  parseInt('42 cats') // 42 Number 比 parseInt严格一点。
  // 对象
  Number([5]) // 5
  Number([1, 2, 3]) // NaN
  ```

  > 转换规则：
  >
  > - [强制数字类型转换](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Data_structures#强制数字类型转换)、[强制 number 类型转换](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Number#number_强制转换)、[强制 BigInt 类型转换](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/BigInt#转化)：`[@@toPrimitive]("number")` → `valueOf()` → `toString()`

- `String()`

  ```
  String(123) // "123"
  String('abc') // "abc"
  String(true) // "true"
  String(undefined) // "undefined"
  String(null) // "null"
  // 对象
  String({a: 1}) // "[object Object]"
  String([1, 2, 3]) // "1,2,3"
  ```

  > 转换规则:
  >
  > - [强制字符串类型转换](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String#字符串强制转换)：`[@@toPrimitive]("string")` → `toString()` → `valueOf()`

- `Boolean()`

  `undefined`,`null`,`0`,`NaN`,`''`，这五个值会转换成`false`

  ```js
  Boolean(undefined) // false
  Boolean(null) // false
  Boolean(0) // false
  Boolean(NaN) // false
  Boolean('') // false
  ```

  ### 其他转换

  - [`+`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Addition) 运算符——如果运算对象是字符串，执行字符串串联；否则，执行数值相加。

  - [`==`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Equality) 运算符——如果一个运算对象是原始值，而另一个运算对象是对象（object），则该对象将转换为没有首选类型的原始值。
  - [`Date()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Date/Date) 构造函数，当它收到一个不是 `Date` 实例的参数时——字符串表示日期字符串，而数值表示时间戳。

## 包装对象和描述对象

- **包装对象：**指的是与数值、字符串、布尔值分别相对应的`Number`、`String`、`Boolean`三个原生对象。这三个原生对象可以把原始类型的值变成（包装成）对象。
- **属性描述对象：**JavaScript 提供了一个内部数据结构，用来描述对象的属性，控制它的行为，比如该属性是否可写、可遍历等等。这个内部数据结构称为“属性描述对象”（attributes object）。每个属性都有自己对应的属性描述对象，保存该属性的一些元信息。

### 包装对象

​	通用实例方法：

- `valueOf()`方法返回包装对象实例对应的原始类型的值。
- `toString()`方法返回对应的字符串形式。

Number实例方法

- `toFixed()`方法先将一个数转为指定位数的小数，然后返回这个小数对应的字符串。
- `toExponential`方法用于将一个数转为科学计数法形式。
- `toPrecision()`方法用于将一个数转为指定位数的有效数字。
- `toLocaleString()`方法接受一个地区码作为参数，返回一个字符串，表示当前数字在该地区的当地书写形式。

String 实例属性

- `length`属性返回字符串的长度。

String 实例方法

- `charAt`方法返回指定位置的字符，参数是从`0`开始编号的位置。
- `charCodeAt()`方法返回字符串指定位置的 Unicode 码点（十进制表示），相当于`String.fromCharCode()`的逆操作。
- `concat`方法用于连接两个字符串，返回一个新字符串，不改变原字符串。
- `slice()`方法用于从原字符串取出子字符串并返回，不改变原字符串。它的第一个参数是子字符串的开始位置，第二个参数是子字符串的结束位置（不含该位置）。
- `substring`方法用于从原字符串取出子字符串并返回，不改变原字符串，跟`slice`方法很相像。它的第一个参数表示子字符串的开始位置，第二个位置表示结束位置（返回结果不含该位置）。
- `substr`方法用于从原字符串取出子字符串并返回，不改变原字符串，跟`slice`和`substring`方法的作用相同。
- `indexOf`方法用于确定一个字符串在另一个字符串中第一次出现的位置，返回结果是匹配开始的位置。如果返回`-1`，就表示不匹配。
- `trim`方法用于去除字符串两端的空格，返回一个新字符串，不改变原字符串。
- `toLowerCase`方法用于将一个字符串全部转为小写，`toUpperCase`则是全部转为大写。它们都返回一个新字符串，不改变原字符串。
- `match`方法用于确定原字符串是否匹配某个子字符串，返回一个数组，成员为匹配的第一个字符串。如果没有找到匹配，则返回`null`。
- `search`方法的用法基本等同于`match`，但是返回值为匹配的第一个位置。如果没有找到匹配，则返回`-1`。
- `split`方法按照给定规则分割字符串，返回一个由分割出来的子字符串组成的数组。
- `localeCompare`方法用于比较两个字符串。它返回一个整数，如果小于0，表示第一个字符串小于第二个字符串；如果等于0，表示两者相等；如果大于0，表示第一个字符串大于第二个字符串。

### 属性描述对象`Object.defineProperty`

元属性：

- `value`属性是目标属性的值。
- `writable`属性是一个布尔值，决定了目标属性的值（value）是否可以被改变。
- `enumerable`（可遍历性）返回一个布尔值，表示目标属性是否可遍历。
- `configurable`(可配置性）返回一个布尔值，决定了是否可以修改属性描述对象。也就是说，`configurable`为`false`时，`writable`、`enumerable`和`configurable`都不能被修改了。

```js
var obj = Object.defineProperty({}, 'p', {
  value: 1,
  writable: false,
  enumerable: false,
  configurable: false,
  get: function () {
    return 'getter';
  },
  set: function (value) {
    console.log('setter: ' + value);
  }
});
```

存取器

- `setter`：存值函数称为`setter`，使用属性描述对象的`set`属性
- `getter`：取值函数称为`getter`，使用属性描述对象的`get`属性。

#### Object 静态方法

`Object.getOwnPropertyDescriptor()`方法可以获取属性描述对象。它的第一个参数是目标对象，第二个参数是一个字符串，对应目标对象的某个属性名。

```js
var obj = { p: 'a' };
// 声明一个对象的默认描述属性
Object.getOwnPropertyDescriptor(obj, 'p')
 { value: "a",
   writable: true,
   enumerable: true,
   configurable: true
 }
// 使用 defineProperty 定义属性，默认默认描述属性
var obj = Object.defineProperty({}, 'p', {});
{
    "writable": false,
    "enumerable": false,
    "configurable": false
}
```

- `Object.preventExtensions`方法可以使得一个对象无法再添加新的属性。
- `Object.seal`方法使得一个对象既无法添加新属性，也无法删除旧属性。
- `Object.freeze`方法可以使得一个对象无法添加新属性、无法删除旧属性、也无法改变属性的值，使得这个对象实际上变成了常量。



## 总结：TODO



## 参考：

[属性描述对象](https://wangdoc.com/javascript/stdlib/attributes)

[包装对象](https://wangdoc.com/javascript/stdlib/wrapper)

[JavaScript 数据类型和数据结构](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Data_structures)

