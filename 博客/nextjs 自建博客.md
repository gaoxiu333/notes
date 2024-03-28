## Nextjs 构建极简博客

### 项目依赖

**环境**

- `Nodejs >18.17`

**堆栈**

React相关的依赖：

- `nextjs` 
- `tailwindcss` 
- `NextUI` 
- `next-themes` 

MDX相关的依赖：

- `next-mdx-remote` 
- `reading-time` 
- `gray-matter`
- `rehype-prism-plus` 
- `remark-gfm` 

预览地址：[blog-example](https://blog-example-indol.vercel.app/)

### 初始化项目

使用`create-next-app`创建项目，根据官方的建议：Nodejs版本要大于`18.17`

```bash
npx create-next-app@latest 
```

执行命令过程中，根据个人便好选择初始化参数；一路回车默认即可（除了配置别名，其他的都是默认）

等待一段时间，项目应该就初始化完成啦，之后删除以下文件中的无用代码。

- `app/page.tsx`
- `app/globals.css`
- `tailwind.config.ts`

### 添加组件库

为了简化开发，引入了UI组件库，我选择了[Tailwindcss](https://tailwindcss.com/)+[NextUI](https://nextui.org/)+[next-themes](https://github.com/pacocoursey/next-themes)

**[Tailwindcss](https://tailwindcss.com/)**

Tailwindcss 提供的CSS原子类可以直接用Nextjs的SSR模式中使用，Tailwindcss发展很快，社区也活跃。项目初始化时默认安装过这个东西，没装过的话，使用`Tailwind CLI`初始化一份配置文件即可。

**[NextUI](https://nextui.org/)**

基于Tailwindcss的组件库有很多，我选择了NextUI，单纯因为个人觉得看起来还不错～ 你也可以选择其他组件库，或者纯手撸。

**使用**

NextUI集成也比较简单，官方都已经封装好了，首先要在`tailwind.config.ts`引入NextUI的模版，并且执行插件，接着使用NextUI封装好的`NextUIProvider` 在根布局包裹整个页面，以便在整个项目中生效。

**[next-themes](https://github.com/pacocoursey/next-themes)**

配置简单的明暗主题切换小工具，当然不需要也行，但是前期为了省心，就先用上啦，拒绝再造轮子～～

**使用**

1. 在`config.darkMode`中配置主题切换方式

配置说明：

- Next-theme 
  - `attribute`：默认`data-theme`，对应`tailwindcss`中的`darkMode`配置
  - `enableSystem` ：开启系统首选项，也就是系统自己暗黑模型（如果操作系统开启了并且浏览器支持的话）
  - `defaultTheme` ：默认`system`，如果没有开启`enableSystem`，默认为`light`
  - `disableTransitionOnChange` ：关闭切换主题时的动画

> 注意：因为开启了`enableSystem`，所以在使用`useTheme`钩子，可以使用`resolvedTheme`来获取当前模式是`dark`还是`light`，因为`resolvedTheme`可以识别系统主题，嫌麻烦也可以直接关闭这一项。

**以下是详细步骤：**

1. 安装依赖

```bash
npm i @nextui-org/react framer-motion next-themes
# framer-motion 是NextUI的动画依赖
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

> 注意：一定要配置`'[data-theme="dark"]'` ，因为next-themes是基于这个属性来切换明暗主题的；当然可以修改这个属性，只需要将next-themes中的attribute和这里的配置一样即可

3. 配置`Provider`

需要使用`NextUIProvider`，`ThemeProvider`包裹，这里直接在`root`组件包裹，也就是让全部页面生效。

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

最后在`root` 布局组件中使用

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

### 配置Markdown

这里主要借助`next-mdx-remote`加载和显示MDX文件，另外说明一下MDX基于`unified`开发，所有`unified`的两大插件系统也能用：

- `rehype` 通过插件转换HTML的工具
- `remark` 通过插件转换markdown的工具

> 还有一个`retext`，这里暂时没用到。

本次暂时只用到了这俩大插件系统中的以下几个插件：

- `remark-gfm` - 添加github风格的Markdown支持 -> 新版本有bug，只能使用`3.0.1`版本
- `rehype-prism-plus` - 语法高亮，且支持更多功能

以及以下几个插件

- `gray-matter` - 解析元数据
- `reading-time` - 添加阅读时间的小工具

1. 安装依赖

```bash
npm i next-mdx-remote rehype-prism-plus remark-gfm gray-matter reading-time
```

2. 配置`next-mdx-remote`

```tsx 
import { MDXRemote } from "next-mdx-remote/rsc";
import rehypePrism from "rehype-prism-plus";
import remarkGfm from "remark-gfm";

function Page(){
  const content = "# hello, world"
  return <MDXRemote
          source={content}
          options={{
            parseFrontmatter: true,
            mdxOptions: {
              remarkPlugins: [remarkGfm as any], // 注入 remarkGfm插件，后面还可以加入你想加入的 remark 插件
              rehypePlugins: [rehypePrism as any], // 注入 语法高亮插件，同样可以添加更多rehype插件
            },
          }}
        />
}
```

代码中`content` 为Markdown文件内解析出来的数据，这里是占位，接下来使用Nodejs去解析`.mdx`文件中的数据

```ts
// mdx.ts
import fs from "fs";
import path from "path";
import matter from "gray-matter";
import readingTime from "reading-time";

const articlesDirectory = path.join(process.cwd(), "app/_articles");

// 获取 MDX/MD 原始数据
export function getMdxRawData(fileName: string, hasSuffix: boolean) {
  let fullPath = path.join(articlesDirectory, `${fileName}`);
  let suffix = hasSuffix // 判断是否有后缀，没有的话就加上后缀
    ? ""
    : fs.existsSync(`${fullPath}.mdx`)
    ? ".mdx"
    : ".md";
  const fileContnts = fs.readFileSync(`${fullPath}${suffix}`, "utf8");
  return fileContnts;
}

// 处理 MDX/MD 原始数据中的 frontmatter
export function getMdxFrontmatter(mdxRawData: string) {
  const { content, data } = matter(mdxRawData);
  return {
    content,
    frontmatter: data,
    readingTime: readingTime(content).text, // 计算阅读时间
  };
}

// 获取文章的所有信息
export function getArticlesData(fileName: string, hasSuffix = false) {
  return {
    ...getMdxFrontmatter(getMdxRawData(fileName, hasSuffix)),
    fileName: fileName.split(".").slice(0, -1).join("."), // 去除后缀
  };
}

// 获取 _articles 目录下的所有文章
export function getAllArticlesData() {
  const fileNames = fs.readdirSync(articlesDirectory);
  const allArticlesData = fileNames.map((fileName) => {
    return getArticlesData(fileName, true);
  });
  return allArticlesData;
}
```

之后完善React部分，直接来代码吧～

```tsx
import { Log } from "@/components/Log";
import { getArticlesData } from "@/lib/mdx";
import { formatDateTime } from "@/lib/time";
import { MDXRemote } from "next-mdx-remote/rsc";
import rehypePrism from "rehype-prism-plus";
import remarkGfm from "remark-gfm";

const Page = async ({ params }: any) => {
  const { content, frontmatter, readingTime } = getArticlesData(params.id);
  return (
    <main className="container pb-24">
      <article className="prose !max-w-none dark:prose-invert">
        <MDXRemote
          source={content}
          options={{
            parseFrontmatter: true,
            mdxOptions: {
              remarkPlugins: [remarkGfm as any],
              rehypePlugins: [rehypePrism as any],
            },
          }}
        />
      </article>
    </main>
  );
};
export default Page;

```

到这里还差最后一步，还没有排版样式，直接使用`@tailwindcss/typography`插件

安装一下

```bash
npm install -D @tailwindcss/typography
```

然后在`tailwind.config.ts`中引入这个插件

```ts
module.exports = {
  // ...
  plugins: [
    nextui(), // NextUI 配置
    require("@tailwindcss/typography"), // markdown typography
  ],
}
```

最后是在需要使用排版样式的地方加上类名`prose`(这个是插件的默认类型，如果有冲突可以在插件上配置自己的类名)

```tsx
<article className="prose !max-w-none dark:prose-invert"> // 这里支持了明暗主题，以及取消max-width
	// HTML 代码片段
</article>
```

以上一个使用Nextjs搭建的简单博客已经完成啦～

源码地址：[blog-example](https://github.com/gaoxiu333/blog-example)

## 参考

- [Markdown and MDX](https://nextjs.org/docs/pages/building-your-application/configuring/mdx)
