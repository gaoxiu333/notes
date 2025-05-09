---
title: "Cursor 使用指南"
date: 2024-07-18
tags: 
  - type/guide
  - subject/ai
  - tool/cursor
status: active
---

# Cursor 使用指南

Cursor是一款基于AI技术的代码编辑器，提供强大的智能编码辅助功能。本文档提供了Cursor的使用方法、配置技巧和最佳实践。

## 官方参考资源

- [Cursor 官方使用指南](https://docs.cursor.com/welcome)

## 核心功能

### 上下文管理

- [代码库索引](https://docs.cursor.com/context/codebase-indexing) - 让AI了解你的项目结构和代码库

### MCP (Machine Critical Path)

机器关键路径是Cursor的重要功能，可以让AI更有效地理解和处理代码。

*待补充具体用法*

## 配置建议

我的Cursor常用设置：

- [从VS Code迁移](https://docs.cursor.com/guides/migration/vscode) - 如何从VS Code迁移到Cursor
- [命令行打开Cursor](https://docs.cursor.com/troubleshooting/common-issues#how-do-i-open-cursor-from-the-command-line) - 设置命令行快捷方式
- **Include project structure** - 开启此选项让模型了解代码库布局

## Rules for AI

Cursor允许你定义规则来指导AI行为，提高生成代码的质量和一致性。

**参考文档**：[Rules for AI](https://docs.cursor.com/context/rules-for-ai)

### 规则类型

- **Project Rules（推荐）** - 使用快捷键：`Cmd + Shift + P` -> `Cursor: Create Rule`
- **Global Rules** - 全局规则，适用于所有项目
- **`.cursorrules`（兼容模式，不建议使用）** - 未来将被删除，建议迁移到Project Rules

### 规则示例：Cursor规则位置管理

下面是一个规则示例，规定了Cursor规则文件的存放位置和命名格式：

```
---
description: Cursor 规则位置
globs: \*.mdc
---

# Cursor 规则位置

关于在仓库中放置和组织 Cursor 规则文件的规则。

<rule>
name: cursor_rules_location
description: 将 Cursor 规则文件放置在正确目录的标准
filters:
  # 匹配任何 .mdc 文件
  - type: file_extension
    pattern: "\\.mdc$"
  # 匹配看起来像 Cursor 规则的文件
  - type: content
    pattern: "(?s)<rule>.*?</rule>"
  # 匹配文件创建事件
  - type: event
    pattern: "file_create"

actions:

- type: reject
  conditions:

  - pattern: "^(?!\\.\\/\\.cursor\\/rules\\/.\*\\.mdc$)"
    message: "Cursor 规则文件 (.mdc) 必须放置在 .cursor/rules 目录中"

- type: suggest
  message: |
  创建 Cursor 规则时：

  1. 始终将规则文件放在 PROJECT_ROOT/.cursor/rules/ 中：

     ```
     .cursor/rules/
     ├── your-rule-name.mdc
     ├── another-rule.mdc
     └── ...
     ```

  2. 遵循命名约定：

     - 使用 kebab-case 格式命名文件
     - 始终使用 .mdc 扩展名
     - 文件名应描述规则的用途

  3. 目录结构：

     ```
     PROJECT_ROOT/
     ├── .cursor/
     │   └── rules/
     │       ├── your-rule-name.mdc
     │       └── ...
     └── ...
     ```

  4. 切勿将规则文件放在：
     - 项目根目录
     - .cursor/rules 之外的子目录
     - 任何其他位置

examples:

- input: |

  # 错误：规则文件位置不正确

  rules/my-rule.mdc
  my-rule.mdc
  .rules/my-rule.mdc

  # 正确：规则文件位置正确

  .cursor/rules/my-rule.mdc
  output: "正确放置的 Cursor 规则文件"

metadata:
priority: high
version: 1.0
</rule>
```

## 实用提示词

### 项目规范编写

```
将规范写入 "specs/" 文件夹，并将每个域主题（包括技术主题）作为单独的 markdown 文件写入。在目录的根目录中创建一个 "SPECS.md"，这是一个概述文档，其中包含一个链接到所有规范的表格。
```

### 规则检测

```
查看 @.cursor 中的 Rust 规则。有哪些规则缺失？哪些不符合最佳实践？
```

### 项目执行助手

```
阅读 @SPECS.md 以获取功能规范。
阅读 @.cursor 以了解技术要求。
实现尚未完成的部分。
编写测试。
执行 cargo build，并验证应用程序是否正常运行。
```

## 进阶功能

### 自定义模式

参考：[创建自定义模式](https://docs.cursor.com/chat/custom-modes#creating-a-custom-mode)

常用自定义模式：

1. **学习模式** - 专注于彻底解释概念，并在提供解决方案之前提出澄清问题
2. **重构模式** - 只专注于改进现有代码结构，不添加新功能
3. **计划模式** - 创建详细的实施计划，将其写入`plan.md`而不直接更改代码
4. **研究模式** - 从多个来源收集信息，在提出解决方案前进行全面研究
5. **调试模式** - 通过收集广泛的背景信息来彻底调查问题，提出有针对性的解决方案

### NotePads笔记功能

参考：[示例笔记本](https://docs.cursor.com/beta/notepads#example-notepad)

适用场景：
1. 项目架构决策记录
2. 开发指南和标准文档
3. 参考资料收集

> 注：NotePads与rules功能有一定重合，但rules更倾向于自动化和约束，NotePads更强调手动记录和灵活性。

## 常见问题解答

1. **如何优化大型monorepo项目的代码索引？**
   参考官方文档：[使用大型monorepos](https://docs.cursor.com/context/codebase-indexing#working-with-large-monorepos)

## 相关工具

- [[Technology/AI/Applications/coding-assistants/vibe-code|Vibe Code]] - AI辅助编程流程
- [[Technology/AI/Applications/coding-assistants/github-copilot|GitHub Copilot]] - GitHub的AI编程助手 