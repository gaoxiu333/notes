---
title: 项目索引
jd_id: J20.05.0001
created: 2025-05-11 13:22
updated: 2025-05-11 13:22
type: moc
status: active
tags: [topic/moc, topic/projects]
---

# 项目索引

本MOC收集了各类项目的管理方法、开发实践和具体项目信息。

## 项目管理方法

- 敏捷开发（待添加）
- 看板方法（待添加）
- 项目规划与跟踪（待添加）
- 任务分解技术（待添加）

## 开发实践

- 开发流程优化（待添加）
- 代码审查最佳实践（待添加）
- 技术栈选择指南（待添加）
- 部署策略（待添加）

## 进行中的项目

- [[10-projects/10-00-PKM/00-MOC-PKM|PKM知识管理系统]] - 个人知识管理系统项目

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

## 项目模板

- 前端项目模板（待添加）
- 后端项目模板（待添加）
- 全栈项目模板（待添加）

## 项目回顾与总结

- 项目成功因素分析（待添加）
- 项目失败教训（待添加）
- 技术选型复盘（待添加）

## 相关MOC

- [[99-system/MOCs/MOC-dashboard|知识库总览]]
- [[20-areas/20-05-项目与资源/MOC-资源集合|资源集合]]
- [[20-areas/20-05-项目与资源/MOC-工具索引|工具索引]] 