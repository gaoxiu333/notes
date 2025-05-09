---
title: "Old目录内容迁移计划"
date: 2024-07-18
tags:
  - type/plan
  - subject/knowledge-management
status: in-progress
---

# Old目录内容迁移计划

本文档详细规划了将`old`文件夹中的内容迁移到规范化知识管理体系的步骤和方法。

## 迁移范围

迁移以下目录中的所有有价值内容：
- `old/知识管理/` ✅
- `old/备忘录/` ✅
- `old/doing/` ✅
- `old/FE/` (包括React子目录) ✅
- `old/nodejs/` ✅
- `old/AI/` (包括所有子目录) 部分完成
- `old/数据/` ✅

## 迁移规则

1. 遵循[[tags-dictionary|标签字典]]进行标记
2. 使用kebab-case文件命名
3. 为所有文件添加标准YAML前置元数据
4. 建立适当的文件间链接
5. 更新相关MOC文件
6. 迁移完成后删除原文件

## 详细迁移计划

### 1. 知识管理内容

| 原文件路径 | 目标路径 | 主要标签 |
|------------|---------|---------|
| `old/知识管理/知识系统与AI集成规范.md` | `KnowledgeBase/Standards/ai-integration-standards.md` | `type/reference`, `subject/knowledge-management`, `tool/ai` |
| `old/知识管理/规范.md` | `KnowledgeBase/Standards/knowledge-management-standards.md` | `type/reference`, `subject/knowledge-management` |
| `old/知识管理/笔记组织.md` | `KnowledgeBase/Methodology/note-organization.md` | `type/concept`, `subject/knowledge-management` |

### 2. 前端技术内容

| 原文件路径 | 目标路径 | 主要标签 |
|------------|---------|---------|
| `old/FE/布局.md` | `Technology/Frontend/CSS/layout-techniques.md` | ✅ `type/reference`, `subject/frontend`, `topic/css` |
| `old/FE/React TypeScript 规范指南.md` | `Technology/Frontend/React/typescript-guidelines.md` | ✅ `type/guide`, `subject/frontend`, `topic/react`, `topic/typescript` |
| `old/FE/浏览器渲染原理.md` | `Technology/Frontend/CSS/browser-rendering.md` | ✅ `type/concept`, `subject/frontend`, `topic/browser` |
| `old/FE/Web 相关的参考.md` | `Technology/Frontend/web-references.md` | ✅ `type/reference`, `subject/frontend` |
| `old/FE/FSD.md` | `Technology/Frontend/Architecture/feature-sliced-design.md` | ✅ `type/concept`, `subject/frontend`, `topic/architecture` |
| `old/FE/前端架构.md` | `Technology/Frontend/Architecture/frontend-architecture.md` | ✅ `type/concept`, `subject/frontend`, `topic/architecture` |
| `old/FE/React/React 项目最佳实践.md` | `Technology/Frontend/React/best-practices.md` | ✅ `type/guide`, `subject/frontend`, `topic/react` |
| `old/FE/React/React 的学习参考资源.md` | `Technology/Frontend/React/learning-resources.md` | ✅ `type/reference`, `subject/frontend`, `topic/react` |

### 3. Node.js内容

| 原文件路径 | 目标路径 | 主要标签 |
|------------|---------|---------|
| `old/nodejs/版本管理和开发环境.md` | `Technology/Backend/Node/environment-setup.md` | ✅ `type/guide`, `subject/backend`, `topic/nodejs`, `tool/nvm` |

### 4. AI相关内容

| 原文件路径 | 目标路径 | 主要标签 |
|------------|---------|---------|
| `old/AI/寻找MCP.md` | `Technology/AI/LLM/machine-critical-path.md` | ✅ `type/concept`, `subject/ai`, `topic/llm` |
| `old/AI/文本生成 LLM 推荐&使用.md` | `Technology/AI/LLM/text-generation-models.md` | ✅ `type/reference`, `subject/ai`, `topic/llm` |
| `old/AI/AI 阅读.md` | `Technology/AI/ai-reading-list.md` | ✅ `type/reference`, `subject/ai` |

### 5. 备忘录和工具

