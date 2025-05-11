---
created: {{date:YYYY-MM-DD HH:mm}}
tags: [vim, 编辑器, 工具, 学习笔记, 开发工具]
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
- `Ctrl+f` - 向下翻页
- `Ctrl+b` - 向上翻页
- `:{number}` - 跳转到指定行号

### 编辑命令

- `x` - 删除当前字符
- `dd` - 删除当前行
- `yy` - 复制当前行
- `p` - 粘贴在光标后
- `P` - 粘贴在光标前
- `u` - 撤销
- `Ctrl+r` - 重做
- `r{char}` - 替换当前字符
- `c{motion}` - 删除并进入插入模式
- `d{motion}` - 删除
- `y{motion}` - 复制

## 进阶技巧

### 文本对象

Vim的文本对象允许你操作语义单元:

- `w` - 单词
- `s` - 句子
- `p` - 段落
- `t` - HTML/XML标签
- `"`, `'`, `` ` `` - 引号内的文本
- `(`, `[`, `{` - 括号内的文本

组合方式：`{operation}{i/a}{text-object}`
- `i` - inner (不包含分隔符)
- `a` - around (包含分隔符)

例如：
- `diw` - 删除光标所在单词(不含周围空格)
- `ci"` - 删除双引号中的内容并进入插入模式
- `ya(` - 复制括号内的所有内容(包括括号)

### 宏录制

1. `q{register}` - 开始录制宏到指定寄存器
2. 执行你想录制的操作
3. `q` - 停止录制
4. `@{register}` - 执行宏
5. `@@` - 重复上次执行的宏

### 多文件操作

- `:e {filename}` - 编辑另一个文件
- `:ls` - 列出缓冲区
- `:b{number}` - 切换到指定缓冲区
- `:bn` - 下一个缓冲区
- `:bp` - 上一个缓冲区
- `:vs` - 垂直分割窗口
- `:sp` - 水平分割窗口
- `Ctrl+w` 然后 `h/j/k/l` - 在窗口间移动

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
set wildmenu        " 命令行自动补全
set ruler           " 显示光标位置
set cursorline      " 高亮当前行
set wrap            " 自动换行
set linebreak       " 不在单词内部换行
set clipboard=unnamed " 使用系统剪贴板

" 搜索设置
set hlsearch        " 高亮搜索结果
set incsearch       " 增量搜索
set ignorecase      " 搜索时忽略大小写
set smartcase       " 如果搜索模式包含大写字母，则区分大小写

" 编码设置
set encoding=utf-8  " 使用utf-8编码
set fileencoding=utf-8

" 键位映射
" 将jj映射为Esc
inoremap jj <Esc>
" 使用space作为leader键
let mapleader = " "
" 快速保存
nnoremap <leader>w :w<CR>
" 快速退出
nnoremap <leader>q :q<CR>
" 快速保存并退出
nnoremap <leader>wq :wq<CR>
" NERDTree切换
map <C-n> :NERDTreeToggle<CR>
```

## 插件系统

Vim拥有丰富的插件生态系统，可以通过插件管理器如Vim-Plug、Vundle或Pathogen进行管理。

### 常用插件推荐
- **NERDTree** - 文件树浏览器
- **fzf.vim** - 模糊查找
- **vim-surround** - 处理成对符号
- **vim-airline** - 状态栏美化
- **vim-fugitive** - Git集成
- **coc.nvim** - 智能补全
- **vim-commentary** - 注释代码
- **vim-multiple-cursors** - 多光标编辑

### 使用Vim-Plug安装插件

在`.vimrc`中添加:

```vim
" 安装Vim-Plug
call plug#begin('~/.vim/plugged')

" 插件列表
Plug 'scrooloose/nerdtree'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'tpope/vim-surround'
Plug 'vim-airline/vim-airline'
Plug 'tpope/vim-fugitive'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'tpope/vim-commentary'
Plug 'terryma/vim-multiple-cursors'

call plug#end()
```

然后在Vim中执行`:PlugInstall`安装插件。

## Neovim简介

Neovim是Vim的现代化分支，带来了更好的性能、更现代的代码库和更好的插件系统。大多数Vim插件和配置对Neovim也适用。

Neovim的配置文件位于`~/.config/nvim/init.vim`或使用lua配置`~/.config/nvim/init.lua`。

## 学习资源

- **vimtutor** - 内置教程，在终端中输入`vimtutor`启动
- **[Vim Adventures](https://vim-adventures.com/)** - 游戏化学习Vim
- **[Learn Vim For the Last Time](https://danielmiessler.com/study/vim/)** - 全面的教程
- **[Practical Vim](https://pragprog.com/titles/dnvim2/practical-vim-2nd-edition/)** - Drew Neil的书，深入讲解Vim技巧
- **[Vim Cheat Sheet](https://vim.rtorr.com/)** - 常用命令速查表

## 相关链接

- [[开发工具]] - 开发工具概览
- [[编辑器比较]] - 不同编辑器的对比
- [[VSCode与Vim集成]] - 如何在VSCode中使用Vim

## 待完善内容

- [ ] 添加个人配置文件示例
- [ ] 添加常见问题解决方案
- [ ] 添加更多高级技巧与示例 