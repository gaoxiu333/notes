---
title: Copilot与VSCode
jd_id: J20-20250511-1220
created: 2025-05-11 12:20
updated: 2025-05-11 12:20
type: resource
status: active
tags: [topic/ai/tools, topic/ai/coding-assistant, topic/editors, lang/chinese]
---

# Copilot与VSCode

## 基本介绍

GitHub Copilot是由GitHub和OpenAI合作开发的AI编码助手，在VSCode中作为扩展使用。本指南介绍Copilot的配置和使用方法，以及如何使用MCP服务增强功能。

## 基本配置

- [Github 中的 Copilot 介绍](https://docs.github.com/en/copilot/quickstart) - Copilot 官方快速入门指南
  - [基本设置](https://github.com/settings/copilot) - 自己账户下的 Copilot 设置
- [VS Code 中的 Copilot](https://code.visualstudio.com/docs/copilot/setup) - 在 VS Code 中设置和使用 Copilot

## MCP 服务

- [Model Context Protocol](https://modelcontextprotocol.io/introduction) - MCP 的基本概念和定义
- [VS Code 添加 MCP](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) - 如何在 VS Code 中配置和使用 MCP 服务器

## 自定义提示词

- [Copilot 自定义](https://code.visualstudio.com/docs/copilot/copilot-customization) - VS Code 中的 Copilot 自定义选项
- [Copilot Chat Cookbook](https://docs.github.com/en/copilot/copilot-chat-cookbook) - GitHub 提供的 Copilot Chat 使用技巧
- [更好的提示词编写指南](https://github.blog/developer-skills/github/how-to-write-better-prompts-for-github-copilot/) - 编写高效提示词的最佳实践

## 调试

- [Copilot 调试指南](https://code.visualstudio.com/docs/copilot/guides/debug-with-copilot) - 使用 Copilot 辅助代码调试

## Vibe Code 工作流

Vibe Code 是一种使用 AI 助手进行编码的工作流，可以在 VSCode+Copilot 或 Cursor 中使用：

### 概念
- AI Code Assistants/Companions
- GenAI Assistants
- MCP: [直观解释 MCP](https://x.com/akshay_pachaar/status/1900170356494917936)

### 工作流程
- `idea` -> `plan` -> `code`

### 资源
- [vibe code 最佳实践](https://www.youtube.com/watch?v=YWwS911iLhg)

### 提示词示例
```
任务说明：
你当前的唯一任务是读取 `idea.md` 文件的内容，并基于其中的项目想法，生成一份名为 `plan.md` 的计划文件。

要求：
1. `plan.md` 应包含逐步的实现指令，每一步应简洁明了，便于执行；
2. 当前阶段禁止进行任何代码生成、文件修改或实现操作；
3. 除非我显式回复"确认计划，开始实现"，否则你不应进行任何超出 plan.md 的行为。

请回复你理解了上述规则，并提交 `plan.md` 的内容。
```

## 设置参考

- [Copilot 设置文档](https://code.visualstudio.com/docs/copilot/reference/copilot-settings) - Copilot 的完整设置选项和参考

## 链接与参考

- [[00-MOC-AI工具|返回AI工具索引]] 