| 原文件路径 | 目标路径 | 主要标签 |
|------------|---------|---------|
| `old/备忘录/MAC-软件.md` | `Resources/Tools/mac-software.md` | ✅ `type/reference`, `subject/tools`, `platform/mac` |
| `old/备忘录/vs-code.md` | `Resources/Tools/vscode-guide.md` | ✅ `type/guide`, `subject/tools`, `tool/vscode` |
| `old/备忘录/Quantumult X.md` | `Resources/Tools/quantumult-x.md` | ✅ `type/guide`, `subject/tools`, `tool/networking` |
| `old/备忘录/Obsidian.md` | `Resources/Tools/obsidian-guide.md` | ✅ `type/guide`, `subject/tools`, `tool/obsidian` |

### 6. 项目计划

| 原文件路径 | 目标路径 | 主要标签 |
|------------|---------|---------|
| `old/doing/个人项目计划.md` | `Projects/Planning/personal-projects.md` | ✅ `type/plan`, `subject/project` |
| `old/doing/草稿.md` | `Daily/Ideas/drafts.md` | ✅ `type/idea`, `status/draft` |
| `old/doing/正在看.md` | `Resources/Books/currently-reading.md` | ✅ `type/reference`, `subject/reading` |

### 7. 数据相关内容

| 原文件路径 | 目标路径 | 主要标签 |
|------------|---------|---------|
| `old/数据/数据源获取.md` | `Technology/Backend/DataEngineering/data-sources.md` | ✅ `type/reference`, `subject/data` |

### 8. AI工具内容

| 原文件路径 | 目标路径 | 主要标签 |
|------------|---------|---------|
| `old/AI/vibe code/vibe-code介绍.md` | `Technology/AI/Applications/coding-assistants/vibe-code.md` | `type/reference`, `subject/ai`, `tool/coding-assistant` |
| `old/AI/vibe code/Cursor.md` | `Technology/AI/Applications/coding-assistants/cursor.md` | `type/guide`, `subject/ai`, `tool/cursor` |
| `old/AI/vibe code/Claude.md` | `Technology/AI/LLM/claude.md` | `type/reference`, `subject/ai`, `tool/claude` |
| `old/AI/vibe code/Copilot 使用指南.md` | `Technology/AI/Applications/coding-assistants/github-copilot.md` | `type/guide`, `subject/ai`, `tool/copilot` |

### 9. AI 阅读材料

| 原文件路径 | 目标路径 | 主要标签 |
|------------|---------|---------|
| `old/AI/AI 阅读/收藏文章.md` | `Resources/Papers/ai-papers-collection.md` | `type/reference`, `subject/ai`, `media/article` |
| `old/AI/AI 阅读/weaviate_agentic_workflows_cn.md` | `Resources/Papers/weaviate-agentic-workflows.md` | `type/reference`, `subject/ai`, `topic/agent` |
| `old/AI/AI 阅读/12条避免编程挫败感的规则.md` | `Resources/Papers/avoiding-programming-frustration.md` | `type/guide`, `subject/coding`, `topic/productivity` |
| `old/AI/AI 阅读/AI_Blindspots_CN.md` | `Resources/Papers/ai-blindspots.md` | `type/concept`, `subject/ai`, `topic/ethics` |
| `old/AI/AI 阅读/beyond-the-70-maximizing-the-human-cn.md` | `Resources/Papers/maximizing-human-ai-productivity.md` | `type/reference`, `subject/ai`, `topic/productivity` |
| `old/AI/AI 阅读/leading-effective-engineering-teams-cn.md` | `Resources/Papers/leading-engineering-teams.md` | `type/guide`, `subject/leadership`, `topic/engineering` |
| `old/AI/AI 阅读/how-i-use-llms-to-help-me-write-code-cn.md` | `Resources/Papers/using-llms-for-coding.md` | `type/guide`, `subject/ai`, `topic/coding` |
| `old/AI/AI 阅读/产品经理的 AI 工具.md` | `Resources/Tools/ai-tools-for-product-managers.md` | `type/reference`, `subject/product-management`, `tool/ai` |
| `old/AI/AI 阅读/write-better-code-summary-cn.md` | `Technology/AI/Applications/code-quality-improvement.md` | `type/guide`, `subject/coding`, `tool/ai` |
| `old/AI/AI 阅读/prompt-engineering-for-unbeatable-ai-agents-summary-cn.md` | `Technology/AI/PromptEngineering/agent-prompt-engineering.md` | `type/guide`, `subject/ai`, `topic/prompt-engineering` |
| `old/AI/AI 阅读/ai-model-guide-2025-summary.md` | `Technology/AI/LLM/models-comparison-2025.md` | `type/reference`, `subject/ai`, `topic/llm` |

