---
title: <% tp.file.title %> 学习看板
jd_id: <% this.app.plugins.plugins["templater-obsidian"].templater.current_functions_object.user.jd_id() %>
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>
type: dashboard
status: active
schema: v1
tags: [主题/学习, 行动/看板]
---

# <% tp.file.title %> 学习看板

## 📋 学习主题概述

<!-- 简要描述这个学习看板涵盖的主题范围和学习目标 -->

## 📊 进度总览

<!--
使用dataview查询展示学习资源的整体完成情况
这里会展示各类型学习资源的总数、完成数、完成百分比
-->

```dataview
TABLE WITHOUT ID
  "📚 学习资源总数" as "指标",
  length(rows) as "数值"
FROM #行动/学习资源
WHERE contains(file.path, "<相关路径>")

UNION

TABLE WITHOUT ID
  "✅ 已完成资源数" as "指标",
  length(rows.completion) as "数值"
FROM #行动/学习资源
WHERE contains(file.path, "<相关路径>") AND completion = 100

UNION

TABLE WITHOUT ID
  "📈 整体完成度" as "指标",
  round(sum(rows.completion) / length(rows)) + "%" as "数值"
FROM #行动/学习资源
WHERE contains(file.path, "<相关路径>")
```

## 🔄 当前进行中

<!--
使用dataview查询展示正在学习的资源
这里会展示进度在1-99%之间的资源
-->

```dataview
TABLE WITHOUT ID
  file.link as "资源名称",
  resource_type as "类型",
  rating as "评分",
  completion + "%" as "完成度",
  level as "级别"
FROM #行动/学习资源
WHERE contains(file.path, "<相关路径>")
  AND completion > 0
  AND completion < 100
SORT completion DESC
```

## 📚 资源清单

### 课程

```dataview
TABLE
  file.link as "课程名称",
  author as "讲师",
  completion + "%" as "完成度",
  rating as "评分",
  level as "级别"
FROM #行动/学习资源
WHERE contains(file.path, "<相关路径>")
  AND resource_type = "course"
SORT completion DESC
```

### 书籍

```dataview
TABLE
  file.link as "书籍名称",
  author as "作者",
  completion + "%" as "完成度",
  rating as "评分",
  level as "级别"
FROM #行动/学习资源
WHERE contains(file.path, "<相关路径>")
  AND resource_type = "book"
SORT completion DESC
```

### 视频

```dataview
TABLE
  file.link as "视频名称",
  author as "创作者",
  completion + "%" as "完成度",
  rating as "评分",
  level as "级别"
FROM #行动/学习资源
WHERE contains(file.path, "<相关路径>")
  AND resource_type = "video"
SORT completion DESC
```

### 教程

```dataview
TABLE
  file.link as "教程名称",
  author as "作者",
  completion + "%" as "完成度",
  rating as "评分",
  level as "级别"
FROM #行动/学习资源
WHERE contains(file.path, "<相关路径>")
  AND resource_type = "tutorial"
SORT completion DESC
```

## 📝 待学习队列

<!--
使用dataview查询展示尚未开始学习的资源
这里会展示进度为0%的资源
-->

```dataview
TABLE WITHOUT ID
  file.link as "资源名称",
  resource_type as "类型",
  level as "级别",
  author as "作者/讲师"
FROM #行动/学习资源
WHERE contains(file.path, "<相关路径>")
  AND completion = 0
SORT file.ctime DESC
```

## ⭐ 高评分资源推荐

<!--
使用dataview查询展示高评分的学习资源
这里会展示评分在4分及以上的资源
-->

```dataview
TABLE WITHOUT ID
  file.link as "资源名称",
  resource_type as "类型",
  rating as "评分",
  level as "级别",
  author as "作者/讲师"
FROM #行动/学习资源
WHERE contains(file.path, "<相关路径>")
  AND rating >= 4
SORT rating DESC
```

## 🗓️ 近期学习活动

<!--
使用dataview查询展示近期更新过的学习资源
这里会展示最近30天内更新过的资源
-->

```dataview
TABLE WITHOUT ID
  file.link as "资源名称",
  resource_type as "类型",
  completion + "%" as "完成度",
  file.mtime as "最近更新"
FROM #行动/学习资源
WHERE contains(file.path, "<相关路径>")
  AND date(file.mtime) >= date(today) - dur(30 days)
SORT file.mtime DESC
```

## 🔍 学习资源按级别分组

<!--
使用dataview查询按学习级别分组展示资源
-->

```dataview
TABLE rows.file.link as "资源"
FROM #行动/学习资源
WHERE contains(file.path, "<相关路径>")
GROUP BY level
SORT length(rows) DESC
```

## 📅 复习计划

<!--
使用dataview查询展示需要复习的内容
这里可以根据复习日期提醒需要复习的内容
-->

## 📈 学习趋势图

<!--
可以使用JavaScript或Dataview来生成一个简单的学习趋势可视化
例如展示每周/每月完成的学习资源数量
-->

## 🔄 更新记录

- <% tp.date.now("YYYY-MM-DD") %> - 创建初始版本

<%* tp.meta.set("updated", tp.date.now("YYYY-MM-DD HH:mm")) %> 