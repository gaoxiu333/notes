---
title: <% tp.file.title %>
jd_id: <% this.app.plugins.plugins["templater-obsidian"].templater.current_functions_object.user.jd_id() %>
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>
type: review
status: active
schema: v1
tags: [action/review]
review_period: "weekly" # weekly/monthly/quarterly/project
---

# <% tp.file.title %> 复盘

## 📋 复盘概述

**复盘周期**: <% tp.frontmatter.review_period %>
**复盘范围**: <!-- 项目名称/学习课程/技术领域 -->
**相关链接**: <!-- 相关项目或资源链接 -->

## 🎯 目标回顾

<!-- 原定目标与完成情况 -->
- [ ] 目标1
- [ ] 目标2

## ✅ 成功之处

<!-- 列出取得的成果和做得好的地方 -->
1. 
2. 

## 🚧 挑战与问题

<!-- 列出遇到的困难和问题 -->
1. 
2. 

## 💡 关键收获

<!-- 总结学到的重要知识点或技能 -->
1. 
2. 

## 🔄 改进机会

<!-- 列出需要改进的地方和具体行动 -->
1. 
2. 

## 📚 可复用的知识

<!-- 提取可以应用到其他场景的知识 -->
1. 

## 📝 行动计划

<!-- 下一步具体行动 -->
- [ ] 
- [ ] 

## 📊 度量与数据

<!-- 相关的量化指标和数据 -->
- 

## 🔗 相关参考

<!-- 链接到相关笔记、资源或参考材料 -->
- [[]]
- [[]]

<%* tp.meta.set("updated", tp.date.now("YYYY-MM-DD HH:mm")) %> 