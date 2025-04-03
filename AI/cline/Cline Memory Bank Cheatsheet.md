
## 快速设置

1. 安装或打开Cline
2. 复制Custom Instructions（从文档中的代码块）
3. 粘贴到Cline - 添加为custom instructions或.clinerules文件
4. 初始化 - 要求Cline "initialize memory bank"

## 核心文件结构

```
memory-bank/
├── projectbrief.md     # 项目基础文档
├── productContext.md   # 产品上下文
├── systemPatterns.md   # 系统架构与模式
├── techContext.md      # 技术上下文
├── activeContext.md    # 当前工作焦点
└── progress.md         # 进度与状态
```

## 关键命令

- `"follow your custom instructions"` - 让Cline读取Memory Bank文件并继续工作（开始任务时使用）
- `"initialize memory bank"` - 开始新项目时使用
- `"update memory bank"` - 触发完整的文档审查和更新

## 核心工作流

### 计划模式 (Plan Mode)

- 用于策略讨论和高层次规划
- 读取Memory Bank → 验证上下文 → 制定策略 → 提出方法

### 执行模式 (Act Mode)

- 用于实施和执行特定任务
- 检查Memory Bank → 更新文档 → 执行任务 → 记录变更

## 文件用途

|文件|用途|更新频率|
|---|---|---|
|projectbrief.md|项目基础、需求和目标|低|
|productContext.md|项目存在的原因、解决的问题|低|
|activeContext.md|当前工作焦点、最近更改|高|
|systemPatterns.md|系统架构、技术决策、设计模式|中|
|techContext.md|使用的技术、开发环境、技术约束|中|
|progress.md|已完成工作、待做事项、当前状态|高|

## 最佳实践

- 用简单的项目简介开始，让结构随时间演变
- 让文档更新自然发生，不要强制更新
- 每次会话开始时确认上下文
- 在实现重大更改后更新Memory Bank
- 内容窗口接近填满时更新Memory Bank并开始新会话

## 提示

- Memory Bank文件是存储在项目中的普通markdown文件
- 可以全局应用（Custom Instructions）或项目特定（.clinerules）
- 可以创建额外文件来组织复杂功能、API文档、测试策略等
- 这种方法也适用于非编程项目

```

## 注意事项
- Cline在会话之间完全重置内存，Memory Bank是唯一的知识连接
- 精确维护文档对Cline的有效性至关重要
- 定期使用"update memory bank"命令确保所有上下文都被保存
```