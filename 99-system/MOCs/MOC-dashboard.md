---
title: MOC-dashboard
created: 2024-06-29 15:20
updated: 2025-05-09 23:15
type: moc
status: active
schema: v1
tags: [topic/moc, topic/dashboard]
---

# 📊 知识库总览仪表盘

## 📑 系统导航

- [[MOC-tags|标签系统]] - 标签管理与维护
- [[MOC-health-check|健康检查]] - 知识库健康状态监控
- [[tag-system-guide|标签系统指南]] - 标签使用规范
- [[linking-strategy-guide|链接策略指南]] - 建立有效链接的方法
- [[graph-view-guide|图谱视图指南]] - 图谱配置与使用

## 🚀 活跃项目

```dataview
TABLE without id 
	file.link as "项目", 
	owner as "负责人", 
	due as "截止日期",
	(date(due) - date(today)).day as "剩余天数"
FROM "10-projects"
WHERE type = "project" AND status = "active" 
SORT (date(due) - date(today)).day ASC
```

## 💼 核心领域

- [[MOC-前端开发|前端开发]]
- [[MOC-AI研究|AI研究]]
- [[MOC-提示词工程|提示词工程]]

## 📚 最近更新

```dataview
TABLE without id 
	file.link as "笔记", 
	updated as "更新时间"
FROM "00-inbox" or "10-projects" or "20-areas" or "30-resources"
SORT updated DESC
LIMIT 10
```

## 📋 待办任务

```dataview
TASK
FROM "10-projects" or "20-areas"
WHERE !completed
LIMIT 20
```

## 📈 知识库健康状态

### 未分类笔记

```dataview
LIST
FROM "00-inbox"
WHERE date(today) - date(file.ctime) > dur(7 days)
```

### 孤岛笔记 (无链接)

```dataview
LIST
FROM "10-projects" OR "20-areas" OR "30-resources"
WHERE length(file.outlinks) = 0 AND length(file.backlinks) = 0
LIMIT 10
```

### 过期项目

```dataview
LIST
FROM "10-projects"
WHERE type = "project" AND status = "active" AND date(updated) < date(today) - dur(30 days)
```

## 🔄 知识循环

- [[MOC-capture|捕获流程]]
- [[MOC-process|处理流程]]
- [[MOC-organize|组织流程]]
- [[MOC-express|输出流程]]

## 主要领域

### 开发技术
- [[20-areas/20-01-前端开发/MOC-前端开发|前端开发]] - 前端技术、框架与最佳实践
- [[20-areas/20-02-AI研究/MOC-AI研究|AI研究]] - AI技术、模型与应用研究
- [[20-areas/20-03-提示词工程/MOC-提示词工程|提示词工程]] - 提示词模式、技巧与应用

### 方法论与思维
- [[20-areas/20-04-方法论与思维/MOC-学习方法|学习方法]] - 学习技巧与资源
- [[20-areas/20-04-方法论与思维/MOC-思维模型|思维模型]] - 思维框架与决策方法
- [[20-areas/20-04-方法论与思维/MOC-生产力|生产力]] - 效率提升与工作流程

### 项目与资源
- [[20-areas/20-05-项目与资源/MOC-项目索引|项目索引]] - 项目管理与开发实践
- [[20-areas/20-05-项目与资源/MOC-资源集合|资源集合]] - 书籍、文章、工具等资源
- [[20-areas/20-05-项目与资源/MOC-工具索引|工具索引]] - 各类实用工具的使用指南

## 资源集合

- [[30-resources/30-01-前端技术/MOC-前端资源|前端资源]] - 前端开发资源与工具
- [[30-resources/30-02-AI资源/MOC-AI资源|AI资源]] - AI研究资源与工具
- [[30-resources/30-02-AI资源/MOC-AI阅读|AI阅读]] - AI相关阅读材料
- [[30-resources/code-snippets/MOC-代码片段|代码片段]] - 常用代码片段集合

## 系统维护

- [[99-system/templates/_index|模板库]] - 文档模板集合
- [[99-system/scripts/_index|脚本库]] - 自动化脚本
- [[memory-bank|记忆银行]] - 知识库核心规范和结构

---

> 最后更新: `$= dv.current().updated` 