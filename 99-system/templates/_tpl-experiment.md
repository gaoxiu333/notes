---
title: <% tp.file.title %>
jd_id: <% this.app.plugins.plugins["templater-obsidian"].templater.current_functions_object.user.jd_id() %>
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>
type: experiment
status: active
schema: v1
tags: [行动/实验]
tech_stack: []  # 相关技术栈标签
experiment_id: EXP-<% tp.date.now("YYYYMMDD") %>-<% Math.floor(Math.random() * 1000).toString().padStart(3, '0') %>
success_criteria: []  # 实验成功的评判标准
---

# <% tp.file.title %> 实验记录

## 🔬 实验概述

**实验目的**：

**假设**：

**预期结果**：

**相关技术栈**：<% tp.frontmatter.tech_stack.join(', ') %>

## 📋 实验设计

### 实验环境

**硬件环境**：
- 处理器：
- 内存：
- 存储：
- 其他硬件：

**软件环境**：
- 操作系统：
- 编程语言版本：
- 框架/库版本：
- 其他依赖：

### 实验参数

| 参数名 | 数据类型 | 默认值 | 可选值范围 | 描述 |
|-------|---------|-------|------------|------|
| 参数1 | | | | |
| 参数2 | | | | |
| 参数3 | | | | |

### 控制变量

| 变量 | 控制方法 | 说明 |
|------|---------|------|
| 变量1 | | |
| 变量2 | | |

### 实验步骤

1. 
2. 
3. 

### 测量指标

| 指标名称 | 单位 | 测量方法 | 阈值/期望值 |
|---------|------|---------|------------|
| 指标1 | | | |
| 指标2 | | | |

## 📊 实验数据

### 原始数据

```
# 实验产生的原始数据
```

### 数据分析

```
# 数据分析代码或结果
```

### 可视化结果

<!-- 插入数据可视化图表或结果 -->

## 🧪 实验过程记录

### 实验 1

**参数配置**：
- 参数1 = 值1
- 参数2 = 值2

**执行时间**：<% tp.date.now("YYYY-MM-DD HH:mm") %>

**观察结果**：

**问题与调整**：

### 实验 2

**参数配置**：
- 参数1 = 值1
- 参数2 = 值2

**执行时间**：

**观察结果**：

**问题与调整**：

## 📝 结果分析

### 结果摘要

<!-- 总结实验结果 -->

### 假设验证

| 假设 | 验证结果 | 说明 |
|------|---------|------|
| 假设1 | 已验证/未验证/部分验证 | |
| 假设2 | 已验证/未验证/部分验证 | |

### 指标达成情况

| 指标 | 目标值 | 实际值 | 达成率 | 状态 |
|------|-------|-------|--------|------|
| 指标1 | | | | 达成/未达成 |
| 指标2 | | | | 达成/未达成 |

### 异常分析

<!-- 记录实验中遇到的异常情况及处理方法 -->

## 💡 结论与建议

### 主要发现

1. 
2. 
3. 

### 技术可行性评估

<!-- 评估该技术方案的可行性 -->

### 性能/质量评估

<!-- 评估性能或质量方面的发现 -->

### 改进建议

1. 
2. 
3. 

## 📚 相关资源

### 代码仓库

<!-- 相关代码仓库链接 -->

### 参考文献

<!-- 实验参考的论文、文档或资源 -->

### 相关实验

<!-- 与本实验相关的其他实验 -->
- [[相关实验1]]
- [[相关实验2]]

## 📅 后续行动

- [ ] 行动项1
- [ ] 行动项2
- [ ] 行动项3

## 🔄 更新记录

- <% tp.date.now("YYYY-MM-DD") %> - 创建实验记录

<%* tp.meta.set("updated", tp.date.now("YYYY-MM-DD HH:mm")) %> 