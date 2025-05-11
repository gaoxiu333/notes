---
title: <% tp.file.title %>
jd_id: <% tp.user.jd_id() %>
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>
type: resource
status: active
tags: [topic/learning, action/learning-resource]
resource_type: course  # course / book / video / article / tutorial
author: 
source_url: 
completion: 0  # 0-100 表示完成百分比
rating: 0  # 0-5 评分
level: beginner  # beginner / intermediate / advanced / expert
related_path: [[]]  # 相关学习路径
---

# <% tp.file.title %>

## 📋 资源概述

**类型**：<% tp.frontmatter.resource_type %>  
**作者/讲师**：<% tp.frontmatter.author %>  
**来源**：[原始链接](<% tp.frontmatter.source_url %>)  
**适合级别**：<% tp.frontmatter.level %>  
**相关学习路径**：<% tp.frontmatter.related_path %>  
**完成度**：<% tp.frontmatter.completion %>%  
**个人评分**：<% tp.frontmatter.rating %>/5  

## 📝 内容摘要

<!-- 简要描述该资源的主要内容和学习目标 -->

## 📚 章节笔记

### 第一章/部分：标题

**核心概念**：
- 概念1
- 概念2

**关键点**：
- 要点1
- 要点2

**代码示例**：
```language
// 示例代码
```

**个人思考**：
- 思考点1
- 思考点2

### 第二章/部分：标题

**核心概念**：
- 概念1
- 概念2

**关键点**：
- 要点1
- 要点2

**代码示例**：
```language
// 示例代码
```

**个人思考**：
- 思考点1
- 思考点2

## 💡 重要收获

<!-- 列出从该资源中获得的最重要收获 -->
1. 收获1
2. 收获2
3. 收获3

## 🔍 实践应用

<!-- 如何将学到的知识应用到实际项目中 -->
- 应用场景1
- 应用场景2
- 示例项目：[[项目链接]]

## 📊 学习进度追踪

| 章节/部分 | 状态 | 完成日期 | 笔记链接 |
|---------|------|---------|---------|
| 第一章/部分 | 🟢 已完成 | YYYY-MM-DD | [[链接]] |
| 第二章/部分 | 🟡 进行中 | - | - |
| 第三章/部分 | ⚪ 未开始 | - | - |

## 📝 待解决问题

<!-- 学习过程中遇到的问题和疑惑 -->
- [ ] 问题1
- [ ] 问题2

## 📚 相关资源

<!-- 与当前资源相关的其他资源 -->
- [[相关资源1]]
- [[相关资源2]]
- [外部资源](URL)
- [ ] 将此资源链接到相关MOC文件中

## 🔍 术语表

| 术语 | 定义 |
|------|------|
| 术语1 | 定义1 |
| 术语2 | 定义2 |

## 📋 复习清单

<!-- 需要定期复习的重要内容 -->
- [ ] 复习点1 - 下次复习日期：YYYY-MM-DD
- [ ] 复习点2 - 下次复习日期：YYYY-MM-DD

## 📌 引用与参考

<!-- 引用资源中的重要观点或参考资料 -->
> 引用内容

## 📅 更新记录

- <% tp.date.now("YYYY-MM-DD") %> - 初始笔记创建

<%* /* this.app.plugins.plugins["templater-obsidian"].templater.current_functions_object.user.update_field() */ %> 