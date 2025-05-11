# 📚 PKM 规范

> 写笔记永远比维护规范更轻松。

## I. 目录结构

| 序号               | 文件夹             | 用途  |
| ---------------- | --------------- | --- |
| **00‑inbox**     | 收集箱 | 新捕获内容暂存处 |
| **10‑projects**  | 项目 | 有明确交付物或截止日期 |
| **20‑areas**     | 领域 | 持续关注的职责范围 |
| **30‑resources** | 资源 | 可复用参考资料与模板 |
| **90‑archive**   | 归档 | 已完结内容（按年分类） |
| **99‑system**    | 系统 | 模板、脚本、样式、MOC |

**命名规则**：
- 文件夹：`XX-job-domain` 格式
- 文件：`XX-中文名.md` 格式
- MOC文件：`00-MOC-主题.md` 格式
- 嵌套层级：最多2层（顶层→子文件夹→文件）

## II. 元数据标准

```yaml
---
title: 文档标题
jd_id: J10-YYYYMMDD-HHMM
created: YYYY-MM-DD HH:MM # 使用MCP工具获取时间
updated: YYYY-MM-DD HH:MM # 使用MCP工具获取时间
type: note                # moc/guide/note
status: draft             # draft/active/archived
tags: []                  # 主题检索标签
---
```

## III. 标签系统

- 命名空间：仅4个 - `topic/`, `status/`, `action/`, `lang/`
- 格式：全小写kebab-case，使用`/`建立层级，如`#topic/ai`
- 维护：月度合并同义词，删除低频（<3次）标签

## IV. 工作流

| 阶段 | 动作 | 工具 | 频率 |
| --- | --- | --- | --- |
| 收集 | 写入`00-inbox` | QuickAdd | 随时 |
| 处理 | 分类添加元数据 | Templater | 每日 |
| 组织 | 更新链接与标签 | Backlinks/Dataview | 每周 |
| 回顾 | 清理孤岛笔记 | Dataview查询 | 每月 |
| 表达 | 输出与复盘 | MOC引用 | 按需 |

## V. 知识内化

知识转化流程：
- 数据→信息：剪藏整理
- 信息→知识：实用记录
- 知识→智慧：复盘应用

## VI. 导航系统

| 类型 | 位置 | 功能 |
| --- | --- | --- |
| 主题MOC | 主题同目录 | 本地索引与上下文 |
| 全局MOC | `99-system/MOC-dashboard.md` | 系统总览与仪表盘 |

每周检查未被全局MOC引用的`MOC-*`文件并补充链接。

## VII. 系统指标

| 指标 | 目标值 | 查询方法 |
| --- | --- | --- |
| 孤岛笔记 | ≤5% | `where outgoing = 0` |
| 过期项目 | 0 | `where status = "active" and updated <= date(today) - dur(30 days)` |

## VIII. 核心模板

| 模板 | 用途 | 特点 |
| --- | --- | --- |
| `_tpl-note` | 标准笔记 | 基础元数据 |
| `_tpl-tech-cheatsheet` | 技术速查 | 最小信息块 |

QuickAdd快捷命令：`qa-note`, `qa-cheat`

## IX. 自动化

- **jd_id**：自动生成文档编号
- **update_field**：自动更新修改时间
- **命名校验**：Git pre-commit或Obsidian Linter

## ✅ 快速实施步骤

1. 创建6+1顶级文件夹，模板置于`99-system`
2. 使用`_tpl-note`创建10条笔记，实践完整工作流
3. 每周检查孤岛笔记比例，超5%进行链接或清理