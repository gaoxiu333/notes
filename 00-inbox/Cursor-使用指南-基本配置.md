---
title: Cursor-使用指南-基本配置
jd_id: J00-20250512-1032
created: 2025-05-12 10:32
updated: 2025-05-12 10:32
type: note
status: draft
tags: []
---

# 始终了解最新信息

通过以下关键词始终了解 Cursor 的最新的最佳实践和资源 Ï

> 获取 Cursor 更新和最佳实践的资源

# Cursor-使用指南-基本配置

# Cursor 基础指南

## 1. 安装与初始设置

### 工作区初始化

对于任何项目，打开项目文件夹后，Cursor 会自动开始索引项目文件以提供智能功能。

可以创建`.cursorignore`文件（与`.gitignore`格式相同）来排除不需要索引的文件夹，例如：

```
node_modules/
dist/
build/
.git/
```

## 2. 基本设置界面

Cursor 的大多数设置可以通过 UI 界面访问：

1. 打开设置:

   - Windows/Linux: File > Preferences > Settings
   - macOS: Code > Preferences > Settings

2. 在设置中搜索"cursor"查看 Cursor 特有的设置项

3. 常用设置包括：
   - 启用/禁用行内代码补全
   - 聊天面板位置和大小
   - 遥测和数据分享设置

## 3. 基本快捷键与工作流

### 核心快捷键

| 功能         | macOS                                      | Windows/Linux |
| ------------ | ------------------------------------------ | ------------- |
| 打开命令面板 | Cmd+Shift+P                                | Ctrl+Shift+P  |
| 打开 AI 聊天 | Cmd+K                                      | Ctrl+K        |
| 接受行内补全 | Tab                                        | Tab           |
| 搜索文件     | Cmd+P                                      | Ctrl+P        |
| 跳转到定义   | Cmd+Click                                  | Ctrl+Click    |
| 查找符号     | Cmd+T                                      | Ctrl+T        |
| 重新加载窗口 | 在命令面板中执行`Developer: Reload Window` |

### AI 功能快捷键

通过命令面板可以访问以下 AI 功能：

- 解释选中代码
- 生成文档注释
- 重构代码
- 生成单元测试
- 分析代码问题

## 4. 提高索引效率的实用技巧

1. **排除无关文件**:

   - 使用`.cursorignore`排除大型库目录、构建产物和二进制文件
   - 这可以显著减少索引时间并提高相关性

2. **工作区分割**:

   - 对于特别大的项目，考虑创建专注于特定模块的工作区
   - 这样可以提高 AI 理解代码上下文的能力

3. **重启索引**:
   - 如果遇到索引问题，可以尝试关闭并重新打开项目
   - 在极端情况下，退出 Cursor，删除`.cursor`隐藏文件夹，然后重新启动

## 5. 基本插件集成

Cursor 基于 VS Code 构建，兼容大多数 VS Code 插件：

1. **安装插件**:

   - 点击左侧边栏的扩展图标
   - 搜索所需插件并安装

## 6. 故障排除与常见问题

### 性能优化

如果应用运行缓慢：

1. 关闭不必要的插件
2. 确保项目中排除了大型文件夹的索引
3. 增加系统可用内存
4. 避免同时打开过多大文件

## 7. 数据与隐私

在设置中可以控制数据分享：

1. 禁用遥测数据收集
2. 调整代码分享设置
3. 管理云同步选项

## 8. 获取最新信息

获取 Cursor 更新和最佳实践的资源：

1. [Cursor 官方网站](https://cursor.sh)
2. [Cursor GitHub 仓库](https://github.com/getcursor/cursor)
3. [Cursor Twitter](https://twitter.com/cursordotdev)
4. Cursor 官方 Discord 社区

## 9. 非常有用但容易遗忘的设置

### 编辑器效率设置

在设置界面可以找到这些提升编码效率的选项：

1. **自动保存**:

   - 搜索"Auto Save"，可设置为"afterDelay"
   - 配合"Auto Save Delay"(默认 1000ms)使用
   - 消除手动保存的需要，提高编码流畅度

2. **制表符与缩进**:

   - "Editor: Tab Size" - 设置制表符宽度(通常为 2 或 4)
   - "Editor: Insert Spaces" - 使用空格而非 Tab 字符
   - "Editor: Detect Indentation" - 自动检测文件缩进方式

3. **行尾设置**:
   - "Files: Eol" - 选择行尾序列(LF 或 CRLF)
   - 在跨平台团队中尤为重要，防止 Git 显示大量换行符更改

### 性能优化选项

通过 UI 设置界面可以调整的性能相关选项：

1. **自动保存延迟**:

   - 如果设置过短可能导致频繁磁盘写入，增大值可减轻系统负担

2. **文件监视排除**:

   - "Files: Watcherexclude" - 添加不需要监视变更的文件模式
   - 默认已排除 node_modules，但可添加其他大型文件夹

3. **搜索排除**:
   - "Search: Exclude" - 定义全局搜索时要排除的文件模式
   - 排除大型生成文件可显著提高搜索速度

### Git 集成设置

Cursor 保留了 VS Code 的 Git 集成功能，以下设置非常有用：

1. **更改装饰**:

   - "Git: Decorations Enabled" - 在文件列表显示 Git 状态
   - 直观了解哪些文件有未提交更改

2. **自动获取**:

   - "Git: Autofetch" - 定期自动获取远程更改
   - 保持本地与远程状态同步的意识

3. **差异视图**:
   - "Diffeditor: Ignoretrimwhitespace" - 忽略空白差异
   - 使代码审查专注于实质内容变化

### 智能补全设置

微调代码补全行为：

1. **接受行为**:

   - "Editor: Accept Suggestion On Commit Character" - 是否在输入如逗号、分号时自动接受建议
   - 依个人习惯调整可显著提高编码流畅度

2. **建议触发**:

   - "Editor: Quick Suggestions" - 控制各种上下文中的补全触发
   - 可为注释、字符串和其他上下文单独配置

3. **片段优先级**:
   - "Editor: Snippet Suggestions" - 调整代码片段在建议列表中的优先级
   - 对经常使用代码模板的开发者很有用

### 语言特定设置

为不同语言优化编辑器行为：

1. **JavaScript/TypeScript**:

   - "Js/ts.implicitprojectconfig.checkjs" - 对 JS 文件启用类型检查
   - "Typescript.suggest.completefunctioncalls" - 自动添加函数调用的括号和参数

2. **HTML/CSS**:

   - "Html.format.wraplineLength" - 设置 HTML 格式化时的换行长度
   - "Css.lint.unknownAtRules" - 控制对未知 CSS 规则的警告

3. **Markdown**:
   - "Markdown.preview.breaks" - 在预览中如何处理换行
   - "Markdown.links.openLocation" - 控制点击链接的行为

### 终端集成设置

优化内置终端体验：

1. **默认终端**:

   - "Terminal > Integrated > Default Profile" - 设置默认终端程序
   - Windows 上可选择 PowerShell 或 WSL，Mac 上可选择 zsh 或 bash

2. **命令历史**:

   - "Terminal > Integrated > Enable Persistent Sessions" - 在工作区间保存命令历史
   - 重启编辑器后仍能访问之前的命令

3. **性能优化**:
   - "Terminal > Integrated > Gpu Acceleration" - 启用 GPU 加速提高渲染性能
   - "Terminal > Integrated > Scroll Back" - 控制终端保留的历史行数
