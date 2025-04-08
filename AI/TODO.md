- 从头提示词开始
- 到工具
- 到应用？
# Prompt Engineering Guide


AI 问卷调查
https://survey.devographics.com/zh-Hans

还有哪些 AI 问卷调查？

[GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents)


我总不能每一篇都复制，然后告诉AI
总结，写cheatsheet吧？
关于这个，有更好的提示词么
有更好的流程么？

## TODO
一个提示词导师，旨在引导用户思考如何一步一步写出提示词，一个完美的提示词需要思考什么，考虑哪些因素，让用户每次写提示词的时候知道该如何思考，而不是盲目的一步一步跟 AI 交互，避免变成“水多加面面对加水”的混乱局面

文档逻辑：
- System Prompt
-  **技术启发**：
-  ## 工程启示
-  推荐实践
-  ### 提示语句模板
-  ### 应用建议
-  

My workflow in Windsurf when trying out new stuff or creating POC. 

1. I ask for my AI assistant to create project folder named "testproject" with idea.md file and open that in Windsurf
2. Then in Windsurf I write my idea of application to idea.md
3. I tell Claude to read idea.md and make plan.md with step by step instructions to implementation and not to do anything else before I accept plan
4. Back and forth discussion about tech stack etc
5. When plan sounds good I tell Claude to go ahead and implement
6. I go make some coffee or vibecode with Cursor / Aider / Cline when Claude is working in Windsurf :)

For refactorization, I'm telling Claude to refactor this way:
First, refactor de file in the same file. Then test it.
Second: based on the refactorization, split the file in the same folder. Then test it
Third: move the files to the correct folders and update imports.
Test it.
This has saved me days of frustration to just a few minutes. Life changing.


## better prompts
比如 
我的温度调整始终为0，为了让AI可以在0的情况下有更多的自主权，保证提示词足够简洁，根据以下提示词技巧来优化提示词
如：...
也可以根据模型是否已经支持思维链来添加是否需要思维链技巧？

🎨**[直观解释 MCP](https://x.com/akshay_pachaar/status/1900170356494917936)** - 一图胜千言。
🚀 **[AI Native Dev](https://ainativedev.io/)** - Tessl.io 为开发人员构建 AI 应用程序的新中心

**[Vibe 编码教程和最佳实践（Cursor / Windsurf）](https://www.youtube.com/watch?v=YWwS911iLhg)** - Matthew Berman 为 vibe 编码开发人员分享他的编码堆栈和最佳实践。🧩

**[使用模型上下文协议构建代理 - Anthropic 的 Mahesh Murag](https://www.youtube.com/watch?v=kQmXtrmQ5Zg)** - 与 MCP 创建者进行深入问答，探讨协议如何统一 AI 系统和数据源。

https://generativeprogrammer.com/ 每周总结写的很好



## 提示词笔记
如何做呢，AI 发展的很快，提示词发展的也很快，也很庞杂
提示词可以分为日常使用和拓展（需要解决日常紧急且复杂的任务时）
另一个就是开发了，这一块可能需要很多技巧
那就先做一个日常的

另外需要添加一个每周阅读的版块（订阅吧）也不知道什么时候能把日常订阅摘录学习这一块搞定