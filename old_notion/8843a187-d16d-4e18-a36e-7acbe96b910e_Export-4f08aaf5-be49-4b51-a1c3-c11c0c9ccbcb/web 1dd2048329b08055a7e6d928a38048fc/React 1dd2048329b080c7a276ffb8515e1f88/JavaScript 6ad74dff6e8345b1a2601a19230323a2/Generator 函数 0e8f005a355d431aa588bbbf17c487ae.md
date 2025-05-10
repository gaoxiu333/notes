# Generator 函数

### Generator 函数的语法

### 语法

- `function * fn(){ yield}`
- 调用该函数后并不执行，但返回一个指向内部的指针对象（遍历器对象）

### API

- `for of`
- `yield`
- `yeild*`
- `next`方法和参数 - 在函数内部可以作为`yield`的返回值
    - 第一个`next`似乎永远没办法传递参数
- `this`

## 特性

1. 双向通信
    
    ```tsx
    function* interactiveGenerator() {
        const x = yield '请输入一个数字:';
        console.log(`你输入的是: ${x}`);
        yield `你输入了: ${x}`;
    }
    
    const gen = interactiveGenerator();
    console.log(gen.next().value); // '请输入一个数字:'
    console.log(gen.next(42).value); // '你输入了: 42'
    ```
    
2. `for...of`
    
    Generator 生成的迭代器可以直接用 for...of 遍历。
    
    ```tsx
    function* numbers() {
        yield 1;
        yield 2;
        yield 3;
    }
    
    for (const num of numbers()) {
        console.log(num);
    }
    // 输出：1, 2, 3
    ```
    
3. 无限序列
    
    ```tsx
    function* infiniteSequence() {
        let i = 0;
        while (true) {
            yield i++;
        }
    }
    
    const seq = infiniteSequence();
    console.log(seq.next().value); // 0
    console.log(seq.next().value); // 1
    console.log(seq.next().value); // 2
    ```
    

### 优势

- 可控的执行流程
- 节省内存
- 简化异步逻辑

## 应用

**斐波那契数列**

```tsx
var fibGenerator = function*() {
    let pre = 0,curr = 1
    yield pre
    yield curr
    while(true){
        yield pre + curr;
        [pre,curr] = [curr,curr+pre]
    }
};
```