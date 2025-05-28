---
title: 分层MOC实践
jd_id: J10-20250509-2214
created: 2025-05-09 22:14
updated: 2025-05-28 12:34
type: guide
status: active
tags: [topic/pkm, topic/moc, topic/structure]
---

# 分层MOC实践

> **知识导航的层次化组织** - MOC系统的结构优化方法

## 🏗️ MOC分层原则

### 层次设计
- **全局MOC**: 系统总览，位于`99-system/MOCs/`
- **主题MOC**: 领域导航，与主题同目录，命名`00-MOC-主题.md`
- **项目MOC**: 项目内容索引，项目根目录

### 连接策略
- **自下而上**: 子主题MOC链接到父级MOC
- **横向关联**: 相关主题MOC间的交叉引用
- **动态维护**: 定期检查更新MOC内容

## 📚 相关实践

- [[01-实践-PKM规范|PKM规范]] - MOC命名规范
- [[00-MOC-PKM|PKM系统MOC]] - 本项目MOC示例

---
*结构清晰，导航便捷*
