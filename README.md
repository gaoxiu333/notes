# 个人知识管理系统

这是一个基于Obsidian的个人知识管理系统，采用PARA方法与Zettelkasten笔记法相结合的方式组织知识。

## 目录结构

- **Technology/** - 技术相关知识
  - Frontend/ - 前端技术
  - Backend/ - 后端技术
  - AI/ - 人工智能

- **Methodology/** - 方法论与思维模型
  - Productivity/ - 效率提升
  - Learning/ - 学习方法
  - Thinking/ - 思维模型

- **Projects/** - 项目相关内容
  - Active/ - 活跃项目
  - Completed/ - 已完成项目
  - Planning/ - 计划中项目

- **Resources/** - 资源库
  - Tutorials/ - 教程集合
  - Guides/ - 使用指南
  - Books/ - 书籍笔记
  - Papers/ - 论文笔记

- **Daily/** - 日常记录
  - Journal/ - 日记
  - Ideas/ - 想法收集
  - Inbox/ - 待处理内容

- **KnowledgeBase/** - 知识库核心
  - MOCs/ - 内容地图
  - Standards/ - 规范与标准
  - Templates/ - 笔记模板

## 主要入口

- [知识库主索引](KnowledgeBase/MOCs/index.md) - 整个知识库的导航中心
- [标签字典](KnowledgeBase/Standards/tags-dictionary.md) - 标准化标签体系
- [笔记模板索引](KnowledgeBase/Templates/index.md) - 各类笔记模板

## 笔记规范

本知识库遵循以下规范：

1. **文件夹名**：使用PascalCase命名法（如`FrontEnd`）
2. **文件名**：使用kebab-case命名法（如`react-hooks.md`）
3. **标签系统**：使用标准化的标签体系，详见[标签字典](KnowledgeBase/Standards/tags-dictionary.md)
4. **内容地图**：各领域使用MOC文件组织内容
5. **链接系统**：使用双括号链接`[[file-name]]`或`[[file-name|显示文本]]`

## 贡献与维护

- [内容迁移指南](KnowledgeBase/Standards/migration-guide.md) - 内容迁移的步骤和注意事项
- [知识管理规范](知识管理/规范.md) - 详细的知识管理规范文档

## 迁移进度

当前知识库正在按照规范进行组织和迁移，进度如下：

- [x] 基础结构搭建完成
- [x] 核心MOC创建完成
  - [x] 前端技术MOC
  - [x] 后端技术MOC
  - [x] AI技术MOC
  - [x] 知识管理MOC
- [x] 标准化模板系统建立
  - [x] 核心笔记模板
  - [x] 内容地图模板
  - [x] 日常记录模板
  - [x] 想法收集模板
- [ ] 内容迁移（进行中）
  - [x] 前端React内容
  - [x] 后端Node.js内容
  - [x] 后端Python/Jupyter内容
  - [x] AI/LLM内容
  - [x] 提示词工程内容
  - [ ] 其他内容（计划中）
- [ ] 标签系统完善（计划中）
- [ ] 知识图谱构建（计划中）

## 技术栈评测与项目实践

1. 大模型特点评测
   1. 客观的评测数据已经收集（权威评测机构评测），正在整理阶段
   2. 社区开发人员评测已收集，正在整理
   3. 主观使用评测（偏向个人参与实际项目开发）
      1. 评估标准，提示词对 AI 辅助编程的影响（正在进行）
      2. 大模型特性（MCP/function call）的影响（未开始）
2. 项目经验/最佳实践
   1. 规范
   2. 根据PRD、开发文档、设计测试还原质量


评测指标：
- token 数量
- 响应速度
- 生成质量