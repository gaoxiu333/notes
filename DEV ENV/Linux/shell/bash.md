“bash” 是 “Bourne Again SHell” 的首字母缩写， 所指的是这样一个事实，bash 是最初 Unix 上由 Steve Bourne 写成 shell 程序 sh 的增强版。

## 基础

	- 需要学习 `bash`，比`zsh`更加灵活，毕竟服务端通常内置了`bash`
	- 熟悉文本编辑器`Vim`
	- 学会使用帮助程序
		- `man tar` - 查看相关命令文档
		- `tar --help` - 获取命令帮助
		- `apropos tar` - 查找命令文档
		- `type tar` - 查看命令类型：来自shell内置还是别名
		- `info tar` - 用来替代man的新命令


### 启动终端

```bash
[me@linuxbox ~]$
```

以上命令构成：用户名@主机名(后缀$)
- `$` => 普通用户？
-  `#` => root 用户

### 简单的命令

```bash
date # 查看时间
cal # 当前月份日历
df # 磁盘剩余空间的数量
free # 空闲内存数量
exit # 结束终端
```

### 配置别名


### 文件系统

- pwd - 打印当前工作目录
- cd - 更改目录
	- `cd`
	- `cd -
	- `cd ~user_name`
- ls - 列出目录内容
	- `ls -a`
	- `ls -l` 
- file - 确定文件类型
- less - 浏览文件内容
- cp - 复制文件
- mv - 移动/重命名文件
- mkdir - 创建目录
- rm - 删除文件/目录
- ln - 创建硬链接和符号链接

[[第五章：操作文件和目录]]
> 记录了文件批量操作的通配符用法，有需要时可以查阅通配符部分


## 配置文件

扩展名 “.bak”，”.sav”， “.old”，和 “.orig” 都是用来指示备份文件的流行方法。
[mac 设置环境变量](https://www.lumin.tech/articles/env-variable/)

## 参考资料

-  [命令行的艺术](https://github.com/jlevy/the-art-of-command-line/blob/master/README-zh.md#%E5%91%BD%E4%BB%A4%E8%A1%8C%E7%9A%84%E8%89%BA%E6%9C%AF) - 我自学的宝典
- [bash 脚本教程](https://wangdoc.com/bash/startup)