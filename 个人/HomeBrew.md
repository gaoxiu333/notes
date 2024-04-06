##  brew 和 brew cask 的区别？

HomeBrew-Cask 拓展了 HomeBrew，允许通过命令行工具安装大型二进制文件，例如 Goole Chrome等应用程序；简单的理解，brew 安装的没有GUI界面的软件，而 brew cask 安装的软件都有 GUI 界面。

## 更新 brew

在执行 brew 任何操作之前先更新一下brew，以保证brew安装或者更新的软件为最新版本

```bash
brew update
```

## 基本使用

### 安装软件

安装软件之前先搜索一下，brew 是否支持

```bash
brew search <package>
```

查看软件的信息

```bash
brew info <package>
```

安装

```bash
brew install <package>
```

卸载

```bash
brew uninstall <package>
```

### 查看软件

查看已经安装的包

```bash
# 查看本地安装的所有包和应用程序
brew list
# 包括版本
brew list --versions 
# 只查看应用程序
brew casks
# 查看所有安装的包（排除依赖）
brew leaves

```

查看是否有软件需要更新

```bash
brew outdated
```

更新软件

```bash
brew upgrade <package> # 更新某个软件
brew upgrade # 更新所有软件
```

HomeBrew 会保留旧的安装包，如果你想清理，执行下面命令

```bash
brew cleanup --dry-up # 查看 cleanup 将删除那些软件包，但不实际删除
brew cleanup # 删除
```

## 使用 brew 启动服务

```bash


```