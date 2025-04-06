# Stop Digging

_2025-03-03_

Outside of very tactical situations, current models do not know how to stop digging when they get into trouble. Suppose that you want to implement feature X. You start working on it, but midway through you realize that it is annoying and difficult to do because you should do Y first. A human can know to abort and go implement Y first; an LLM will _keep digging_, dutifully trying to finish the original task it was assigned. In some sense, this is desirable, because you have a lot more control when the LLM does what is asked, rather than what it _thinks_ you actually want.

Usually, it is best to avoid getting into this situation in the first place. For example, it’s very popular to come up with a plan with a reasoning model to feed to the coding model. The planning phase can avoid asking the coding model to do something that is ill advised without further preparation. Second, agentic LLMs like Sonnet will proactively load files into its context, read them, and do planning based on what it sees. So the LLM might figure out something that it needs to do without you having to tell it.

Ideally, a model would be able to realize that “something bad” has happened, and ask the user for request. Because this takes precious context, it may be better for this detection to happen via a separate watchdog LLM instead.

## Examples

- After having made some changes that changed random numbers sampling on a Monte Carlo simulation, I asked Claude Code to fix all of the tests, some of which were snapshots on exact random sampling strategy. However, it turns out that the new implementation was nondeterministic at test time, so the tests would nondeterministically pass/fail depending on sampling. Claude Code was incapable of noticing that the tests were flipping between passing/failing, and after unsuccessfully trying to bash the tests into passing, started greatly relaxing the test conditions to account for nondeterminism, instead of proposing that we should refactor the simulation to sample deterministically.# LLM 应用成功标准 Cheatsheet

## 强标准的基本原则 SMART

### 具体 (Specific)
- ✅ 明确定义预期目标,如"情感分类准确率"
- ❌ 避免模糊表述,如"良好表现"

### 可衡量 (Measurable)
- 量化指标示例:
  - 任务相关: F1分数、BLEU分数、困惑度
  - 通用性: 准确率、精确率、召回率
  - 运营性: 响应时间(毫秒)、正常运行时间(%)

### 可达成 (Achievable)
- 基于以下因素设定目标:
  - 行业基准
  - 前期实验
  - AI研究进展
  - 专家知识

### 相关性 (Relevant)
- 与应用目的和用户需求对齐
- 考虑场景重要性(如医疗vs聊天应用)

## 常见评估维度

### 1. 任务准确性
- 基本任务表现
- 边缘案例处理能力
- 对罕见/挑战性输入的处理

### 2. 一致性 
- 相似输入的响应一致性
- 同一问题多次回答的语义相似度

### 3. 相关性与连贯性
- 对用户问题/指令的直接回应程度
- 信息呈现的逻辑性和可理解性

### 4. 语气与风格
- 输出风格与预期匹配度
- 语言对目标受众的适当性

### 5. 隐私保护
- 敏感信息处理
- 遵循信息使用限制

### 6. 上下文利用
- 对提供上下文的使用效果
- 历史信息的参考和延续能力

### 7. 延迟性能
- 响应时间要求
- 实时性需求满足度

### 8. 成本控制
- API调用成本
- 模型规模成本
- 使用频率成本

## 评估方法

### 量化评估
- A/B测试: 与基线模型或早期版本比较
- 用户反馈: 任务完成率等隐式指标
- 边缘案例分析: 错误处理百分比

### 定性评估
- Likert量表: 1-5分评分系统
- 专家评审: 基于定义标准的专业评估

## 示例: 情感分析项目成功标准

```
✅ 好的标准:
- F1分数 ≥ 0.85 (10k测试集)
- 99.5% 输出无毒性
- 90% 错误仅造成不便而非严重问题
- 95% 响应时间 < 200ms

❌ 差的标准:
"模型应该能很好地分类情感"
```

## 评估清单
- [ ] 是否设定具体目标?
- [ ] 是否有可衡量的指标?
- [ ] 目标是否切实可行?
- [ ] 是否与业务需求相关?
- [ ] 是否考虑多个评估维度?
- [ ] 是否定义了评估方法?
- [ ] 是否设置了基准比较?
