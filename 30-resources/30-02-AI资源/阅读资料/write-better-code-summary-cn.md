---
title: 用AI编写更好的代码：Claude 3.5案例研究摘要
created: 2024-06-29 15:30
updated: 2024-06-29 15:30
type: resource
status: active
schema: v1
tags: [topic/ai/coding, topic/ai/llm, lang/chinese]
---

# 用AI编写更好的代码：Claude 3.5案例研究摘要

**作者:** Max Woolf (@minimaxir)
**原文链接:** [https://minimaxir.com/2025/01/write-better-code/](https://minimaxir.com/2025/01/write-better-code/)

## 概述

本文探讨了使用"编写更好的代码"这样简单的提示词，如何通过AI（特别是Claude 3.5 Sonnet）来迭代改进代码。作者通过一个查找数字和为30的最大与最小数之差的Python编程问题，展示了从初始解决方案到高度优化的多次迭代过程。

## 关键发现

通过简单地要求Claude"编写更好的代码"，每次迭代都产生了显著的性能提升：
- 初始解决方案：657毫秒
- 第一次优化：速度提升2.7倍
- 最终优化：速度提升267倍！

## 优化技术演进

### 初始实现
```python
import random

def digit_sum(n):
    """计算一个数的各位数字之和"""
    return sum(int(digit) for digit in str(n))

def find_difference():
    # 生成包含 100 万个随机整数的列表
    numbers = [random.randint(1, 100000) for _ in range(1000000)]

    # 初始化数字和为 30 的最小和最大数字的变量
    min_num = float('inf')  # 初始化为正无穷大
    max_num = float('-inf')  # 初始化为负无穷大

    # 查找数字和为 30 的数字
    for num in numbers:
        if digit_sum(num) == 30:
            min_num = min(min_num, num)
            max_num = max(max_num, num)

    # 检查是否找到了任何数字和为 30 的数字
    if min_num == float('inf') or max_num == float('-inf'):
        return "未找到数字和为 30 的数字"

    return max_num - min_num
```

### 主要优化进展

1. **第一次迭代**
   - 引入面向对象设计（类）
   - 预计算数字和（使用整数运算避免类型转换）
   - 使用数组存储预计算结果

2. **第二次迭代**
   - 引入NumPy向量化操作
   - 添加多进程并行处理
   - 分块处理大量数据

3. **第三次迭代**
   - 使用数学优化（数字和的确切公式）
   - 消除随机性，使用确定性算法
   - 添加函数类型注释和详细文档

4. **最终迭代**
   - 重构为高度优化的纯数学解决方案
   - 使用位操作和查找表进一步优化
   - 发现问题的解析解

## 关键启示

1. **AI能够像人类一样迭代改进代码**
   - 从简单的初始解决方案开始
   - 在每次迭代中加入更复杂的优化

2. **AI编码知识层次**
   - 了解多种编程范式（OOP、函数式等）
   - 能够应用先进的算法和数据结构
   - 懂得利用特定语言的库（如NumPy）进行优化

3. **实际应用指导**
   - 开始使用简单提示获取初始解决方案
   - 使用"编写更好的代码"这种简单提示迭代改进
   - 在特定的瓶颈上使用更具体的提示

## 结论

即使使用最简单的提示词，AI也能够产生巨大的代码优化。Claude 3.5在每次迭代中都展示了深刻的编程知识，能够从多个角度（算法、数据结构、并行处理、语言特性）来优化代码。

这表明在实际编程中，可以通过反复要求AI"编写更好的代码"来获得高质量、高性能的解决方案，而无需深入了解所有优化技术。

## 链接与参考

- [[MOC-AI阅读]]
- [[MOC-AI资源]] 