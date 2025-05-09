---
title: "Claude 使用指南"
date: 2024-07-18
tags: 
  - type/reference
  - subject/ai
  - tool/claude
status: active
---

# Claude 使用指南

Claude是Anthropic公司开发的大型语言模型，提供强大的自然语言处理和生成能力。本文档提供Claude命令行工具的基本设置和使用信息。

## 系统要求

- Node.js 18+
- git 2.23+ (可选)
- 用于PR工作流程的GitHub或GitLab CLI（可选）
- ripgrep (rg) 用于增强文件搜索（可选）

### 安装ripgrep

```bash
brew install ripgrep
```

## 安装Claude命令行工具

```bash
npm install -g @anthropic-ai/claude-code
```

## 主要特性

- 强大的代码理解和生成能力
- 遵循安全和道德AI原则
- 上下文窗口较大，能处理长文本和复杂问题

## 相关工具

- [[Technology/AI/Applications/coding-assistants/cursor|Cursor]] - 集成Claude的代码编辑器
- [[Technology/AI/Applications/coding-assistants/vibe-code|Vibe Code]] - AI辅助编程流程 