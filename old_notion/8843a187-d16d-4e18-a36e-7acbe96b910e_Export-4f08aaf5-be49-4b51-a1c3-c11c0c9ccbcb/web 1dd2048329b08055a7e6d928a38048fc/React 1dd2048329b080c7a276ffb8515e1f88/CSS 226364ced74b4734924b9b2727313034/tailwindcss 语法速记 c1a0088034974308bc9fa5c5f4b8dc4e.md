# tailwindcss 语法速记

# **tailwindcss 语法速记**

## **伪元素**

参考：[Pseudo-elements](https://tailwindcss.com/docs/hover-focus-and-other-states#pseudo-elements)

```html
<label class="block">
  <span class="after:content-['*'] after:ml-0.5 after:text-red-500 block text-sm font-medium text-slate-700">
    Email
  </span>
  <input type="email" name="email" class="mt-1 px-3 py-2 bg-white border shadow-sm border-slate-300 placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-sky-500 block w-full rounded-md sm:text-sm focus:ring-1" placeholder="you@example.com" />
</label>
```

## 核心概念

### Function & Directives

## 速查表

### Tailwind CSS 速查表

### 布局

- `flex`：设置元素为弹性容器。
- `inline-flex`：设置元素为内联弹性容器。
- `flex-row`：设置弹性容器的主轴为水平方向。
- `flex-col`：设置弹性容器的主轴为垂直方向。
- `items-center`：设置弹性项目在交叉轴上的居中对齐。
- `justify-center`：设置弹性项目在主轴上的居中对齐。
- `p-{n}`：设置内边距（`n` 为 0 到 96 的数值）。
- `m-{n}`：设置外边距（`n` 为 0 到 96 的数值）。

### 尺寸

- `w-full`：设置元素宽度为 100%。
- `w-1/2`：设置元素宽度为 50%。
- `h-screen`：设置元素高度为视口高度。
- `min-w-0`：设置元素最小宽度为 0。
- `max-w-xs`：设置元素最大宽度为 `20rem`。
- `min-h-0`：设置元素最小高度为 0。
- `max-h-xs`：设置元素最大高度为 `20rem`。

### 排版

- `text-xs`：设置字体大小为 `0.75rem`。
- `text-base`：设置字体大小为 `1rem`。
- `text-2xl`：设置字体大小为 `1.5rem`。
- `font-thin`：设置字体粗细为 100。
- `font-bold`：设置字体粗细为 700。
- `text-left`：设置文本左对齐。
- `text-center`：设置文本居中对齐。
- `text-gray-500`：设置文本颜色为灰色（500）。
- `text-black`：设置文本颜色为黑色。

### 背景

- `bg-white`：设置背景颜色为白色。
- `bg-gray-800`：设置背景颜色为灰色（800）。
- `bg-cover`：设置背景图像覆盖。
- `bg-center`：设置背景图像居中。

### 边框

- `border`：设置边框宽度为 1px。
- `border-2`：设置边框宽度为 2px。
- `border-solid`：设置边框样式为实线。
- `border-dashed`：设置边框样式为虚线。
- `rounded`：设置元素的边框半径为 `0.25rem`。
- `rounded-lg`：设置元素的边框半径为 `0.5rem`。
- `border-gray-500`：设置边框颜色为灰色（500）。
- `border-blue-500`：设置边框颜色为蓝色（500）。

### 效果

- `shadow-sm`：设置小阴影。
- `shadow-lg`：设置大阴影。
- `opacity-50`：设置不透明度为 50%。
- `opacity-100`：设置不透明度为 100%。

### 交互

- `hover:bg-blue-500`：悬停时背景颜色变为蓝色（500）。
- `focus:border-blue-500`：聚焦时边框颜色变为蓝色（500）。
- `active:bg-blue-800`：激活时背景颜色变为蓝色（800）。

### 响应式设计

- `sm:text-sm`：在小屏幕上设置字体大小为 `0.875rem`。
- `md:text-base`：在中屏幕上设置字体大小为 `1rem`。
- `lg:text-lg`：在大屏幕上设置字体大小为 `1.125rem`。
- `xl:text-xl`：在超大屏幕上设置字体大小为 `1.25rem`。
- `sm:w-1/2`：在小屏幕上设置宽度为 50%。
- `md:w-1/3`：在中屏幕上设置宽度为 33.33%。
- `lg:w-1/4`：在大屏幕上设置宽度为 25%。
- `xl:w-1/5`：在超大屏幕上设置宽度为 20%。

### 暗模式

- `dark:bg-gray-800`：在暗模式下设置背景颜色为灰色（800）。
- `dark:text-white`：在暗模式下设置文本颜色为白色。

### 组选择器

- `.group`：标记父元素。
- `group-hover:*`：父元素悬停时，子元素应用样式。
- `group-focus:*`：父元素聚焦时，子元素应用样式。

### 兄弟选择器

- `.peer`：标记兄弟元素。
- `peer-hover:*`：兄弟元素悬停时，应用样式。
- `peer-checked:*`：兄弟元素被选中时，应用样式。

### 父子选择器

- `hover:*`：悬停时应用样式。
- `focus:*`：聚焦时应用样式。

## 常见问题

- 管理 CSS 冲突，如使用 important 等：[参考](https://tailwindcss.com/docs/styling-with-utility-classes#managing-style-conflicts)