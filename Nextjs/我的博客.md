# 我是如何构建我的博客的

## Markdown 处理



### 元数据

```markdown
---
title: Next.js 入门
publishedOn: '2023-05-09T03:05:58.626Z'
updatedOn: '2023-05-09T03:05:58.626Z'
# title: How I Built My Blog
# seoTitle: How I Built my Blog using MDX, Next.js, and React
# abstract: An in-depth look at the technical structure for my blog.
# isPublished: true
# publishedOn: 2021-04-20T09:15:00-0400
# layout: Article
---
```

- 通过nodejs的`readFileSync` 读取文件内容
- 使用`gray-matter` 解析元信息
- 使用`reading-time`解析文章阅读时间





## 草稿

以标签为分类查看

比如：vue 标签

- 该标签匹配到很多堆栈，这些堆栈还可以有其他标签
- 遍历堆栈多其他标签，进行归类渲染在一个 card里面
- 最后，为了减轻不熟悉的人的心智负担，预先设置好一些标签，以供快速查看

预先：

1. 前端框架
2. vue 技术栈... 其他
3. nodejs
4. python
5. 学习资源？
6. 前端！！

UI -------->

列出前端技术栈

vue、react、angular

列出node技术栈

列出python框架

列出数据库

列出学习资源

开源项目？

- 主页技术栈卡片---->只显示主技术栈+icon(要不要显示名字？版本号？)



## 预览页面

标题 - 堆栈

副标题 - == 深色->我使用过的堆栈 浅色 ==> 我很感兴趣，但是还没有使用的堆栈

技术栈1...

卡片...

- 卡片内容：技术栈名称

  - 比如：前端技术栈，与这个技术栈相关的icon

- 详情

  - vue...
  - 构建平台
  - UI框架
  - 动画
  - 样式
  - 以上是分类
  - 具体显示，就直接显示详情吧，一列显示，简单专注

  TODO=>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

- 会动的向右箭头