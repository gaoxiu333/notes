# Cursor 使用指南

---

## Rules for AI

**参考文档**：[Rules for AI](https://docs.cursor.com/context/rules-for-ai?ref=ghuntley.com#project-rules-recommended)

### 规则概念

- **Project Rules（推荐）** - 使用快捷键：`Cmd + Shift + P` -> `Cursor: Create Rule`
- **Global Rules** - 全局规则，适用于整个项目
- **`.cursorrules`（兼容模式，不建议使用）** - 未来将被删除，建议迁移到 Project Rules

第一条规则：让 Cursor 编写规则

````
---
description: Cursor Rules Location
globs: *.mdc
---
# Cursor Rules Location

Rules for placing and organizing Cursor rule files in the repository.

<rule>
name: cursor_rules_location
description: Standards for placing Cursor rule files in the correct directory
filters:
  # Match any .mdc files
  - type: file_extension
    pattern: "\\.mdc$"
  # Match files that look like Cursor rules
  - type: content
    pattern: "(?s)<rule>.*?</rule>"
  # Match file creation events
  - type: event
    pattern: "file_create"

actions:
  - type: reject
    conditions:
      - pattern: "^(?!\\.\\/\\.cursor\\/rules\\/.*\\.mdc$)"
        message: "Cursor rule files (.mdc) must be placed in the .cursor/rules directory"

  - type: suggest
    message: |
      When creating Cursor rules:

      1. Always place rule files in PROJECT_ROOT/.cursor/rules/:
         ```
         .cursor/rules/
         ├── your-rule-name.mdc
         ├── another-rule.mdc
         └── ...
         ```

      2. Follow the naming convention:
         - Use kebab-case for filenames
         - Always use .mdc extension
         - Make names descriptive of the rule's purpose

      3. Directory structure:
         ```
         PROJECT_ROOT/
         ├── .cursor/
         │   └── rules/
         │       ├── your-rule-name.mdc
         │       └── ...
         └── ...
         ```

      4. Never place rule files:
         - In the project root
         - In subdirectories outside .cursor/rules
         - In any other location

examples:
  - input: |
      # Bad: Rule file in wrong location
      rules/my-rule.mdc
      my-rule.mdc
      .rules/my-rule.mdc

      # Good: Rule file in correct location
      .cursor/rules/my-rule.mdc
    output: "Correctly placed Cursor rule file"

metadata:
  priority: high
  version: 1.0
</rule>
````

## 常用提示词

### 给自己的项目写规范

```
将规范写入 “specs/” 文件夹，并将每个域主题（包括技术主题）作为单独的 markdown 文件写入。在目录的根目录中创建一个 “SPECS.md”，这是一个概述文档，其中包含一个链接到所有规范的表格。
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
