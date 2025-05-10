### 第一条规则

让 Cursor 编写规则的规则

这个规则规定了 Cursor 规则文件(.mdc)必须存放在项目根目录的.cursor/rules/文件夹中，并要求使用 kebab-case 命名格式。

````
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
````
