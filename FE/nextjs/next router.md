
目录结构

```bash
.
├── README.md
├── api
├── app
│   ├── about
│   │   └── page.tsx
│   ├── layout.tsx 
│   └── page.tsx # 1. 根路由
├── components
├── lib
├── next-env.d.ts
├── next.config.js
├── package-lock.json
├── package.json
├── pnpm-lock.yaml
├── postcss.config.js
├── public
│   ├── favicon.png
│   ├── favicon.svg
│   ├── next.svg
│   └── vercel.svg
├── styles
│   └── globals.css
├── tailwind.config.ts
├── tsconfig.json
└── yarn-error.log
```

## 路由基础知识

以下笔记为`app router`路由笔记

- 概念
	- 基于文件系统的路由器
		- `/` - 根路由，`app/page.tsx`
		- `/[文件名字]` - 其他路由，`[文件名字]/page.tsx`
	- 嵌套的文件结构定义了路由的结构
- 路由结构
	- `layout`
	- `page`
	- `template`
		- 切换路由，不保留模版内的状态，和layout相反
	- `route`
	- `loading`
	- `not-found`
	- ...[查看更多](https://nextjs.org/docs/app/building-your-application/routing#file-conventions)
- 根路由
	- 必须定义`<html>`和`<body>`标签
	- 可以设置SEO支持
- 嵌套路由
	- 文件嵌套
- 导航
	- `<Link/>`
	- `useRouter`
	- `History API`
- 路由组 - 不影响页面`URL`的情况下，对路由文件分组
- 动态路由
	- 语法：`[folderName]`
	- 参数：`props.params`，通过`props`获取路由参数


--- 
草稿
- [`usePathname()`](https://nextjs.org/docs/app/api-reference/functions/use-pathname) - 查看当前路由路径
- 重定向
## 高级路由

- [创建多个根路由](https://nextjs.org/docs/app/building-your-application/routing/route-groups#creating-multiple-root-layouts)
- [并行路由](https://nextjs.org/docs/app/building-your-application/routing/parallel-routes) - 同一个布局中渲染多个页面，常用在动态数据较多的页面
- [Intercepting Routes](https://nextjs.org/docs/app/building-your-application/routing/intercepting-routes) - 不需要打开页面，直接预览

跟路由可以配置多个，配置方法可参考官方文档[Creating multiple root layouts](https://nextjs.org/docs/app/building-your-application/routing/route-groups#creating-multiple-root-layouts)

- `page`
- `lyaout`
	- 可修改网站元数据
	- `<head/>` 
	- favicon 
- template
- loading
- error
> TODO: template 和 layout 在渲染上有什么区别？以及page和components？


