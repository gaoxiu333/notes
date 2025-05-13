---
title: MOC-知识库总览
jd_id: J99-20250511-1622
created: 2025-05-11 16:22
updated: 2025-05-13 08:00
type: moc
status: active
tags: [topic/moc, topic/dashboard]
---

# 知识库总览

本文档是整个知识库的中央集线器，提供了对所有主要知识领域的导航。

## 项目 (10-projects)

- [[../../10-projects/10-00-PKM/00-MOC-PKM|PKM项目]] - 个人知识管理系统的建设与维护
- [[../../10-projects/10-01-blog/00-MOC-博客项目|博客项目]] - 个人博客的设计与开发

## 领域 (20-areas)

- [[../../20-areas/20-00-方法论与思维/00-MOC-方法论|方法论与思维]] - 学习方法、思维模型和个人成长
  - [[../../20-areas/20-00-方法论与思维/学习方法/00-MOC-学习方法|学习方法]] - 高效学习的方法与技巧
- [[../../20-areas/20-01-提示词工程/00-MOC-提示词工程|提示词工程]] - AI提示词设计与优化
- [[../../20-areas/20-02-AI研究/00-MOC-AI研究|AI研究]] - 人工智能技术研究与应用
  - [[../../20-areas/20-02-AI研究/01-AI工具使用/00-MOC-AI工具|AI工具]] - AI工具使用指南
- [[../../20-areas/20-03-前端开发/00-MOC-前端开发|前端开发]] - 前端开发技能与实践
- [[../../20-areas/20-04-Nodejs/核心概念/00-MOC-Nodejs核心概念|Nodejs核心概念]] - Node.js技术基础
- [[../../20-areas/20-05-项目与资源/MOC-项目索引|项目索引]] - 项目资源导航

## 资源 (30-resources)

- [[../../30-resources/30-01-前端技术/00-MOC-前端技术|前端技术]] - 前端技术知识与资源
  - [[../../30-resources/30-01-前端技术/02-React/00-MOC-React|React]] - React框架相关资源
  - [[../../30-resources/30-01-前端技术/03-常用堆栈/00-MOC-常用堆栈|前端常用堆栈]] - 前端技术栈与架构
- [[../../30-resources/30-02-AI资源/00-MOC-AI资源|AI资源]] - AI领域的学习资源与参考资料
- [[../../30-resources/30-03-技术指南/00-MOC-技术指南|技术指南]] - 各类技术指南与教程
- [[../../30-resources/30-04-数据集/00-MOC-数据集|数据集]] - 数据集资源与处理方法
- [[../../30-resources/30-05-工具指南/00-MOC-工具指南|工具指南]] - 各类工具使用指南

## 系统 (99-system)

- [[MOC-索引管理|索引管理]] - 管理知识库的索引和分类系统
- [[MOC-模板|模板]] - 知识库中使用的各类文档模板
- [[MOC-tag-system|标签系统]] - 知识库标签系统说明
- [[../../99-system/scripts/00-MOC-scripts|脚本]] - 知识库维护和自动化脚本

## 统计与健康度

- 总文档数: {{文档数量}}
- 活跃笔记: {{活跃笔记数}}
- 未分类笔记: {{未分类笔记数}}
- 孤立笔记比例: {{孤立笔记比例}}%

## 最近更新

1. [[../../10-projects/10-01-blog/00-MOC-博客项目|博客项目]] - {{更新时间}}
2. [[../../20-areas/20-02-AI研究/01-AI工具使用/00-MOC-AI工具|AI工具]] - {{更新时间}}
3. [[../../30-resources/30-01-前端技术/00-MOC-前端技术|前端技术]] - {{更新时间}}
4. [[../../20-areas/20-00-方法论与思维/00-MOC-方法论|方法论与思维]] - {{更新时间}}
5. [[../../30-resources/30-05-工具指南/00-MOC-工具指南|工具指南]] - {{更新时间}}

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

- [[20-areas/20-03-前端开发/MOC-前端开发|前端开发]]
- [[20-areas/20-02-AI研究/MOC-AI研究|AI研究]]
- [[20-areas/20-01-提示词工程/MOC-提示词工程|提示词工程]]
- [[20-areas/20-00-方法论与思维/MOC-思维模型|思维模型]]
- [[20-areas/20-04-Nodejs/MOC-Nodejs|Node.js]]

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
- [[20-areas/20-03-前端开发/MOC-前端开发|前端开发]] - 前端技术、框架与最佳实践
- [[20-areas/20-02-AI研究/MOC-AI研究|AI研究]] - AI技术、模型与应用研究
- [[20-areas/20-01-提示词工程/MOC-提示词工程|提示词工程]] - 提示词模式、技巧与应用
- [[20-areas/20-04-Nodejs/MOC-Nodejs|Node.js]] - Node.js核心概念与应用

### 方法论与思维
- [[20-areas/20-00-方法论与思维/MOC-学习方法|学习方法]] - 学习技巧与资源
- [[20-areas/20-00-方法论与思维/MOC-思维模型|思维模型]] - 思维框架与决策方法
- [[20-areas/20-00-方法论与思维/MOC-生产力|生产力]] - 效率提升与工作流程

### 项目与资源
- [[20-areas/20-05-项目与资源/MOC-项目索引|项目索引]] - 项目管理与开发实践
- [[20-areas/20-05-项目与资源/MOC-资源集合|资源集合]] - 书籍、文章、工具等资源
- [[20-areas/20-05-项目与资源/MOC-工具索引|工具索引]] - 各类实用工具的使用指南

## 资源集合

- [[30-resources/30-01-前端技术/00-MOC-前端技术|前端资源]] - 前端开发资源与工具
- [[30-resources/30-02-AI资源/00-MOC-AI资源|AI资源]] - AI研究资源与工具
- [[30-resources/30-02-AI资源/01-MOC-AI阅读|AI阅读]] - AI相关阅读材料
- [[30-resources/30-03-技术指南/00-MOC-技术指南|技术指南]] - 各类技术主题的简明指南与参考
- [[30-resources/30-05-工具指南/00-MOC-开发工具|开发工具]] - 开发工具使用指南

## 系统维护

- [[99-system/templates/_index|模板库]] - 文档模板集合
- [[99-system/scripts/_index|脚本库]] - 自动化脚本
- [[memory-bank|记忆银行]] - 知识库核心规范和结构

---

> 最后更新: `$= dv.current().updated` 