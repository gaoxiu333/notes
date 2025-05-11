---
title: Inbox迁移计划
jd_id: J10-20250511-1257
created: 2025-05-11 12:57
updated: 2025-05-11 12:57
type: project
status: active
tags: [topic/pkm, action/project, topic/organization]
---

# Inbox清空迁移计划

## 1. 概述

本计划旨在清理和重组`00-inbox`目录中的文件，将它们迁移到PKM系统中更合适的位置，以保持知识库的有序性和可访问性。

## 2. 文件迁移清单

### 2.1 知识类文件

| 文件名 | 目标位置 | 元数据更新 | 标签更新 |
|--------|----------|------------|----------|
| cladude 学习笔记.md | 20-areas/20-02-AI研究/01-AI工具使用/ | jd_id: J20.02.0001<br>updated: 当前时间 | topic/ai/tools |
| nestjs.md | 20-areas/20-04-Nodejs/核心概念/ | jd_id: J20.04.0001<br>updated: 当前时间 | topic/backend/nestjs, topic/nodejs |
| web 性能优化.md | 20-areas/20-03-前端开发/ | jd_id: J20.03.0001<br>updated: 当前时间 | topic/frontend/performance |
| js 手写算法要点.md | 30-resources/30-01-前端技术/02-React/核心原理/ | jd_id: J30.01.0001<br>updated: 当前时间 | topic/frontend/javascript, topic/algorithms |
| 函数式编程.md | 30-resources/30-01-前端技术/ | jd_id: J30.01.0002<br>updated: 当前时间 | topic/frontend/javascript, topic/programming/functional |
| MAC-使用备忘录.md | 30-resources/30-05-工具指南/开发工具/ | jd_id: J30.05.0001<br>updated: 当前时间 | topic/tools/mac |
| 设计软件-figma.md | 30-resources/30-05-工具指南/开发工具/ | jd_id: J30.05.0002<br>updated: 当前时间 | topic/tools/design, topic/tools/figma |
| 知识库的内容填充.md | 10-projects/10-00-PKM/ | jd_id: J10.00.0001<br>updated: 当前时间 | topic/pkm |
| javascript-todo.md | 20-areas/20-03-前端开发/ | jd_id: J20.03.0002<br>updated: 当前时间 | topic/frontend/javascript, action/todo |
| LINK.md | 99-system/MOCs/ | jd_id: J99.00.0001<br>updated: 当前时间<br>type: moc | topic/pkm/moc |

### 2.2 code-snippets 目录

| 源位置 | 目标位置 | 处理方式 |
|--------|----------|----------|
| 00-inbox/code-snippets/ | 30-resources/code-snippets/ | 整体迁移，保持内部结构不变 |

### 2.3 待办事项

| 文件名 | 处理方式 |
|--------|----------|
| 00-待办事项.md | 内容整合到10-projects相应项目，并更新相关MOC文件 |

## 3. 迁移步骤

### 3.1 准备工作

1. 备份整个`00-inbox`目录
2. 确认目标目录存在，如不存在则创建

### 3.2 文件迁移

对每个文件执行以下操作：

1. 更新元数据：
   - 保留原始`created`时间
   - 更新`updated`时间为当前时间
   - 更新`jd_id`按照目标位置的分类规则
   - 设置合适的`type`和`status`
   - 添加或更新`tags`

2. 移动文件到目标位置

3. 在相关MOC文件中添加链接：
   - 查找目标目录中的MOC文件
   - 如不存在，创建新的MOC文件
   - 添加新迁移文件的链接

### 3.3 code-snippets 处理

1. 复制整个目录结构到`30-resources/code-snippets/`
2. 更新`MOC-代码片段.md`的元数据和位置

### 3.4 待办整合

1. 分析`00-待办事项.md`中的内容
2. 将待办事项分配到相应的项目文件中
3. 更新项目的MOC文件

## 4. MOC更新

### 4.1 更新主题MOC

确保每个迁移的文件在对应的主题MOC中有链接：

- 在`20-areas/20-02-AI研究/01-AI工具使用/`中找到或创建MOC
- 在`20-areas/20-04-Nodejs/核心概念/`中找到或创建MOC
- 依此类推...

### 4.2 更新全局MOC

1. 更新`99-system/MOCs/MOC-dashboard.md`，确保所有主题MOC都被链接
2. 使用`LINK.md`的内容扩充全局链接结构

## 5. 验证与清理

### 5.1 迁移验证

1. 检查所有文件是否成功迁移
2. 验证链接是否正常工作
3. 确认元数据是否正确更新

### 5.2 最终清理

1. 确认所有内容已正确迁移后，清空`00-inbox`目录
2. 保留`00-inbox/README.md`文件，说明inbox的用途和处理流程

## 6. 后续行动

1. 建立定期清理inbox的流程（建议每周一次）
2. 设置提醒以防止inbox积累过多未处理内容
3. 考虑使用自动化脚本辅助inbox内容迁移

## 注意：
迁移过程中注意内容查重，避免知识库重复臃肿