# VUE源码学习

V2.6.11源码目录结构

```bash
├─dist                   # 项目构建后的文件
├─scripts                # 与项目构建相关的脚本和配置文件
├─flow                   # flow的类型声明文件
├─src                    # 项目源代码
│    ├─complier          # 与模板编译相关的代码
│    ├─core              # 通用的、与运行平台无关的运行时代码
│    │  ├─observe        # 实现变化侦测的代码
│    │  ├─vdom           # 实现virtual dom的代码
│    │  ├─instance       # Vue.js实例的构造函数和原型方法
│    │  ├─global-api     # 全局api的代码
│    │  └─components     # 内置组件的代码
│    ├─server            # 与服务端渲染相关的代码
│    ├─platforms         # 特定运行平台的代码，如weex
│    ├─sfc               # 单文件组件的解析代码
│    └─shared            # 项目公用的工具代码
└─test                   # 项目测试代码
```

## 暂定学习路线

- 数据监听
- 虚拟DOM
- 模版编译
- 实例方法
- 全局API
- 生命周期
- 指令
- 过滤器
- 内置组件

## 深入VUE响应式原理

vue源码中的数据监听部分首先需要深入vue的响应式原理；

核心原理是vue将遍历data对象所有的property，并使用`Object.defineProperty`，把这些property全部转为getter/setter；

这些getter/setter能够让vue追踪依赖，在property被访问和修改时通知变更。

每个组件实例都对应一个wattcher实例，他会对组件渲染的过程中把‘接触’过的数据property记录为依赖，之后依赖项的setter触发时，会通知watcher，从而使它关联的组件重新渲染。

![data](https://v2.cn.vuejs.org/images/data.png)



### 源码中数据监听的实现

```bash
observer 文件部分。
-	array.js
-	dep.js
-	index.js
-	scheduler.js
-	traverse.js
-	watcher.js
```

