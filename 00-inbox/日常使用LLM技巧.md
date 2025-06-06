---
title: 日常使用LLM技巧
jd_id: J00-20250526-1021
created: 2025-05-26 10:21
updated: 2025-05-26 10:21
type: note
status: draft
tags: []
---

# 日常使用 LLM 技巧

## 概述

记录了我阅读 blog 的一些概述

## 日常工程工作的实用人工智能技术

> 参考：[日常工程工作的实用人工智能技术](https://www.seangoedecke.com/practical-ai-techniques/)

### 核心理念

作者认为流行的 AI 建议过于关注工具和"魔法提示词"，忽略了核心技能。这篇文章针对已经具备能力的软件工程师，而非技术新手。

### 两大核心技术

#### 1. "第二意见"技术

**原理：** 当你已经有了可行方案时，让 AI 审查是否有更简洁或更符合惯例的解决方案

**使用方法：** 将代码差异复制粘贴给 AI，询问"这看起来怎么样？"

**关键要点：**

- 只花几分钟时间，如果没有立即的"顿悟时刻"就停止
- 适用于代码更改、架构计划、调试笔记等各种技术工作产品
- 不建议使用现有的代码审查工具，这更像是高层次的直觉检查

#### 2. "一次性调试脚本"技术

**原理：** AI 在编写 10-30 行简单代码方面比强工程师更快

**应用场景：** 调试复杂问题时，AI 可以快速生成脚本来缩小问题范围

**实例：** 作者在设置 Elasticsearch 索引时，GPT-4o 立即生成了一个脚本来逐步测试查询的各个部分

**前提条件：** 需要对问题有一定理解，能够解释你想要的调试脚本类型

### 其他辅助技术

- **寻找证据支持已知观点：** 使用带搜索功能的 LLM 来找到第三方研究或证据来支持你的立场
- **填补专业领域外的技术空白：** 在不熟悉的领域（如 nginx 配置）快速从零基础达到"强初级"水平

## 我的 LLM 代码生成工作流程

> 参考：[我的 LLM 代码生成工作流程](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/)
>
> **离散循环：** 指的是将开发过程分解为独立的、不重叠的阶段，每个阶段都有明确的开始和结束点。

### 核心理念

作者认为成功的 LLM 代码生成需要：**头脑风暴规范 → 制定计划 → 执行**，采用离散循环的方式，然后就是魔法般的效果。

### 两种开发场景

#### 绿地项目（Greenfield）工作流

##### 第一步：构思完善

- 使用对话式 LLM（ChatGPT 4o/o3）逐步完善想法
- **关键提示词：** 让 AI 一次只问一个问题，逐步构建详细规范
- **最终输出：** 保存为 `spec.md` 的开发者就绪规范

##### 第二步：规划

- 将规范传递给推理模型（o1*、o3*、r1）
- 分为 TDD 和非 TDD 两种提示模板
- 将项目分解为小的、可迭代的步骤
- **输出：** `prompt_plan.md`（提示计划）和 `todo.md`（待办清单）
- 整个过程仅需约 15 分钟

##### 第三步：执行

**支持多种工具：**

- **Claude 方式：** 与 claude.ai 配对编程，逐步粘贴提示
- **Aider 方式：** 自动化程度更高，像玩"点击游戏"一样轻松

#### 遗留项目（非绿地）工作流

##### 获取上下文

- 使用 repomix 等工具将源代码打包
- 配置 mise 任务管理系统，支持各种 LLM 操作：
  - 生成代码审查
  - 生成 GitHub 问题
  - 生成缺失测试
  - 生成 README 等

##### 执行流程

类似绿地项目，但更专注于单个任务而非整体项目规划

### 实用提示词技巧

- **代码审查提示词：** 要求作为资深开发者进行全面代码审查，输出 markdown 格式，包含行号和上下文信息
- **GitHub 问题生成：** 识别代码中的漏洞、设计选择或代码清洁性问题
- **缺失测试：** 审查代码并列出应该存在的测试用例

## 我如何驯服 Cursor AI 来每次编写完美的代码

> 参考：[我如何驯服 Cursor AI 来每次编写完美的代码](https://freedium.cfd/https://medium.com/coding-nexus/how-i-tamed-cursor-ai-to-write-perfect-code-every-time-951851a92f6f)

这篇文章分享了作者如何"驯服"Cursor AI 的实战经验，让它每次都能生成完美代码。

### 核心问题诊断

#### Cursor 失败的根本原因

- **Cursor 不是读心术师：** 没有计划就开始编码，等于让它瞎猜你的需求
- **缺乏上下文：** 没有足够的背景信息，Cursor 会做出愚蠢的决定
- **从零开始的困难：** Cursor 在项目搭建阶段表现很差

### 七步驯服法

#### 第 1 步：制定详细计划

**核心原则：** 70% 规划，30% 执行

#### 第 2 步：文档化一切

使用 **CodeGuide 工具**生成两个关键文档：

##### 产品需求文档(PRD)：定义"做什么"

- 功能特性
- 用户故事
- 边界情况

##### 技术栈文档：定义"怎么做"

- 框架选择
- 库和工具

#### 第 3 步：不要从零开始

**问题：** Cursor 在项目搭建阶段很糟糕

#### 第 4 步：正确设置 Cursor

**操作步骤：**

1. 在项目根目录创建 `Instructions` 文件夹
2. 将 CodeGuide 文档放入其中
3. 告诉 Cursor 使用这些文档作为上下文

#### 第 5 步：项目规则的魔法

##### 旧方法的问题：`.cursorrules` 文件

- 所有规则堆在一个文件里
- Cursor 经常忽略一半规则
- 不可扩展

##### 新方法：项目规则（`.mdc` 文件）

#### 第 6 步：收获成果

**项目规则带来的改变：**

- Cursor 犯错更少
- 记住你的编码风格
- 第一次就做对

#### 第 7 步：项目规则最佳实践

**实用技巧：**

- **保持规则具体：** 分离前端、后端等，不要堆在一个文件里
- **使用精确作用域：** 仅在需要的地方应用规则，如 `.tsx` 用于 React，`api/*/**.ts` 用于后端
- **早期测试：** 先生成小代码片段检查 Cursor 是否遵循规则
- **及时更新：** 项目变化时更新规则，不要让规则过时


## Agent TeamCoding：结合氛围编程与敏捷工作流构建复杂项目

> 参考：[Agent TeamCoding：结合氛围编程与敏捷工作流构建复杂项目](https://medium.com/@tydev2025/agent-teamcoding-combining-vibe-coding-with-agile-workflow-to-build-complex-projects-290face4f915)

### 核心概念

#### 什么是"氛围编程"(Vibe Coding)

- **快速流畅：** 想法瞬间变成代码，生产力飙升
- **开环控制系统：** 快速但不稳定
- **适用场景：** 小脚本、原型项目
- **问题：** 项目复杂度增加时容易崩溃

### 作者的实战经验

#### 项目背景

构建 **ARCH**（容器自动恢复工具）—— 一个中等复杂度的开源工具

#### 结果

**10倍生产力提升：** 1个人1个月完成通常需要3-4人团队3个月的工作

### 氛围编程的问题

#### 初期工具尝试

- ChatGPT + VSCode 粘贴
- Cline + Google Gemini API
- Cursor

#### 遇到的主要问题

- **幻觉API：** AI提出不存在的函数，浪费时间
- **调试混乱：** AI经常猜错根本原因，代码偏离正轨

### 解决思路

将氛围编程的速度与敏捷的结构相结合

### Agent TeamCoding：七步方法论

#### 1. 强大的PRD文档

**AI角色：** 产品经理

- 将粗略想法转化为结构化的产品需求文档
- 定义用户故事和功能需求
- 多角度审查（用户、系统架构师）

#### 2. 扎实的工程设计

**AI角色：** 系统架构师

- 提供支撑文档减少幻觉（API文档、技术栈规范）
- 要求多个设计选项
- 使用多个LLM交叉审查设计
- 不同角色反馈（QA主管、安全专家）

#### 3. 规划实施冲刺

**AI角色：** 工程经理

- 将功能分解为可测试、可交付的里程碑
- 保持每个冲刺专注和快速
- 从最小脚手架开始

#### 4. 自动化和可恢复的开发环境

**AI角色：** DevOps工程师

- 使用GitHub版本控制
- 生成提交、构建、测试的自动化脚本
- 维护开发环境的干净VM快照
- 频繁提交避免不可逆错误

#### 5. AI生成和AI审查代码

**AI角色：** 高级开发者

- 提供设计文档、技术栈参考、风格指南
- 严格限定生成范围—一次一个功能
- 包含可配置的调试级别日志
- AI解释逻辑、证明设计对齐、突出可能的Bug

#### 6. 生成系统和单元测试

**AI角色：** QA工程师

- 基于PRD、工程设计和代码生成测试计划
- 手动审查和调试AI生成的测试工具
- 明确测试用例、输入输出断言、模拟边界
- 记录测试覆盖率指标

#### 7. AI调试工作流程

**AI角色：** 高级开发者

- 一次专注一个Bug
- 首先进行根本原因分析
- 提出多个修复选项，选择影响最小的
- 标记涉及系统设计变更的修复
- 运行单元和系统测试检查回归

### 核心洞察

#### 从氛围编程到Agent TeamCoding

- 不是选择速度还是纪律，而是将它们结合
- 给AI分配不同角色：产品经理、架构师、QA、工程师
- 构建AI团队：每个代理在结构化敏捷工作流中贡献
- **心态转变：** 从提示AI到管理协作的、角色驱动的工程团队

#### Agent TeamCoding的价值

- 保持快速迭代的同时维护生产质量软件所需的检查和平衡
- 将AI从助手转变为可靠的团队成员
- 结合敏捷实践（规划、审查门禁、测试驱动开发）

### 总结

**Agent TeamCoding = 氛围编程的速度 + 敏捷的结构 + AI角色分工**

这种方法让AI开发从快速原型扩展到复杂的生产级项目，实现了真正可持续的AI辅助开发。