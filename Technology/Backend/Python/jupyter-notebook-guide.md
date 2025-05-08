---
title: "Jupyter Notebook使用指南"
date: 2024-07-15
updated: 2024-07-15
tags: 
  - type/reference
  - subject/backend/python
status: active
---

# Jupyter Notebook使用指南

## 简介

Jupyter Notebook是一个交互式的计算环境，支持代码、文本、公式和可视化的混合编写。它常用于数据分析、机器学习和科学计算。

## 核心功能

- **代码执行**：支持多种编程语言（如Python、R、Julia等）
- **可视化**：可以直接显示图表和图像
- **Markdown支持**：可以编写富文本文档，包括标题、列表和公式
- **交互性**：支持交互式小部件和动态输出

## 基础示例

### 创建代码单元格

```python
# 这是一个简单的Python示例
print("Hello, Jupyter!")

# 数据分析示例
import pandas as pd
import matplotlib.pyplot as plt

# 创建简单的数据框
df = pd.DataFrame({
    'x': range(1, 11),
    'y': [i**2 for i in range(1, 11)]
})

# 绘制图表
plt.figure(figsize=(8, 4))
plt.plot(df['x'], df['y'], marker='o')
plt.title('y = x²')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
```

### 创建Markdown单元格

```markdown
# 这是一个标题

这是普通文本。

## 列表示例
- 项目一
- 项目二
- 项目三

## 公式示例
$E = mc^2$

## 表格示例
| 名称 | 值 |
|------|-----|
| A | 100 |
| B | 200 |
```

## 快捷键参考

### 命令模式（按`Esc`激活）

| 快捷键 | 功能 |
|--------|------|
| `A` | 在当前单元格上方插入新单元格 |
| `B` | 在当前单元格下方插入新单元格 |
| `D, D` | 删除当前单元格 |
| `Z` | 撤销删除单元格 |
| `M` | 将单元格转换为Markdown |
| `Y` | 将单元格转换为代码 |
| `Shift + Up/Down` | 多选单元格 |

### 编辑模式（按`Enter`激活）

| 快捷键 | 功能 |
|--------|------|
| `Ctrl + Enter` | 运行当前单元格 |
| `Shift + Enter` | 运行当前单元格并选中下一个单元格 |
| `Alt + Enter` | 运行当前单元格并在下方插入新单元格 |
| `Ctrl + S` | 保存笔记本 |

## 环境设置

### 安装

```bash
# 使用pip安装
pip install notebook

# 使用conda安装
conda install -c conda-forge notebook
```

### 启动

```bash
# 在当前目录启动
jupyter notebook

# 指定端口启动
jupyter notebook --port=8889
```

## 在VS Code中使用

1. **安装扩展**：
   - 打开VS Code的扩展市场，搜索并安装"Jupyter"扩展

2. **打开文件**：
   - 直接打开`.ipynb`文件，VS Code会以交互式界面显示

3. **运行单元格**：
   - 点击单元格左侧的运行按钮，或使用快捷键`Shift + Enter`

4. **切换内核**：
   - 点击右上角的内核选择器，选择适合的Python环境

## 最佳实践

- 为笔记本添加明确的标题和描述
- 将代码拆分为逻辑清晰的小单元格
- 使用Markdown单元格为代码添加注释和解释
- 定期保存工作
- 考虑使用版本控制(如Git)管理笔记本

## 相关资源

- [Jupyter官方文档](https://jupyter.org/documentation)
- [Jupyter Notebook快速入门](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html)
- [Markdown语法指南](https://www.markdownguide.org/) 