---
title: Claude学习笔记
jd_id: J20.02.0001
created: 2025-05-11 11:42
updated: 2025-05-11 13:01
type: note
status: active
tags: [topic/ai/tools, topic/ai/claude]
---

# Claude学习笔记

教程合集：https://support.anthropic.com/zh-CN/

## 桌面客户端

参考：https://support.anthropic.com/en/articles/10181068-configuring-and-using-styles

- use style 可以随时切换
- 预设 style：
    - 正常（Normal）：Claude 的默认回答风格
    - 简洁（Concise）：更短和更直接的回答
    - 正式（Formal）：清晰和精致的回答
    - 解释性（Explanatory）：适合学习新概念的教育性回答

## MCP

参考：https://support.anthropic.com/en/articles/10949351-getting-started-with-model-context-protocol-mcp-on-claude-for-desktop

使用AI构建MCP：https://modelcontextprotocol.io/tutorials/building-mcp-with-llms

MCP 合集文章：https://dev.to/fallon_jimmy/top-12-game-changing-mcp-libraries-transform-your-ai-development-in-2025-iep

## **Artifacts**

确保账户设置已经开启：[Profile Settings](https://claude.ai/settings/profile)

**Claude 何时使用 Artifacts？**

- 它很重要且自包含，通常超过 15 行内容
- 您可能希望在对话之外对其进行编辑、迭代或重用
- 它表示一个独立的复杂内容，不需要额外的对话上下文
- 这是您可能想要回顾或稍后使用的内容

它通常是文档/HTML网页

## 记录

安装期间由于 zod 报错，通过使用 `npx clear-npx-cache` 清除npx缓存解决。 