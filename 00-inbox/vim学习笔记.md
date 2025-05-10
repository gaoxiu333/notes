---
created: {{date:YYYY-MM-DD HH:mm}}
tags: [vim, 编辑器, 工具, 学习笔记]
aliases: [Vim编辑器, 文本编辑器]
---

# Vim 学习笔记

## 基础概念

Vim是一个高度可配置的文本编辑器，专为高效文本编辑而设计。它是Vi编辑器的改进版本。

### 模式系统

Vim的核心特性是它的模式系统:

- **普通模式(Normal Mode)**: 默认模式，用于导航和操作文本
- **插入模式(Insert Mode)**: 用于输入文本
- **可视模式(Visual Mode)**: 用于选择文本块
- **命令模式(Command Mode)**: 用于执行命令

## 基本操作

### 模式切换

- `i` - 进入插入模式
- `Esc` - 返回普通模式
- `v` - 进入可视模式
- `:` - 进入命令模式

### 导航命令

- `h`、`j`、`k`、`l` - 左、下、上、右移动光标
- `w` - 移动到下一个单词开头
- `b` - 移动到上一个单词开头
- `0` - 移动到行首
- `$` - 移动到行尾
- `gg` - 移动到文件开头
- `G` - 移动到文件末尾

### 编辑命令

- `x` - 删除当前字符
- `dd` - 删除当前行
- `yy` - 复制当前行
- `p` - 粘贴
- `u` - 撤销
- `Ctrl+r` - 重做

## 进阶技巧

### 文本对象

Vim的文本对象允许你操作语义单元:

- `w` - 单词
- `s` - 句子
- `p` - 段落
- `t` - HTML/XML标签
- `"`, `'`, `` ` `` - 引号内的文本
- `(`, `[`, `{` - 括号内的文本

### 组合命令

Vim命令可以组合使用:

- `d3w` - 删除3个单词
- `ci"` - 改变双引号内的内容
- `ya{` - 复制大括号内所有内容(包括大括号)

## Vim配置

基本配置可以通过`.vimrc`文件进行:

```vim
" 基础设置
set number          " 显示行号
set relativenumber  " 显示相对行号
set tabstop=4       " Tab宽度为4个空格
set shiftwidth=4    " 缩进宽度为4个空格
set expandtab       " 将Tab转换为空格
set autoindent      " 自动缩进
set smartindent     " 智能缩进

" 搜索设置
set hlsearch        " 高亮搜索结果
set incsearch       " 增量搜索

" 键位映射
map <C-n> :NERDTreeToggle<CR>
```

## 插件系统

Vim拥有丰富的插件生态系统，可以通过插件管理器如Vim-Plug、Vundle或Pathogen进行管理。

常用插件推荐:
- NERDTree (文件树浏览器)
- fzf.vim (模糊查找)
- vim-surround (处理成对符号)
- vim-airline (状态栏美化)

## 学习资源

- vimtutor - 内置教程，在终端中输入`vimtutor`启动
- [Vim Adventures](https://vim-adventures.com/) - 游戏化学习Vim
- [Learn Vim For the Last Time](https://danielmiessler.com/study/vim/) - 全面的教程

## 待完善内容

- [ ] 添加更多实用插件推荐
- [ ] 添加个人配置文件示例
- [ ] 添加常见问题解决方案 