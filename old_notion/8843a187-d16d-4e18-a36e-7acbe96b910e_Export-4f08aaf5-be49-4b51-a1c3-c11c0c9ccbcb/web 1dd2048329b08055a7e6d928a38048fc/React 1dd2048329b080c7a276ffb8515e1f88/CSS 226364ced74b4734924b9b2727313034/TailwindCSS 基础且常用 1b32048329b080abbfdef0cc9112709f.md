# TailwindCSS 基础且常用

## 基本用法 Styling with utility classes

### 概述

使用 Tailwind，通过在标记中组合多个单一用途的展示类（实用类）来样式化组件。

### 示例组件

```html
HTML

<div class="mx-auto flex max-w-sm items-center gap-x-4 rounded-xl bg-white p-6 shadow-lg outline outline-black/5 dark:bg-slate-800 dark:shadow-none dark:-outline-offset-1 dark:outline-white/10">
  <img class="size-12 shrink-0" src="/img/logo.svg" alt="ChitChat Logo" />
  <div>
    <div class="text-xl font-medium text-black dark:text-white">ChitChat</div>
    <p class="text-gray-500 dark:text-gray-400">You have a new message!</p>
  </div>
</div>

```

### 使用的工具类

- **布局和间距：** `flex`, `shrink-0`, `p-6`, `max-w-sm`, `mx-auto`
- **背景色、边框和阴影：** `bg-white`, `rounded-xl`, `shadow-lg`
- **宽度和高度：** `size-12`
- **间距：** `gap-x-4`
- **文本样式：** `text-xl`, `text-black`, `font-medium`, `text-gray-500`

### 样式的好处

- **更快完成工作**：不需要花时间命名类或决定选择器。
- **更安全的修改**：添加或移除工具类只会影响该元素。
- **更容易维护旧项目**：仅需修改类名而非大段自定义CSS。
- **代码更具可移植性**：结构和样式在同一位置，易于复制粘贴。
- **避免CSS膨胀**：工具类高度复用，CSS不会随项目增长线性增加。

### 工具类 vs 行内样式

- **设计约束**：使用工具类构建一致的UI，而非行内样式的魔法数。
- **状态样式**：工具类支持状态变体，如 `hover:bg-sky-700`。
- **媒体查询**：工具类支持响应式变体，如 `sm:grid-cols-3`。

### 响应式组件示例

```html
HTML

<div class="flex flex-col gap-2 p-8 sm:flex-row sm:items-center sm:gap-6 sm:py-4">
  <img class="mx-auto block h-24 rounded-full sm:mx-0 sm:shrink-0" src="/img/erin-lindford.jpg" alt="" />
  <div class="space-y-2 text-center sm:text-left">
    <div class="space-y-0.5">
      <p class="text-lg font-semibold text-black">Erin Lindford</p>
      <p class="font-medium text-gray-500">Product Engineer</p>
    </div>
    <button class="border-purple-200 text-purple-600 hover:border-transparent hover:bg-purple-600 hover:text-white active:bg-purple-700">
      Message
    </button>
  </div>
</div>

```

### 样式状态变体

- **示例：**
    
    ```html
    HTML
    
    <button class="bg-sky-500 hover:bg-sky-700">Save changes</button>
    
    ```
    

### 媒体查询和断点

- **示例：**
    
    ```html
    HTML
    
    <div class="grid grid-cols-2 sm:grid-cols-3">
      <!-- ... -->
    </div>
    
    ```
    

### 深色模式

- **示例：**
    
    ```html
    HTML
    
    <div class="bg-white dark:bg-gray-800 rounded-lg px-6 py-8 ring shadow-xl ring-gray-900/5">
      <div>
        <span class="inline-flex items-center justify-center rounded-md bg-indigo-500 p-2 shadow-lg">
          <svg class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
            <!-- ... -->
          </svg>
        </span>
      </div>
      <h3 class="text-gray-900 dark:text-white mt-5 text-base font-medium tracking-tight">Writes upside-down</h3>
      <p class="text-gray-500 dark:text-gray-400 mt-2 text-sm">
        The Zero Gravity Pen can be used to write in any orientation, including upside-down. It even works in outer space.
      </p>
    </div>
    
    ```
    

### 类组合

- **示例：**
    
    ```html
    HTML
    
    <div class="blur-sm grayscale">
      <!-- ... -->
    </div>
    
    ```
    

### 使用任意值

- **示例：**
    
    ```html
    HTML
    
    <button class="bg-[#316ff6]">
      Sign in with Facebook
    </button>
    
    ```
    

### 复杂选择器

- **示例：**
    
    ```html
    HTML
    
    <button class="dark:lg:data-current:hover:bg-indigo-600">
      <!-- ... -->
    </button>
    
    ```
    

