## Prompt Engineering 实用手册 (中文版)

### 通用任务提示模板（General Utility Prompts）

```
根据从文档中提取的相关引文（由<quotes></quotes>分隔）和原始文档（由####分隔），请构建对问题的回答。请确保答案准确、语气友好且有帮助。
```

### 编码相关（Code Generation & Planning）

#### 编程任务规划

```markdown
首先告诉我你的计划，不要编码。
给我几个选项，从最简单的开始。不要编码。
想多久就多久，如果需要更多信息，请问我问题。
```

#### 拆解复杂任务

#### 查找边界情况

```
这个函数的边界情况是什么？
```

#### 基于已有代码继续构建

```
基于此文件，缺少哪些函数或组件？
建议实施功能 X 的后续步骤列表。
```

### 解释代码（Code Explanation）

#### 简化解释

```
用简单的术语解释这个文件是如何工作的。
```

#### 添加注释

```
添加解释代码的注释。
```

#### 使用辅助工具

*   [Repomix](https://repomix.com/) - 将代码仓库打包为单文件，适合上传给 LLM 处理

### 代码重构与优化（Refactoring）

#### 重写代码

```
重写此函数以使其更高效/可读。
```

#### 风格 & 命名优化

```
建议更好的变量和函数名称。
```

### 文档与说明生成（Documentation）

#### 自动生成文档注释

```
使用 Google 风格格式向此代码添加文档字符串。
```

#### 创建 README

```
创建一个简洁的 README，解释如何使用此项目。
```

### 多文件 & 项目级别提示

#### 结构分析

```
解释这个项目的整体架构。
```

#### 文件关系梳理

```
绘制以下文件如何相互交互。
```

### 高级技巧（Chain-of-Thought / System Prompts）

#### 多步推理

```
让我们逐步解决这个问题。
```

#### 模拟专家角色

```
你是一名拥有 10 多年经验的高级后端工程师。解释此代码中的性能权衡。
```

#### 检查输出质量

```
以下代码是否遵循最佳实践？如果不是，请列出问题。
