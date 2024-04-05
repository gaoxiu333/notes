## web 的开端 - 字体

构建web总要在选择字体上纠结一下，这里记录一下web字体；

使用易于阅读的字体很重要，正确的字体也可以为品牌打造强大的形象。

## 字体基础

```css
body{
  font-family: "Open Sans","Helvetica Neue",sans-serif;
}
```

这是一段传统的无衬线的网络安全字体写法，`"Open Sans"`和`"Helvetica Neue"`这两个很容易就能看出来是两个字体的名字，`sans-serif`是什么呢？它在CSS被称为通用字体名称。

### css 通用字体名称

CSS 定义了 5 个常用的字体名称：

- `serif` - 衬线字体，衬线代表笔画末端的小装饰（比如宋体字）

- `sans-serif` - 无衬线字体，适合阅读

- `monospace` - 等宽字体，看起来比较机械，常用于代码

- `cursive` - 手写字体

- `fantasy` - 装饰字体，也可以理解为艺术字体

五种字体的通用名字，当你不知道要用什么样的无衬线字体时，直接使用通用字体名字`sans-serif`，让浏览器帮你选择字体，这样虽然方便，但是你不知道浏览器会具体使用哪一种无衬线字体。

### web 安全字体

尽量选择在所有操作系统上都支持或者预装的字体，这种字体被称为安全字体；不然会很尴尬，你精心选择的字体系统上没有时会被忽略。

```css
body{
  font-family: Helvetica, Arial, Sans-serif
}
/* 中文世界的安全字体？ */
body{
  /* 小米 */
  font-family:font-family: “Arial”,”Microsoft YaHei”,”黑体”,”宋体”,sans-serif;
  /* 淘宝 */
  font: 12px/1.5 Tahoma,Helvetica,Arial,’宋体’,sans-serif;
}
```

安全字体有点很明显，它免费且浏览器不需要下载时间，但通常看起来过时，因此不经常使用。

查看网络安全字体：

- [CSS Fonts](https://www.cssfontstack.com/) - 网站维护了一个可用在 Windows 和 Mac 操作系统上使用的网页安全字体的列表
- [CSS 网络安全字体](https://www.w3schools.com/cssref/css_websafe_fonts.php) - w3schools 总结的最佳网络安全字体

### 网络字体

比较常见的是Google和Adobe两家提供的在线字体，使用也比较简单。

- [Adobe TypeKit](https://fonts.adobe.com/)
- [Google Fonts](https://fonts.google.com/)

使用Google `Noto Sans`字体例子：

```css
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@100..900&family=Noto+Sans:ital,wght@0,100..900;1,100..900&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap')
 
body{
  font-family: "Noto Sans SC", sans-serif;
  font-optical-sizing: auto;
  font-weight: <weight>;
  font-style: normal;
}
/*  */

```

除了上面的在线托管，也可以通过自托管网络分发等方式优化字体加载速度，或者字体放在项目内使用 @font-face 来加载字体

```css
@font-face {
  font-family: myFirstFont;
  src: url(sansation_light.woff);
  ... 其他字体配置
}
```

虽然网络字体支持了更丰富的字体，以及更好看的字体，但不适合中文，因为中文字体包实在在是太大了，比如Google的`Noto Sans`简体中文就有一百多兆。

## 现代系统字体

当大多数计算机只预装了少量好的字体时（以前），网络字体在英文世界也非常有用，现在操作系统不论Windows还是Mac都预装很好看的默认字体，所以直接选择使用默认字体就行。

- [现代字体堆栈](https://github.com/system-fonts/modern-font-stacks)
- [System font stack](https://systemfontstack.com/)

```css
/* 现在主流的无衬线系统字体 */
body{
 font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"
}
```

## 我的字体堆栈

- 中文
  - [得意黑](https://github.com/atelier-anchor/smiley-sans)
  - 思源黑体
  - [赫蹏（hètí）](https://github.com/sivan/heti) - 中文排版，基于通行的中文排版规范而来
- 代码
  - [Monaspace](https://github.com/githubnext/monaspace)
- [beautiful-web-type](https://github.com/ubuwaits/beautiful-web-type) - 最佳开源字体合集

### 一些字体资料

- [size-adjust](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/size-adjust) - 控制字体缩放比例，防止两种字体切换引起页面抖动
  - [@font-face 的 CSS size-adjust](https://web.dev/articles/css-size-adjust?hl=zh-cn) 
- [字体最佳实践](https://web.dev/articles/font-best-practices?hl=zh-cn) - 主要是针对加载本地字体的速度优化
- [网页可变字体简介](https://web.dev/articles/variable-fonts?hl=zh-cn) - 介绍可变字体的优势的博文（简单来说，可变字体就是单独的字体文件就可以支持不同格式的字体。）

## 总结

安全字体已经成了过去式，网络字体对中文不适用，**系统字体更适合**。

