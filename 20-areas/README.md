# 20-areas 领域文件夹

这里存放需要**持续关注或维护的职责域**，没有明确的完成时间，但需要长期积累和维护的知识领域。

## 子目录结构

按技术领域分区：

- 20-00-方法论与思维
- 20-01-提示词工程
- 20-02-AI研究
- 20-03-前端开发
- 20-04-Nodejs

## 领域笔记规范

- 每个领域建立单独文件夹，以`20-XX-领域名称`命名
- 每个领域文件夹下必须有一个MOC（内容地图）笔记，命名为`00-MOC-领域名称`
- 所有文件必须遵循`XX-中文名.md`格式命名，确保有序显示
- 每个文件必须包含规范的YAML前置元数据，包括title、jd_id、created、updated、type、status和tags
- 标签使用命名空间前缀：`topic/`, `status/`, `action/`, `lang/`

## 元数据规范示例

```yaml
---
title: 文档标题
jd_id: J20-YYYYMMDD-HHMM  # Johnny-Decimal ID
created: YYYY-MM-DD HH:MM # 创建时间
updated: YYYY-MM-DD HH:MM # 更新时间
type: note                # moc / guide / note / dashboard ...
status: draft             # draft / active / archived
tags: []                  # 使用命名空间前缀，如topic/ai
---
```

## 领域与项目的关系

- 领域是长期积累的知识和技能
- 项目可以应用和扩展领域知识
- 项目完成后的经验和总结应反馈到相关领域中
- 通过领域间的链接形成知识网络 