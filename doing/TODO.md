- 从头提示词开始
- 到工具
- 到应用？

# Prompt Engineering Guide

## TODO

一个提示词导师，旨在引导用户思考如何一步一步写出提示词，一个完美的提示词需要思考什么，考虑哪些因素，让用户每次写提示词的时候知道该如何思考，而不是盲目的一步一步跟 AI 交互，避免变成“水多加面面对加水”的混乱局面

## 提示词的未来模版

```
- System Prompt
- 技术启发
- 工程启示
- 推荐实践
- 提示语句模板
- 应用建议
```

## Vibe code flow

- `cursor` -> `idea` -> `plan` -> `code`

## idea to plan

```
任务说明：
你当前的唯一任务是读取 `idea.md` 文件的内容，并基于其中的项目想法，生成一份名为 `plan.md` 的计划文件。

要求：
1. `plan.md` 应包含逐步的实现指令，每一步应简洁明了，便于执行；
2. 当前阶段禁止进行任何代码生成、文件修改或实现操作；
3. 除非我显式回复“确认计划，开始实现”，否则你不应进行任何超出 plan.md 的行为。

请回复你理解了上述规则，并提交 `plan.md` 的内容。
```

## better prompts


## 文章/工具｜ Spec Driven 规范驱动

- [AISpec](https://github.com/cbora/aispec?tab=readme-ov-file) - 一个新兴的提示词规范，有很多值得学习、借鉴参考的观点，初看时非常值得深入研究。
- [Carrot](https://github.com/talvinder/carrot-product-requirements-document-prd) - 一篇探讨 PRD 文档生成的提示词规范，作为储备吧

## 提示词设计理念

最开始只是有一个意图，但是这个意图是模糊的，直接告诉 AI，可以能会获得没有边界的结果
但是如果你告诉 AI 你想要的结果是什么，AI 就会在这个范围内进行思考
也可以通过你的意图引导 AI 生成更符合你意图的提示，再给 AI
比如：[SpecStory](https://specstory.com/) 这样的工具

## TODO

- 代码生成在 测试调试/审查
- 帮我构建一个 XXX 规范放在 xxx 位置
