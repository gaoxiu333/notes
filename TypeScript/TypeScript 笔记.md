## TypeScript 初始化

### 初始化

安装TypeScript，并且使用默认配置初始化一个TS项目：

```
npm i typescript -D
npx tsc --init
```

- [配置参考-官方](https://www.typescriptlang.org/tsconfig)

### 构建目标

- target

- lib

- noLib

target选项制定了编译器将会生成的JavaScript代码的目标版本

lib用于指定编译器需需要的类型生命文件（`.d.ts`文件）列表

- DOM

- WebWorker等

noLib用于禁用默认的TypeScrit类型库引用

- 如在node环境不包含DOM

- 或者自定义JS对象类型

### 构建解析

- files

- include

- exclude

files只能指定完整的路径，文件越来越多，就使用include和exclude相结合，对文件进行匹配。

### 两个根目录

- baseUrl

- rootDir

baseUrl表示文件解析的根目录；

rootDir表示项目文件的根目录

> 没搞懂

### 配置别名

- 支持JSON

- module支持

- es2022 - 支持Top-Level Await

- 声明文件

### 一些常用配置

- `strictNullChecks` - null和undefined

- `strictFunctionTypes` - 双向协变

- `noImpliciAny`

- 配置后必须显式指定`any`类型



## TypeScript 类型基础

TypeScript 中有许多内置类型，它们用于表示 JavaScript 中常见的数据类型和数据结构。以下是 TypeScript 中一些常用的内置类型，也包含了一些特殊类型：

**基本类型：**

- `number`: 表示数字类型，包括整数和浮点数。

- `string`: 表示字符串类型。

- `boolean`: 表示布尔类型，只有两个值：`true`和`false`。

- `null`: 表示空值。

- `undefined`: 表示未定义值。

- `symbol`: 表示唯一的、不可变的值，通常用于对象属性的键。

- `bigint`: 表示任意精度的整数。

- `void`: 表示没有任何类型，通常用于函数没有返回值的情况。

**特殊类型：**

- `any`: 表示任意类型，允许任何值的赋值和操作，通常用于旧代码或跳过类型检查。

- `unknown`: 表示未知类型，与`any`类似，但对其进行操作之前需要进行类型检查或类型断言。

- `never`：表示永远不会发生的值的类型

**复合类型：**

- `object`: 表示非原始类型的值，即除了`number`、`string`、`boolean`、`bigint`、`symbol`、`null`和`undefined`之外的类型。

- `Array`: 表示数组类型。

- `Tuple`: 表示固定长度和类型的数组。

- `Function`: 表示函数类型。

- `Map`: 表示键值对集合，其中键可以是任意类型。

- `Set`: 表示一组唯一值的集合。

- `Promise`: 表示异步操作的结果。

**特殊数据结构**

- `enum`

**类型操作符：**

- `typeof`: 返回一个值的类型的字符串表示。

- `keyof`: 返回一个类型的所有键的联合类型。

- `in`: 判断一个属性是否存在于一个类型中。

**不建议**

- Object - 表示所有类型的值，尽量不用。

- 包装类型 - 少用！

- Sring

- Number

- ...

### 枚举

- 一种特殊的数据类型，它并不是对象类型，它是一个独立的概念

- 用来定义一组命名的常量值

- 默认情况下，值是下标，也就是数字类型

- 应用场景：状态表示、选项表示、常量值表示

- `enum`

**枚举和元祖的区别？**

- 枚举定义一组命名的常量值，可以反向映射，允许通过值或者成员名称，通常表示一组相关的常量

- 元祖表示固定长度和固定类型的数组，适用于将不同类型的值组合在一起的情况

```
// 枚举
enum Color{ Red,Green,Blue }
let col = Color.Red // col = 0 

// 联合类型
type Color = 'red' | 'blue'
```

### 配置

- `strictNullChecks`

- 选项被开启时，`null` 和 `undefined` 不再是所有类型的子类型，

- 这意味着变量不能隐式地具有 `null` 或 `undefined` 值，除非显式地声明其类型为 `null` 或 `undefined`。

- `void` 和 `null`、`undefined` 并不等价

### 类型问题

1. `object`、`Object`、`{}` 有什么区别？

- 小写的 `object` 表示除了基础类型（`number`、`string`、`boolean`、`bigint`、`symbol`、`null` 和 `undefined`）以外的所有类型，包括函数、数组、对象等。当你声明一个类型为 `object` 时，你实际上指定了该变量的值必须是一个对象。

- 大写的 `Object` 表示所有非原始类型的值，包括对象、数组、函数等，但不包括 `null` 和 `undefined`。当你声明一个类型为 `Object` 时，你可以赋予它任何值。

- 空的花括号 `{}` `{}` 类型表示任意对象类型，这意味着该变量可以存储任何结构的对象，但是它必须是一个对象

1. 几种特殊类型的区别？

- `any`

- 放弃类型检查，表示任意类型

- `unknown`

- 表示未知类型，类似`any`，但是接受类型断言和类型检查

- `never`

- 表示永远不会发生值的类型

- 通常用于函数，表示函数不会正常返回或者抛出异常

- 类型推导的尽头就是`never`

### 函数

- 函数的类型签名

- `voild`返回值

- 可选参数

- rest参数

- 重载

- 异步函数

- 特殊函数：异步函数、Generator

## TypeScript 类型层级

- 类型层级指的是所有类型的兼容关系

- 类型兼容性

### 类型兼容性判断

```
T extends D ? 1:2 // 如果T是D的子类型，返回1，否则返回2
```

![sbXodXeNZyk3M-AzmKNhcUoqa40adEDb4ezLAMyZjjc=.blob](file://./workspace/19756965-28fc-42d8-8cfc-5102bb22d6d3/assets/sbXodXeNZyk3M-AzmKNhcUoqa40adEDb4ezLAMyZjjc=.blob)



## 高级类型概念

 TypeScript 中的高级类型概念，用于增强类型系统的能力，让开发者可以更灵活地定义和操作类型

1. 类型别名 (Type Aliases)。

1. 字面量类型（Literal Types）

1. 类型推断（Type Inference）

1. 泛型 (Generics)。

1. 联合类型 (Union Types)。

1. 交叉类型 (Intersection Types)。

1. 索引类型 (Index Types)。

1. 映射类型 (Mapped Types)。

1. 类型断言 (Type Assertion)。

1. 类型守卫（Type Guards）

1. 字面量类型 (Literal Types)。

1. 可辨识联合 (Discriminated Unions)。

1. 条件类型（Conditional Types）

1. `infer`

### 交叉类型

**定义：**

1. 通过使用 `&` 运算符，可以将多个类型合并为一个类型

1. 同时满足A和B两个类型

**特性：**

- **基础类型合并**

- 基础数据交叉，类型不同时直接返回`never`

- **对象属性合并**

- 不同命属性合并

- 同名属性，类型不同直接返回`nerver`且导致无法赋值

- 修饰符不同，似乎也会产生影响，像叠buff一样叠加

- **联合类型合并**

- 取交集

- **函数交叉**

- 没有找到具体应用场景

- **小问题**

- 使用交叉类型的分布式特性避免？

### 泛型

几种常用的泛型用法

- 类型别名中的泛型

- 接口泛型

- 类泛型

- 函数泛型

泛型的特性

- 泛型默认值

- 泛型约束

**泛型默认值**

```
type MyGenericType<T = string> = { // T = string;在T没有指定类型时为string类型
    value: T;
};
```

**泛型约束**

- 使用`extends`实现
- 可以确保泛型函数或类中使用的类型道具有某些特定的属性或行为
- 用于限制泛型类型参数的类型
- 类型必须是约束类型的超集

```ts
type ResStatus<ResCode extends number = 10000> = ResCode extends 10000 | 10001 | 10002
  ? 'success'
  : 'failure';
// ResCode 是一个泛型类型参数，它默认为 10000。
// extends number = 10000 表示 ResCode必须是 number 类型，且默认值为 10000。
// ResCode extends 10000 | 10001 | 10002 
// 如果 ResCode 的值是 10000、10001 或 10002 中的一个，则返回 'success'，否则返回 'failure'。
```

**类型别名中的泛型**

- 接受一个未知类型

应用场景一

一个典型的应用场景，定义一个联合类型，但是另外一个类型不确定，使用范型，可以在使用时定义最后不确定的那个类型

```
// 定义三个类型 未知类型T ｜ number ｜ string
type Factory<T> = T | number | string
// 确定未知类型
type Fnum = Factory<boolean>
let a:Funm //number、string、boolean 
```

**对象类型中的泛型 - 简单**

泛型嵌套

函数中的泛型

- 泛型在调用时被填充

Class中的泛型

- 被属性、方法或者装饰器消费

### 索引类型

索引类型（Index Types）是 TypeScript 中一种高级类型特性，允许我们使用类型的索引来访问其属性。这使得我们能够以一种动态的方式来定义类型，使代码更加灵活和可重用。

- 态访问对象属性的方式。

- 在编译时确定属性名称核型

- 常见的索引类型

- 索引签名类型

- 索引类型查询

- 索引类型访问（索引值）

**索引签名类型**

- 语法：`[key:string]:string`

- 定义对象动态属性，简单粗暴，比较适用于重构场景

- 索引签名类型使得 TypeScript 中的对象能够拥有动态的属性

- 允许定义对象的索引类型和索引返回值类型

- 通过索引签名，可以在对象中动态添加属性，或者通过动态的属性名来获取属性值

- 使用场景：重构代码时，属性太多，不想编写类型，但是又要防止报错

**索引类型查询**

- 查询key对字面量类型

- 使用 `keyof` 关键字可以实现索引类型查询（通常是key的字面量类型）

- `keyof`通常返回的是一个联合类型

- 所以索引类型查询的结果就是一个联合类型？

**索引类型访问**

- 使用类型的索引来访问其属性值的类型（这个就不一定是字面量类型了）

- 通过 `T[K]` 来访问 `T` 中属性 `K` 的值的类型

- 可以用于获取对象的属性类型，或者用于动态生成的函数签名

- 代码示例中还有一个**特殊用法**

```ts
// 索引签名类型
type AllStringTypes = {
  [key:string]: string
}

// 索引类型查询
type Keys = keyof Foo
// 属性1 ｜ 属性2 ... 生成一个对象属性类型的字面量类型，同时也是一个联合类型

// 索引类型访问（索引值类型！！！）
interface Foo {
  propA: number;
  propB: boolean;
  propC: string;
}

type PropTypeUnion = Foo[keyof Foo]; // string | number | boolean
```

### 映射类型

- 从现有类型创建新类型的强大工具

- 根据现有类型的结构动态地创建新的类型

**常用的映射类型工具**

- Partial

- Readonly

- Record

- 自定义映射类型

**自定义映射类型**

- 关键点： `K in keyof T`

- `T`是要遍历的对象类型；

- `keyof T`是获取`T`的所有属性键构成的联合类型；

- `K`是联合类型中的每一个属性键。

- `in` 操作符配合索引类型可以很方便地遍历对象的属性

```ts
interface Person {
    name: string;
    age: number;
}

// 定义一个通用的映射类型，将对象的所有属性转换为可选属性
type Optional<T> = {
    [K in keyof T]?: T[K]; // 使用 in 操作符遍历对象的所有属性; keyof 是获取 T 的所有属性键构成的联合类型
};

// 使用 Optional 映射类型，将 Person 类型中的所有属性转换为可选属性
type OptionalPerson = Optional<Person>;
// 等价于 type OptionalPerson = { name?: string; age?: number; }
```

### 类型断言

类型断言显式的告诉类型检查程序当前变量的类型，迫不得已时使用

- **语法**
  - 尖括号语法
  - as关键字

- **特殊断言**
  - 双重断言
    - 先断言道`any/unkown`再断言到具体类型
    - 如果两个类型没有公共类型时就需要双重断言了。

  - 非空断言`!` - 表示剔除null和undefined


### **类型守卫**

- 强大的推导能力

- 随着代码逻辑不断尝试收窄类型

- 类型的控制流分析 - 类型推导

- **几种类型守卫实现方式：**

- typeof类型守卫

- **instanceof 类型守卫**

- **自定义类型守卫**

- 留意`asserts`关键字

- in类型守卫

- 核心逻辑就是通过判断，追减收窄类型

### 条件类型

**语法**

```
type MyConditionalType<T> = T extends U ? X : Y;
```

特殊用法：

1. **联合类型中的条件类型**：条件类型常常用于联合类型中，以便根据联合类型的成员属性来选择相应的类型。

1. **分布式条件类型**：当条件类型应用于联合类型时，它会被称为分布式条件类型。这意味着条件类型会自动分发到联合类型的每个成员上，并将结果组合成一个新的联合类型。

应用场景：

1. **条件渲染**：在编写泛型代码时，可能需要根据输入类型的属性或关系来进行不同的处理或操作。条件类型使得能够根据条件来选择不同的类型，从而实现条件渲染。

1. **类型映射**：条件类型可以用于类型映射，使得能够根据输入类型的不同特征来映射到不同的输出类型，从而实现更灵活的类型转换和处理。

1. **类型推断**：通过条件类型，可以实现复杂的类型推断，使得能够根据已知类型推断出其他类型的信息，从而提高类型安全性和编码效率。

**Infer**

`infer` 关键字通常与条件类型一起使用，用于推断类型。

一下是一个典型的用法

```
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;

function foo(): string {
    return 'hello';
}

type FooReturnType = ReturnType<typeof foo>; // 推断 FooReturnType 为 string 类型
```

**分布式条件类型**

- 条件类型应用于联合类型是，它会被称为分布式条件类型

- 条件类型会自动分发到联合类型的每个成员上，并将结果组合成一个新的联合类型

```
type NonNullable<T> = T extends null | undefined ? never : T;

type NullableString = string | null | undefined;
type NonNullableString = NonNullable<NullableString>; // 分布式条件类型应用于联合类型
// NonNullableString 的类型为 string
```

## Class

### Class

- 结构

- 构造函数

- 属性

- 方法

- 访问符

- 修饰符

- `public`

- `private`

- `protected`

- `readonly`

- 此为操作性修饰符，其他为访问性修饰符

- `static`

- 类的操作

- 继承 - `extends`

- 重点：派生类对基类成员的访问与覆盖

- 访问：`super`

- 覆盖：`override`

- 实现 - `implements`

- 抽象类 - `abstract`

**public、private、protected 的区别？**

- public：在类、类的实例、子类中都能访问

- private：只能在类的内部访问

- protected：只能在类和子类中被访问

- 可以用来保护`constructor`表示该类只能被继承而不能被直接实例化

- 可以通过实例的方法访问

**Statc是用来干嘛的？**

- 静态成员，可以通过类本身直接访问的变量

- 它不会被实例继承

**什么是抽象类？什么是实现？**

- 抽象类描述类的结构，对类结构与方法的抽象，它无法声明静态的抽象成员

- 具体来说，一个抽象类描述了一个类中应当有哪些成员（属性方法等）

- 使用`abstract`关键字声明，也可以使用`interface`关键字实现

- 实现：使用`implements`来实现一个抽象类

- 必须完全实现抽象类的每一个抽象成员

- ts无法声明静态的抽象成员

### 装饰器

装饰器本质上是一个函数

- 类装饰器

- 方法装饰器

- 访问符装饰器

- 属性装饰器

- 参数装饰器

基于装饰器的依赖注入

- 控制反转与依赖注入



## Function

### 逆变和协变

- 逆变：

- 逆变发生在函数参数类型上，它表示参数类型的变化方向与函数类型的相反。

- 在逆变中，如果子类型的参数类型是父类型的参数类型的超集，则子类型可以赋值给父类型。

- 协变：

- 协变发生在函数返回值类型上，它表示返回值类型的变化方向与函数类型的相同

- 在协变中，如果子类型的返回值类型是父类型的返回值类型的子集，则子类型可以赋值给父类型。

- 双向协变：

- TypeScript默认开启选项，通过`strictFunctionTypes`配置修改

- 双向协变是一种特殊的类型关系，它表示类型之间的相互协变

- 双向协变则包括了参数类型和返回值类型的协变，使得子类型可以在参数类型和返回值类型上都是父类型的子类型。

- 双向协变是否应该关闭

- 双向协变增加了灵活性，但是会出现难以排查的安全性问题

- 可能会导致类型不匹配的错误在编译阶段不被捕获，而在运行时产生异常。

- 关闭双向协变后 List<Dog> 能否为 List<Animal> 的子类型？

- 答案是不能

- 这是因为关闭双向协变会禁止参数类型的协变，即使 `Dog` 是 `Animal` 的子类型，`List<Dog>` 也不能被视为 `List<Animal>` 的子类型。

```typescript
// 关闭双向协变后 List<Dog> 能否为 List<Animal> 的子类型？
class Animal {
    name: string;
}

class Dog extends Animal {
    bark() {
        console.log("Woof!");
    }
}

class List<T> {
    elements: T[] = [];

    add(element: T) {
        this.elements.push(element);
    }
}

let animalList: List<Animal> = new List<Animal>();
let dogList: List<Dog> = new List<Dog>();

// 在关闭双向协变的情况下
animalList = dogList; // 错误，List<Dog> 不是 List<Animal> 的子类型
```

## TypeScript 声明文件

草稿

- 工程能力

- 框架继承

- ES语法

- TSConfig

- Node API

### 类型检查指令

使用注释忽略TS全局配置

```
// 忽略下一行代码的类型检查
// @ts-ignore 

// 只有下一行类型报错时忽略下一行类型检查，否则不能使用（更人性化的@ts-ignore）
// @ts-expect-error 

// eslint 禁用下一行类型检查
/* eslint-disable-next-line */

// eslint 放在文件首行，禁用整个文件类型检查
/* eslint-disable */

// tsc 禁用检查
// @ts-nocheck
```

### 类型声明

#### 语法

- `declare module`

- `declare namespace`

- `declare`

- 类型声明和类型标注的区别是什么？

- 非代码文件？JSON?

- js文件？

- 全局变量或者改写全局变量

**不支持TS的npm包**

```
// .d.ts
declare module 'pkg' {
  const handler:()=>boolean
}

// main.ts
import foo from 'pkg'

const res = foo.handler()
```

**对代码文件导入**

- `.md`、`.css`、`.module.css`、`.png`等文件

markdown文件

```
// d.ts
declare module "*.d" {
  const raw:string;
  export default raw
}

// main.ts
import raw from './note.md'
const content = raw.replace('',...)
```

**修改全局变量**

- 使用`interface`声明类型时，如果有多个同名类型，则**自动合并**

```
// .d.ts
interface Window { // 将于工具类中的Window接口自动合并
  someKey:any
}
```

### 三斜线指令

- 类似ts的配置文件

- 它可以定制当前文件编译配置

- 也可以在没有模块化时，自己引入依赖

- 它的作用是声明当前文件依赖的其他类型声明

- 必须放在文件的顶部才能生效

### 其他问题

- React 中不引入React，就能使用是怎么做到的?

- `allowUmdGlobalAccess`

- TS 配置，开启后，React作为全局变量

``` 
export = React;
export as namespace React; // React 将作为全局变量，不需要导入
declare namespace React {
  // 省略了不必要的类型标注
  function useState<S>(initialState): [];
}
```
