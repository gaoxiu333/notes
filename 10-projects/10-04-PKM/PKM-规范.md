# 📚 PKM 规范

> 宗旨：写笔记永远比维护规范更轻松。

---

## I. 目录结构

*理论：信息架构 5±2 原则——顶层分类越少越易检索*

| 序号               | 文件夹             | 说明  |
| ---------------- | --------------- | --- |
| **00‑inbox**     | 收集箱，任何新捕获内容先落此处 |     |
| **10‑projects**  | 有交付物或截止日期的事务    |     |
| **20‑areas**     | 持续关注/职责域        |     |
| **30‑resources** | 可复用参考资料、模板、最佳实践 |     |
| **90‑archive**   | 已完结或弃置内容，按年份归档  |     |
| **99‑system**    | 模板、脚本、样式、全局 MOC |     |

**Johnny‑Decimal**：只在文件夹使用 `XX‑job‑domain`；文件名直接中文即可

---

## II. 元数据层

*理论：外部化元记忆减轻认知负荷*

### 1. 标准 YAML 模板

```yaml
---
title: 规范
jd_id: J11-20250511-0050
created: 2025-05-11 00:50 # AI 创建时，使用MCP获取时间
updated: 2025-05-11 00:50 # AI 创建时，使用MCP获取时间
type: note            # moc / guide / note ...
status: draft         # draft / active / archived
tags: [] # 主题检索（见标签系统）
---


## III. 标签系统

*理论：语义网络提高搜索"香气"*

- **顶级命名空间 = 4**：`topic/`, `status/`, `action/`, `lang/`
- 全小写 kebab‑case，使用 `/` 建层级：`#topic/ai`, `#action/todo`
- 每月用 Tag Wrangler 合并同义词；使用频次 < 3 的标签考虑删除。

---

## IV. 工作流

*理论：GTD Capture → Review 强调闭环*

| 阶段 | 动作 | 工具 | 节奏 |
| --- | --- | --- | --- |
| Capture | 快键写入 `00‑inbox` | QuickAdd | 随时 |
| Process | 分类补元数据 | Templater | 每日 |
| Organize | 链接、标签、MOC 更新 | Backlinks、Dataview | 每周 |
| Review | 清理孤岛、更新项目 | Dataview Query | 每月 |
| Express | 输出博客/复盘 | MOC 引用 | 需求驱动 |

---

## V. 知识内化

*理论：DIKW & SECI 循环*

- `Data → Information`：剪藏→整理
- `Information → Knowledge`：写用法
- `Knowledge → Wisdom`：复盘发布

SECI：社会化记录→外化成笔记→组合重组→内化运用。

---

## VI. 导航 & MOC

*理论：空间认知—局部近，整体稳*

| 类型 | 放置 | 作用 |
| --- | --- | --- |
| 主题 MOC | 与主题同目录 | 本地索引，快速上下文 |
| 全局 MOC | `99‑system/MOC‑dashboard.md` | 总览+仪表盘 |

Dataview 每周列出未被全局 MOC 引用的 `MOC‑*` 进行补链。

---

## VII. 维护指标

*理论：Kaizen 持续改进*

| 指标 | 目标 | 查询片段 |
| --- | --- | --- |
| **孤岛笔记** | ≤ 5 % | `where outgoing = 0` |
| **Stale Projects** | 0 | `where status = "active" and updated <= date(today) - dur(30 days)` |

---

## VIII. 模板库（`99‑system/templates/`）

*理论：Miller 7±2 控制信息块*

| 模板 | 核心用途 | 字段差异 |
| --- | --- | --- |
| `_tpl-note` | 普通笔记 | 基础字段 |
| `_tpl-tech-cheatsheet` | 技术速查 | 最小信息块，符号锚点 |

> QuickAdd 各模板绑定宏：qa-note, qa-cheat。


---

## IX. 自动化脚本

- **jd_id**：自动生成Johnny-Decimal编号，在模板中使用完整路径调用
- **update_field**：自动更新元数据中的updated字段，通过完整路径调用
- **命名校验**：若常用Git，保留pre-commit；否则使用Obsidian Linter手动触发

---

### ✅ 最简落地清单

1. 建 6 + 1 顶级文件夹，模板放入 `99‑system`。
2. 用 `_tpl-note` 写 10 条笔记，练习 Capture→Process→Organize 3 步骤。
3. 每周查看孤岛查询；超 5 % 就补链或删除。

规范到此，剩下交给实践——写比改规更重要 🙂