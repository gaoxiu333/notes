---
title: MOC-知识库总览
jd_id: J99-20250511-1622
created: 2025-05-11 16:22
updated: 2025-05-13 17:03
type: moc
status: active
tags: [topic/moc, topic/dashboard]
---

# 📚 知识库总览

本文档是整个知识库的中央集线器，提供了对所有主要知识领域的导航。

## 🎯 核心领域&重要参考

- [[../../20-areas/20-03-前端开发/00-MOC-前端开发|前端开发]]
- [[../../20-areas/20-02-AI研究/00-MOC-AI研究|AI研究]]
- [[../../20-areas/20-01-提示词工程/00-MOC-提示词工程|提示词工程]]
- [[../../20-areas/20-00-方法论与思维/00-MOC-方法论|思维模型]]
- [[../../20-areas/20-04-Nodejs/核心概念/00-MOC-Nodejs核心概念|Node.js]]
- [[00-MCP相关资源|MCP相关资源]]
- [[02-个人-AI-导航|AI 导航]]

## 📂 知识体系

### 项目 (10-projects)

- [[../../10-projects/10-00-PKM/00-MOC-PKM|PKM项目]] - 个人知识管理系统的建设与维护
- [[../../10-projects/10-01-blog/00-MOC-博客项目|博客项目]] - 个人博客的设计与开发

### 领域 (20-areas)

- [[../../20-areas/20-00-方法论与思维/00-MOC-方法论|方法论与思维]]
  - [[../../20-areas/20-00-方法论与思维/学习方法/00-MOC-学习方法|学习方法]]
  - [[../../20-areas/20-00-方法论与思维/MOC-思维模型|思维模型]]
  - [[../../20-areas/20-00-方法论与思维/MOC-生产力|生产力]]
- [[../../20-areas/20-01-提示词工程/00-MOC-提示词工程|提示词工程]]
- [[../../20-areas/20-02-AI研究/00-MOC-AI研究|AI研究]]
  - [[../../20-areas/20-02-AI研究/01-AI工具使用/00-MOC-AI工具|AI工具]]
- [[../../20-areas/20-03-前端开发/00-MOC-前端开发|前端开发]]
- [[../../20-areas/20-04-Nodejs/核心概念/00-MOC-Nodejs核心概念|Nodejs核心概念]]
- [[../../20-areas/20-05-项目与资源/MOC-项目索引|项目索引]]

### 资源 (30-resources)

- [[../../30-resources/30-01-前端技术/00-MOC-前端技术|前端技术]]
  - [[../../30-resources/30-01-前端技术/02-React/00-MOC-React|React]]
  - [[../../30-resources/30-01-前端技术/03-常用堆栈/00-MOC-常用堆栈|前端常用堆栈]]
- [[../../30-resources/30-02-AI资源/00-MOC-AI资源|AI资源]]
  - [[../../30-resources/30-02-AI资源/01-MOC-AI阅读|AI阅读]]
- [[../../30-resources/30-03-技术指南/00-MOC-技术指南|技术指南]]
- [[../../30-resources/30-04-数据集/00-MOC-数据集|数据集]]
- [[../../30-resources/30-05-工具指南/00-MOC-工具指南|工具指南]]
  - [[../../30-resources/30-05-工具指南/00-MOC-开发工具|开发工具]]

### 系统 (99-system)

- [[MOC-索引管理|索引管理]] - 管理知识库的索引和分类系统
- [[MOC-模板|模板]] - 知识库中使用的各类文档模板
- [[MOC-tag-system|标签系统]] - 知识库标签系统说明
- [[../../99-system/scripts/00-MOC-scripts|脚本]] - 知识库维护和自动化脚本

## 📊 知识库状态

### 统计与健康度

```dataview
TABLE WITHOUT ID
	length(rows) as "文档数量",
	length(filter(rows, (r) => length(r.file.outlinks) = 0)) as "无出链笔记",
	length(filter(rows, (r) => length(r.file.backlinks) = 0)) as "无入链笔记"
FROM "10-projects" OR "20-areas" OR "30-resources"
GROUP BY null
```

### 最近更新

```dataview
TABLE without id
	file.link as "笔记",
	updated as "更新时间"
FROM "00-inbox" or "10-projects" or "20-areas" or "30-resources"
SORT updated DESC
LIMIT 10
```

## 📋 任务管理

### 待办任务

```dataview
TASK
FROM "10-projects" or "20-areas"
WHERE !completed
LIMIT 10
```

### 需要关注

#### 未分类笔记 (超过 7 天)

```dataview
LIST
FROM "00-inbox"
WHERE date(today) - date(file.ctime) > dur(7 days)
LIMIT 5
```

#### 孤岛笔记

```dataview
LIST
FROM "10-projects" OR "20-areas" OR "30-resources"
WHERE length(file.outlinks) = 0 AND length(file.backlinks) = 0
LIMIT 5
```

#### 过期项目

```dataview
LIST
FROM "10-projects"
WHERE type = "project" AND status = "active" AND date(updated) < date(today) - dur(30 days)
LIMIT 5
```

## 🔄 知识管理流程

- [[MOC-capture|捕获]] - 信息收集与记录
- [[MOC-process|处理]] - 信息整理与分类
- [[MOC-organize|组织]] - 知识结构化与关联
- [[MOC-express|输出]] - 知识应用与分享

## 🛠️ 系统维护

- [[99-system/templates/_index|模板库]] - 文档模板集合
- [[99-system/scripts/_index|脚本库]] - 自动化脚本
- [[memory-bank|记忆银行]] - 知识库核心规范和结构

---

> [!tip] 最后更新
> `$= dv.current().updated`
