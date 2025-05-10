# TypeScript 高级类型概念

# TypeScript 高级类型概念

TypeScript 中的高级类型概念，用于增强类型系统的能力，让开发者可以更灵活地定义和操作类型

1. 类型别名 (Type Aliases)。
2. 字面量类型（Literal Types）
3. 类型推断（Type Inference）
4. 泛型 (Generics)。
5. 联合类型 (Union Types)。
6. 交叉类型 (Intersection Types)。
7. 索引类型 (Index Types)。
8. 映射类型 (Mapped Types)。
9. 类型断言 (Type Assertion)。
10. 类型守卫（Type Guards）
11. 字面量类型 (Literal Types)。
12. 可辨识联合 (Discriminated Unions)。
13. 条件类型（Conditional Types）
    1. `infer`

### 交叉类型

**定义：**

1. 通过使用 `&` 运算符，可以将多个类型合并为一个类型
2. 同时满足A和B两个类型

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

- 泛型默认值
- 泛型约束
- 类型别名中的泛型
- 接口泛型
- 类泛型
- 函数泛型

**泛型默认值**

```tsx
type MyGenericType<T = string> = { // T = string;在T没有指定类型时为string类型    value: T;};
```

**泛型约束**

- 使用`extends`实现
- 可以确保泛型函数或类中使用的类型道具有某些特定的属性或行为
- 用于限制泛型类型参数的类型
- 类型必须是约束类型的超集
- 可以确保泛型函数或类中使用的类型道具有某些特定的属性或行为

```tsx
type ResStatus<ResCode extends number = 10000> = ResCode extends 10000 | 10001 | 10002  ? 'success'  : 'failure';// ResCode 是一个泛型类型参数，它默认为 10000。// extends number = 10000 表示 ResCode必须是 number 类型，且默认值为 10000。// ResCode extends 10000 | 10001 | 10002// 如果 ResCode 的值是 10000、10001 或 10002 中的一个，则返回 'success'，否则返回 'failure'。
```

**类型别名中的泛型**

- 接受一个未知类型

应用场景一

一个典型的应用场景，定义一个联合类型，但是另外一个类型不确定，使用范型，可以在使用时定义最后不确定的那个类型

```tsx
// 定义三个类型 未知类型T ｜ number ｜ stringtype Factory<T> = T | number | string// 确定未知类型type Fnum = Factory<boolean>let a:Funm //number、string、boolean
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
- 索引签名类型使得 TypeScript 中的对象能够拥有动态的属性
- 允许定义对象的索引类型和索引返回值类型
- 通过索引签名，可以在对象中动态添加属性，或者通过动态的属性名来获取属性值
- 使用场景：重构代码时，属性太多，不想编写类型，但是又要防止报错

**索引类型查询**

- 获取对象可被索引的键的类型
- 使用 `keyof` 关键字可以实现索引类型查询
- `keyof`通常返回的是一个联合类型
- 所以索引类型查询的结果就是一个联合类型？

**索引类型访问**

- 使用类型的索引来访问其属性的类型
- 通过 `T[K]` 来访问 `T` 中属性 `K` 的类型。
- 可以用于获取对象的属性类型，或者用于动态生成的函数签名
- 代码示例中还有一个**特殊用法**

```tsx
// 索引签名类型type AllStringTypes = {
  [key:string]: string}
// 索引类型查询type Keys = keyof Foo
// string ... 生成一个对象属性类型的字面量类型，同时也是一个联合类型// 索引类型访问（索引值类型！！！）interface Foo {
  propA: number;  propB: boolean;  propC: string;}
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

```tsx
interface Person {
    name: string;    age: number;}
// 定义一个通用的映射类型，将对象的所有属性转换为可选属性type Optional<T> = {
    [K in keyof T]?: T[K]; // 使用 in 操作符遍历对象的所有属性; keyof 是获取 T 的所有属性键构成的联合类型};// 使用 Optional 映射类型，将 Person 类型中的所有属性转换为可选属性type OptionalPerson = Optional<Person>;// 等价于 type OptionalPerson = { name?: string; age?: number; }
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
    - 非空断言
        - `!` - 表示剔除null和undefined

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

```tsx
type MyConditionalType<T> = T extends U ? X : Y;
```

特殊用法：

1. **联合类型中的条件类型**：条件类型常常用于联合类型中，以便根据联合类型的成员属性来选择相应的类型。
2. **分布式条件类型**：当条件类型应用于联合类型时，它会被称为分布式条件类型。这意味着条件类型会自动分发到联合类型的每个成员上，并将结果组合成一个新的联合类型。

应用场景：

1. **条件渲染**：在编写泛型代码时，可能需要根据输入类型的属性或关系来进行不同的处理或操作。条件类型使得能够根据条件来选择不同的类型，从而实现条件渲染。
2. **类型映射**：条件类型可以用于类型映射，使得能够根据输入类型的不同特征来映射到不同的输出类型，从而实现更灵活的类型转换和处理。
3. **类型推断**：通过条件类型，可以实现复杂的类型推断，使得能够根据已知类型推断出其他类型的信息，从而提高类型安全性和编码效率。

**Infer**

`infer` 关键字通常与条件类型一起使用，用于推断类型。

一下是一个典型的用法

```tsx
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;function foo(): string {
    return 'hello';}
type FooReturnType = ReturnType<typeof foo>; // 推断 FooReturnType 为 string 类型
```

**分布式条件类型**

- 条件类型应用于联合类型是，它会被称为分布式条件类型
- 条件类型会自动分发到联合类型的每个成员上，并将结果组合成一个新的联合类型

```tsx
type NonNullable<T> = T extends null | undefined ? never : T;type NullableString = string | null | undefined;type NonNullableString = NonNullable<NullableString>; // 分布式条件类型应用于联合类型// NonNullableString 的类型为 string
```