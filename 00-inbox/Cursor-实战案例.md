---
title: Cursor-实战案例
jd_id: J00-20250512-2345
created: 2025-05-12 23:45
updated: 2025-05-12 23:45
type: note
status: draft
tags: []
---

# Cursor-实战案例

## 草稿

PR 规模：≈120 行（保持在 300 行以内，超大 diff 需分块，否则 LLM 会截断上下文） 
1. 创建 checklist
   1. 在仓库根目录创建 .cursor/rules/frontend-checklist.mdc
```
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
> 为什么要写成 Rule？
> 每次调用 Chat / ⌘K 时，Cursor 都会把以上清单塞进系统提示，确保 AI 自动对照检查，而不必你重复贴


## 内容

正文内容...

## 链接与参考

- [[相关笔记]]
- [[相关概念]]

## 待办事项

- [ ] 代码审查 
- [ ] 

 

