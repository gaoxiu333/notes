---
title: Mac使用备忘录
jd_id: J30.05.0001
created: 2025-05-11 11:10
updated: 2025-05-11 13:01
type: note
status: active
tags: [topic/tools/mac, topic/development/setup]
---

# Mac使用备忘录

## 概述

本文档收集了macOS系统的常用软件、配置和开发环境设置，作为日常使用和开发环境搭建的参考指南。

## 常用软件推荐

### 效率工具

- (⭐) [RayCast](https://www.raycast.com/) - Spotlight和Alfred的替代品，内置剪贴板管理器、窗口管理器、文件搜索和大量社区插件
- (⭐) [Velja](https://sindresorhus.com/velja) - 浏览器链接管理器，可以选择用哪个浏览器打开链接
- (⭐) [Bartender4](https://www.macbartender.com/) - 菜单栏图标管理器
- [Cron](https://cron.com/) - 现代macOS日历，比系统自带日历更强大
- [BeFocused](https://apps.apple.com/us/app/be-focused-focus-timer/id973134470?mt=12) - 番茄工作法计时器
- [CleanMyMac](https://cleanmymac.com/) - macOS系统清理和维护工具

### 开发工具

- [Warp](https://www.warp.dev/) - 现代、基于Rust的终端
- [iTerm2](https://github.com/gnachman/iTerm2) - 增强版终端
- [Tabby](https://github.com/Eugeny/tabby) - 跨平台终端
- [VSCode](https://code.visualstudio.com/) - 代码编辑器
- [Cursor](https://www.cursor.com/) - 基于VS Code的AI助手编辑器
- [zsh](https://github.com/zsh-users/zsh) + [Oh My Zsh](https://ohmyz.sh/) - 终端框架

### 设计与多媒体

- [Figma](https://figma.com/) - 设计工具，创建UI设计、流程图等
- [OBS Studio](https://obsproject.com/) - 录制产品演示和直播
- [Kap](https://getkap.co/) - 轻量级屏幕录制工具
- [PixelSnap](https://getpixelsnap.com/) - 测量屏幕元素间距离
- [VLC](https://www.videolan.org/) - 开源视频播放器，支持几乎所有格式

### 生产力与组织

- [Notion](https://www.notion.so/) - 笔记、文档和项目管理
- [1Password](https://1password.com/) - 密码管理器
- [Endel](https://endel.io/) - 专注状态音景应用程序
- [RunCat](https://apps.apple.com/us/app/runcat/id1429033973?mt=12) - 显示CPU使用情况的菜单栏工具
- [Relax](https://www.dangercove.com/relax/) - 断开耳机或睡眠时自动静音扬声器

## VS Code 配置

### 常用插件分类

#### HTML/CSS/前端

- [Auto Close Tag](https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-close-tag) - 自动闭合HTML标签
- [Auto Rename Tag](https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag) - 自动重命名配对的HTML标签
- [Color Highlight](https://marketplace.visualstudio.com/items?itemName=naumovs.color-highlight) - 高亮显示颜色代码
- [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) - Tailwind自动补全和排序
- [Import Cost](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost) - 显示导入包的大小

#### 代码质量与协作

- [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) - Git增强工具
- [EditorConfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig) - 团队代码风格统一
- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) - 代码格式化
- [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) - 代码检查
- [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens) - 增强错误显示

#### 框架支持

- Vue: [Volar](https://marketplace.visualstudio.com/items?itemName=johnsoncodehk.volar), [Vue VSCode Snippets](https://marketplace.visualstudio.com/items?itemName=sdras.vue-vscode-snippets)
- React: [ES7+ React/Redux/React-Native-snippets](https://marketplace.visualstudio.com/items?itemName=dsznajder.es7-react-js-snippets), [Auto Import](https://marketplace.visualstudio.com/items?itemName=steoates.autoimport)

#### Markdown

- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) - Markdown编辑增强
- [Markdown Table Formatter](https://marketplace.visualstudio.com/items?itemName=fcrespo82.markdown-table-formatter) - 表格格式化
- [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) - Markdown语法检查

#### 美化与体验

- [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme) - 文件图标主题
- [Dracula Official](https://marketplace.visualstudio.com/items?itemName=dracula-theme.theme-dracula) - 深色主题
- [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments) - 增强注释显示
- [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree) - 管理TODO注释
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) - 代码拼写检查

#### 其他实用工具

- [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) - 接口测试
- [Project Manager](https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager) - 项目管理
- [DotENV](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv) - 环境变量文件支持
- [Path Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense) - 路径自动完成
- [Comment Translate](https://marketplace.visualstudio.com/items?itemName=intellsmi.comment-translate) - 注释翻译
- [Polacode](https://marketplace.visualstudio.com/items?itemName=pnp.polacode) - 代码截图

## Mac常用操作

### Hosts文件修改

1. 打开终端
2. 输入命令：`sudo nano /etc/hosts`
3. 输入密码
4. 编辑hosts文件
5. 按Ctrl+O保存，Ctrl+X退出
6. 刷新DNS：`sudo killall -HUP mDNSResponder`

### 系统设置优化

- 触控板设置
  - 启用三指拖移：系统设置 > 辅助功能 > 指针控制 > 触控板选项
  - 增加跟踪速度：系统设置 > 触控板
  
- Finder设置
  - 显示所有文件扩展名：Finder > 设置 > 高级
  - 显示隐藏文件：`Command + Shift + .`

## 待办事项

- [ ] 完善Mac初始化设置脚本
- [ ] 添加常用软件安装脚本
- [ ] 整理VS Code设置同步方案
- [ ] 补充终端配置和自定义命令 