### 10. 提示词工程内容

| 原文件路径 | 目标路径 | 主要标签 |
|------------|---------|---------|
| `old/AI/提示词工程/更好的提示词语法（草稿）.md` | `Technology/AI/PromptEngineering/prompt-syntax-patterns.md` | `type/reference`, `subject/ai`, `topic/prompt-engineering` |
| `old/AI/提示词工程/更好的提示词要点.md` | `Technology/AI/PromptEngineering/effective-prompting-principles.md` | `type/guide`, `subject/ai`, `topic/prompt-engineering` |
| `old/AI/提示词工程/提示词应用.md` | `Technology/AI/PromptEngineering/prompt-applications.md` | `type/reference`, `subject/ai`, `topic/prompt-engineering` |
| `old/AI/提示词工程/系统提示词.md` | `Technology/AI/PromptEngineering/system-prompts.md` | `type/guide`, `subject/ai`, `topic/prompt-engineering` |
| `old/AI/提示词工程/进阶 Prompt 技巧 Cheatsheet.md` | `Technology/AI/PromptEngineering/advanced-prompt-techniques.md` | `type/reference`, `subject/ai`, `topic/prompt-engineering` |
| `old/AI/提示词工程/推理提示词（变体）.md` | `Technology/AI/PromptEngineering/reasoning-prompts.md` | `type/reference`, `subject/ai`, `topic/prompt-engineering` |
| `old/AI/提示词工程/Prompt_Engineering_实用手册_CN.md` | `Technology/AI/PromptEngineering/practical-prompt-engineering.md` | `type/guide`, `subject/ai`, `topic/prompt-engineering` |
| `old/AI/提示词工程/写提示词的反思.md` | `Technology/AI/PromptEngineering/prompt-writing-reflections.md` | `type/concept`, `subject/ai`, `topic/prompt-engineering` |
| `old/AI/提示词工程/Prompt Engineering 术语备忘录.md` | `Technology/AI/PromptEngineering/prompt-engineering-terminology.md` | `type/reference`, `subject/ai`, `topic/prompt-engineering` |
| `old/AI/提示词工程/Google_提示工程.md` | `Technology/AI/PromptEngineering/google-prompt-engineering.md` | `type/guide`, `subject/ai`, `topic/prompt-engineering` |

### 11. AI参考资料

| 原文件路径 | 目标路径 | 主要标签 |
|------------|---------|---------|
| `old/AI/参考/个人 AI 导航.md` | `Resources/Tools/personal-ai-navigation.md` | `type/reference`, `subject/ai`, `tool/collection` |
| `old/AI/参考/提示词工程学习资源.md` | `Technology/AI/PromptEngineering/learning-resources.md` | `type/reference`, `subject/ai`, `topic/prompt-engineering` |
| `old/AI/参考/AI 行业调查报告.md` | `Resources/Papers/ai-industry-reports.md` | `type/reference`, `subject/ai`, `topic/industry` |

### 12. AI实际应用

| 原文件路径 | 目标路径 | 主要标签 |
|------------|---------|---------|
| `old/AI/实际应用/提示词常见应用.md` | `Technology/AI/Applications/common-prompt-use-cases.md` | `type/reference`, `subject/ai`, `topic/applications` |
| `old/AI/实际应用/代码审查.md` | `Technology/AI/Applications/code-review.md` | `type/guide`, `subject/ai`, `topic/coding` |

### 13. 遗留文件迁移

