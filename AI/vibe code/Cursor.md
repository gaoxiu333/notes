# Cursor 使用指南

---

## Context（上下文）

- [index your code](https://docs.cursor.com/context/codebase-indexing)
- @-symbols
  - **常用：**
    - @Files/@Folders/@code - 定位代码作为引用
    - @web/@Docs - 外部文档
    - @rules - 使用规则
    - @Definitions - 定义
    - @Lint errors - 检查错误
  - **高级：**
    - @Recent Changes - 最近修改的代码作为引用

## MCP

待补充

## 配置

- [VS Code 迁移](https://docs.cursor.com/guides/migration/vscode)

## Rules for AI

**作用**：让 Cursor 按照你的规则来工作

**参考文档**：[Rules for AI](https://docs.cursor.com/context/rules-for-ai?ref=ghuntley.com#project-rules-recommended)

### 规则概念

- **Project Rules（推荐）** - 使用快捷键：`Cmd + Shift + P` -> `Cursor: Create Rule`
- **Global Rules** - 全局规则，适用于整个项目
- **`.cursorrules`（兼容模式，不建议使用）** - 未来将被删除，建议迁移到 Project Rules

### 第一条规则

让 Cursor 编写规则的规则

这个规则规定了 Cursor 规则文件(.mdc)必须存放在项目根目录的.cursor/rules/文件夹中，并要求使用 kebab-case 命名格式。

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
