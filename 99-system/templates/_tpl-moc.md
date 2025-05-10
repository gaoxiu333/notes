---
title: <% tp.file.title %>
jd_id: <% tp.user.jd_id() %>
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>
type: moc
status: active
schema: v1
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
FROM [[<% tp.file.title %>]] AND #type/resource
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

<% /* 
自动更新时间脚本
此行代码确保每次保存文件时，元数据中的updated字段会更新为当前时间
请确保已正确配置Templater插件，并在99-system/scripts/目录下有update_field.js文件
如果要启用此功能，请取消下面行的注释：
*/ %>
<%* /* this.app.plugins.plugins["templater-obsidian"].templater.current_functions_object.user.update_field() */ %> 