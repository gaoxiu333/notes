# Next.js 入门

Next.js是一个轻量级的react服务端渲染应用框架。

## 创建项目

```bash
npx create-next-app@latest
```

## 路由

当一个文件被添加到`pages`目录时，会自动创建一个路径。

**示例**

- `pages/index.js`→`/`  **根路径**
- `pages/blog/index.js`→`/blog` **默认访问index**
- `pages/blog/first-post.js`→`/blog/first-post` **嵌套的**
- `pages/blog/[slug].js`→ `/blog/:slug`( `/blog/hello-world`)  **动态的**

## dynamic

迟加载外部库

```js
import dynamic from 'next/dynamic'

const DynamicHeader = dynamic(() => import('../components/header'), {
  loading: () => <p>Loading...</p>,
})

export default function Home() {
  return <DynamicHeader />
}
```

## 布局

## Markdown

[next-mdx-remote](https://github.com/hashicorp/next-mdx-remote)和[mdx-bundler](https://github.com/kentcdodds/mdx-bundler)区别

- 支持数学符号

## 主题

深色模式

