##  Mac终端常用命令



### 常用操作 

| 命令                               | 功能描述                     | 举例/备注          |
| ---------------------------------- | ---------------------------- | ------------------ |
| sudo                               | 获取root权限                 | sudo -s            |
| Car + D/exit                       | 退出root权限                 |                    |
| clear                              | 清楚屏幕或者窗口内容         |                    |
| ping                               | 给网络主机发送回应请求       | ping www.baidu.com |
| man                                | 查看命令说明                 | man ls             |
| which                              | 查看指定程序的路径           | which python       |
| history                            | 列出最近执行过的命令及编号   |                    |
| hostname                           | 电脑在网络中的名称           |                    |
| env                                | 显示当前所有设置过的环境变量 |                    |
| passwd                             | 修改用户密码                 |                    |
| date                               | 显示系统时间                 |                    |
| cal                                | 显示日历                     |                    |
| sudo periodic daily                | 每日清理系统                 |                    |
| sudo periodic weekly               | 每周清理系统                 |                    |
| sudo periodic monthly              | 每月清理系统                 |                    |
| sudo periodic daily weekly monthly | 以上三个都执行               |                    |



### 快捷键

- `Command + Shift + .`：显示隐藏文件
- `⌘ + Shift + Control + 4`：截图

### 目录和文件操作

| 命令名     | 功能描述                      | 举例或备注                       |
| ---------- | ----------------------------- | -------------------------------- |
| cd         | 进入指定文件夹路径            | cd ~/Desktop                     |
| pwd        | 显示当前的目录路径            | /Users/xz/Desktop                |
| ls         | 显示当前目录下的内容          |                                  |
| ls -la     | 显示当前目录下的详细内容      |                                  |
| ls -A      | 显示当前目录下的内容          | 含点 (`.`) 开头的文件            |
| mkdir      | 创建目录                      | mkdir dir_name                   |
| touch      | 创建指定格式的文件            | touch file.format                |
| mvdir      | 移动目录                      | mvdir dir1 dir2                  |
| mv         | 移动 / 重命名 — 文件 / 文件夹 | mv dir1 dir2MAC 没有重命名的命令 |
| rm         | 删除文件 或 **空**目录        |                                  |
| rm -rf dir | 删除一个 **非空** 目录        |                                  |
| rmdir      | 删除 **空** 目录              |                                  |
| cp         | 复制文件或目录                | cp file1 file2                   |
| file       | 显示文件类型                  | file file_name                   |
| find       | 使用匹配表达式查找文件        | find *.file_format               |
| open       | 使用默认的程序打开文件        | open file_name                   |
| cat        | 显示或连接文件内容            | cat file                         |
| ln         | 为文件创建联接                | ln -s file1 file2s 表示软联接    |
| head       | 显示文件的最初几行            | head -20 file_name               |
| tail       | 显示文件的最后几行            | tail -10 file_name               |
| paste      | 横向拼接文件内容              | paste file1 file2                |
| diff       | 比较并显示两个文件的内容差异  | diff file1 file2                 |
| wc         | 统计文件的字符数、词数和行数  | wc file_name                     |
| uniq       | 去掉文件中的重复行            | uniq file_name                   |
