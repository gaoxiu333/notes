# Personal Knowledge Management System

这是一个个人知识管理系统，专注于技术学习和研究。

## 核心目录

- `inbox/`: 新内容的临时存放处
- `projects/`: 项目相关的笔记和文档
- `areas/`: 持续关注的领域笔记
- `resources/`: 可复用的参考资料
- `archive/`: 归档内容
- `system/`: 系统配置和模板

## 使用指南

### 1. 内容组织

- 新内容先放入 `inbox/`
- 定期整理 inbox 内容到对应目录
- 使用 MOC (Map of Content) 文件作为导航
- 通过标签系统进行横向关联

### 2. 文件命名

- 文件：`主题-子主题.md`
- MOC文件：`主题-MOC.md`
- 避免使用特殊字符和空格

### 3. 标签系统

使用四个顶级命名空间:
- `#topic/`: 主题分类
- `#status/`: 内容状态
- `#action/`: 待办事项
- `#lang/`: 编程语言

### 4. 元数据规范

每个文件的 YAML front matter:

```yaml
---
title: 文档标题
created: YYYY-MM-DD HH:MM
updated: YYYY-MM-DD HH:MM
type: note/moc/guide
status: draft/active/archived
tags: []
---
```

### 5. 写作流程

1. 在 inbox 中快速记录
2. 定期整理和分类
3. 建立知识链接
4. 定期复习和更新

### 6. 维护指标

- 定期清理 inbox
- 更新 MOC 文件
- 检查孤立笔记
- 归档过期内容

## 快速链接

- [主页](00-MOC.md)
- [项目追踪](projects/projects-MOC.md)
- [学习资源](resources/resources-MOC.md)
- [归档内容](archive/archive-MOC.md)

## 注意事项

1. 保持目录结构扁平，避免过深嵌套
2. 优先使用标签和链接而不是目录来组织内容
3. 定期维护和更新 MOC 文件
4. 遵循 PARA 方法论管理内容