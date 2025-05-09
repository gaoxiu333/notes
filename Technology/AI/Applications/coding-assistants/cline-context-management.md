---
title: "Cline 上下文管理指南"
date: 2024-03-13
tags:
  - type/guide
  - subject/ai
  - tool/cline
  - topic/context-management
---

# Cline 上下文管理指南

## 基础概念
- **上下文** = Cline 了解的项目信息
- **上下文窗口** = 单次可处理信息量 
  - Claude 3.5 Sonnet: 200k tokens
  - 1 token ≈ 3/4 英文单词
  - 使用量 >70% 建议新会话

## 构建方式
1. **自动收集**
   - 读取相关文件
   - 探索项目结构
   - 分析依赖关系

2. **用户引导**
   - 分享文件/文档
   - 回答问题
   - 指导关注点

## 上下文文件

### Memory Bank
```
projectbrief.md   # 项目基础
techContext.md    # 技术背景
systemPatterns.md # 系统模式
activeContext.md  # 当前状态
```

### 任务文档
```markdown
# task-context.md
- 需求和约束
- 技术方案
- 实现细节
```

## 最佳实践

### 监控窗口
- 关注进度条(↑输入 ↓输出)
- 长会话注意用量
- 处理多文件时监控

### 文件维护
- 重大更改后更新
- 删除过时信息
- 记录关键决策

### 使用提示
1. 保持信息聚焦
2. 复杂讨论用 Plan 模式
3. 适时开启新会话
4. 确保跨会话理解 