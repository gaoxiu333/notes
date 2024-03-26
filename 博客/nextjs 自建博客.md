## Nextjs 自建博客

记录自建博客

环境

- `Nodejs >18.17`
- 

堆栈

- nextjs
- next-mdx-remote
- next-themes
- reading-time
- tailwindcss
- NextUI

[MDX](https://mdxjs.com/)是 Markdown 的超集，可让您编写[JSX](https://react.dev/learn/writing-markup-with-jsx)直接在您的 Markdown 文件中。这是在内容中添加动态交互性和嵌入 React 组件的强大方法。

remark

rehype

### 初始化项目

使用`create-next-app`创建项目，根据官方要求，注意下Nodejs版本，要大于`18.17`

```bash
npx create-next-app@latest 
```

执行完命令，根据个人便好选择初始化参数；除了别名配置，我其他配置都选择了默认，一路回车下去，开始安装依赖。

项目初始化完成后移除一下几个文件不需要的代码：

- `app/page.tsx`
- `app/globals.css`
- `tailwind.config.ts`

### 配置 NextUI和明暗主题

经过对比选择，觉得NextUI的样式比较好看，组件也够用；next-themes用来切换明暗主题。

- [NextUI](https://nextui.org/)
- [next-themes](https://github.com/pacocoursey/next-themes)

> 缺点是这俩都需要客户端渲染，不支持服务端渲染。

1. 安装依赖

```bash
npm i @nextui-org/react framer-motion next-themes
```

2. Tailwind CSS 设置

```ts
// tailwind.config.ts
import { nextui } from "@nextui-org/react";
import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./node_modules/@nextui-org/theme/dist/**/*.{js,ts,jsx,tsx}", // NextUI 配置
  ],
  darkMode: ["selector", '[data-theme="dark"]'], // 明暗主题配置：next-themes 默认修改的HTML属性data-theme来切换主题的
  theme: {
    extend: {},
  },
  plugins: [
    nextui() // NextUI 配置
  ],
};
export default config;
```

> 注意：明暗主题配置有个小坑；一定要配置`'[data-theme="dark"]'` ，因为next-themes是基于这个属性来切换明暗主题的。

3. 配置`Provider`

由于NextUI和next-themes的依赖信息

```tsx
// Provider.tsx
"use client";

import { NextUIProvider } from "@nextui-org/react";
import { ThemeProvider } from "next-themes";

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <ThemeProvider enableSystem disableTransitionOnChange>
      <NextUIProvider>{children}</NextUIProvider>
    </ThemeProvider>
  );
}

```

在`root` 布局组件中使用

```tsx
// /app/layout.tsx
export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Providers>
          <PageHeader />
          {children}
        </Providers>
      </body>
    </html>
  );
}
```

配置说明：

- Next-theme 
  - `attribute`：默认`data-theme`
  - `enableSystem` ：开启系统首选项
  - `defaultTheme` ：默认`system`，如果没有开启`enableSystem`，默认为`light`
  - `disableTransitionOnChange` ：关闭切换主题时的动画

> 注意：因为开启了`enableSystem`，所以在使用`useTheme`钩子，可以使用`resolvedTheme`来获取当前模式是`dark`还是`light`，因为`resolvedTheme`可以识别系统主题，嫌麻烦可以直接关闭。

### 配置Markdown

主要用到`next-mdx-remote`

- `rehype` 通过插件转换HTML的工具
- `remark` 通过插件转换markdown的工具

1. 安装依赖

```bash
npm i next-mdx-remote rehype-prism-plus remark-gfm gray-matter reading-time
```

- 解析Markdown存放目录
- 通过gray-matter解析元数据
- 通过reading-time计算阅读时间
- rehype-prism-plus
- Remark-gfm - 添加github风格的Markdown支持 -> 只能使用3.0.1
- next-mdx-remote 用来将原始内容渲染成html

typography





## 参考

- [Markdown and MDX](https://nextjs.org/docs/pages/building-your-application/configuring/mdx)
