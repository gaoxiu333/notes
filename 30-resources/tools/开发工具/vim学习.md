---
title: vim学习
created: 2024-07-22 10:30
updated: 2024-07-22 10:30
type: note
status: draft
schema: v1
tags: [topic/tools/vim, topic/dev-environment, action/research]
---

# Vim 学习笔记

## 基础模式
- 正常模式（Normal mode）：默认模式，用于导航和简单编辑
- 插入模式（Insert mode）：用于输入文本
- 命令模式（Command mode）：用于执行命令
- 可视模式（Visual mode）：用于选择文本块

## 基本命令

### 模式切换
- `i` - 进入插入模式
- `Esc` - 返回正常模式
- `:` - 进入命令模式
- `v` - 进入可视模式

### 导航命令
- `h`, `j`, `k`, `l` - 左、下、上、右移动光标
- `w` - 下一个单词开头
- `b` - 上一个单词开头
- `0` - 行首
- `$` - 行尾
- `gg` - 文件开头
- `G` - 文件结尾

### 编辑命令
- `dd` - 删除当前行
- `yy` - 复制当前行
- `p` - 粘贴
- `u` - 撤销
- `Ctrl+r` - 重做

### 保存与退出
- `:w` - 保存
- `:q` - 退出
- `:wq` 或 `:x` - 保存并退出
- `:q!` - 不保存强制退出

## 待扩展内容
- Vim插件系统
- 常用插件推荐
- 个人Vim配置示例
- Vim与IDE集成方案 