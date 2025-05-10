# Promise 面试题

## 参考

- [xx 道题](https://github.com/LinDaiDai/niubility-coding-js/blob/master/JavaScript/异步/要就来45道Promise面试题一次爽到底.md)

## 知识点

1. `Promise`的状态一经改变就不能再改变。
2. `.then`和`.catch`都会返回一个新的`Promise`。
3. `catch`不管被连接到哪里，都能捕获上层的错误。
4. 在`Promise`中，返回任意一个非 `promise` 的值都会被包裹成 `promise` 对象，例如`return 2`会被包装为`return Promise.resolve(2)`。
5. `Promise` 的 `.then` 或者 `.catch` 可以被调用多次, 当如果`Promise`内部的状态一经改变，并且有了一个值，那么后续每次调用`.then`或者`.catch`的时候都会直接拿到该值。
    1. 多次调用 `.then` ，需要前者 `return` 后面才有值
    2. 多次调用 `.catch` ，同样需要前者 `throw` 后面才能捕获
6. `.then` 或者 `.catch` 中 `return` 一个 `error` 对象并不会抛出错误，所以不会被后续的 `.catch` 捕获。
7. `.then` 或 `.catch` 返回的值不能是 promise 本身，否则会造成死循环
8. `.then` 或者 `.catch` 的参数期望是函数，传入非函数则会发生值透传。
9. `.then`方法是能接收两个参数的，第一个是处理成功的函数，第二个是处理失败的函数，在某些时候你可以认为`catch`是`.then`第二个参数的简便写法
10. `.finally` 不接受任何参数，方法也是返回一个`Promise`，他在`Promise`结束的时候，无论结果为`resolved`还是`rejected`，都会执行里面的回调函数。

### 基础

```jsx
const promise = new Promise((resolve, reject) => {
  console.log(1);
  resolve('success')
  console.log(2);
});
promise.then(() => {
  console.log(3);
});
console.log(4);
```

- 结果
    
    ```jsx
    1 2 4 3
    ```
    

### Promise 和 SetTimeout

```jsx
console.log('start')
setTimeout(() => {
  console.log('time')
})
Promise.resolve().then(() => {
  console.log('resolve')
})
console.log('end')
```

- 结果
    
    ```jsx
    start end resolve time
    ```
    

### seTimeout中嵌套promise

```jsx
setTimeout(() => {
  console.log('timer1');
  Promise.resolve().then(() => {
    console.log('promise')
  })
}, 0)
setTimeout(() => {
  console.log('timer2')
}, 0)
console.log('start')
```

- 结果
    
    ```jsx
    start timer1 promise timer2
    ```
    

### Promise 自动 reject

- 在 `resolve` 之前 JS 抛出错误或者通过 `throw` 主动抛出错误

```jsx
const promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('success')
  }, 1000)
})
const promise2 = promise1.then(() => {
  throw new Error('error!!!')
})
console.log('promise1', promise1)
console.log('promise2', promise2)
setTimeout(() => {
  console.log('promise1', promise1)
  console.log('promise2', promise2)
}, 2000)
```

- 结果：
    
    ```bash
    promise1 Promise <pending>
    promise2 Promise <pending>
    Uncaught Error
    promise1 promise <fulfilled>: success
    promise2 promise <rejected>: Error:error
    ```
    

### 如果将 setTimeout换成 promise

```jsx
const promise1 = new Promise((resolve, reject) => {
      resolve("success");
});
const promise2 = promise1.then(() => {
  throw new Error("error!!!");
});
console.log("promise1", promise1);
console.log("promise2", promise2);
setTimeout(() => {
  console.log("promise1", promise1);
  console.log("promise2", promise2);
}, 2000);
```

- 结果
    
    ```bash
    promise1 promise <fulfilled>: success
    promise2 promise <pending>
    Uncaught Error
    promise1 promise <fulfilled>: success
    promise2 promise <rejected>: Error:error
    ```
    

### then 或者 catch 返回一个promise

```jsx
const promise = new Promise((resolve, reject) => {
  reject("error");
  resolve("success2");
});
promise
.then(res => {
    console.log("then1: ", res);
  }).then(res => {
    console.log("then2: ", res);
  }).catch(err => {
    console.log("catch: ", err);
  }).then(res => {
    console.log("then3: ", res);
  })
```

- 结果
    
    ```jsx
    catch: error
    then3: undefined => 这里需要注意，catch返回了一个promise，所以有了 then3
    ```
    

## then/catch 和 return/throw

```jsx
Promise.reject(1)
  .then((res) => {
    console.log(res);
    return 2;
  })
  .catch((err) => {
    console.log(err);
    return 3;
  })
  .then((res) => {
    console.log(res);
    throw 4;
  })
  .catch((err) => {
    console.log(err);
  });
```

- 结果：
    - 第二个`then`中的`res`得到的是`catch`中的返回值（返回了 Promise）
    - 第二个 `catch` 中的 `err` 得到的是第二个 `then` 抛出的错误
    
    ```jsx
    1
    3
    ```
    

## 如果 return 一个 Error

```jsx
Promise.resolve().then(() => {
  return new Error('error!!!')
}).then(res => {
  console.log("then: ", res)
}).catch(err => {
  console.log("catch: ", err)
})
```

- 结果：
    
    ```jsx
    then: Error:error!!!
    ```
    

## return 一个 Promise

```jsx
const promise = Promise.resolve().then(() => {
  return promise;
})
promise.catch(console.err)
```

- 结果：造成死循环
    
    ```jsx
    Uncaught (in promise) TypeError: Chaining cycle detected for promise #<Promise>
    ```
    

## 如果传入的是非函数

```jsx
Promise.resolve(1)
  .then(2)
  .then(Promise.resolve(3))
  .then(console.log)
```

- 结果：发生透传
    
    第一个`then`和第二个`then`中传入的都不是函数，一个是数字类型，一个是对象类型，因此发生了透传，将`resolve(1)` 的值直接传到最后一个`then`里。
    
    ```jsx
    1
    ```
    

### promise.all

```jsx
function runAsync(x) {
  const p = new Promise((r) => setTimeout(() => r(x, console.log(x)), 1000));
  return p;
}
Promise.all([runAsync(1),() => 2,3,4,5,6, runAsync(3)]).then((res) =>
  console.log(res)
);
```

- 结果：如果数组内有非 Promise，则直接返回，无论是什么数据结构
    
    ```jsx
    1
    3
    [1,f,3,4,5,6,3]
    ```
    

### promise.rece

- 并发，并且优先获取最先执行完的结果，其他的依然会执行，但结果会被舍弃。
- 如果数组内有非 Promise 则立即完成，并且返回这个值
- 如果有报错，而且报错最先完成，则取报错的这个结果

### async/await

- 注意这道题的顺序， `await` 之前的代码属于同步代码

```jsx
async function async1() {
  console.log("async1 start");
  await async2();
  console.log("async1 end");
}
async function async2() {
  console.log("async2");
}
async1();
console.log('start')
```

- 结果：
    
    ```
    'async1 start'
    'async2'
    'start'
    'async1 end'
    ```
    

### await 和 setTimeout

```jsx
async function async1() {
  console.log("async1 start");
  await async2();
  console.log("async1 end");
  setTimeout(() => { // 主意这个异步，它在微任务之后了
    console.log('timer1')
  }, 0)
}
async function async2() {
  setTimeout(() => {
    console.log('timer2')
  }, 0)
  console.log("async2");
}
async1();
setTimeout(() => {
  console.log('timer3')
}, 0)
console.log("start")
```

- 结果
    
    ```
    'async1 start'
    'async2'
    'start'
    'async1 end'
    'timer2'
    'timer3'
    'timer1'
    ```
    

### 一小不小就掉坑里的题

不看结果之前，看看自己会不会掉进去！！

```jsx
async function async1 () {
  console.log('async1 start');
  await new Promise(resolve => {
    console.log('promise1')
  })
  console.log('async1 success');
  return 'async1 end'
}
console.log('srcipt start')
async1().then(res => console.log(res))
console.log('srcipt end')
```

- 结果：
    
    ```
    'script start'
    'async1 start'
    'promise1'
    'script end'
    ```
    

### 上题的加强版

```jsx
async function async1 () {
  console.log('async1 start');
  await new Promise(resolve => {
    console.log('promise1')
    resolve('promise1 resolve') 
  }).then(res => console.log(res)) // --> 会被先执行，比 async1 success 还早
  console.log('async1 success');
  return 'async1 end'
}
console.log('srcipt start')
async1().then(res => console.log(res))
console.log('srcipt end')
```

- 结果
    - `await` 后面的 Promise 即使有链式调用，比如多个 `.then` ，会等待链式调用也执行完毕
    
    ```jsx
    'script start'
    'async1 start'
    'promise1'
    'script end'
    'promise1 resolve'
    'async1 success'
    'async1 end'
    ```
    

### Async 处理错误

```jsx
async function async1 () {
  await async2();
  console.log('async1');
  return 'async1 success'
}
async function async2 () {
  return new Promise((resolve, reject) => {
    console.log('async2')
    reject('error')
  })
}
async1().then(res => console.log(res))
```

- 结果
    - `reject` 的错误必须要使用 `try/catch` 捕获，不然会直接阻塞代码
    
    ```
    'async2'
    Uncaught (in promise) error
    ```
    

### 综合1

```jsx
const first = () => (new Promise((resolve, reject) => {
    console.log(3);
    let p = new Promise((resolve, reject) => {
        console.log(7);
        setTimeout(() => {
            console.log(5);
            resolve(6);
            console.log(p)
        }, 0)
        resolve(1);
    });
    resolve(2);
    p.then((arg) => {
        console.log(arg);
    });
}));
first().then((arg) => {
    console.log(arg);
});
console.log(4);
```

### 综合2

```jsx
const async1 = async () => {
  console.log('async1');
  setTimeout(() => {
    console.log('timer1')
  }, 2000)
  await new Promise(resolve => {
    console.log('promise1')
  })
  console.log('async1 end')
  return 'async1 success'
} 
console.log('script start');
async1().then(res => console.log(res));
console.log('script end');
Promise.resolve(1)
  .then(2)
  .then(Promise.resolve(3))
  .catch(4)
  .then(res => console.log(res))
setTimeout(() => {
  console.log('timer2')
}, 1000)
```

### 综合3

```jsx
const p1 = new Promise((resolve) => {
  setTimeout(() => {
    resolve('resolve3');
    console.log('timer1')
  }, 0)
  resolve('resovle1');
  resolve('resolve2');
}).then(res => {
  console.log(res)
  setTimeout(() => {
    console.log(p1)
  }, 1000)
}).finally(res => {
  console.log('finally', res)
})
```

### Promise 按照顺序执行

```jsx
const arr = [1, 2, 3]
arr.reduce((p, x) => p.then(() => new Promise(r => setTimeout(() => r(console.log(x)), 1000))), Promise.resolve())
```

### 使用 Promise+ 实现

- [《Promise不会？？看这里！！！史上最通俗易懂的Promise！！！》](https://juejin.im/post/5afe6d3bf265da0b9e654c4b#heading-7)
- [《写一个符合 Promises/A+ 规范并可配合 ES7 async/await 使用的 Promise》](https://zhuanlan.zhihu.com/p/23312442)