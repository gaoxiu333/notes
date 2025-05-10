---
title: <% tp.file.title %>
jd_id: <% this.app.plugins.plugins["templater-obsidian"].templater.current_functions_object.user.jd_id() %>
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>
type: capture
status: draft
schema: v1
tags: [action/process]
---

# <% tp.file.title %>

<% tp.file.cursor() %>

## 参考链接

- 

## 相关想法

- 

## 后续行动

- [ ] 分类并移动到对应区域
- [ ] 添加相关链接和标签
- [ ] 补充更多细节

<%* tp.meta.set("updated", tp.date.now("YYYY-MM-DD HH:mm")) %> 