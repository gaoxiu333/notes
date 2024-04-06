# 基本使用

## 插件

[Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) : 编辑器插件，提供自动完成、语法突出显示和 linting 等高级功能来增强 Tailwind 开发体验。

## 使用总结？

当作是常用css库使用，毕竟不常用的还是要自己实现。多人协作成本也会很低 。

``````js {1, 3-4} showLineNumbers
var num1, num2, sum
num1 = prompt('Enter first number')
num2 = prompt('Enter second number')
sum = parseInt(num1) + parseInt(num2) // "+" means "add"
alert('Sum = ' + sum) // "+" means combine into a string


``````

## 生态？

https://headlessui.com/react/transition

https://tailwindui.com/components# 

## 与 css in js 比较

原子css定义过于分散，和模块化开发有些背道而驰。

如果对原子css很熟悉，一开始构建页面布局和样式的时候很有用

随着时间的推移，模块化的css in js  模块越来越多，反而会比原子css得心应手。

用着很不顺手？？？

原子css也几乎没有什么生态，只有样式。

如果你既想要样式和交互结合，css in js 还是最好的选择

Css in js 在nextjs 中支持的不是很好。



经过比较还是 nextjs

可能使用起来比较困难

**Gatsby**是一个适用于静态网页或个人博客的不错的框架，但如果你想在未来增加应用程序的大小，它在构建期间会变得相对缓慢，或者可能根本不会构建。因此，它存在严重的缩放问题。

另一方面，**Next.js**紧跟[最新的企业 Web 开发趋势](https://radixweb.com/blog/enterprise-web-development-trends)，是目前构建大型应用程序的最佳选择之一。使用此框架，您可以向登录用户无缝显示独特且引人入胜的内容。



# 速记

## 重置样式

Tailwind 通过 [modern-normalize](https://github.com/sindresorhus/modern-normalize) 重置了浏览器的基本样式，在使用`h1`标题等样式很不习惯，所以这里提供了解决的方案

第一种方式，是在 全局css中定义

```css
@tailwind base;

@layer base {
  h1 {
    @apply text-2xl;
  }
  h2 {
    @apply text-xl;
  }
  h3 {
    @apply text-lg;
  }
  a {
    @apply text-blue-600 underline;
  }
}

@tailwind components;

@tailwind utilities;
```

> 缺点是很难访问到在tailwind.config中自定义的主题。

另一种方式，直接在 tailwind.config 中定义

```js
 plugins: [
    plugin(function ({ addBase, addComponents, addUtilities, theme }) {
      addBase({
        a: {
          '&:hover': {
            color: theme('colors.primary'),
          },
        },
        'h1': { fontSize: theme('fontSize.2xl') },
        'h2': { fontSize: theme('fontSize.xl') },
        'h3': { fontSize: theme('fontSize.lg') },
      })
    }),
    require('@tailwindcss/typography')({
      className: 'reset',
    }),
]
```



## 排版

```html
<h4 className='text-dark dark:text-while' hover:bg-sky-700>{summary}</h4>

```



