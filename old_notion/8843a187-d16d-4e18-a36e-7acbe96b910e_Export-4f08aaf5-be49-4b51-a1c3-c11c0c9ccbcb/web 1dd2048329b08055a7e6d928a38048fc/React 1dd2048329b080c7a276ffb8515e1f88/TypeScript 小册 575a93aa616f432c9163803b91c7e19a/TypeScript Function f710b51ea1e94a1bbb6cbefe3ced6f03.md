# TypeScript Function

# TypeScript Function

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

```tsx
// 关闭双向协变后 List<Dog> 能否为 List<Animal> 的子类型？class Animal {
    name: string;}
class Dog extends Animal {
    bark() {
        console.log("Woof!");    }
}
class List<T> {
    elements: T[] = [];    add(element: T) {
        this.elements.push(element);    }
}
let animalList: List<Animal> = new List<Animal>();let dogList: List<Dog> = new List<Dog>();// 在关闭双向协变的情况下animalList = dogList; // 错误，List<Dog> 不是 List<Animal> 的子类型
```