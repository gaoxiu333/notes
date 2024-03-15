# TypeScript Cheat Sheet

* [原始参考-官方](https://www.typescriptlang.org/cheatsheets)

### Types

* **关键点**

  * 它的完整名称是"类型别名"，用于为类型文字提供名称

  * 支持比接口更丰富的类型系统功能。

* Type VS Interface

  * 接口只能描述对象形状 

  * 接口可以通过多次声明来扩展 

* 将类型视为变量

  * 就像变量可以在不同的范围内声明和使用一样，类型也可以在不同的作用域中声明和使用，类型具有相同的语义。

* 使用 Utility 类型工具

  * TypeScript 包含很多全局类型,这些类型将帮助您完成类型系统中的常见任务。

#### 对象字面量语法

还不完整，参考Intefrace

```typescript
type JSONResponse = {
    version: number;                        // Field
    payloadSize: number;                    // 
    outOfStock?: boolean;                   // 可选
    update: (retryTimes: number) => void;   // 箭头函数
    update(retryTimes: number): void;       // 函数
    (): JSONResponse;                       // 类型是可以调用的？
    [key: string]: number;                  // 接受任何key
    new(s: string): JSONResponse;           // ？？
    readonly body: string;                  // 只读
}
```

#### 常用类型

几种常见的类型声明方式

* 原始类型

* 对象字面量类型

* 元祖

* 联合类型

* 类型索引

```typescript
// 原始类型
type SanitizedInput = string;
type MissingNo = 404

// 对象字面量类型
type Location ={
  x:number;
  y:number;
}

// 元组 - 元组是一个特殊情况下的数组,具有特定索引的已知类型。
type Data = [
  location:Location,
  timestamp:string
]

// 联合类型
type Size = 'samll' | 'medium' | 'large'

// Intersection Types - 一种合并类型的方法
type Location = {x:number} & {y:number}
// {x:number,y:number}

// 类型索引 - 从类型的子集提取和命名的一种方法
type Response = {data:{...}}
type data = Response['data']

// 从具体值创建类型 - 通过 typeof 操作符重用现有 JavaScript 运行时值的类型。
const data = {...}
type Data = typeof data

// 从返回值创建类型 - 重用函数的返回值作为类型。
const createFixtures = () => { ... }
type Fixtures = ReturnType<typeof createFixtures>

function test(fixture:Fixtures){}

// 从Module创建类型 
const data: import("./data").data


```

#### 其他

* 很少见，在大多数TypeScript应用程序中很少见

* 但是这些功能对于构建库很合适

* Mapped Types

* Conditional Types

* Template Union Types

```typescript
// Mapped Types - 行为就像类型系统的映射语句,允许输入类型改变结构的新类型。
type Artist = { name:string, bio: string}

// 循环遍历类型通用参数"Type"中的每个字段
// 将type设置为一个函数，并将原始类型作为参数
type Subscriber<Type> = {
  [Property in keyof Type]:(newValue:Type[Property]) => void
}
type ArtistSub = Subscriber<Artist>
// 参考以下
{
  name:(nv:string)=>void
  bio:(nv:string)=>void
}

// Conditional Types - 充当类型系统内的if语句。通过泛型创建，然后通常用于减少类型联合中的选项数量。
type hasFourLegs<animal> = Animal extends {legs:4} ? Animal : never
type Animals = Bird | DOg | Ant | Wolf;
type FourLegs = HasFourLegs<Animals>
// Dog | Wolf

// Template Union Types - 模板字符串可用于组合和操作类型系统中的文本。
type SupportedLangs = 'en' | 'pt' | 'zh'
type FooterLocaleIDs = 'header' | 'foooter'

type AllLocaleIds = `${SupportedLangs}_${FooterLocaleIds}_id`
// "en_header_id" | "en_footer_id" | "pt_header_id" | "pt_footer_id"| "zh_


```

### &#x20;Interface

#### 关键点

* 用于描述物体的形状,并且可以由其他人扩展。

* JavaScript中的几乎所有东西都是对象，而接口的构建是为了匹配它们的运行时行为。

#### 内置类型

* 原始类型

  * boolean, string, number,undefined, null, any,unknown, never, void,bigint, symbol

* 内置JS对象

  * Date, Error, Array, Map,Set, Regexp, Promise

* 类型字面量

  * Obejct:`{field: string}`

  * Function:`(arg:number)=>string`

  * Arrays:`string[]`or `Array<string>`

  * Tuple:`[string,number]`

* 避免

  * Object, String, Number, Boolean

#### 常见语法

```typescript
// HTTPAble: 可选地从现有接口或类型中获取属性
interface JSONResponse extends Response, HTTPAble {
    version: number;
    payloadSize: number;
    outOfStock?: boolean;
    update: (retryTimes: number) => void;
    update(retryTimes:number): void;
    (): JSONResponse;
    new(s: string): JSONResponse;
    [key: string]: number;
    readonly body: string;
}
```

#### 常见类型声明方式

* 普通

* 重载

* Get\&Set

* 合并拓展

* 类的一致性

```typescript
//普通 - 声明一个可以在界面中更改的类型
interface APICal<Response> { // 类型传参
  data: Response
}

// 使用
const api:APICall<ArtworKcall> = ...
api.data // Artwork

// 可以通过extends关键字约束泛型参数接受的类型。
// 对类型设置约束,这意味着只能使用具有"状态"属性的类型
interface APICall‹Response extends {status:number}>{
  data:Response
}
const api:APICall<ArtworkCall> = ...
api.data.status

// 重载 - 一个可调用接口可以对不同的参数集有多个定义
interface Expect{
  (matcher:boolean):string
  (matcher:string):boolean
}

// Get&Set - 对象可以有自定义的 getter 或 setter
interface Ruler{
  get size():number
  set size(value:number:string)
}
// 使用
const r:Ruler = ...
r.size = 12
r.size = '36'

// Extension via merging - 接口是合并的，因此多个声明将向类型定义添加新字段。
interface APICall{
  data:Response
}

interface APICall{
  error?:Error
}

// Class conformance - 你可以通过实现确保一个类符合一个接口
interface Syncable {sync():void}
class Account implements Syncable{...}
```

### Class

#### 关键点

* TypeScript 类对 ES2015 JavaScript 类有一些特定于类型的扩展，以及一个或两个运行时添加。

#### 常见语法

```typescript

// extends 继承 Account 类
// implements 确保类符合一组接口或类型
class User extends Account implements Updatable, Serializable {
    id: string;                           // 字段
    displayName?: boolean                 // 可选
    name!: string                         // 就在那里？
    #attributes: Map<any, any>            // 私有属性
    roles = ["user"]                      // 带有默认值
    readonly createdAt = new Date()。     // 只读，并且带有默认值

    constructor(id:string,email:string){ // 代码被new调用
        super(id)
        this.email = email               // strict:true 根据字段检查此代码，以确保其设置正确
        ...
    }
    
    // 描述类方法(和箭头函数字段)的方法
    setName(name:string) {this.name=name} 
    verifyName = (name:string)=>{...}
    
    // 具有 2 个重载定义的函数
    sync():Promise<{...}>
    sync(cd:((result:string)=>void)):void
    sync(cd?:((result:string)=>void)):void | Promise<{...}>{...}

    // Getters 和 Setters
    get accountID(){...}
    set accountID(value:string){}

    // 私有访问只是对这个类，受保护的允许子类。仅用于类型检查，默认为 public。
    private makeRequest(){...}
    protected handleRequest(){...}
    
    // 静态变量和金泰方法
    static #userCount = 0
    static registerUser(user:User){...}
    
    // 用于设置静态变量的静态块。 “this”指的是静态类
    static {this.#userCount = -1}
}
```

#### 常见类型出声明方式

* 普通

* 创建类型和实例

* private vs #private

* 类型和值

声明一个可以在类方法中更改的类型。

```typescript
// 普通 -  声明一个可以在类方法中更改的类型。
class Box<Type>{ // 定义类型参数
  contents: Type
  constructor(value: Type){ // 使用类型参数
    this.contents = value
  }
}
const stringBox = new Box('a package')

// 创建类和实例 - 新 ABC 的参数来自构造函数。
class ABC{...}
const abc = new ABC()

// private vs #private - 前缀 private 是仅类型添加的，在运行时不起作用。在以下情况下，类外部的代码可以访问item属性：
class Bag{
  private item:any
}
// 与 #private 相比，它是运行时私有的，并且在 JavaScript 引擎中强制要求它只能在类内访问：
class Bag {
  #item:any
}

// 类型和值 - 令人惊讶的是,类既可以用作类型,也可以用作值。
const a:Bag = new Bag()

// 请不要这样做！
class C implements Bag{}
```

#### TypeScrpt 独有特性

这些功能是特定于 TypeScript 的语言扩展，可能永远无法以当前语法应用于 JavaScript。

* Parameter Properties

* Abstract Classes

* Decorators and Attributes

```typescript
// Parameter Properties - 特定于 TypeScript 的类扩展，用于自动将实例字段设置为输入参数
class Location{
  constructor(public c:number,public y:number){}
}
const loc = new Location(20,40)
loc.x // 20
loc.y //40

// Abstract Classes - 一个类可以被声明为不可实现，但可以被声明为存在，以便在类型系统中被子类化。班级成员也可以。
abstract class Animal{
  abstract getName():string
  printName(){
    console.log('hello,' + this.getName())
  }
}
clas Dog extends Animal{
  getName():{..}
}

// Decorators and Attributes - 可以在类、类方法、访问器、属性和方法参数上使用修饰器。
import {Syncable,triggersSync,preferCache,required} from 'mylib'

@Syncable
class User{
  @triggersSync()
  save(){...}

  @preferCache(false)
  get displayName(){...}
  update(@required info: Partial<User>){...}
}
```

#### class中的this

* 函数中“this”的值取决于函数的调用方式。它不能保证始终是您在其他语言中可能习惯的类实例。您可以使用“此参数”

* 您可以使用“this parameters”、使用 bind 函数或箭头函数在问题发生时解决该问题。

### 控制流

#### 关键点

* CFA 几乎总是采用并集，并根据代码中的逻辑减少并集内的类型数。

* 大多数情况下，CFA 在自然的 JavaScript 布尔逻辑中工作，但有一些方法可以定义自己的函数，这些函数会影响 TypeScript 缩小类型范围的方式。

#### If Statements

大多数范围来自 if 语句中的表达式，其中不同类型的运算符在新作用域内缩小

* typeof(for primitives)

* intranceof(for classes)

* "property" in object(for object)

* type-guard function(for anything)

* Expressions

```typescript
// 
const imput = getUserInput()
input // string | number

if(typeof input === 'string'){
  input // string
}

// instanceof(for classes)
const imput = getUserInput()
input // number | number[]

if(input instalof Array){
  input // number[]
}

// 'property' in object(for objects)
const input = getUserInput()
input // string | {error:...}

if('error' in input){
  input // {error:...}
}

// type-guard functions (for anything)
const input = getUserInput()
input // number | number[]

if(Array.isArray(input)){
  input // number[]
}

//Expressions - 在执行布尔运算时，缩小也发生在与代码相同的一行上
const input = getUserInput()
input // string | number

const inputLength = (typeof input === 'string' && input.length) || input 
// input:string
```

#### Discriminated Unions

```typescript
// 工会的所有成员都有相同的财产名称，终审法院可以对此进行歧视。
type Responses =
  | {status:200,data:any}
  | {status:301,to:string}
  | {status:400,error:Error}

// 使用
const response = getResponse()
response // Responses

switch(response.status){
  case 200 return response.data
  case 301 return redirect(response.to)
  case 400 return response.error
}
```

#### Type Guards

一个函数，其返回类型描述新作用域的 CFA 更改（如果为 true）。

```typescript
// [obj is APIErrorResponse]:返回类型 position 描述 whattheassertionis
function isErrorResponse(obj:Response):[obj is APIErrorResponse]{
  return obj instanceof APIErrorResponse
}

// 使用
const response = getResponse()
response // Response | APIErrorResponse

if(isErrorResponse(response)){
  response // APIErrorResponse
}
```

#### Assertion Functions

描述影响当前作用域的 CFA 更改的函数，因为它会抛出而不是返回 false。

```typescript
function asserResponse(obj:any):[asserts obj is SuccessResponse]{
  if(!(obj instanceof SuccessResponse)){
    throw new Error('Not a success!')
  }
}

// 使用
const res = getResponse()
res // SuccessResponse | ErrorResponse

assertResponse(res) // 断言函数改变当前作用域或抛出

res // SuccessResponse
```

#### Assignment

* 使用 'as const' 缩小类型

* 通过相关变量跟踪

* 重新分配类型

```typescript
// 使用 'as const' 缩小类型 - 对象中的子字段被视为可以更改，并且在赋值期间，类型将被“扩大”为非文本版本。前缀“as const”将所有类型锁定为其文本版本。
const data1 = {
  name:"Zagreus"
}
// 类型
typeof data1 = {name:string}

const data2 = {
  name:'Zagreus'
} as const
// 类型
typeof data2 = {name:"Zagreus"}

// 通过相关变量跟踪
const response = getResponse()
const isSuccessResponse = res instanceof SuccessResponse

if(isSuccessResponse){
  res.data // SuccessResponse
}

// 重新分配更新类型
let data:string | number = ...
data // string | number
data = 'hello'
data // string
```




```typescript
// Object
{field:}
```









111
