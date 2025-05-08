---
title: "标签字典"
date: 2024-07-15
tags: 
  - type/reference
  - subject/knowledge-management
status: active
---

# 标签字典

本文档定义了整个知识库中使用的标准化标签体系，以保持标签的一致性和可管理性。

## 标签类别

标签按层级组织，形式为`category/tag`或`category/subcategory/tag`。

### 1. 类型标签 (type/)

描述笔记的类型或形式。

| 标签 | 描述 |
|------|------|
| `type/note` | 普通笔记，一般性知识记录 |
| `type/concept` | 概念笔记，对特定概念的解释和定义 |
| `type/moc` | 内容地图(Map of Content)，索引类笔记 |
| `type/reference` | 参考资料，如术语表、速查表等 |
| `type/tutorial` | 教程类内容 |
| `type/idea` | 想法或灵感 |
| `type/project` | 项目相关文档 |
| `type/template` | 模板文件 |
| `type/daily` | 日常记录或日记 |
| `type/meeting` | 会议笔记 |

### 2. 主题标签 (subject/)

描述笔记所属的主题或领域。

#### 2.1 技术相关

| 标签 | 描述 |
|------|------|
| `subject/frontend` | 前端技术相关 |
| `subject/frontend/javascript` | JavaScript相关 |
| `subject/frontend/css` | CSS相关 |
| `subject/frontend/react` | React框架相关 |
| `subject/backend` | 后端技术相关 |
| `subject/backend/nodejs` | Node.js相关 |
| `subject/backend/python` | Python相关 |
| `subject/ai` | 人工智能相关 |
| `subject/ai/prompt` | 提示词工程相关 |
| `subject/ai/llm` | 大语言模型相关 |
| `subject/ai/ml` | 机器学习相关 |

#### 2.2 方法论相关

| 标签 | 描述 |
|------|------|
| `subject/productivity` | 生产力与效率提升相关 |
| `subject/learning` | 学习方法相关 |
| `subject/thinking` | 思维模型相关 |
| `subject/knowledge-management` | 知识管理相关 |

#### 2.3 项目相关

| 标签 | 描述 |
|------|------|
| `subject/project/[项目名]` | 特定项目相关 |

### 3. 状态标签 (status/)

描述笔记的处理状态。

| 标签 | 描述 |
|------|------|
| `status/draft` | 草稿状态，尚未完成 |
| `status/active` | 活跃状态，已完成但可能会更新 |
| `status/completed` | 已完成状态，内容相对稳定 |
| `status/archived` | 归档状态，不再活跃更新 |

### 4. 关系标签 (relation/)

描述笔记与其他事物的关系。

| 标签 | 描述 |
|------|------|
| `relation/continues` | 继续发展某个特定主题 |
| `relation/inspired` | 从某事物获得灵感 |
| `relation/response` | 对某事物的回应或评论 |

## 标签使用规范

1. **标签格式**：使用小写字母、连字符(-)和斜杠(/)，避免使用空格和特殊字符
2. **保持简洁**：每篇笔记通常使用3-7个标签，不要过多
3. **优先使用已有标签**：尽量从标签字典中选择标签
4. **层次结构**：优先使用更具体的子类标签，必要时可同时使用父类标签
5. **新增标签**：如需增加新标签，应更新此标签字典

## 标签模式示例

**技术笔记**
```yaml
tags:
  - type/tutorial
  - subject/frontend/react
  - status/active
```

**概念解释**
```yaml
tags:
  - type/concept
  - subject/ai/llm
  - status/completed
```

**项目文档**
```yaml
tags:
  - type/project
  - subject/project/website-redesign
  - status/active
```

**日常记录**
```yaml
tags:
  - type/daily
  - status/archived
```

## 标签管理

- 每月进行标签审核，清理不再使用的标签
- 标签字典定期更新，以反映知识系统的演变
- 考虑使用Obsidian的标签面板功能，查看整个标签体系 