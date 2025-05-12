---
title: 未命名
jd_id: J00-20250512-1056
created: 2025-05-12 10:56
updated: 2025-05-12 10:56
type: note
status: draft
tags: []
---

# 未命名

## 概述

Cursor 的发展呈现三大趋势：

1. AI 能力深度集成 IDE
2. 算法创新驱动计算效率提升
3. 定制化工作流日益重要

建议开发者重点关注：

- MCP 优化框架应用
- 上下文管理体系构建
- AI 模型依赖的版本管控

## 内容

## 高级开发技巧

## 代理模式编排

高效模式包括：

- **YOLO 模式**：预设允许列表（如 `allow: [tsc, vitest, mkdir]`）自动测试修复循环
- **影子工作区**：实验性重构的隔离环境，避免影响生产代码
- **提示链**：`生成→测试→重构` 等任务通过状态保持的代理线程顺序执行

### 最佳实践

    3.	工作流打磨：
    •	跟着 Dev.to & Reddit 帖子把 .cursorrules、Composer、Notepads 串起来，练习“测试先行写代码 → Agent Review”。

#### 项目规则系统

使用 `.mdc` 规则文件：

1. 在项目根目录创建 `.cursor/rules/` 文件夹存放 `.mdc` 规则文件
2. 将旧的 `.cursorrules` 文件迁移到新的 `.mdc` 格式
3. 规则文件可以包含项目特定的代码标准、命名约定等

**规则文件结构示例：**

```text
.cursor/rules/
├── style/
│   ├── formatting.mdc
│   └── naming.mdc
├── testing/
│   ├── unit-tests.mdc
│   └── integration-tests.mdc
└── documentation/
    └── comments.mdc
```

**编写有效规则的要点：**

- 保持规则简洁（建议少于 500 行）
- 使用具体名称和描述
- 使用 `@filename.ts` 引用相关文件
- 重用规则块而非重复提示

### 提高生产力的技巧

#### 上下文管理

- 使用 `.cursorignore` 排除不必要的文件索引
- 利用 "Reference Open Editors" 命令一次添加多个打开的文件到上下文
- 使用 Notepads 功能记录项目相关信息，可在聊天中引用

#### 大型项目工作流

- 建立生成/测试/运行测试的循环，让 AI 自我纠正
- 创建项目计划并让 AI 检查和改进
- 为 AI 创建专用文档文件夹，类似培训工程团队

#### 高效提示技巧

- 编写具体且可操作的提示，避免模糊指令
- 首先询问 Cursor 确认任务理解
- 使用 `@Commit`（工作状态差异）查看未提交的更改

## 额外工具与资源

**官方资源：**

- [Cursor 官方网站](https://cursor.com/features)
- [Cursor 社区论坛](https://forum.cursor.com)

**社区资源：**

- [cursor.directory](https://cursor.directory)：提供样例用法和模板
- [GitHub - digitalchild/cursor-best-practices](https://github.com/digitalchild/cursor-best-practices)
- [GitHub - sanjeed5/awesome-cursor-rules-mdc](https://github.com/sanjeed5/awesome-cursor-rules-mdc)

## 链接与参考

适用于 Cursor Rule 的参考

- [dotcursorrules](https://dotcursorrules.com/)
- [CursorFocus](https://github.com/RenjiYuusei/CursorFocus)

## 待办事项

- [ ] 相关任务
- [ ] 将此笔记链接到相关 MOC 文件中