### 使用组变体

- **示例：**
    
    ```html
    HTML
    
    <a href="#" class="group rounded-lg p-8">
      <!-- ... -->
      <span class="group-hover:underline">Read more…</span>
    </a>
    
    ```
    

### 使用内联样式

- **示例：**
    
    ```jsx
    JSX
    
    export function BrandedButton({ buttonColor, textColor, children }) {
      return (
        <button
          style={{
            backgroundColor: buttonColor,
            color: textColor,
          }}
          className="rounded-md px-3 py-1.5 font-medium"
        >
          {children}
        </button>
      );
    }
    
    ```
    

### 管理重复

- **使用循环：**
    
    ```html
    HTML
    
    <div>
      <div class="flex items-center space-x-2 text-base">
        <h4 class="font-semibold text-slate-900">Contributors</h4>
        <span class="bg-slate-100 px-2 py-1 text-xs font-semibold text-slate-700">204</span>
      </div>
      <div class="mt-3 flex -space-x-2 overflow-hidden">
        {#each contributors as user}
          <img class="inline-block h-12 w-12 rounded-full ring-2 ring-white" src={user.avatarUrl} alt={user.handle} />
        {/each}
      </div>
      <div class="mt-3 text-sm font-medium">
        <a href="#" class="text-blue-500">+ 198 others</a>
      </div>
    </div>
    
    ```
    
- **使用多光标编辑：**
    
    ```html
    HTML
    
    <nav class="flex justify-center space-x-4">
      <a href="/dashboard" class="font-mediu rounded-lg px-3 py-2 text-gray-700 hover:bg-gray-100 hover:text-gray-900">Home</a>
      <a href="/team" class="font-mediu rounded-lg px-3 py-2 text-gray-700 hover:bg-gray-100 hover:text-gray-900">Team</a>
      <a href="/projects" class="font-mediu rounded-lg px-3 py-2 text-gray-700 hover:bg-gray-100 hover:text-gray-900">Projects</a>
      <a href="/reports" class="font-mediu rounded-lg px-3 py-2 text-gray-700 hover:bg-gray-100 hover:text-gray-900">Reports</a>
    </nav>
    
    ```
    
- **使用组件：**
    
    ```jsx
    JSX
    
    export function VacationCard({ img, imgAlt, eyebrow, title, pricing, url }) {
      return (
        <div>
          <img className="rounded-lg" src={img} alt={imgAlt} />
          <div className="mt-4">
            <div className="text-xs font-bold text-sky-500">{eyebrow}</div>
            <div className="mt-1 font-bold text-gray-700">
              <a href={url} className="hover:underline">{title}</a>
            </div>
            <div className="mt-2 text-sm text-gray-600">{pricing}</div>
          </div>
        </div>
      );
    }
    
    ```
    
- **使用自定义CSS：**
    
    ```html
    HTML
    
    <button class="btn-primary">Save changes</button>
    
    ```
    
    ```css
    CSS
    
    @import "tailwindcss";
    @layer components {
      .btn-primary {
        border-radius: calc(infinity * 1px);
        background-color: var(--color-violet-500);
        padding-inline: --spacing(5);
        padding-block: --spacing(2);
        font-weight: var(--font-weight-semibold);
        color: var(--color-white);
        box-shadow: var(--shadow-md);
        &:hover {
          @media (hover: hover) {
            background-color: var(--color-violet-700);
          }
        }
      }
    }
    
    ```
    

### 管理样式冲突

- **冲突的工具类：**
    
    ```html
    HTML
    
    <div class="grid flex">
      <!-- ... -->
    </div>
    
    ```
    
- **使用 `important` 修饰符：**
    
    ```html
    HTML
    
    <div class="bg-teal-500 bg-red-500!">
      <!-- ... -->
    </div>
    
    ```
    
- **使用 `important` 标记：**
    
    ```css
    CSS
    
    @import "tailwindcss" important;
    
    ```
    
- **使用前缀选项：**
    
    ```css
    CSS
    
    @import "tailwindcss" prefix(tw);
    
    ```
    

## 变体：Hover, focus, and other states

## 状态样式

### 伪类

- `hover:` 鼠标悬停时应用
- `focus:` 元素获得焦点时应用
- `active:` 元素被激活时应用
- `visited:` 链接被访问后应用
- `focus-within:` 元素或其子元素获得焦点时应用
- `focus-visible:` 使用键盘导航时应用

### 示例

```html
HTML

<button class="bg-blue-500 hover:bg-blue-700 focus:outline-none">按钮</button>

```

### 伪元素

