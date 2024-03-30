Linux 中的 shell 是什么？Vim 又是什么？为什么高效？

## 基础

需要先了解 [[bash]]，善于通过命令行的帮助程序学习终端命令

### 帮助程序 tldr

tldr **-pages**项目是社区维护的命令行工具帮助页面的集合，旨在成为传统[手册页](https://en.wikipedia.org/wiki/Man_page)的更简单、更平易近人的补充。

- 主要是可以查看中文文档，如果 tldr 中有收录或者翻译的话
- 安装：参考 [how do i use it](https://github.com/tldr-pages/tldr#how-do-i-use-it)
- 配置 tldr 中文
```bash
echo $LANG # 查看当前终端语言
LANG=zh tldr tar # 指定 以中文 语言查看文档
alias tldr="tldr --color=true" # 配置别名
brew install tealdeer
```




### Linux 方向

- 运维
	- 服务器维护 - 提供一个可靠的服务器运行环境和技术支持
	- 比如：搭建开发环境、FTP、DNS、MYSQL 服务等配置
- 开发
	- Linux 应用开发？
- 底层
	- 对底层芯片的支持，适配芯片？



## 参考

#### 书

**The Linux Command Line 中文版**

> 算得上是介绍 Linux 命令行的最佳入门书。它不仅讲述 Linux 命令的用法，而且也包含如何编写 Shell 脚本的内容。如果你想寻求掌握 Linux 命令行的书籍，我推荐你阅读这一本。

**没有名字的书**

> 这本书来自于 GIt book，比较接近于常用和实战


-  [Linux工具快速教程](https://linuxtools-rst.readthedocs.io/zh_CN/latest/index.html#linux "永久链接至标题")
- [Arch linux Wiki](https://wiki.archlinuxcn.org/wiki/Arch_Linux)
- [中文版：Linux C/C++编程一站式学习](https://akaedu.github.io/book/)
-  [DEBIAN 管理员手册](https://debian-handbook.info/)
- [英文版 不知道是什么书](https://0xax.gitbooks.io/linux-insides/content/Booting/linux-bootstrap-1.html)
- **Linux从入门到精通**
- **鸟哥的Linux私房菜**
-  **Linux就该这么学**
- **Linux命令行与shell脚本编程大全**
- **Linux Shell脚本攻略**
- [The Linux Command Line](https://linuxcommand.org/tlcl.php)  [中文版](https://billie66.github.io/TLCL/book/index.html) [看云](https://www.kancloud.cn/thinkphp/linux-command-line/39431)
- [Linux开发入门需要具备哪些条件？](https://www.zhihu.com/question/22377953/answer/33382471)
- Redhat Linux用户基础 - 红帽
- [博客文章](https://hedzr.com/devops/linux/linux-man-command/)
- [man 文档](https://man7.org/linux/man-pages/man1/bash.1.html)

[合集](https://github.com/Jackpopc/CS-Books-Store#8-Linux)


[reddit 学习linux ](https://www.reddit.com/r/linux/comments/12dll1h/linux_command_line_cheat_sheet_all_the_commands/?rdt=54643&onetap_auto=true)
### 备忘录
https://www.stationx.net/linux-command-line-cheat-sheet/
[实用工具](https://chegva.com/2560.html)
