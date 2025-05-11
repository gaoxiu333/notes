---
title: <% tp.date.now("YYYY-MM-DD") %>
jd_id: <% tp.user.jd_id() %>
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>
type: daily
status: active
tags: [topic/daily-note, status/active]
---

# <% tp.date.now("YYYY-MM-DD") %> 日记

## 📝 今日计划

- [ ] 

## 📥 收集箱

> 临时想法、灵感、链接等快速捕获

- 

## 📊 今日进度

- 

## 🔄 复盘

### 🎯 完成的任务

- 

### 💡 新的发现/想法

- 

### 📚 学习内容

- 

### ⏭️ 明日计划

- [ ] 

<%* tp.file.cursor() %> 

<%* /* this.app.plugins.plugins["templater-obsidian"].templater.current_functions_object.user.update_field() */ %> 