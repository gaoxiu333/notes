**通用任务提示模板（General Utility Prompts）**
```
根据从文档中提取的相关引文（由<quotes></quotes>分隔）和原始文档（由####分隔），请构建对问题的回答。请确保答案准确、语气友好且有帮助。
```

## **编码相关（Code Generation & Planning）**
**编程任务规划**
```markdown
Tell me your plan first; don’t code.
Give me a few options, starting with the simplest first. Don’t code.
Think as long as you need and ask me questions if you need more info.
```

**拆解复杂任务**
**查找边界情况**
```
What are the edge cases for this function?
```
**基于已有代码继续构建**
```
Based on this file, what functions or components are missing?
Suggest a list of next steps to implement feature X.
```
## **解释代码（Code Explanation）**
**简化解释**
```
explain how this file works in simple terms.
```
**添加注释**
```
Add comments that explain the code.
```
**使用辅助工具**
• [Repomix](https://repomix.com/) - 将代码仓库打包为单文件，适合上传给 LLM 处理

## **代码重构与优化（Refactoring）**
**重写代码**
```
Rewrite this function to be more efficient/readable.
```
 **风格 & 命名优化**
```
Suggest better variable and function names.
```

### 文档与说明生成（Documentation）

#### 📝 自动生成文档注释

text

复制编辑

`Add docstrings to this code using Google-style format.`

#### 📄 创建 README

text

复制编辑

`Create a concise README that explains how to use this project.`

---

### 🧩 多文件 & 项目级别提示

#### 📦 结构分析

text

复制编辑

`Explain the overall architecture of this project.`

#### 🗃️ 文件关系梳理

text

复制编辑

`Map out how the following files interact with each other.`

---

### ⛓️ 高级技巧（Chain-of-Thought / System Prompts）

#### 🧭 多步推理

text

复制编辑

`Let’s solve this step by step.`

#### 🧠 模拟专家角色

text

复制编辑

`You are a senior backend engineer with 10+ years experience. Explain the performance trade-offs in this code.`

#### 🧪 检查输出质量

text

复制编辑

`Does the following code follow best practices? If not, list the issues.`