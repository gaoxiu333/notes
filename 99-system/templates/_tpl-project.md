---
title: <% tp.file.title %>
jd_id: <% tp.user.jd_id() %>
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>
type: project
status: planning
owner: 
due: <% tp.date.now("YYYY-MM-DD", 30) %>
tags: [topic/project, status/planning, action/project]
---

# <% tp.file.title %> 项目

## 项目概述

简要描述本项目的目标、背景和重要性。

## 目标与交付物

- 主要目标：
- 具体交付物：
  - [ ] 交付物1
  - [ ] 交付物2

## 任务分解

- [ ] 任务1
  - [ ] 子任务1.1
  - [ ] 子任务1.2
- [ ] 任务2
  - [ ] 子任务2.1

## 时间线

- 开始日期：<% tp.date.now("YYYY-MM-DD") %>
- 计划完成：<% tp.date.now("YYYY-MM-DD", 30) %>
- 里程碑：
  - 里程碑1：<% tp.date.now("YYYY-MM-DD", 10) %>
  - 里程碑2：<% tp.date.now("YYYY-MM-DD", 20) %>

## 相关资源

- [[相关技术笔记]]
- [[参考资料]]
- [ ] 将此项目链接到相关MOC文件中

## 项目日志

### <% tp.date.now("YYYY-MM-DD") %> - 项目启动

- 初始规划
- 设定目标 

<% /* 
自动更新时间脚本
此行代码确保每次保存文件时，元数据中的updated字段会更新为当前时间
请确保已正确配置Templater插件，并在99-system/scripts/目录下有update_field.js文件
如果要启用此功能，请取消下面行的注释：
*/ %>
<%* /* this.app.plugins.plugins["templater-obsidian"].templater.current_functions_object.user.update_field() */ %> 