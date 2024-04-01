## 前言

JavaScript模块化是一种将代码拆分为独立文件或模块的方法，以便更好地管理代码、提高可维护性和可重用性。在JavaScript中，有几种常见的模块化方案：

1. CommonJS
2. AMD (Asynchronous Module Definition)
3. UMD (Universal Module Definition)
4. ES6 Modules。

## 模块化发展历史

有一篇很好的文章介绍 JavaScript 模块化的发展历史：

- [JavaScript 模块化七日谈](https://huangxuan.me/2015/07/09/js-module-7day/)

以及梳理早期JS模块化的设计思想

- [早期的模块模式](https://www.adequatelygood.com/JavaScript-Module-Pattern-In-Depth.html)

## CommonJS

为 Node.js 服务器创建的模块系统，简称CJS
- CommonJS是模块化规范，主要用于服务器端的Node.js环境。
- 通过`require`函数导入模块，使用`module.exports`导出模块。
- 同步的
```js
// 模块导出
module.exports = {
    foo: function() {
        // code
    },
    bar: function() {
        // code
    }
};

// 模块导入
const module = require('./module');
module.foo();
```

## AMD

最古老的模块系统之一，最初由 [require.js](http://requirejs.org/) 库实现。
- AMD是一种异步加载模块的规范，适用于浏览器环境。
- 浏览器上的异步借助`<script async />` （require.js的实现）
	- `async` 加载完js立即执行，多个js文件会出现执行顺序问题
	
- 提前执行，推崇依赖前置

```js
// 模块定义 
define(['dependency1', 'dependency2'], function(dep1, dep2) {
    return {
        foo: function() {
            // code
        },
        bar: function() {
            // code
        }
    };
});

// 模块导入
require(['module'], function(module) {
    module.foo();
});

```

## UMD

 - UMD是一种通用的模块定义方式，兼容CommonJS、AMD和全局变量的使用。
 - 通过判断环境来确定模块加载方式，  直接封装 AMD、CommonJS、IIFE 三种方式并根据环境自动切换
 - [UMD 规范如何实现的样板代码](https://github.com/umdjs/umd?tab=readme-ov-file)
#### 不同规范的模块导出

**全局变量**

```js
const MyModule = function(){}
```

**CommonJS**

```js
const MyDependency = require('my-dependency')

module.exports = function(){}
```

**AMD**

```js
define(['my-dependency'],function(MyDependency)){
	   return function (){}
}
```

**UMD 通用样板代码**

```js
(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD
        define(['dependency'], factory);
    } else if (typeof exports === 'object') {
        // CommonJS
        module.exports = factory(require('dependency'));
    } else {
        // 挂载到全局变量
        root.MyModule = factory(root.Dependency);
    }
}(this, function (Dependency) {
    return {
        // 模块的具体实现s
        
        function foo(){}
        function bar(){}
        
        // 导出模块
	    return {
		    foo:foo,
		    bar:bar
	    }
    };
}));

```

## ES Modules

- ES6 Modules是ECMAScript 2015引入的官方模块系统。
- 使用`import`导入模块，使用`export`导出模块。

```js
// 模块导出
export function foo() {
    // code
}

// 模块导入
import { foo } from './module';
foo();

```

## ES6 Module 和 CommonJS差异

ES6 Module简称ESM；CommonJS简称CJS

- CommonJS 
  - 使用`require()`和`module.exports`
  - 模块输出的是一个值的拷贝；
  - 模块是运行时并且是同步加载。
- ESM
  - 使用`import`和`export`。
  - ESM 模块输出的是值的引用；
  - ESM 是异步加载，但是有一个静态解析阶段，在编译时输出。


> **关于拷贝和引用** 
>
> CommonJS 模块输出的是值的拷贝，也就是说，一旦输出一个值，模块内部的变化就影响不到这个值；ES6 模块的运行机制与 CommonJS 不一样。JS 引擎对脚本静态分析的时候，遇到模块加载命令`import`，就会生成一个只读引用。等到脚本真正执行时，再根据这个只读引用，到被加载的那个模块里面去取值，原始值变了，`import`加载的值也会跟着变，并且不会缓存值。

## 浏览器中使用 ESM

**使用** 

- 在script标签上添加属性`type="module"` 
  - 异步加载，默认`defer`，文档解析完成后按顺序执行


**特点**

- 自动采用严格模式
- `.js` 后缀不可省略
- 模块内顶层`this`指向`undefined` 

## Nodejs 中的模块

 CommonJS 模块是 Node.js 专用，与 ES6 模块不兼容； Node.js 12.0.0 版本开始正式支持ES6 模块支持

### 两种模式的加载方式

Nodejs支持`.js`、`.cjs`、`.mjs`三种后缀格式的文件：

- `.js` 格式文件，默认以CJS模块方式加载
- `.cjs` 格式文件，只能以CJS模块的方式加载
- `.mjs` 格式文件，只能以ESM模块方式加载

**如何修改`.js`文件模块的加载方式？**

通过修改`package.json`中的`type`来指定`.js`文件模块的加载方式

- `type:module` - 指定ES方式加载
- `type:commonjs` 指定CommonJS方式加载
- `type`只影响`.js`后缀的文件，并不会影响`.cjs`、`.mjs`后缀的文件。

### 混用CJS和ESM

**CJS 模块如何引入 ESM？**

因为CommonJS是同步的，而ES6模块是异步，没办法兼容，但是可以使用`import()`方法来加载ES模块

```js
// main.cjs
(async () => {
  const esModule =await import('./es_module.mjs) 
})()
```

**ESM 模块如何引入CJS模块？**

因为CommonJS导出的`module.exports`是一个对象，无法被静态分析，所以只能整体加载。

```js
import commonjsModule from './c_main.cjs'

console.log('我是 ES Module')
console.log('我引入了一个commonjs模块文件', commonjsModule)
```

其他方法：
- Nodejs 内置的`module.createRequire()` 

### CommonJS和ES6 Module的差异

以下几个全局变量只存在于CommonJS中：

- `this` 
- `arguments`
- `require`
- `module`
- `exports`
- `__filename`
- `__dirname`

> 了解更多：[NodeJS中的ES模块-故障排除](https://docs.joshuatz.com/cheatsheets/node-and-npm/node-esm/)

## 参考

- [现代javascript 模块简介](https://zh.javascript.info/modules-intro)
- [ES6 Module Cheatsheet](https://www.samanthaming.com/tidbits/79-module-cheatsheet/)
- [AMD](https://en.wikipedia.org/wiki/Asynchronous_module_definition)
- [require.js](http://requirejs.org/)
- [UMD](https://github.com/umdjs/umd) 
- [CommonJS](http://wiki.commonjs.org/wiki/Modules/1.1) 
- [ES6 模块与 CommonJS 模块的差异](https://es6.ruanyifeng.com/#docs/module-loader)



