---
title: <% tp.file.title %>
jd_id: <% this.app.plugins.plugins["templater-obsidian"].templater.current_functions_object.user.jd_id() %>
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>
type: snippet
status: active
language: javascript
schema: v1
tags: [lang/javascript]
complexity: 2       # 1-5，越高越复杂
reusability: 4      # 1-5，越高越容易复用
performance: 3      # 1-5，越高性能越好
maintainability: 4  # 1-5，越高越容易维护
tested: true        # 是否经过测试
environment: all    # browser/node/all
---

# <% tp.file.title %>

## 📝 概述

<!-- 简要描述该代码片段的用途、功能及解决的问题 -->

## 🧩 代码

```javascript
// 代码片段内容
function example() {
  return 'Hello World';
}
```

## 🚀 使用示例

```javascript
// 使用示例
const result = example();
console.log(result); // 输出: Hello World
```

## 📊 参数说明

| 参数名 | 类型 | 默认值 | 必填 | 描述 |
|-------|------|-------|------|------|
| param1 | String | '' | ✅ | 参数1的描述 |
| param2 | Number | 0 | ❌ | 参数2的描述 |

## 📋 返回值

| 类型 | 描述 |
|------|------|
| String | 返回值的描述 |

## ⚠️ 注意事项

- 使用此代码片段的注意事项
- 可能的副作用或限制
- 兼容性问题

## 🔍 工作原理

<!-- 简要解释代码的工作原理或算法 -->

## 🔄 替代方案

<!-- 可能的替代实现方法或库 -->

## 📚 相关代码片段

- [[相关代码片段1]]
- [[相关代码片段2]]

## 🔗 相关概念

- [[相关技术概念1]]
- [[相关技术概念2]]

## 📖 参考资料

<!-- 参考的文档、文章或资源链接 -->
- [MDN Web Docs](https://developer.mozilla.org/)
- [Stack Overflow问题](https://stackoverflow.com/)

## 📝 使用情境

<!-- 适合使用此代码片段的情境 -->
- 情境1
- 情境2

## 🏷️ 修改历史

- <% tp.date.now("YYYY-MM-DD") %> - 创建初始版本

<%* this.app.plugins.plugins["templater-obsidian"].templater.current_functions_object.user.update_field() %> 