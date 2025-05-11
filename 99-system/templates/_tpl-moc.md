---
title: <% tp.file.title %>
jd_id: <% tp.user.jd_id() %>
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>
type: moc
status: active
tags: [topic/moc]
---

# <% tp.file.title %> 内容地图

## 概述

简要描述本MOC涵盖的内容领域和组织方式。

## 核心概念

- [[概念1]]
- [[概念2]]
- [[概念3]]

## 主要内容

### 分类1

- [[相关笔记1]]
- [[相关笔记2]]

### 分类2

- [[相关笔记3]]
- [[相关笔记4]]

## 常用资源

```dataview
LIST
FROM [[<% tp.file.title %>]] AND #topic/resource
SORT file.ctime DESC
```

## 最近更新

```dataview
TABLE updated as "更新时间", file.folder as "位置"
FROM [[<% tp.file.title %>]]
SORT updated DESC
LIMIT 10
```

## 相关MOC

- [[MOC-dashboard|仪表盘]]
- [[相关领域MOC]]
- [ ] 将此MOC链接到全局MOC仪表盘

<%* /* this.app.plugins.plugins["templater-obsidian"].templater.current_functions_object.user.update_field() */ %> 