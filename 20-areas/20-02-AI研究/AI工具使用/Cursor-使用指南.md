---
title: Cursor 使用指南
created: 2024-07-31
updated: 2024-07-31
type: resource
status: active
schema: v1
tags:
  - topic/ai/tools
  - topic/ai/coding-assistant
  - action/review
  - lang/chinese
---

# Cursor 使用指南

---

## 参考

- [Cursor 使用指南](https://docs.cursor.com/welcome)
- [Cursor 生态推荐（rules、prompt、modes）](https://playbooks.com/rules)

## Context（上下文）

- [index your code](https://docs.cursor.com/context/codebase-indexing)

## MCP

待补充

## 配置

我的 cursor 设置

- [VS Code 迁移](https://docs.cursor.com/guides/migration/vscode)
- [如何从命令行打开 cursor](https://docs.cursor.com/troubleshooting/common-issues#how-do-i-open-cursor-from-the-command-line)
- **Include project structure**
  - 包含简化的目录树，以便模型了解你的代码库布局
  - 开启

## Rules for AI

参考: [最佳实践](https://docs.cursor.com/context/rules#best-practices)
用途：

- 对代码库的特定领域知识进行编码
- 自动化特定于项目的工作流程或模板
- 标准化风格或架构决策

### 规则概念

- **Project Rules（推荐）** - 使用快捷键：`Cmd + Shift + P` -> `Cursor: Create Rule`
- **Global Rules** - 全局规则，适用于整个项目
- **`.cursorrules`（兼容模式，不建议使用）** - 未来将被删除，建议迁移到 Project Rules

## 进阶使用

### 自定义模式

参考：[创建自定义模式](https://docs.cursor.com/chat/custom-modes#creating-a-custom-mode)
用途：

1. 学习：专注于彻底解释概念，并在提供解决方案之前提出澄清问题
2. 重构：只专注于改进现有代码结构，不添加新功能
3. 计划：创建详细的实施计划，无需直接更改代码。将其写入`plan.md`
4. 研究：在提出解决方案之前，从多个来源收集全面的信息
5. 调试：在提出有针对性的解决方案之前，通过收集广泛的背景信息来彻底调查问题

### NotePads

参考：[示例笔记本](https://docs.cursor.com/beta/notepads#example-notepad)
用途：

1. 项目架构决策
2. 开发指南和标准
3. 参考文档
   > 看起来与 rule 功能有些重合，但我觉得 rule 更加倾向于自动化，NotePads 更加强调手动控制，而且规则更加轻量级，限制 500 行

## 常见问题

1. 大型 monorepo 项目如何优化代码索引（Codebase Indexing）?
   参考官方：[使用大型 monorepos](https://docs.cursor.com/context/codebase-indexing#working-with-large-monorepos)
