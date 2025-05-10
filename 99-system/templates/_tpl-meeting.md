---
title: <% tp.file.title %>
jd_id: <% tp.user.jd_id() %>
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>
type: note
status: active
schema: v1
tags: [action/meeting]
---

# <% tp.file.title %> 会议纪要

## 会议信息

- **日期时间**：<% tp.date.now("YYYY-MM-DD HH:mm") %>
- **参与人员**：
- **会议目的**：

## 议程

1. 
2. 
3. 

## 讨论内容

### 主题1

- 
- 

### 主题2

- 
- 

## 决策事项

- [ ] 决策1：
- [ ] 决策2：

## 行动项

- [ ] 任务1 - 负责人：@xxx, 截止日期：
- [ ] 任务2 - 负责人：@xxx, 截止日期：

## 后续会议

- 下次会议日期：
- 下次会议主题：

## 附件与链接

- [[相关文档]]

<% /* 
自动更新时间脚本
此行代码确保每次保存文件时，元数据中的updated字段会更新为当前时间
请确保已正确配置Templater插件，并在99-system/scripts/目录下有update_field.js文件
如果要启用此功能，请取消下面行的注释：
*/ %>
<%* /* this.app.plugins.plugins["templater-obsidian"].templater.current_functions_object.user.update_field() */ %> 