- `before:` 在元素前应用样式
- `after:` 在元素后应用样式
- `placeholder:` 对输入框的占位符应用样式
- `marker:` 列表标记符号应用样式
- `selection:` 选中文本应用样式
- `file:` 文件输入按钮样式

### 示例

```html
HTML

<input class="placeholder:text-gray-500 placeholder:italic" placeholder="输入内容...">

```

## 响应式断点

- `sm:` 小屏幕
- `md:` 中屏幕
- `lg:` 大屏幕
- `xl:` 超大屏幕
- `2xl:` 特大屏幕

### 示例

```html
HTML

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4">内容</div>

```

## 媒体查询

- `dark:` 深色模式
- `motion-reduce:` 减少动画
- `motion-safe:` 保持动画
- `contrast-more:` 高对比度模式
- `contrast-less:` 低对比度模式
- `print:` 打印模式

### 示例

```html
HTML

<div class="bg-white dark:bg-gray-900">内容</div>

```

## 表单状态

- `disabled:` 禁用状态
- `required:` 必填状态
- `invalid:` 无效输入
- `valid:` 有效输入
- `checked:` 选中状态
- `indeterminate:` 不确定状态

### 示例

```html
HTML

<input type="text" class="disabled:bg-gray-200 required:border-red-500">

```

## 属性选择器

- `aria-checked:` 基于 ARIA 属性
- `data-[...]` 基于自定义数据属性

### 示例

```html
HTML

<div aria-checked="true" class="aria-checked:bg-sky-700">内容</div>

```

## 父子关系

- `group:` 父元素组
- `peer:` 兄弟元素组

### 示例

```html
HTML

<div class="group">
  <button class="group-hover:text-red-500">按钮</button>
</div>

```

## 自定义变体

- 使用任意变体通过方括号定义自定义选择器
- `supports-[...]` 基于功能支持
- `not-[...]` 取反条件

### 示例

```html
HTML

<div class="bg-white supports-[display:grid]:bg-gray-900">内容</div>

```

## 其他

- `first:` 第一个子元素
- `last:` 最后一个子元素
- `odd:` 奇数子元素
- `even:` 偶数子元素
- `empty:` 空元素
- `only:` 唯一子元素

### 示例

```html
HTML

<ul>
  <li class="first:pt-0 last:pb-0 odd:bg-gray-200">项</li>
</ul>

```

## 快速参考表

| **变体** | **CSS** |
| --- | --- |
| `hover` | `&:hover` |
| `focus` | `&:focus` |
| `active` | `&:active` |
| `visited` | `&:visited` |
| `target` | `&:target` |
| `first` | `&:first-child` |
| `last` | `&:last-child` |
| `odd` | `&:nth-child(odd)` |
| `even` | `&:nth-child(even)` |
| `disabled` | `&:disabled` |
| `enabled` | `&:enabled` |
| `checked` | `&:checked` |
| `indeterminate` | `&:indeterminate` |
| `default` | `&:default` |
| `optional` | `&:optional` |
| `required` | `&:required` |
| `valid` | `&:valid` |
| `invalid` | `&:invalid` |
| `in-range` | `&:in-range` |
| `out-of-range` | `&:out-of-range` |
| `placeholder-shown` | `&:placeholder-shown` |
| `autofill` | `&:autofill` |
| `read-only` | `&:read-only` |
| `before` | `&::before` |
| `after` | `&::after` |
| `first-letter` | `&::first-letter` |
| `first-line` | `&::first-line` |
| `marker` | `&::marker` |
| `selection` | `&::selection` |
| `file` | `&::file-selector-button` |
| `backdrop` | `&::backdrop` |
| `placeholder` | `&::placeholder` |
| `sm` | `@media (min-width: 640px)` |
| `md` | `@media (min-width: 768px)` |
| `lg` | `@media (min-width: 1024px)` |
| `xl` | `@media (min-width: 1280px)` |
| `2xl` | `@media (min-width: 1536px)` |
| `dark` | `@media (prefers-color-scheme: dark)` |
| `motion-safe` | `@media (prefers-reduced-motion: no-preference)` |
| `motion-reduce` | `@media (prefers-reduced-motion: reduce)` |
| `contrast-more` | `@media (prefers-contrast: more)` |
| `contrast-less` | `@media (prefers-contrast: less)` |
| `print` | `@media print` |
| `supports-[...]` | `@supports (...)` |
| `aria-[...]` | `&[aria-...]` |
| `data-[...]` | `&[data-...]` |
| `rtl` | `&:dir(rtl)` |
| `ltr` | `&:dir(ltr)` |
| `open` | `&[open]` |

通过这个简洁的速查表，你可以更高效地使用 Tailwind CSS 进行开发。