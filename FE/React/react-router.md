# React 路由

### 依赖

```bash
npm i react-router-dom
```

## 使用

```js
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

const router = createBrowserRouter([ // 创建路由对象
  {
    path: '/',
    element: <div>hello world</div>
  }
])

// 注入路由
<RouterProvider router={router} />
```

常用配置：

- 创建`routes`文件夹
- 创建`root.tsx`文件

### 错误处理页面

- 未找到页面
- 其他错误？
- 这些错误会向上冒泡到最近的`errorElement`.

```js
const error = useRouteError(); // 获取到路由的错误

// ---

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <ErrorPage />, // 配置错误页面
  },
]);

```

### 参数路由 

### 嵌套路由

### 自动加载路由/动态路由 

### 重定向

默认页面

获取参数







