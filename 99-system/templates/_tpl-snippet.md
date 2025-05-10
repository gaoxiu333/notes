---
title: <% tp.file.title %>
jd_id: <% tp.user.jd_id() %>
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>
type: snippet
status: active
language: javascript
schema: v1
tags: [lang/javascript]
---

# <% tp.file.title %>

## 用途

简要描述该代码片段的用途和功能。

## 代码

```javascript
// 示例代码
function example() {
  return 'Hello World';
}
```

## 使用示例

```javascript
// 使用示例
const result = example();
console.log(result); // 输出: Hello World
```

## 参数说明

| 参数名 | 类型 | 默认值 | 描述 |
|-------|------|-------|------|
| param1 | String | '' | 参数1的描述 |
| param2 | Number | 0 | 参数2的描述 |

## 注意事项

- 使用此代码片段的注意事项
- 可能的副作用或限制

## 相关代码

- [[相关代码片段]]
- [[相关技术概念]]

<% /* 
自动更新时间脚本
此行代码确保每次保存文件时，元数据中的updated字段会更新为当前时间
请确保已正确配置Templater插件，并在99-system/scripts/目录下有update_field.js文件
如果要启用此功能，请取消下面行的注释：
*/ %>
<%* /* this.app.plugins.plugins["templater-obsidian"].templater.current_functions_object.user.update_field() */ %> 