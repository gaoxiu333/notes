# TypeScript

*TypeScript* - *TS* ，是一种由微软开发的自由和开源的编程语言。

随着项目规模的增大，原始弱类型 JavaScript 已不能满足需求。因此类型安全的 Typescript 应运而生。它是 JS 的超集，大大提高了代码的可读性和可维护性；同时，它可与原 JS 共存，项目可通过渐进式迁移至新项目。

### TypeScript 是什么

*TypeScript* 是 *JavaScript* 的 **超集** ，简单的说就是在 *JavaScript* 的基础上加入了 **类型系统**，让每个参数都有明确的意义，从而带来了更加 **智能** 的提示。

*TypeScript* 属于**强类型**语言，所以对于项目而言，会使代码更加规范，从而解决了大型项目代码的复杂性。

## 资料

#### 官方资料

- [TypeScript Playground](https://www.typescriptlang.org/play)：在线调试
  - [Babel](https://babeljs.io/repl#?presets=typescript)：Babel 的在线调试
- [TSConfig](https://www.typescriptlang.org/tsconfig)：config配置说明
- [tsc CLI](https://www.typescriptlang.org/docs/handbook/compiler-options.html)：命令行

- [cheat sheets](https://www.typescriptlang.org/cheatsheets)：语法速记
  - [语法速查](https://learnxinyminutes.com/docs/typescript/) - 非官方

- [Do's and Don'ts](https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html)：最佳实践小例子

#### 社区教程

- [傅说 | 玩转 TypeScript](https://mp.weixin.qq.com/s/9OZMfsUagYr96fD5uNsoiA)
- [TypeScript 入门指南](https://rualc.com/cs/typescript-language-basic/#gai-lan-2)
- [官方手册汉化](https://github.com/zhongsp/TypeScript)
- [TypeScript 入门教程](https://ts.xcatliu.com/)
- [深入理解 TypeScript](https://jkchao.github.io/typescript-book-chinese/)
- [TS 常见问题](https://juejin.cn/post/6844904055039344654)

## TypeScript 环境

- 运行
  - [命令行](https://www.typescriptlang.org/docs/handbook/compiler-options.html) - `tsc`
  - [parcel](https://parceljs.org/) - 快速构建一个 TS 运行环境
- 运行配置
  - [Compiler Options](https://www.typescriptlang.org/docs/handbook/compiler-options.html)：编译选项
  - [tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html)：配置文件

- 工程化
  - 工具
    - [types-checker](https://www.npmjs.com/package/types-checker)：自动安装 @types
    - [DefinitelyTyped](http://definitelytyped.org/)：@types 官网

  - ESLint
    - [Getting Started with ESLint ](https://eslint.org/docs/user-guide/getting-started)：ESLint 官方教程
    - [@typescript-eslint/parser](https://github.com/typescript-eslint/typescript-eslint/tree/master/packages/parser)：ESLint 的 TS 插件

  - 打包插件
    - [@babel/preset-typescript ](https://babeljs.io/docs/en/babel-preset-typescript)：babel 的
    - [rollup-plugin-typescript2 ](https://www.npmjs.com/package/rollup-plugin-typescript2)：rollup 


## TypeScript 基础语法

#### 安装&使用

```bash
npm init -y #初始化项目
npm i typescript # 安装 TS
npx tsc --init # 初始化 TS 项目，生成TSConfig.json
npm init @eslint/config # 初始化 ESlint 配置
```

## 类型

- 基本类型
  - *string*, *number*, *boolean*, *symbol*, *bigint*, *null*, *undefined*
  - *null* 和 *undefined* 两个类型一旦赋值上，就不能在赋值给任何其他类型
- 引用类型
  - *array*,  *Tuple*元组,  *object*包含*Object*和*{}*, *function*
- 特殊类型
  - *any*, *unknow*, *void*, *nerver*, *enum*
- 别名/接口
  - *type*, *interface*
- 其他类型
  - 类型推理、字面量类型、交叉类型

### 引用类型

#### Array 数组

两种使用方式：

1. T + `[]`
2. `Array<T>`：泛型语法

```typescript
let arr1: number[] = [1, 2, 3]

let arr2: Array<number> = [1, 2, 3]

let arr3: Array<number> = [1, 2, '3'] // error
// TS2322: Type 'string' is not assignable to type 'number'.

// 支持多种类型，使用｜符号
let arr4: Array<number | string> = [1, 2, '3'] //ok
```

#### Tuple 元祖

*Tuple* 可以说是 *Array* 的一种特殊情况。

-  *Tuple* 的作用就是限制 **元素的类型** 并且 **限制个数** 的数组
- 可以使用 `push` 等操作元祖，但是修改后长度不能通过下标访问
- *TS 4.0* 后支持标签

```typescript
let t: [number, string] = [1, '2']; // ok
```

#### Object 对象

- object：**首字母小写**几乎不用，常用`{}`
- Object：**首字母大写**表示`Object`实例，除了`null`、`undefined`的所有类型

```typescript
let obj1: object = {a: 1, b: 2}
obj1.a = 3 // error
let obj: Object;
obj = null; // error
// Type 'null' is not assignable to type 'Object'.(2322)
obj = undefined; // error
// Type 'undefined' is not assignable to type 'Object'.(2322)
```

#### 函数

```
JavaScript --> TypeScript
  
  class TypeScript{
    含有类型
    箭头函数
    函数类型
    必填和可选参数
    默认参数
    剩余参数
    函数重载
  }
     
  class JavaScript{
    无类型
    箭头函数（ES2015）
    无函数类型
    所有参数都是可选的
    默认参数
    剩余参数
    无函数重载
  }
```

- 定义函数

  - `function`

  - 箭头函数

- 函数重载
  - 使用 **相同名称** 和 **不同参数数量或类型** 创建多个方法的一种能力
  - 引擎按照自上而下的顺序查找重载表，因此要把最精确的定义放在最前面，以减少查找时间。
- 返回值类型
  - 没有定义时，TS会根据类型推断设置返回值类型

### 特殊类型

- any
  - 任何类型都可以归于 *any* 类型
  - 如果不设置类型，并且不进行赋值时，将会被被自动推论为 *any* 类型
- unknow
  - *unknow* 与 *any* 一样，都可以作为所有类型的 **顶级类型** ，但 *unknow* 更加**严格**
  - *unknow* 类型的值，只能被赋值给 *any* 类型和 *unknown* 类型本身
- void
  - 当一个函数，没有返回值时，*TS* 会默认它的返回值为 *void* 类型，实际为 *undefined* 
- never
  - *never* 表示一个函数永远不存在返回值
  - 与 *void* 相比， *never* 应该是 *void* 子集， 因为 *void* 实际上的返回值为 *undefined* ，而 *never* 连 *undefined* 也不行
  - 符合 *never* 的情况有：当抛出异常的情况和无限死循环
- enum 枚举
  - 可以定义一些带名字的常量
  - 枚举的类型只能是 *string* 或 *number*
  - 定义的名称不能为 **关键字**

#### 其他类型

- 字面量类型
  - 直接指定参数的可选的字面量，多个字面量通过 `|` 分隔 ，目前支持字符串*string*、数字*number*、布尔*boolean* 类型
- 模版字面量
  - 模板字面量类型以 字符串字面量类型为基础，可以通过 联合类型*^union^* 扩展成多个字符串。

```typescript
// 字面量
let str:'foo'|'bar'
let num: 1 | 2 | 3 = 1

// 模版字面量
type world = "world";
type World = "World";

type Greeting = `hello ${world | World}`;
// type Greeting = "hello world"
```

## Assertion 断言

类型断言可以用来手动指定一个值的类型。

- 用途：
  1. 将一个 联合类型 断言为其中一个类型语法
  2. 将一个 父类 断言为更加具体的 子类
  3. 将任何一个类型断言为 *any* / 将 *any* 断言为具体类型

- 语法：

  - `值 as 类型`

  - `<类型>值`

```typescript
//尖括号
let num: any = 'foo'
let res1: number = (<string>num).length; // React中会 error

// as 语法
let str: any = 'bar';
let res: number = (str as string).length;
```

- `as .. as` 双重断言
  - 使用类似 `as any as Foo` 的语法，对变量进行两次断言，来达到将任何一个类型断言为任何另一个类型的效果。

- `for key`确定赋值断言
  - 在实例属性或变量后面放置一个 `!` 号，以告诉 *TS* 该属性会被明确赋值
- `for value` 非空断言
  - 在上下文中当类型检查器无法断定类型时，一个新的后缀表达式操作符 `!` 可以用于断言操作对象是非 *null* 和非 *undefined* 类型。

```typescript
let bar!: string; // 确定赋值断言
const name2: string = str!; // 添加!符号进行非空断言，可以确定是非 null 和非 undefined 
const foo = bar as any as number // 双重断言
```

## Guards 类型守卫

*Type guards* 是可执行运行时检查的一种表达式，用于确保该类型在一定的范围内。使用守卫进行 *Type narrowing* 后，就可以使用相应的类型方法和属性了。

- `in` - 成员检测
  - 用于判断某个属性是否存在于对象当中。
- `typeof` - 类型检测
  - 用于 变量是否属于某个基本类型*basic-type instance* 
- `instanceof` - 实例检测
  - 用于判断一个 对象*^object^* 是不是某个 类*^class^* 的 实例*^instance^* ，见 *EcmaScript* [*instanceof*](05 EcmaScript.md/#class-instanceof-usage-es6 "*instanceof*") 。
- `is` - 定于类型保护
  - *is* 关键字用于定义类型保护，用于自定义函数返回类型。

> 类型守卫和断言的概念非常相似，都是确定参数的类型。
>
> - 断言直接告诉编辑器，这个参数就是这个类型
> - 类型守卫判断这个参数是什么类型

```typescript
// in
if ("isManager" in data ) { ... }
// typeof
if (typeof x === "string") { ... }
// instanceof
if (obj instanceof MyClass) { ... }

// is
function isString(value: unknown): value is string {
  return typeof value === "string";
}

function processValue(value: unknown) {
  if (isString(value)) {
    // 值被缩小为字符串
    // 可以执行特定于字符串的操作。
  } else {
    // 其他处理
  }
}
```

## Combine 类型组合

- 联合类型

  - 使用 `|` 符号连接
  - 将多个类型合并为一个类型并集
  - 联合类型只能使用类型中的共有方法

- 可辨识联合

  - 可辨识要求联合类型中的每个元素都至少含有一个 **相同** 单例类型属性

- 交叉类型

  - 使用 `&` 符号连接
  - 将 **多个类型** 合并为 **一个** 拥有它们**属性**并集的类型
  - 同名属性合并
    - 类型不同自动转为`never`类型
    - 类型相同，转为同类型属性

  ```typescript
  // 联合类型
  let num: 1 | 2 = 1;
  
  // 可辨识，有一个相同的属性 kind 
  type Shape =
    | { kind: "circle"; radius: number }
    | { kind: "square"; x: number }
    | { kind: "triangle"; x: number; y: number };
  
  function area(s: Shape) {
    switch (s.kind) {
      case "circle": // Type Narrowing
        return Math.PI * s.radius * s.radius;
      case "square":
        return s.x * s.x;
      case "triangle":
        return (s.x * s.y) / 2;
    }
    // 当类型无法收窄至上述类型，就会报错
    const check: never = s;
  }
  
  // 交叉类型
  type AProps = { foo: string }
  type BProps = { bar: number }
  
  type allProps = AProps & BProps
  
  const Info: allProps = {
    foo: '1',
    bar: 2
  }
  ```

  

  

## 接口

在 *TypeScript* 中，使用 接口`interfaces` 来定义对象的类型。

- 描述对象形状
- `?`可选属性
- `any`任意属性
- `readonly`只读属性
  - 定义后，只允许一次初始化，之后便不允许修改。
  - 可以理解为，初始化对象的时候，就必须提供一个初始值。
- `[index: string]`索引签名
  - 定义未知属性
  - 用方括号语法来描述可能值的类型
  - key的可选类型有 *string, number, symbol* 
- `[key: string]`映射类型
  - 声明未提前声明的属性类型

```typescript
```

### interface vs type

- 与接口类型不一样，类型别名可以用于一些其他类型，比如原始类型、联合类型和元组：

### Extend 继承

接口和类型别名都能够被扩展，但语法有所不同。此外，接口和类型别名不是互斥的。接口 *interface* 可以扩展类型别名 *alias* ，而反过来是不行的。

- `inteface` 继承需要 `extends`
- `type` 继承需要 `&`

```typescript
// Interface extends interface  接口继承接口
interface PartialPointX { x: number; }
interface Point extends PartialPointX { 
  y: number; 
}

// Type alias extends type alias 别名继承别名
type PartialPointX = { x: number; };
type Point = PartialPointX & { y: number; };

// Interface extends type alias 接口继承别名
type PartialPointX = { x: number; };
interface Point extends PartialPointX { y: number; }

// Type alias extends interface 别名继承接口
interface PartialPointX { x: number; }
type Point = PartialPointX & { y: number; };
```

### Implements 实现

类可以以相同的方式实现接口 *interface* 或类型别名*type* ，但类不能实现由类型别名 *type* 定义的联合类型 *union* ：

```typescript
interface Point {
  x: number;
  y: number;
}

class SomePoint implements Point {
  x = 1;
  y = 2;
}

type Point2 = {
  x: number;
  y: number;
};

class SomePoint2 implements Point2 {
  x = 1;
  y = 2;
}

type PartialPoint = { x: number; } | { y: number; };

class SomePartialPoint implements PartialPoint { // Error
  x = 1;
  y = 2;
}
```

### Declaration merging 声明合并

与类型别名不同，接口可以定义多次，会被自动合并为单个接口。

```typescript
interface Point { x: number; }
interface Point { y: number; }

const point: Point = { x: 1, y: 2 };
```

## Class 类

包括：静态属性，静态方法、成员属性、成员方法、私有属性、私有方法、构造器、*getter & setter* 。

> :memo: *Note*需要注意的是： 在静态方法中，如果不给默认值，并且不使用是会报错的，如果不想报错就使用 `!` 关键字，如：`memberProperty!:string` 。

```typescript
class Class {
    /* 1. 静态属性 */
    static staticProperty: string = '静态属性';
    // static name!:string;
    // TS1255: A definite assignment assertion '!' is not permitted in this context.

    /* 2. 静态方法 */
    static staticMember = () => {
        return `我是静态方法:${this.staticProperty}`;
    }

    /* 3. 成员属性 */
    // 实际上是通过public上进行修饰，只是省略了
    member1: string = '成员属性';
    member2: string; // note: 并没有报错
    memberProperty!: string; // ok 不设置默认值的时候必须加入！

    /* 4. 成员方法 */
    memberMethod = () => {
        return `我是成员方法:${this.memberProperty}`;
    }
    getPrivateMethod = () => {
        return this.#privateMethod();
    }

    /* 5. 私有属性 */
    #privateProperty: string = '私有属性';

    /* 6. 私有方法 */
    #privateMethod = () => {
        return `我是私有方法:${this.#privateProperty}`;
    };

    /* 7. 构造器 */
    constructor(_name: string) {
        this.memberProperty = _name;
    }

    /* 8. get */
    get getter() {
        return this.memberProperty;
    }

    /* ... & set */
    set getter(val) {
        this.memberProperty = val;
    }
}

const instance = new Class('成员属性');
console.log(Class.staticMember());
console.log(instance.getPrivateMethod());
console.log(instance.memberMethod());
// 我是静态方法:静态属性
// 我是私有方法:私有属性
// 我是成员方法:成员属性
```

### 修饰符

- `public` - 修饰的属性或方法是公有的，可以在任何地方被访问到，默认所有的属性和方法都是 *public* 的。
- `protected` - 修饰的属性或方法是受保护的，它和 *private* 类似，但允许被子类继承从而被访问。
- `private` - 修饰的属性或方法是私有的，不能在声明它的类的外部访问。
  - 该限制仅存在于编译期间，编译之后的代码中，并没有限制  *private* 属性在外部的可访问性。
- `#` - 在 *TS 3.8* 版本便开始支持 *ES2022* 新增的私有方法
  - 私有字段以 `#` 字符开头，也叫私有名称
  - 每个私有字段名称都 **唯一** 地限定于其包含的类
  - 不能在私有字段上使用 *TypeScript* 可访问性修饰符（如 *public* 或 *private*）
  - 私有字段不能在包含的类之外访问，甚至不能被检测到。
- `readonly` 只读属性

### Extends 继承

指的是一个类（称为子类、子接口）继承另外的一个类（称为父类、父接口）的功能，并可以增加它自己的新功能的能力，继承是类与类或者接口与接口之间最常见的关系。

### Implements 实现

用于检测某个类是否实现了相应接口，不符合则报错。

```typescript
// @errors: 2420
interface Pingable {
  ping(): void;
}

class Sonar implements Pingable {
  ping() {
    console.log("ping!");
  }
}

class Ball implements Pingable {
  // error, Ball中没有ping()方法
  pong() {
    console.log("pong!");
  }
}
```

### Abstract 抽象类

用 *abstract* 关键字声明的类叫做 **抽象类**，声明的方法叫做 **抽象方法** 。

- **抽象类**：指不能被实例化，因为它里面包含一个或多个抽象方法。
- **抽象方法**：是指不包含具体实现的方法；

```typescript
abstract class Shape {
    protected readonly name;

    protected constructor({name = ''}) {
        this.name = name;
    }

    // Abstract class constructor can be made protected
    abstract getArea(): number;
}

class Rectangle extends Shape {
    protected readonly height;
    protected readonly width;

    constructor(name, [height = 0, width = 0]) {
        super({name});
        this.height = height;
        this.width = width;
    }

    getArea() {
        return this.height * this.width;
    }
}
```

### 重写和重载

1. **重写** override ：使用 *extends* 关键字使子类能重写继承自父类中的方法
2. **重载** overload：允许同一个函数拥有多个类型定义

### Infer 类型推断

当 `noImplicitAny` 配置属性被启用之后，*TypeScript* 就可以使用控制流分析来确认类中的属性类型：

- 默认 *TS* 并不会自动推断 类 *class*  的成员 *property* 类型：
- 如果我们没法保证对成员属性都进行赋值，那么该属性可能会被认为是 `undefined`。

```typescript
class Person {
   fullName;  // (property) Person.fullName: string
   firstName; // (property) Person.firstName: string | undefined
   lastName; // (property) Person.lastName: string | undefined

   constructor(fullName: string) {
     this.fullName = fullName;
     if(Math.random()){
       this.firstName = fullName.split(" ")[0];
       this.lastName =   fullName.split(" ")[1];
     }
   }  
}
```

## Generics 泛型

*TypeScript* 可以在定义函数、接口或类的时候，不预先指定具体的类型，而在使用的时候再指定类型。

```typescript
function identity<T>(value: T): T {
  // T:传递类型 --> T链式传递给参数类型和返回类型
  return value;
}

identity<Number>(1);
```

常见泛型变量代表的意思：

1. `T` - 类型变量，通常用作第一个类型变量的名称
2. `K` - 表示对象中的键类型
3. `V` - 表示对象中的值类型
4. `E` - 表示元素类型

- 接口泛型
- 类泛型
- 泛型工具
  - `typeof` - 获取一个变量声明或对象的类型。
  - `keyof` - 获取某种类型的所有键，其返回类型是联合类型。
  - `in` - 用来遍历 可枚举类型
  - `infer` - 在条件类型语句中，可以用 `infer` 声明一个类型变量并且对它进行使用。
  - `extends` - 有时候我们定义的泛型不想过于灵活或者说想继承某些类等，可以通过 *extends* 关键字添加泛型约束。
  - `partial` - `Partial<T>` 的作用就是将某个类型里的属性全部变为可选项 `?` 。

```typescript
// 接口泛型
interface GenericIdentityFn<T> {
  (arg: T): T;
}
// 类泛型
class GenericNumber<T> {
  zeroValue: T;
  add: (x: T, y: T) => T;
}

let myGenericNumber = new GenericNumber<number>();
myGenericNumber.zeroValue = 0;
myGenericNumber.add = function (x, y) {
  return x + y;
};

// 泛型工具
// typeof
const str = typeof string

// keyof
interface Person {
  name: string;
  age: number;
}

type K1 = keyof Person; // "name" | "age"
type K2 = keyof Person[];
// 数组类型  Alias for: keyof Person[]/keyof []
// "length" | "toString" | "toLocaleString" | "pop" | "push" | "concat" | "join" | "reverse" | "shift" | "slice" | "sort" | ...

// in
type Keys = "a" | "b" | "c"

type Obj = {
  [p in Keys]: any;
} // 遍历Key类型中的所有成员作为键名
// Initial type:  {a: any, b: any, c: any}

type Str = {
  [P in keyof '']: ''[P];
} // 获取字符串中的所有键名: 内容为字符串类型中的所有键值
// Initial type:  {toString(): string, ...

// infer
type ReturnType<T> = T extends (
  ...args: any[]
) => infer R ? R : any;

// extends
interface Lengthwise {
  length: number;
}

function loggingIdentity<T extends Lengthwise>(arg: T): T {
  console.log(arg.length);
  return arg;
}

// Partial
type Partial<T> = {
  [P in keyof T]?: T[P];
};
```

## Decorator 装饰器

随着 *TypeScript* 和 *ES6* 中 类 *class*  的引入，现在存在某些需要附加功能来支持 注释 *comment*  或修改类和类成员的场景。装饰器*decorator* 提供了一种为类声明和成员添加注释和元编程语法的方法。装饰器是 *JavaScript* 的 *stage2* 提案，可作为 *TypeScript* 的实验性功能使用。它是一个表达式：

1. 该表达式被执行后，返回一个函数
2. 函数的入参分别为 *target*、*name* 和 *descriptor*
3. 执行该函数后，可能返回 *descriptor* 对象，用于配置 *target* 对象

装饰器是一种函数，写成 `@ + 函数名` 。它可以放在类和类方法的定义前面。

```typescript
// 普通的
function decorator(target): void {
  	(target as any).isTestable = true; // 静态属性
    target.prototype.isTestable = true; //实例属性
}

@decorator
class DecorativeClass {
  // ...
}

// 利用 IIFE 实现传参
function decorator(...param): ClassDecorator {
  return target => {
    (target as any)[param[0]] = param[1]; // 静态属性
    Object.assign(target.prototype, ...list)// 实例属性
  }
}

@decorator('foo', 'bar')
class ParamDecorativeClass {
  // ...
}

console.log((ParamDecorativeClass as any).foo);

```

> 装饰器对类的行为的改变，是代码 **编译** 时发生的，而不是在运行时。这意味着，装饰器能在编译阶段运行代码。

- class 装饰器
- 属性装饰器
  - 似乎没什么用
  - 原因是装饰器的本意是要“装饰”类的 实例*^instance^* ，但是这个时候实例还没生成，所以只能去装饰 原型*^prototype^* 
  - 由于无法直接在类的顶层创建直接修改原型的语句，因此会产生一个和实例同名的属性，从而原型上的属性会直接被实例上的属性覆盖。
- 方法装饰器
- 参数装饰器
  - 也没什么用
- 装饰器应用

## TypeScript 编译

*TypeScript* 通过 `tsconfig.json` 修改编译选项，可以：

1. 用于标识 *TypeScript* 项目的根路径
2. 用于配置 *TypeScript* 编译器
3. 用于指定编译的文件

### 重要字段

1. *files* - 设置要编译的文件的名称
2. *include* - 设置需要进行编译的文件，支持路径模式匹配
3. *exclude* - 设置无需进行编译的文件，支持路径模式匹配
4. *compilerOptions* - 设置与编译流程相关的选项

### CompilerOptions

*compilerOptions* 支持很多选项，常见的有 `baseUrl`、 `target`、`baseUrl`、 `moduleResolution` 和 `lib` 等。

```json
{
  "compilerOptions": {

    /* 基本选项 */
    "target": "es5",                       // 指定 ECMAScript 目标版本: 'ES3' (default), 'ES5', 'ES6'/'ES2015', 'ES2016', 'ES2017', or 'ESNEXT'
    "module": "commonjs",                  // 指定使用模块: 'commonjs', 'amd', 'system', 'umd' or 'es2015'
    "lib": [],                             // 指定要包含在编译中的库文件
    "allowJs": true,                       // 允许编译 javascript 文件
    "checkJs": true,                       // 报告 javascript 文件中的错误
    "jsx": "preserve",                     // 指定 jsx 代码的生成: 'preserve', 'react-native', or 'react'
    "declaration": true,                   // 生成相应的 '.d.ts' 文件
    "sourceMap": true,                     // 生成相应的 '.map' 文件
    "outFile": "./",                       // 将输出文件合并为一个文件
    "outDir": "./",                        // 指定输出目录
    "rootDir": "./",                       // 用来控制输出目录结构 --outDir.
    "removeComments": true,                // 删除编译后的所有的注释
    "noEmit": true,                        // 不生成输出文件
    "importHelpers": true,                 // 从 tslib 导入辅助工具函数
    "isolatedModules": true,               // 将每个文件做为单独的模块 （与 'ts.transpileModule' 类似）.

    /* 严格的类型检查选项 */
    "strict": true,                        // 启用所有严格类型检查选项
    "noImplicitAny": true,                 // 在表达式和声明上有隐含的 any类型时报错
    "strictNullChecks": true,              // 启用严格的 null 检查
    "noImplicitThis": true,                // 当 this 表达式值为 any 类型的时候，生成一个错误
    "alwaysStrict": true,                  // 以严格模式检查每个模块，并在每个文件里加入 'use strict'

    /* 额外的检查 */
    "noUnusedLocals": true,                // 有未使用的变量时，抛出错误
    "noUnusedParameters": true,            // 有未使用的参数时，抛出错误
    "noImplicitReturns": true,             // 并不是所有函数里的代码都有返回值时，抛出错误
    "noFallthroughCasesInSwitch": true,    // 报告 switch 语句的 fallthrough 错误。（即，不允许 switch 的 case 语句贯穿）

    /* 模块解析选项 */
    "moduleResolution": "node",            // 选择模块解析策略： 'node' (Node.js) or 'classic' (TypeScript pre-1.6)
    "baseUrl": "./",                       // 用于解析非相对模块名称的基目录
    "paths": {},                           // 模块名到基于 baseUrl 的路径映射的列表
    "rootDirs": [],                        // 根文件夹列表，其组合内容表示项目运行时的结构内容
    "typeRoots": [],                       // 包含类型声明的文件列表
    "types": [],                           // 需要包含的类型声明文件名列表
    "allowSyntheticDefaultImports": true,  // 允许从没有设置默认导出的模块中默认导入。

    /* Source Map Options */
    "sourceRoot": "./",                    // 指定调试器应该找到 TypeScript 文件而不是源文件的位置
    "mapRoot": "./",                       // 指定调试器应该找到映射文件而不是生成文件的位置
    "inlineSourceMap": true,               // 生成单个 soucemaps 文件，而不是将 sourcemaps 生成不同的文件
    "inlineSources": true,                 // 将代码与 sourcemaps 生成到一个文件中，要求同时设置了 --inlineSourceMap 或 --sourceMap 属性

    /* 其他选项 */
    "experimentalDecorators": true,        // 启用装饰器
    "emitDecoratorMetadata": true          // 为装饰器提供元数据的支持
  }
}
```

## 模块

使用 ES6 模块语法即可

```typescript
export const someVar = 123; // 导出
import {someVar} from 'module' // 导入
```

### 什么是 `place`

我提及被检查的 `place` 时，我想表达的是在这个 `place` 上，TypeScript 将会检查以下内容（例如一个 `foo` 的 `place`）：

- 如果这个 `place` 表示一个文件，如：`foo.ts`，欢呼！
- 否则，如果这个 `place` 是一个文件夹，并且存在一个文件 `foo/index.ts`，欢呼！
- 否则，如果这个 `place` 是一个文件夹，并且存在一个 `foo/package.json` 文件，在该文件中指定 `types` 的文件存在，那么就欢呼！
- 否则，如果这个 `place` 是一个文件夹，并且存在一个 `package.json` 文件，在该文件中指定 `main` 的文件存在，那么就欢呼！

从文件类型上来说，我实际上是指 `.ts`， `.d.ts` 或者 `.js`

就是这样，现在你已经是一个模块查找专家（这并不是一个小小的成功）。

### 重写类型的动态查找

通过 `declare module 'somePath'` 声明一个全局模块的方式，来解决查找模块路径的问题。

```typescript
// global.d.ts
declare module 'foo' {
  // some variable declarations
  export var bar: number;
}

// anyOtherTsFileInYourProject.ts
// 被重写了
import * as foo from 'foo';
// TypeScript 将假设（在没有做其他查找的情况下）
// foo 是 { bar: number }
```

## global.d.ts

- `global.d.ts` 是一种扩充 `lib.d.ts` 很好的方式，如果你需要的话。
- 当你从 `JS` 迁移到 `TS` 时，定义 `declare module "some-library-you-dont-care-to-get-defs-for"` 能让你快速开始。

## 环境声明

环境声明允许你安全地使用现有的 JavaScript 库，并且能让你的 JavaScript、CoffeeScript 或者其他需要编译成 JavaScript 的语言逐步迁移至 TypeScript。

### 声明文件

- 通过 `declare` 关键字来告诉 TypeScript，你正在试图表述一个其他地方已经存在的代码；
- 把这些声明放入 `.ts` 或者 `.d.ts` 里。

语法

- [`declare var`](https://ts.xcatliu.com/basics/declaration-files.html#declare-var) 声明全局变量
- [`declare function`](https://ts.xcatliu.com/basics/declaration-files.html#declare-function) 声明全局方法
- [`declare class`](https://ts.xcatliu.com/basics/declaration-files.html#declare-class) 声明全局类
- [`declare enum`](https://ts.xcatliu.com/basics/declaration-files.html#declare-enum) 声明全局枚举类型
- [`declare namespace`](https://ts.xcatliu.com/basics/declaration-files.html#declare-namespace) 声明（含有子属性的）全局对象
- [`interface` 和 `type`](https://ts.xcatliu.com/basics/declaration-files.html#interface-和-type) 声明全局类型
- [`export`](https://ts.xcatliu.com/basics/declaration-files.html#export) 导出变量
- [`export namespace`](https://ts.xcatliu.com/basics/declaration-files.html#export-namespace) 导出（含有子属性的）对象
- [`export default`](https://ts.xcatliu.com/basics/declaration-files.html#export-default) ES6 默认导出
- [`export =`](https://ts.xcatliu.com/basics/declaration-files.html#export-1) commonjs 导出模块
- [`export as namespace`](https://ts.xcatliu.com/basics/declaration-files.html#export-as-namespace) UMD 库声明全局变量
- [`declare global`](https://ts.xcatliu.com/basics/declaration-files.html#declare-global) 扩展全局变量
- [`declare module`](https://ts.xcatliu.com/basics/declaration-files.html#declare-module) 扩展模块
- [`/// `](https://ts.xcatliu.com/basics/declaration-files.html#san-xie-xian-zhi-ling) 三斜线指令
