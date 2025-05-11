---
title: MAC-使用备忘录
jd_id: J00-20250511-1110
created: 2025-05-11 11:10
updated: 2025-05-11 11:10
type: note
status: draft
tags: []
---

# MAC-使用备忘录

## 概述

简要描述本笔记的主要内容和目的。

## 内容

正文内容...

## 链接与参考

- [[相关笔记]]
- [[相关概念]]

## 待办事项

- Mac 修改Hosts 备忘录
- Mac setup 备忘录

## MAC 软件

- [Warp](https://www.warp.dev/) - 现代、基于 Rust 的终端；
- [OBS Studio](https://obsproject.com/) - 录制产品演示和互动视频；
- [Kap](https://getkap.co/) - 快速录制我的屏幕；

现在，让我们谈谈我每天使用的让我的生活更轻松的软件。

- (⭐) [Velja](https://sindresorhus.com/velja) - Velja 是 macOS 浏览器的“看门人”。简而言之，您将其设置为“默认”浏览器，当您单击链接时，将出现一个包含您已安装的所有浏览器的弹出窗口，以便您可以选择要打开的浏览器。
- (⭐) [RayCast](https://www.raycast.com/) - Spotlight 和 Alfred 的 macOS 替代品。这是迄今为止我最喜欢的软件。它有一个内置的剪贴板管理器、窗口管理器、聊天 GPT、文件搜索（比原生 macOS 搜索更好）和大量社区插件；
- Google Chrome - 作为后备浏览器
- [CleanMyMac](https://cleanmymac.com/) - macOS 问题修复程序。我用它来做一些高清清理、更新或卸载软件等；
- [Cron](https://cron.com/) - 现代 macOS 日历。比苹果自带的日历好很多；
- [Endel](https://endel.io/) - 帮助集中注意力的音景应用程序；
- 
- [zsh](https://github.com/zsh-users/zsh) + [“哦我的 ZSH！”](https://ohmyz.sh/) - 终端框架；
- [VSCode](https://code.visualstudio.com/) - 文本/代码编辑器
- [观念](https://www.notion.so/)——做笔记、写草稿、以及个人的整体组织；
- [Figma](https://figma.com/) - 创建设计、随机流程、Instagram 帖子等。
- (⭐) [1Password](https://1password.com/) - 密码管理器；
- [VLC](https://www.videolan.org/) - 用于观看视频的开源播放器。它支持所有可能的扩展；
- (⭐) [Bartender4](https://www.macbartender.com/) - 菜单栏图标管理器；
- [RunCat](https://apps.apple.com/us/app/runcat/id1429033973?mt=12) - 很好地显示 CPU 使用情况；
- [BeFocused](https://apps.apple.com/us/app/be-focused-focus-timer/id973134470?mt=12) - 计时器进行[番茄工作法](https://en.wikipedia.org/wiki/Pomodoro_Technique)；
- [PixelSnap](https://getpixelsnap.com/) - 测量屏幕中元素之间的距离。对于像素完美的实现很有用；
- [Relax](https://www.dangercove.com/relax/) - 当您断开耳机或在笔记本电脑上睡觉时，该应用程序会将扬声器静音。对于您打开笔记本电脑并开始大声播放某些内容的情况很有帮助

## 终端(terminal)

- https://github.com/Eugeny/tabby
- https://github.com/gnachman/iTerm2

## 编辑器

- - https://www.cursor.com/ - 基于 VS Code 的 AI 助手编辑器

VS Code Setup

## 资料：

- 下载：[Visual Studio Code](https://code.visualstudio.com/Download)
- 查看文档：[VSCode 操作文档](https://code.visualstudio.com/docs)

## 制作自己的拓展包

https://code.visualstudio.com/blogs/2017/03/07/extension-pack-roundup

```bash
6TW7lRvAT9KLuDRhXWzgChU4SUZqOC4uqR5t32A1V106vX5B8AxHJQQJ99ALACAAAAAAAAAAAAASAZDOOvJO
```

- **gx-web**

**HTML**

- [Auto Close Tag](https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-close-tag)：快速完成 HTML 标签的闭合。
- [Auto Rename Tag](https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag)：修改标签，会同步修改闭合标签。
- [颜色突出显示](https://marketplace.visualstudio.com/items?itemName=naumovs.color-highlight)：用颜色突出显示 hex/rgb/rgba/hsl 代码
- [**Tailwind CSS IntelliSense**](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) - Tailwind 自动补全（[通过 Prettier 自动排序](https://tailwindcss.com/blog/automatic-class-sorting-with-prettier#how-classes-are-sorted)）

**多人协作**

- [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)  - 多人协作，git 增强工具
- [EditorConfig for VSCode](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)：添加协作规范
- [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)：格式化代码
- [VSCode ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)：代码检查

**Markdown**

- [Markdown 一体化](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) - 提供 Markdown 编辑功能，包括预览、快捷方式和自动格式化。
- [Markdown Table Formatter](https://marketplace.visualstudio.com/items?itemName=fcrespo82.markdown-table-formatter) - 仅格式化
- [**markdownlint](https://www.notion.so/VS-Code-Setup-15f2048329b080f49144f45bdc39504a?pvs=21) -** Markdown 语法检查

**美化**

- [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme) - 左侧文件的图标
- [Dracula Official](https://marketplace.visualstudio.com/items?itemName=dracula-theme.theme-dracula) - VSCode 主题

**其他**

- [Chinese (Simplified)](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans)：中文补丁
- [DotENV](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv) - 高亮`.env`环境变量配置文件
- [JavaScript (ES6) code snippets](https://marketplace.visualstudio.com/items?itemName=xabikos.JavaScriptSnippets) - ES6 语法代码片段
- [Comment Translate](https://marketplace.visualstudio.com/items?itemName=intellsmi.comment-translate) - 对注释进行 Google 翻译
- [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens) - 体验更好的内连错误
- [Project Dashboard](https://marketplace.visualstudio.com/items?itemName=kruemelkatze.vscode-dashboard) - 快速浏览所有项
- [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments) - 通过使用警报、信息、待办事项等进行注释来改进您的代码注释！
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) - 源代码的英文拼写检查器。避免拼写错误的效果非常好
- [专案经理](https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager) - 轻松在项目之间切换。
- [待办事项树](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree)：以树视图形式显示代码中的 TODO 注释。
- [REST 客户端](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)：允许您直接在 VS Code 中发送 HTTP 请求并查看响应。
- [~~括号对着色器 2](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2)：用相同的颜色突出显示匹配的括号。~~
- [路径智能感知](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense) ：自动完成项目中的文件名。

## Vue 插件

- [Volar](https://marketplace.visualstudio.com/items?itemName=johnsoncodehk.volar)：Vue 官方推荐的 VSCode 扩展，用以代替 Vue 2 时代的 [Vetur](https://marketplace.visualstudio.com/items?itemName=octref.vetur) 。
- [Vue VSCode Snippets](https://marketplace.visualstudio.com/items?itemName=sdras.vue-vscode-snippets)：Vue 代码片段的生成，比如：`ts`快速生成Vue代码片段

## React

- [**ES7+ React/Redux/React-Native-snippets，**](https://marketplace.visualstudio.com/items?itemName=dsznajder.es7-react-js-snippets)快速轻松访问重复的 React 代码
- [**自动导入**](https://marketplace.visualstudio.com/items?itemName=steoates.autoimport)自动查找、解析并为所有可用导入提供代码操作和代码完成。适用于 Typescript 和 TSX。
- [Prisma](https://marketplace.visualstudio.com/items?itemName=Prisma.prisma)

## nodejs

- [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) - 在 VSCode 中调试接口

## Docer

- [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) - 管理 Docker 容器

## 前端插件推荐

1. [Duplicate selection or line](https://marketplace.visualstudio.com/items?itemName=geeebe.duplicate) - 复制粘贴
2. [Import Cost](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost) - 检测包的大小
3. [Bracket Select](https://marketplace.visualstudio.com/items?itemName=chunsen.bracket-select) - 在括号之前快速选择代码
- Front-End Extension Gold Pack - 前端插件合集

## Python

- autoDocstring - Python 文档字符串生成器链接：

## 其他

- [Polacode](https://marketplace.visualstudio.com/items?itemName=pnp.polacode) - 代码截图
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)

## TODO

Debug: https://code.visualstudio.com/docs/nodejs/reactjs-tutorial