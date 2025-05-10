---
title: <% tp.file.title %> 速查表
jd_id: <% tp.user.jd_id() %>
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>
type: cheatsheet
status: active
schema: v1
tags: [topic/技术, lang/]
---

# <% tp.file.title %> 速查表

## 基础语法

| 语法 | 说明 | 示例 |
|------|------|------|
| 基础语法1 | 说明文本 | `示例代码` |
| 基础语法2 | 说明文本 | `示例代码` |

## 常用函数

| 函数 | 说明 | 示例 |
|------|------|------|
| `函数1()` | 说明文本 | `示例代码` |
| `函数2()` | 说明文本 | `示例代码` |

## 常见错误与解决方案

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| 错误1 | 原因描述 | 解决步骤 |
| 错误2 | 原因描述 | 解决步骤 |

## 最佳实践

- 最佳实践1
- 最佳实践2

## 相关资源

- [[相关技术笔记]]
- [[官方文档链接]]

<% /* 
自动更新时间脚本
此行代码确保每次保存文件时，元数据中的updated字段会更新为当前时间
请确保已正确配置Templater插件，并在99-system/scripts/目录下有update_field.js文件
如果要启用此功能，请取消下面行的注释：
*/ %>
<%* /* this.app.plugins.plugins["templater-obsidian"].templater.current_functions_object.user.update_field() */ %> 