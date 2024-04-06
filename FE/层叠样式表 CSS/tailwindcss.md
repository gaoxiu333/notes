
Less、Sass，大概率用不了了。
## postcss


## 编辑器配置

- [VS Code 插件](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss)
- [Prettier 排序](https://tailwindcss.com/blog/automatic-class-sorting-with-prettier#how-classes-are-sorted)

## postcss 预处理

依赖

```bash
npm install -D postcss-import autoprefixer postcss-nesting
```

配置

```js
// postcss.config.js
module.exports = {
  plugins: {
    'postcss-import': {}, // css 文件分块
    'tailwindcss/nesting': 'postcss-nesting', // css 嵌套
    tailwindcss: {},
    require('autoprefixer'), // 浏览器前缀
    ...(process.env.NODE_ENV === 'production' ? { cssnano: {} } : {}) // 压缩
  }
}
```

## 核心

- 伪类
- 响应式
- 深色模式

## 指令

- `@tailwind`
	- `base` - 原生元素样式，通常是重置css默认样式
	- `components` - 组件类名
	- `utilities` - 布局、文本、背景边框、响应式等类名
	- `variants` - 变体，伪类等
- `@layer`
- `@apply` - 在css中使用tailwind
- `theme()` - 使用tailwind变量
- `screen` - 媒体查询

## js 中访问 tailwind

[参考](https://tailwindcss.com/docs/configuration#referencing-in-java-script)

```js
import resolveConfig from 'tailwindcss/resolveConfig'
import tailwindConfig from './tailwind.config.js'

const fullConfig = resolveConfig(tailwindConfig)

fullConfig.theme.width[4]
// => '1rem'

fullConfig.theme.screens.md
// => '768px'

fullConfig.theme.boxShadow['2xl']
// => '0 25px 50px -12px rgba(0, 0, 0, 0.25)'
```

## 主题切换

- Dark Mode
	- variant？
- `prefers-color-scheme` - 媒体查询功能，检测系统是否开启`dard`或者`light`模式
- css策略 - 手动切换
- `tailwind.config` 中配置 `darkmode`
	- 默认 - `prefers-color-scheme`
	- `class` - 通过css策略手动切换

radix-ui
- radix-ui 推荐使用 `next-theme`来切换主题
shadcn/ui
- 同上
daisyui
- 推荐 [`theme-change`](https://github.com/saadeghi/theme-change)
nextui
	- 推荐next-theme

> 总结: 通过修改tailwind的`darkMode`配置自定义`data-`的方式修改主题
> 使用`next-theme`切换，可以统一不同框架之间的主题切换
> TODO：内部切换机制是如何，还有待学习

