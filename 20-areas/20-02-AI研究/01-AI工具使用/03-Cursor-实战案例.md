---
title: Cursor-实战案例
jd_id: J20-20250513-0748
created: 2025-05-12 23:45
updated: 2025-05-13 07:48
type: note
status: draft
tags: [topic/ai, topic/ide]
---

# Cursor-实战案例

> 本文档记录了在 Cursor 中落地规则、代码审查与规范管理的实战经验，便于后续复用与知识沉淀。

## 1. 代码审查实践

- PR 规模建议：单次 diff 保持在 300 行以内，超大 diff 需分块，否则 LLM 容易截断上下文。
- 审查 checklist 建议：
  - 在仓库根目录创建 `.cursor/rules/frontend-checklist.mdc`，内容如下：

```markdown
---
description: Front‑end code review checklist
globs: ["frontend/**/*.tsx", "frontend/**/*.ts"]
alwaysApply: true
---

- All fetch calls **must** throw on non‑2xx.
- No `any` types; prefer `unknown` + narrowing.
- Wrap inline lambdas in `useCallback` / `useMemo`.
- New component ⇒ add `*.test.tsx` with RTL.
```

- **为何写成 Rule？**
  - 每次调用 Chat / ⌘K 时，Cursor 会自动加载清单，确保 AI 按 checklist 检查，无需重复粘贴。

## 2. 规范与参考

- 规范建议写入 `specs/` 文件夹，每个主题单独 markdown 文件，根目录建 `SPECS.md` 作为总览并链接所有规范。
- 检查规则建议：查看 `.cursor` 目录下的规则文件，识别缺失或不符合最佳实践的部分。

## 3. 提示词参考

- 写代码：

  > 将规范写入 "specs/" 文件夹，并将每个域主题（包括技术主题）作为单独的 markdown 文件写入。在目录的根目录中创建一个 "SPECS.md"，这是一个概述文档，其中包含一个链接到所有规范的表格。

- 检查 rule：
  > 查看 @.cursor 中的 Rust 规则。有哪些规则缺失？哪些不符合最佳实践？

## 4. 链接与参考

- [[相关笔记]] <!-- TODO: 补充具体笔记链接 -->
- [[相关概念]] <!-- TODO: 补充具体概念链接 -->
