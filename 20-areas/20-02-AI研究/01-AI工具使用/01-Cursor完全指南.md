---
title: Cursor完全指南
jd_id: J20-20250511-1220
created: 2025-05-11 12:20
updated: 2025-05-11 12:20
type: resource
status: active
tags: [topic/ai/tools, topic/ai/coding-assistant, topic/ai/prompt-engineering, lang/chinese]
---

# Cursor完全指南

## 基本概念

[Cursor](https://docs.cursor.com/welcome) 是一款强大的AI编码助手，基于大语言模型，提供代码生成、重构、解释等功能。本指南集合了Cursor的使用方法、常用提示词和最佳实践。

## 配置与设置

### 基础配置
- [VS Code 迁移](https://docs.cursor.com/guides/migration/vscode)
- [如何从命令行打开 cursor](https://docs.cursor.com/troubleshooting/common-issues#how-do-i-open-cursor-from-the-command-line)
- **Include project structure**
  - 包含简化的目录树，以便模型了解你的代码库布局
  - 开启

### 代码索引
- [index your code](https://docs.cursor.com/context/codebase-indexing)
- 大型 monorepo 项目优化：[使用大型 monorepos](https://docs.cursor.com/context/codebase-indexing#working-with-large-monorepos)

## Rules for AI

**参考文档**：[Rules for AI](https://docs.cursor.com/context/rules-for-ai?ref=ghuntley.com#project-rules-recommended)

### 规则概念
- **Project Rules（推荐）** - 使用快捷键：`Cmd + Shift + P` -> `Cursor: Create Rule`
- **Global Rules** - 全局规则，适用于整个项目
- **`.cursorrules`（兼容模式，不建议使用）** - 未来将被删除，建议迁移到 Project Rules

### 规则最佳实践
参考: [最佳实践](https://docs.cursor.com/context/rules#best-practices)
用途：
- 对代码库的特定领域知识进行编码
- 自动化特定于项目的工作流程或模板
- 标准化风格或架构决策

### 第一条规则示例

```markdown
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
</rule>
```

## 常用提示词

### 给自己的项目写规范

```
将规范写入 "specs/" 文件夹，并将每个域主题（包括技术主题）作为单独的 markdown 文件写入。在目录的根目录中创建一个 "SPECS.md"，这是一个概述文档，其中包含一个链接到所有规范的表格。
```

### 检测规则

```
查看 @.cursor 中的 Rust 规则。有哪些规则缺失？哪些不符合最佳实践？
```

### 执行

```
阅读 @SPECS.md 以获取功能规范。
阅读 @.cursor 以了解技术要求。
实现尚未完成的部分。
编写测试。
执行 cargo build，并验证应用程序是否正常运行。
```

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
   > 看起来与 rule 功能有些重合，但rule更加倾向于自动化，NotePads更加强调手动控制，而且规则更加轻量级，限制500行

## 链接与参考

- [[00-MOC-AI工具|返回AI工具索引]]
- [Cursor 官方文档](https://docs.cursor.com)
- [Cursor 生态推荐（rules、prompt、modes）](https://playbooks.com/rules) 