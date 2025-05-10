---
title: MOC-Health-Check
jd_id: 99.12.0001
created: 2023-11-01 16:00
updated: 2023-11-01 16:00
type: moc
status: active
schema: v1
tags: [topic/maintenance, topic/moc]
---

# 知识库健康检查

这个MOC提供了一系列查询，用于定期检查知识库的健康状态，识别需要维护的区域。

## 孤岛笔记（无链接）

没有任何出站或入站链接的笔记：

```dataview
TABLE file.cday as "创建日期", file.mday as "修改日期"
FROM "10-projects" OR "20-areas" OR "30-resources"
WHERE length(file.outlinks) = 0 AND length(file.backlinks) = 0
SORT file.mday DESC
```

## 未分类笔记

在收集箱中存在超过7天的笔记：

```dataview
TABLE file.cday as "创建日期", (date(today) - file.cday).day as "存在天数"
FROM "00-inbox"
WHERE (date(today) - file.cday).day > 7
SORT (date(today) - file.cday).day DESC
```

## 过期项目

处于活跃状态但30天未更新的项目：

```dataview
TABLE 
    owner as "负责人", 
    due as "截止日期", 
    (date(today) - file.mday).day as "未更新天数"
FROM "10-projects"
WHERE type = "project" 
    AND status = "active" 
    AND file.mday < date(today) - dur(30 days)
SORT (date(today) - file.mday).day DESC
```

## 迫近截止的项目

活跃项目中截止日期在7天内的：

```dataview
TABLE 
    owner as "负责人", 
    due as "截止日期", 
    (date(due) - date(today)).day as "剩余天数"
FROM "10-projects"
WHERE type = "project" 
    AND status = "active" 
    AND date(due) <= date(today) + dur(7 days)
    AND date(due) >= date(today)
SORT (date(due) - date(today)).day ASC
```

## 过期项目（已超截止日期）

已超过截止日期但仍处于活跃状态的项目：

```dataview
TABLE 
    owner as "负责人", 
    due as "截止日期", 
    (date(today) - date(due)).day as "逾期天数"
FROM "10-projects"
WHERE type = "project" 
    AND status = "active" 
    AND date(due) < date(today)
SORT (date(today) - date(due)).day DESC
```

## 缺少元数据的笔记

缺少关键元数据字段的笔记：

```dataview
TABLE file.folder as "文件夹"
FROM -"00-inbox" AND -"99-system"
WHERE !type OR !status OR !tags
SORT file.folder ASC
```

## 标签使用不足

标签数量少于2个的非收集箱笔记：

```dataview
TABLE 
    length(file.tags) as "标签数量", 
    file.tags as "已有标签"
FROM -"00-inbox" AND -"99-system"
WHERE length(file.tags) < 2
SORT length(file.tags) ASC
```

## 文件命名问题

文件名不符合规范的笔记（包含特殊字符或过长）：

```dataview
TABLE file.folder as "所在文件夹"
FROM "10-projects" OR "20-areas" OR "30-resources"
WHERE regexmatch(file.name, "[\\[\\]\\#\\^\\|\\*]") OR length(file.name) > 50
SORT file.folder ASC
```

## MOC健康检查

### 缺少核心领域的MOC

检查是否为每个核心技术领域创建了MOC：

```dataview
LIST
FROM "20-areas"
WHERE !startswith(file.name, "MOC-")
GROUP BY file.folder
```

### MOC链接密度检查

链接数量不足的MOC（可能需要添加更多链接）：

```dataview
TABLE 
    length(file.outlinks) as "链接数量"
FROM "20-areas" OR "99-system/MOCs"
WHERE startswith(file.name, "MOC-") AND length(file.outlinks) < 10
SORT length(file.outlinks) ASC
```

## 内容更新需求

可能需要更新的技术内容（6个月未更新）：

```dataview
TABLE 
    file.mday as "最后更新", 
    (date(today) - file.mday).month as "月数"
FROM "20-areas" OR "30-resources"
WHERE file.mday < date(today) - dur(6 months)
SORT file.mday ASC
LIMIT 20
```

## 健康报告汇总

| 指标 | 目标 | 当前 | 状态 |
|------|------|------|------|
| 孤岛笔记比例 | ≤ 5% | `= round(100 * TABLE FROM "10-projects" OR "20-areas" OR "30-resources" WHERE length(file.outlinks) = 0 AND length(file.backlinks) = 0 FLATTEN count(rows) AS count) / (TABLE FROM "10-projects" OR "20-areas" OR "30-resources" FLATTEN count(rows) AS count) END, 1)` % | - |
| 过期项目数量 | 0 | `= TABLE FROM "10-projects" WHERE type = "project" AND status = "active" AND file.mday < date(today) - dur(30 days) FLATTEN count(rows) AS count END` | - |
| 未分类笔记（>7天） | 0 | `= TABLE FROM "00-inbox" WHERE (date(today) - file.cday).day > 7 FLATTEN count(rows) AS count END` | - |
| 标签使用不足 | ≤ 10% | `= round(100 * TABLE FROM -"00-inbox" AND -"99-system" WHERE length(file.tags) < 2 FLATTEN count(rows) AS count) / (TABLE FROM -"00-inbox" AND -"99-system" FLATTEN count(rows) AS count) END, 1)` % | - |

## 维护行动

- [ ] 处理收集箱中的笔记
- [ ] 连接孤岛笔记
- [ ] 更新过期项目状态
- [ ] 完善缺少元数据的笔记
- [ ] 补充标签不足的笔记
- [ ] 更新过时的技术内容
- [ ] 检查并增强MOC链接

## 相关资源

- [[MOC-dashboard|知识库总览]]
- [[tag-system-guide|标签系统指南]]
- [[linking-strategy-guide|链接策略指南]] 