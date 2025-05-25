---
title: cursor-workflow
jd_id: J00-20250525-0926
created: 2025-05-25 09:26
updated: 2025-05-25 09:26
type: note
status: draft
tags: []
---

# cursor-workflow(草稿)

## 工作流参考

### [cursor-memory-bank](https://github.com/vanzan01/cursor-memory-bank)

- Claude “Think” 工具方法论 值得参考
- 其他的都没看懂，也有可能是搞太复杂了，看起来是使用 AI 构建的

### [cursor-custom-agents-rules-generator](https://github.com/bmadcode/cursor-custom-agents-rules-generator)

我的评价只能说是接近于实战，面向初级，但是有一个 Cursor 的 VSCode 配置蛮有趣：可以隐藏 .mdc 文件的元数据，其他的就没什么了吧，迷茫的时候可以回来找一点自信吧。嗯。就这样

```json
"workbench.editorAssociations": {
  "*.mdc": "default"
}
```

## Cline Memory Bank

- 非常值得借鉴的上下文管理模式，其实也有工作流的影子？

### [Curskleosr](https://github.com/kleosr/cursorkleosr/tree/main)

- Cursor 社区中提出的 workflow 概念，很值得借鉴
- [社区地址](https://forum.cursor.com/t/guide-a-simpler-more-autonomous-ai-workflow-for-cursor-new-update/70688)

### [claude-task-master](https://github.com/eyaltoledano/claude-task-master)

- 非常复杂，且完善的 workflow 概念
- 需要慢慢啃了，大概是必须要会的吧

### [cursor-tools](https://github.com/eastlondoner/cursor-tools)

- 哇哦，里面提示词优化很棒工具，这不是我一直想要的么！！
- 还有仓库的读取
- 总之汇集了很多最佳实践

[graphiti](https://github.com/getzep/graphiti)
为 AI 代理构建实时知识图谱，需要了解么？


## 最简单的工作流

两步法：计划+执行

参考：[一个简明指南 放下包袱](https://read.highgrowthengineer.com/p/2025-guide-to-prompt-engineering?utm_source=%2Fbrowse%2Frecommendations&utm_medium=reader2)
[一切从简 提示词](https://beyondthebuildnewsletter.substack.com/p/ai-prompt-only-guide-for-smarter-results?utm_source=%2Fbrowse%2Frecommendations&utm_medium=reader2)