---
title: MOC-Tags
jd_id: 99.11.0001
created: 2023-11-01 14:00
updated: 2023-11-01 14:00
type: moc
status: active
schema: v1
tags: [topic/organization, topic/moc]
---

# 标签系统总览

这个 MOC 提供了知识库中所有标签的组织和管理视图，按照四大命名空间分类展示所有标签。

## 标签体系指南

- [[tag-system-guide|标签系统指南]] - 了解我们的标签体系结构和使用规范

## 标签分布总览

```dataview
TABLE length(rows) as "数量"
FROM "/"
FLATTEN file.tags as tags
GROUP BY regexreplace(tags, "^#([^/]+).*$", "$1/") as "标签命名空间"
WHERE tags
SORT length(rows) DESC
```

## 1. topic/ 主题标签

### 一级主题标签

```dataview
TABLE length(rows) as "笔记数量"
FROM "/"
FLATTEN file.tags as tags
WHERE startswith(tags, "#topic/") AND length(regexreplace(tags, "^#topic/([^/]*).*$", "$1")) = length(regexreplace(tags, "^#topic/", ""))
GROUP BY tags as "标签"
SORT length(rows) DESC
```

### 二级主题标签

```dataview
TABLE length(rows) as "笔记数量"
FROM "/"
FLATTEN file.tags as tags
WHERE startswith(tags, "#topic/") AND regexmatch(tags, "^#topic/[^/]+/[^/]+$")
GROUP BY tags as "标签"
SORT tags ASC
```

### 三级主题标签

```dataview
TABLE length(rows) as "笔记数量"
FROM "/"
FLATTEN file.tags as tags
WHERE startswith(tags, "#topic/") AND regexmatch(tags, "^#topic/[^/]+/[^/]+/.+")
GROUP BY tags as "标签"
SORT tags ASC
```

## 2. status/ 状态标签

```dataview
TABLE length(rows) as "笔记数量"
FROM "/"
FLATTEN file.tags as tags
WHERE startswith(tags, "#status/")
GROUP BY tags as "标签"
SORT length(rows) DESC
```

## 3. action/ 行动标签

```dataview
TABLE length(rows) as "笔记数量"
FROM "/"
FLATTEN file.tags as tags
WHERE startswith(tags, "#action/")
GROUP BY tags as "标签"
SORT length(rows) DESC
```

## 4. lang/ 语言标签

```dataview
TABLE length(rows) as "笔记数量"
FROM "/"
FLATTEN file.tags as tags
WHERE startswith(tags, "#lang/")
GROUP BY tags as "标签"
SORT length(rows) DESC
```

## 5. 未分类标签

以下标签不属于四大命名空间，应考虑重新分类：

```dataview
TABLE length(rows) as "笔记数量"
FROM "/"
FLATTEN file.tags as tags
WHERE tags AND !startswith(tags, "#topic/") AND !startswith(tags, "#status/") AND !startswith(tags, "#action/") AND !startswith(tags, "#lang/")
GROUP BY tags as "未分类标签"
SORT length(rows) DESC
```

## 标签维护

### 低频标签（使用次数 ≤2）

这些标签应考虑合并或删除：

TODO

### 最近添加的标签

过去 30 天内新增的标签：

```dataview
TABLE min(rows.file.ctime) as "首次使用时间"
FROM "/"
FLATTEN file.tags as tags
GROUP BY tags as "新增标签"
WHERE date(min(rows.file.ctime)) >= date(today) - dur(30 days)
SORT min(rows.file.ctime) DESC
```

## 标签管理操作

- [[tag-merge-log|标签合并记录]] - 记录已进行的标签合并操作
- [[tag-review-procedure|标签审查流程]] - 标签定期审查的标准流程
- [[tag-name-convention|标签命名约定]] - 详细的标签命名规范
