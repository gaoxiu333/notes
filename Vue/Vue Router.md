# Vue Router

* 入门

* 配置路由

* 路由参数、查询、通配符

* 路由过渡效果

* 路由原理：HTML5 history和hash

* 滚动行为

* url正确编码

* 路由守卫

### 入门

* `<router-link>`

* `<router-view>`

* `cureteRouter`

* `useRouter`

* `useRoute`

> 使用`createRouter`创建路由实例
> 使用`<router-link>`导航路由
> 使用`<router-view>`控制现实导航的内容、嵌套路由等
> 使用`useRouter`返回Router实例，来控制路由
> 使用`useRoute`返回路由数据，查看当前路由信息，比如参数等

### 路由配置

**动态路由**

* 配置：`/user/:username`

* 访问：`$route.params`

* 监听：Vue的`watch`监听

**嵌套路由**

* 配置：通过`children`配置嵌套

* DOM：通过`router-view`配置嵌套

**命名路由**

* `name`

* 给路由添加名字，方便导航

**命名视图**

* 也有命名视图，用来处理一些特殊情况

* 具有多个视图时，又不想把视图搞的特别复杂，就用多个视图分开。

**重定向**

* `redirect`

**路由元信息**

* `meta`

* 用来配置额外的数据，比如权限

**懒加载**

* `import()`

* 返回一个Promise即可

* 路由分块，可以借助打包工具来配置

* webpack借助注释

* vite需要在`output.manualChunks`中显式地配置

### 导航守卫

**全局守卫**

* `beforeEach`

* `beforeResolve`

* `afterEach`

* 执行顺序

* 组件内守卫

* `触发`=>`组件beforeRouteLeave`=>`全局beforeEach`=>`复用组件beforeRouteUpdate`=>`beforeEnter`=>`解析异步组件`=>`组件beforeRouterEnter`=>`全局beforeResolve`=>`导航被确定`=>`全局afterEach`=>`DOM更新`=>`beforeRouteEnter内执行next`

### 动态配置路由

* `createRouter()`

* `addRoute()`

* `removeRoute()`

### AIPs

**访问**

* `$route.params`

* `$route.query`

* `$route.hash`

* `$route.meta`

* `$router.addRoute`

* `$router.back`

* `$router.push`

* `$router.replace`

### 原理

**hash**

* `window.history`记录hash的修改

* `window.onhashchange`监听hash的改变

* hash改变会回发生页面刷新

**History**

* HTML5 提供的新特性，改变前端路由而不会刷新页面

* `history.pushState()`添加一条历史记录

* `history.replaceState()`修改历史记录

* `history.state`访问历史记录

* `window.onpopstate`监听pushState和replaceState的调用

* 问题

  * 需要配置后端路由，不然刷新页面请求服务端会造成404
