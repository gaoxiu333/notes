# SVG

## path

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

