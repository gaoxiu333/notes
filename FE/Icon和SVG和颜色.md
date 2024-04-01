## Icon 资源推荐

- [流行品牌SVG库](https://simpleicons.org/)
- [iconify](https://iconify.design/) - 开源的矢量图标- nextjs 服务端组件不可用
- [Feather Icons](https://github.com/feathericons/feather)
- [Lucide](https://github.com/lucide-icons/lucide) - feather 替代

## SVG 常用属性

在SVG中常用的就是，填充以及描边这两个简单的属性，后续学习到其他属性再补充～

- `fill` - 填充颜色
  - 常用值：`#000`、`none`、`inherit`、`currentColor`、`transparent`
- `stroke` - 描边
  - 常用值：`#000`、`none`、`inherit`、`currentColor`、`transparent`
- `stroke-width` - 描边宽度
  - 常用值：`0`、`123...`
- 其他
  - `fill-opacity`
  - `stroke-opacity`
  - `transformation`

## SVG 绘制

[参考](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Tutorial/Paths)

`path`元素是 SVG 中最强大的一个，可以创建线条，曲线，弧形等

#### 命令

- `M` 移动画笔，只会移动画笔不画线
- `H` 绘制水平线
- `V` 垂直
- `L` 将会在当前位置和新位置（L 前面画笔所在的点）之间画一条线段。

大写标识绝对定义，小写表示相对定位

#### 例子

```html
 <path d="M 10 10 H 90 V 90 L 10 100 Z " fill="transparent" stroke="black"/>
```

- `M 10 10` 向右、下移动画笔 10
- `H 90`  水平绘制一条长 90 的线
- `V 90` 垂直绘制一条长 90 的线
- `L 10 100` 绘制到 距离坐标原点(10,100)
- `Z` 结束

