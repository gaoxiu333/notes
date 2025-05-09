---
title: "Vibe Code 编程流程介绍"
date: 2024-07-18
tags: 
  - type/reference
  - subject/ai
  - tool/coding-assistant
status: active
---

# Vibe Code 编程流程介绍

## 基本工作流程

Vibe Code 是一种基于AI辅助编程的工作方法，遵循以下流程：
- `cursor` -> `idea` -> `plan` -> `code`

这种流程强调在编写代码前先有清晰的想法和计划，然后借助AI助手完成实现。

## 核心概念

- **AI Code Assistants** - 人工智能代码助手
- **AI Code Companions** - 人工智能编程伴侣
- **GenAI Assistants** - 生成式AI助手
- **MCP（Machine Critical Path）** - 机器关键路径，[直观解释 MCP](https://x.com/akshay_pachaar/status/1900170356494917936)

## 学习资源

- [Vibe Code 最佳实践](https://www.youtube.com/watch?v=YWwS911iLhg) - YouTube视频教程

## 提示词模板示例

### Idea to Plan 转换提示词

```
任务说明：
你当前的唯一任务是读取 `idea.md` 文件的内容，并基于其中的项目想法，生成一份名为 `plan.md` 的计划文件。

要求：
1. `plan.md` 应包含逐步的实现指令，每一步应简洁明了，便于执行；
2. 当前阶段禁止进行任何代码生成、文件修改或实现操作；
3. 除非我显式回复"确认计划，开始实现"，否则你不应进行任何超出 plan.md 的行为。

请回复你理解了上述规则，并提交 `plan.md` 的内容。
```

## 相关工具

- [[Technology/AI/Applications/coding-assistants/cursor|Cursor]] - 基于AI的代码编辑器
- [[Technology/AI/Applications/coding-assistants/github-copilot|GitHub Copilot]] - GitHub的AI编程助手
- [[Technology/AI/LLM/claude|Claude]] - Anthropic的大型语言模型 