---
title: JS手写算法要点
jd_id: J30.01.0001
created: 2025-05-11 11:37
updated: 2025-05-11 13:01
type: note
status: active
tags: [topic/frontend/javascript, topic/algorithms]
---

# JS手写算法要点

## 概述

本文档总结了JavaScript手写实现常见功能和算法的核心要点，这些知识点对前端面试和实际开发都有重要价值。

## Promise实现要点

1. **处理异步回调队列**
   - 维护`onFulfilled`和`onRejected`回调队列
   - 状态变更后依次执行对应队列中的回调

2. **链式调用**
   - `then`方法返回新的Promise实例
   - 异步处理前一个Promise的返回值
   - 处理返回值是Promise的情况

3. **值穿透**
   - 处理非函数参数，提供默认处理函数
   - 确保值可以正确地在链中传递

4. **错误冒泡机制**
   - 捕获回调执行过程中的异常
   - 将异常传递到链的下一个`catch`或`then`的reject回调

## 实现示例

```javascript
// Promise简易实现
class MyPromise {
  constructor(executor) {
    this.state = 'pending';
    this.value = undefined;
    this.reason = undefined;
    this.onFulfilledCallbacks = [];
    this.onRejectedCallbacks = [];

    const resolve = (value) => {
      if (this.state === 'pending') {
        this.state = 'fulfilled';
        this.value = value;
        this.onFulfilledCallbacks.forEach(fn => fn());
      }
    };

    const reject = (reason) => {
      if (this.state === 'pending') {
        this.state = 'rejected';
        this.reason = reason;
        this.onRejectedCallbacks.forEach(fn => fn());
      }
    };

    try {
      executor(resolve, reject);
    } catch (e) {
      reject(e);
    }
  }

  then(onFulfilled, onRejected) {
    // 值穿透处理
    onFulfilled = typeof onFulfilled === 'function' ? onFulfilled : value => value;
    onRejected = typeof onRejected === 'function' ? onRejected : err => { throw err };

    // 返回新Promise以支持链式调用
    const promise2 = new MyPromise((resolve, reject) => {
      if (this.state === 'fulfilled') {
        setTimeout(() => {
          try {
            const x = onFulfilled(this.value);
            this.resolvePromise(promise2, x, resolve, reject);
          } catch (e) {
            reject(e);
          }
        }, 0);
      }

      if (this.state === 'rejected') {
        setTimeout(() => {
          try {
            const x = onRejected(this.reason);
            this.resolvePromise(promise2, x, resolve, reject);
          } catch (e) {
            reject(e);
          }
        }, 0);
      }

      if (this.state === 'pending') {
        this.onFulfilledCallbacks.push(() => {
          setTimeout(() => {
            try {
              const x = onFulfilled(this.value);
              this.resolvePromise(promise2, x, resolve, reject);
            } catch (e) {
              reject(e);
            }
          }, 0);
        });

        this.onRejectedCallbacks.push(() => {
          setTimeout(() => {
            try {
              const x = onRejected(this.reason);
              this.resolvePromise(promise2, x, resolve, reject);
            } catch (e) {
              reject(e);
            }
          }, 0);
        });
      }
    });

    return promise2;
  }

  resolvePromise(promise2, x, resolve, reject) {
    // 防止循环引用
    if (x === promise2) {
      return reject(new TypeError('循环引用Promise'));
    }

    // 处理Promise返回值
    if (x instanceof MyPromise) {
      x.then(resolve, reject);
    } else {
      // 处理普通值
      resolve(x);
    }
  }

  catch(onRejected) {
    return this.then(null, onRejected);
  }

  // 其他Promise方法...
}
```

## this绑定要点

1. **处理context为null时的情况**
   - 如果绑定的上下文是`null`或`undefined`，则指向全局对象

2. **属性冲突处理**
   - 使用Symbol创建唯一属性，避免覆盖原有属性

3. **处理new操作符优先级**
   - `bind`返回的函数被new调用时，绑定的this应失效
   - 原型链要正确设置

## 实现示例

```javascript
// call实现
Function.prototype.myCall = function(context, ...args) {
  // 处理null或undefined
  context = context || window;
  
  // 使用Symbol避免属性冲突
  const fnSymbol = Symbol('fn');
  
  // 将函数作为上下文对象的方法
  context[fnSymbol] = this;
  
  // 调用并获取结果
  const result = context[fnSymbol](...args);
  
  // 删除临时属性
  delete context[fnSymbol];
  
  return result;
};

// bind实现
Function.prototype.myBind = function(context, ...bindArgs) {
  const self = this;
  
  function Bound(...args) {
    // 处理new调用的情况
    return self.apply(
      this instanceof Bound ? this : context, 
      [...bindArgs, ...args]
    );
  }
  
  // 设置原型链，保持原函数的原型
  Bound.prototype = Object.create(this.prototype);
  
  return Bound;
};
```

## 其他常见手写算法

1. **深拷贝**
   - 处理循环引用（使用WeakMap）
   - 支持多种数据类型（Date, RegExp, Symbol等）

2. **防抖节流**
   - 防抖：延迟执行，重置定时器
   - 节流：限制执行频率，保证间隔

3. **数组扁平化**
   - 使用递归或迭代方式展开嵌套数组
   - 支持指定深度

4. **排序算法**
   - 快速排序可优化基准选择（三数取中法）
   - 注意时间复杂度/空间复杂度

## 优化注意点

- 时间复杂度与空间复杂度的平衡
- 代码可读性与维护性
- 边界情况处理
- 考虑大数据量下的性能

## 参考资源

- [MDN Promise文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [JavaScript高级程序设计](https://www.amazon.com/Professional-JavaScript-Developers-Matt-Frisbie/dp/1119366445)
- [You Don't Know JS: this & Object Prototypes](https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/README.md) 