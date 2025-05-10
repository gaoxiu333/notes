## Vibe code flow

- `cursor` -> `idea` -> `plan` -> `code`
## 概念
- AI Code Assistants
- AI Code Companions
- GenAI Assistants
- MCP: [直观解释 MCP](https://x.com/akshay_pachaar/status/1900170356494917936)


## youtube
- [vibe code 最佳实践](https://www.youtube.com/watch?v=YWwS911iLhg)

## 提示词
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