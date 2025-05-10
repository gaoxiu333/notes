# Mac setup

# **Mac setup**

## **系统偏好设置**

### **触控板**

**Apple 菜单 () > 关于本机 > 触控板**

- **光标与点按**
    - **单指轻点>开** - 轻点代替使劲点击触控板，很实用。
    - **查询与数据检测器>三指轻点** - 三根手指轻点，快预览或者查询启用单词查询

### **辅助功能**

**Apple 菜单 () > 关于本机 > 辅助功能**

- **指针控制>鼠标与触控板**
    - **触控板选项...>拖移样式>三指拖移** - 三指按住拖动窗口，有时候会比较方便
    - **连按速度>右边第三个**
    - **弹开载入速度>右边第三个**
- **键盘>键盘设置...**
    - **键重复速率>最最右边**
    - **重复前延迟>右边第二个**

### **安装软件**

**Apple 菜单 () > 关于本机 > 隐私与安全性**

- **安全性>允许从以下位置下载的应用程序>App Store和被认可的开发者** - 经常不在 App Store 下载软件，所以选择这一项

### **同步电脑配置**

TODO： - 代码都放在 `~/code/` - 编辑器、终端等配置文件使用`git`同步

## **开发环境配置**

### **Xcode**

Xcode 是 Mac OS 的集成开发环境，git、HomeBrew 等都依赖它，所以它优先安装。

```bash
xcode-select --install

```

### **HomeBrew**

HomeBrew 自称为 Mac OS 缺失的包管理器，安装和更新软件都很方便。 安装完 Xcode 之后安装 HomeBrew 来安装电脑上的其他软件。

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

> 安装之前最好查看一下brew 主页提供的最新安装命令。
> 

验证安装是否成功

```bash
brew doctor

```

### **iTerm2**

[iTerm2](http://www.iterm2.com/)是 Apple 终端的开源替代品。它具有高度可定制性，并具有许多有用的功能。

```bash
brew install --cask iterm2

```

### **定制化**

使用`Minimal`主题：**`⌘`**** + `,` >Appearance>General>Theme>Minimal** 字体：

- Source Code Pro Lite - `brew tap homebrew/cask-fonts && brew install --cask font-source-code-pro`

### **终端工具**

### **Oh My Zsh**

[Oh My Zsh](https://github.com/robbyrussell/oh-my-zsh)是一个开源的、社区驱动的框架，用于管理您的`zsh`配置。它具有一系列开箱即用的功能，可改善您的终端体验。

安装 Oh My Zsh

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

```

> 参考官网最新安装命令
> 

Zsh 主题

- Powerlevel10k - 据说提升 zsh 的响应速度，但是这个主题的效果对我来说并不是很满意。

### **其他**

- git
- fzf - 命令行模糊查找器
- tree - 递归目录列表目录，可生成生成深度缩进的文件列表
- ack - 代码搜索工具，grep 的替代品
- lsd - ls命令替代品
- fd - find 命令替代品
- rg - 文本搜索

### **node**

Node.js 是基于 Chrome 的 V8 JavaScript 引擎构建的 JavaScript 运行时。

node 有多个版本管理工具

- fnm - rust 写的 node 版本管理工具
- nvm - 比较流行的 node 版本管理工具
- asdf - asdf 是一个 CLI 工具，可以按项目管理多个语言运行时版本。它就像`gvm`、`nvm`、`rbenv`& `pyenv`（以及更多）合而为一！只需安装您的语言的插件即可！

推荐 fnm

```bash
brew install fnm

```

为了能使用 fnm use，需要配置环境变量

```bash
# .zshrceval "$(fnm env --use-on-cd)"

```

pnpm - 使用 corepack 安装 pnpm

```bash
corepack enable# 开启 pnpm、yarn
corepack disable# 关闭
```

### **python**

Mac 系统自带 python，安装在 `/usr/bin/python3`

pyenv 版本管理

```bash
brew install pyenv

```

配置环境变量

```bash
# .zshrcexport PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

```

### **docker**

TODO

## **软件**

### **浏览器**

- [Google Chrome Canary](https://wiki.nikiv.dev/web/browsers/google-chrome) - 它的[开发工具](https://wiki.nikiv.dev/web/browsers/google-chrome/chrome-dev-tools)非常出色
- [Safari 技术预览版](https://developer.apple.com/safari/technology-preview/) - 仅将其用于浏览[Twitter](https://wiki.nikiv.dev/tools/twitter)
- TODO
    - 浏览器 flags
    - Chrome 插件

安装插件/工具

```bash
brew install git

```

安装常用应用程序

- chrome 浏览器
- visual studio code
- 飞书
- 微信
- obsidian
- 腾讯柠檬？

```bash
brew install --cask google-chrome visual-studio-code feishu wechat obsidian tencent-lemon

```

### **RSS**

- NetNewsWire

## **其他软件**

- [Rust](https://www.rust-lang.org/tools/install) - 官方推荐使用`rustup`安装和管理rust。

## **问题**

- mac 上的换行符和 windows 上的换行符格式不一致导致 eslint 报错的问题该怎么解决？

## **参考**

[mac setup](https://github.com/sb2nov/mac-setup) [webstom 配置教程](https://github.com/judasn/IntelliJ-IDEA-Tutorial)