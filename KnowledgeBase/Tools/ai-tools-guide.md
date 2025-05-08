---
title: "AI工具使用指南"
date: 2024-07-15
tags: 
  - type/reference
  - subject/ai/tools
  - subject/knowledge-management
status: complete
---

# AI工具使用指南

## 简介

本文档提供了知识库中AI工具的安装、配置和使用说明。这些工具旨在帮助自动化知识管理流程，提高笔记间的互联性，并帮助提取和组织知识。

## 安装与配置

### 前提条件

- Python 3.8+ 
- OpenAI API密钥
- `requests`库

### 配置步骤

1. 确保已安装Python和必要依赖：

```bash
pip install requests
```

2. 设置OpenAI API密钥：

```bash
# macOS/Linux
export OPENAI_API_KEY='your-api-key'

# Windows
set OPENAI_API_KEY='your-api-key'
```

3. 给脚本添加执行权限（仅Unix/Linux/macOS）：

```bash
chmod +x scripts/ai-assistant.py
```

## 工具说明

### 1. AI助手脚本 (`scripts/ai-assistant.py`)

该脚本提供三个核心功能：

#### 1.1 生成MOC内容摘要

分析MOC文档，生成结构化摘要，帮助理解知识领域。

```bash
python scripts/ai-assistant.py summarize-moc [MOC文件路径]
```

示例：
```bash
python scripts/ai-assistant.py summarize-moc KnowledgeBase/MOCs/ai-moc.md
```

输出包括：领域概述、核心概念、结构分析、完整度评估和改进建议。

#### 1.2 分析笔记关联性

分析目标笔记与库中其他笔记的关联，提出链接建议。

```bash
python scripts/ai-assistant.py find-connections [笔记文件路径]
```

示例：
```bash
python scripts/ai-assistant.py find-connections Technology/AI/LLM/llm-recommendations.md
```

输出JSON格式的关联建议，包括：关联笔记路径、关联强度、关联类型、建议链接文本等。

#### 1.3 提取关键概念

从长文档中提取核心概念和术语。

```bash
python scripts/ai-assistant.py extract-concepts [文档文件路径]
```

示例：
```bash
python scripts/ai-assistant.py extract-concepts Resources/Books/book-summary.md
```

输出JSON格式的概念列表，包括：概念名称、描述、重要性评分、相关概念等。

## 提示词模板

系统提供了三个标准化提示词模板，存放在`KnowledgeBase/Tools/prompts/`目录：

1. **concept-extractor.prompt**：从文章提取关键概念的提示词
2. **connection-finder.prompt**：发现笔记间隐含关联的提示词
3. **summary-generator.prompt**：生成内容摘要的提示词

这些模板可以根据需要进行自定义，以适应特定的知识管理需求。

## 最佳实践

### 摘要生成

- 优先对主要MOC文档生成摘要，帮助快速理解领域
- 摘要可以作为MOC文档的简介部分
- 定期对更新的MOC重新生成摘要

### 关联发现

- 对新创建的重要笔记运行关联分析
- 对孤立笔记（无外部链接）进行关联分析
- 根据分析结果添加双向链接，加强知识网络

### 概念提取

- 对长篇文献笔记提取关键概念
- 根据提取的概念创建独立的概念笔记
- 使用提取的概念丰富MOC文档

## 故障排除

1. **API密钥问题**：确保环境变量正确设置
2. **解析错误**：检查提示词模板格式
3. **模型限制**：对于非常长的文档，考虑分段处理

## 进阶用法

### 自定义提示词

可以创建自定义提示词模板，添加到`KnowledgeBase/Tools/prompts/`目录，并修改脚本以支持新的功能。

### 批处理

可以创建批处理脚本，对多个文件进行批量处理：

```bash
#!/bin/bash
for file in KnowledgeBase/MOCs/*.md; do
  python scripts/ai-assistant.py summarize-moc "$file" > "${file%.md}-summary.md"
done
```

## 未来规划

- 集成到Obsidian工作流
- 添加基于嵌入的语义搜索功能
- 开发自动MOC生成工具 