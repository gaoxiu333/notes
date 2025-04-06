# LLM代码生成优化 Cheatsheet

> 总结自: [Write Better Code: All You Need Is "write better code"?](https://minimaxir.com/2025/01/write-better-code/)

## 核心技巧: Planning提示

### Planning的重要性
- 源自经典的"let's think step by step"方法
- 是帮助对齐LLM输出的有效技巧
- 特别适用于Claude 3.5 Sonnet等现代LLM
- 通过要求LLM先规划后执行，提高输出质量

### 使用方式
```
[任务描述]
Before writing the code, plan out all the necessary [steps/optimizations/approaches].
```

## 提示词策略对比 

### 1. 简单迭代策略
- **特点**: 直接要求改进，如"write better code"
- **优势**: 操作简单，LLM会逐步改进
- **劣势**: 方向不明确，可能导致过度工程化
- **示例**:
```
write better code
```

### 2. 工程化提示策略
- **特点**: 明确优化目标和约束
- **优势**: 更快达到目标，代码质量更高
- **劣势**: 可能引入细微bug
- **示例**:
```
系统提示:
All code you write MUST be fully optimized.
"Fully optimized" includes:
- maximizing algorithmic big-O efficiency
- using parallelization and vectorization
- following proper style conventions
- no extra code beyond necessities
```

## LLM代码优化行为分析

### 1. 简单迭代模式下
- 逐步引入更复杂的优化
- 倾向添加额外功能(如日志、监控)
- 可能导致代码膨胀
- 性能提升不稳定

### 2. 工程化提示模式下
- 快速采用高效算法
- 保持代码简洁
- 更专注于性能优化
- 提升更稳定、显著

## 最佳实践

### 1. 初始提示策略
```
1. 提供明确问题描述
2. 要求优化计划
3. 设定具体约束

示例:
Write Python code to solve this problem:
[问题描述]
Before writing the code, plan out all the necessary optimizations.
```

### 2. 迭代优化策略
```
1. 指出具体改进方向
2. 设置优化目标
3. 保持提示简洁

示例:
Your code is not fully optimized because [具体原因].
Improve it focusing on [具体方向].
```

## 注意事项

### 1. 提示词陷阱
- 过于模糊的提示会导致方向偏离
- 过度约束可能限制创新解决方案
- 缺乏具体目标可能引起过度工程化

### 2. 代码质量监控
- 每次迭代后检查代码正确性
- 警惕性能与可维护性的平衡
- 注意隐藏的bug和边缘情况

### 3. LLM局限性
- 可能生成看似合理但有细微错误的代码
- 在高性能优化时可能产生幻觉
- 需要人工验证关键逻辑

## 效果评估

### 1. 简单迭代效果
- 代码改进: 循序渐进
- 功能增加: 显著
- 性能提升: 不稳定
- 代码体积: 趋向增大

### 2. 工程化提示效果
- 代码改进: 快速明显
- 功能专注: 保持核心
- 性能提升: 显著稳定
- 代码体积: 保持精简

## 总结建议

1. **提示词策略**
   - 使用明确的优化目标
   - 包含具体的约束条件
   - 要求优化计划
   - 保持迭代反馈

2. **验证机制**
   - 每次迭代后验证代码
   - 检查性能提升
   - 评估代码质量
   - 确认核心功能

3. **工程化思维**
   - 平衡优化与可维护性
   - 保持代码简洁
   - 关注核心需求
   - 避免过度工程化
