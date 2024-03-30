## TS 速查

## Interface

关键点

- 用于描述物体的形状，并且可以扩展。
- JavaScript 中的几乎所有内容都是 obiect 和 接口 构建的都与它们的运行时行为相匹配

内置基本类型

常见的内置对象

字面量类型

常用语法

- （可选）从现有接口或类型中获取属性



```typescript

// TypeScript 中有 3 种基本类型
let isDone: boolean = false;
let lines: number = 42;
let name: string = "Anders";

// 但是，如果变量派生自显式文本，则可以省略类型注释
let isDone = false;
let lines = 42;
let name = "Anders";

// 当不可能知道时，有“Any”类型
let notSure: any = 4;
notSure = "maybe a string instead";
notSure = false; // 好的，绝对是一个 boolean

// 对常量使用 const 关键字
const numLivesForCat = 9;
numLivesForCat = 1; // Error

// 对于集合，有类型数组和泛型数组
let list: number[] = [1, 2, 3];
// 或者，使用通用数组类型
let list: Array<number> = [1, 2, 3];

// 对于枚举
enum Color { Red, Green, Blue };
let c: Color = Color.Green;
console.log(Color[c]); // "Green"

// 最后，“void”用于函数不返回任何内容的特殊情况
function bigHorribleAlert(): void {
  alert("I'm a little annoying box!");
}

// 函数是一等公民，支持 lambda“粗箭头”语法和使用类型推断

// 以下是等效的，相同的签名将由 // 编译器推断 并发出相同的 JavaScript 
let f1 = function (i: number): number { return i * i; }
// 推断的返回类型
let f2 = function (i: number) { return i * i; }
// “粗箭头”语法
let f3 = (i: number): number => { return i * i; }
// 带有推断返回类型的“粗箭头”语法
let f4 = (i: number) => { return i * i; }
// 带有推断返回类型的“粗箭头”语法，无括号意味着没有返回需要关键字
let f5 = (i: number) => i * i;

// 接口是结构化的，任何具有属性的东西都符合 接口
interface Person {
  name: string;
  // 可选属性，标有“？” 
  age?: number;
  // 当然还有函数
  move(): void;
}

// 实现“Person”接口的对象
// 可以被视为一个 Person，因为它具有 name 和 move 属性
let p: Person = { name: "Bobby", move: () => { } };
// 具有可选属性的对象：
let validPerson: Person = { name: "Bobby", age: 42, move: () => { } };
// 不是人，因为年龄不是数字
let invalidPerson: Person = { name: "Bobby", age: true };

// 接口也可以描述函数类型
interface SearchFunc {
  (source: string, subString: string): boolean;
}
// 只有参数的类型很重要，名称不重要。
let mySearch: SearchFunc;
mySearch = function (src: string, sub: string) {
  return src.search(sub) != -1;
}

// 类 - 默认情况下成员是公共的
class Point {
  // 属性
  x: number;

  // 构造函数 - 此上下文中的 public/private 关键字将生成
  // 属性的样板代码和
  // 构造函数中的初始化。
  // 在此示例中，“y”将像“x”一样定义，但代码更少
  // 也支持默认值

  constructor(x: number, public y: number = 0) {
    this.x = x;
  }

  // 函数
  dist(): number { return Math.sqrt(this.x * this.x + this.y * this.y); }

  // 静态成员
  static origin = new Point(0, 0);
}

// 类可以显式标记为实现接口。
// 任何缺少的属性都会在编译时导致错误。
class PointPerson implements Person {
    name: string
    move() {}
}

let p1 = new Point(10, 20);
let p2 = new Point(25); //y 将为 0

// 继承
class Point3D extends Point {
  constructor(x: number, y: number, public z: number = 0) {
    super(x, y); // 对超类构造函数的显式调用是强制性的
  }

  // 覆盖
  dist(): number {
    let d = super.dist();
    return Math.sqrt(d * d + this.z * this.z);
  }
}

// 模块“.” 可用作子模块的分隔符
module Geometry {
  export class Square {
    constructor(public sideLength: number = 0) {
    }
    area() {
      return Math.pow(this.sideLength, 2);
    }
  }
}

let s1 = new Geometry.Square(5);

// 引用模块的本地别名
import G = Geometry;

let s2 = new G.Square(10);

// 泛型
// 类
class Tuple<T1, T2> {
  constructor(public item1: T1, public item2: T2) {
  }
}

// 接口
interface Pair<T> {
  item1: T;
  item2: T;
}

// 函数
let pairToTuple = function <T>(p: Pair<T>) {
  return new Tuple(p.item1, p.item2);
};

let tuple = pairToTuple({ item1: "hello", item2: "world" });

// 包括对定义文件的引用：
/// <reference path="jquery.d.ts" />

// 模板字符串（使用反引号的字符串）
// 使用模板字符串进行字符串插值
let name = 'Tyrone';
let greeting = `Hi ${name}, how are you?`
// 带模板字符串的多行字符串
let multiline = `This is an example
of a multiline string`;

// READONLY: New Feature in TypeScript 3.1
interface Person {
  readonly name: string;
  readonly age: number;
}

var p1: Person = { name: "Tyrone", age: 42 };
p1.age = 25; // 错误，p1.age 是只读的

var p2 = { name: "John", age: 60 };
var p3: Person = p2; // Ok, read-only alias for p2
p3.age = 35; // Error, p3.age is read-only
p2.age = 45; // 好的，但是因为别名也改变了 p3.age

class Car {
  readonly make: string;
  readonly model: string;
  readonly year = 2018;

  constructor() {
    this.make = "Unknown Make"; // 构造函数中允许赋值
    this.model = "Unknown Model"; // 构造函数中允许赋值
  }
}

let numbers: Array<number> = [0, 1, 2, 3, 4];
let moreNumbers: ReadonlyArray<number> = numbers;
moreNumbers[5] = 5; // 错误，元素是只读的
moreNumbers.push(5); // 错误，没有 push 方法（因为它改变了数组）
moreNumbers.length = 3; // 错误，长度为只读
numbers = moreNumbers; // 错误，缺少变异方法

// 用于建模状态的标记联合类型，可以是多种形状中的一种
type State = 
  | { type: "loading" }
  | { type: "success", value: number }
  | { type: "error", message: string };

declare const state: State;
if (state.type === "success") {
  console.log(state.value);
} else if (state.type === "error") {
  console.error(state.message);
}

// 模板文字类型
// 用于创建复杂的字符串类型
type OrderSize = "regular" | "large";
type OrderItem = "Espresso" | "Cappuccino";
type Order = `A ${OrderSize} ${OrderItem}`;

let order1: Order = "A regular Cappuccino";
let order2: Order = "A large Espresso";
let order3: Order = "A small Espresso"; // Error

// 迭代器和生成器

// for..of 语句
// 迭代被迭代对象的值列表
let arrayOfAnyType = [1, "string", false];
for (const val of arrayOfAnyType) {
    console.log(val); // 1, "string", false
}

let list = [4, 5, 6];
for (const i of list) {
   console.log(i); // 4, 5, 6
}

// for..in 语句
// 遍历被迭代对象的键列表
for (const i in list) {
   console.log(i); // 0, 1, 2
}

// 类型断言

let foo = {} // 将 foo 创建为一个空对象
foo.bar = 123 // 错误：`{}`  foo上不存在属性“bar” 
foo.baz = 'hello world' // 错误：`{}` 上不存在属性 'baz'   

// 因为 foo 的推断类型是 `{}`（具有 0 个属性的对象），所以您
// 不允许向其添加 bar 和 baz。然而，使用类型断言，
// 以下将通过：

interface Foo { 
  bar: number;
  baz: string;
}

let foo = {} as Foo; // 在这里输入断言
foo.bar = 123;
foo.baz = 'hello world'

```