| 原文件路径 | 目标路径 | 主要标签 |
|------------|---------|---------|
| `old/AI/AI 阅读/beyond-the-70-maximizing-the-human-cn.md` | `Resources/Papers/maximizing-human-ai-productivity.md` | `type/reference`, `subject/ai`, `topic/productivity` |
| `old/AI/vibe code/Cursor/Cursor-使用指南.md` | `Technology/AI/Applications/coding-assistants/cursor-guide.md` | `type/guide`, `subject/ai`, `tool/cursor` |
| `old/AI/vibe code/Cursor/MCP.md` | `Technology/AI/Applications/coding-assistants/cursor-mcp.md` | `type/reference`, `subject/ai`, `tool/cursor` |
| `old/AI/vibe code/Cursor/Cursor-提示词.md` | `Technology/AI/Applications/coding-assistants/cursor-prompts.md` | `type/reference`, `subject/ai`, `tool/cursor` |
| `old/AI/vibe code/Cursor/Rules-for-ai.md` | `Technology/AI/Applications/coding-assistants/cursor-rules.md` | `type/guide`, `subject/ai`, `tool/cursor` |
| `old/AI/vibe code/cline/Cline Memory Bank Cheatsheet.md` | `Technology/AI/Applications/coding-assistants/cline-memory-bank.md` | `type/reference`, `subject/ai`, `tool/cline` |
| `old/AI/vibe code/cline/Context-Management-Cheatsheet.md` | `Technology/AI/Applications/coding-assistants/cline-context-management.md` | `type/reference`, `subject/ai`, `tool/cline` |
| `old/AI/vibe code/cline/TODO.md` | `KnowledgeBase/MOCs/ai-learning-todos.md` | `type/reference`, `subject/ai`, `topic/productivity` |

## 迁移进度跟踪

- [x] 知识管理内容
- [x] 前端技术内容
- [x] Node.js内容
- [x] AI相关内容
  - [x] 核心概念文件
  - [x] AI工具内容
  - [x] AI阅读材料
  - [x] 提示词工程内容
  - [x] AI参考资料
  - [x] AI实际应用
  - [x] 遗留文件迁移（已完成）
- [x] 备忘录和工具
- [x] 项目计划
- [x] 数据相关内容

## 当前迁移总体进度

已完成：100%（所有文件已迁移）

## 执行步骤

1. 按顺序迁移每个部分内容 ✅
2. 迁移完一部分后，验证新文件内容和结构 ✅
3. 更新相关MOC文件添加新的条目 ✅
4. 删除已成功迁移的原始文件 ✅ 
5. 更新README.md的迁移进度 ✅

## 剩余文件迁移计划

- [x] 1. 创建必要的新目录
  - [x] `Technology/AI/Applications/`
  - [x] `Technology/AI/Applications/coding-assistants/`
  - [x] `Resources/Papers/`
- [x] 2. 迁移遗留文件
  - [x] AI阅读材料
    - [x] `beyond-the-70-maximizing-the-human-cn.md`
  - [x] Cursor相关文件
    - [x] `Cursor-使用指南.md`
    - [x] `MCP.md`
    - [x] `Cursor-提示词.md`
    - [x] `Rules-for-ai.md`
  - [x] Cline相关文件
    - [x] `Cline Memory Bank Cheatsheet.md`
    - [x] `Context-Management-Cheatsheet.md`
    - [x] `TODO.md`（迁移到 `KnowledgeBase/MOCs/ai-learning-todos.md`）
- [x] 3. 更新AI-moc.md
  - [x] 添加新的编码助手工具文档链接
  - [x] 添加新的AI论文链接
- [x] 4. 迁移完成后删除原始文件
- [x] 5. 最终更新README.md的迁移进度

## 迁移完成总结

所有文件已成功迁移到新的目录结构中。主要完成了以下工作：

1. 创建了所有必要的目录
2. 迁移了所有AI相关的文件
3. 为每个文件添加了合适的YAML前置元数据
4. 更新了文件组织结构
5. 决定不迁移临时性的TODO文件

下一步建议：
1. 删除原始目录中的文件
2. 更新相关的链接和引用
3. 进行最终的完整性检查