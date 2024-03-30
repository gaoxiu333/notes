
### 添加子模块

```bash
# 在一个新项目中添加 子模块
git submodule add https://github.com/chaconinc/DbConnector
```
### 更新子模块

当拉取一个有子模块的仓库时，子模块文件夹是空的，需要执行两个命令来更新。
```bash
# 克隆仓库并更新所有子模块，包含嵌套的子模块
git clone --recurse-submodules 
# 如果忘记了后面的参数，执行以下命令
git submodule init # 初始化本地配置文件
git submodule update # 从该项目中抓取所有数据并检出父项目中列出的合适的提交
git submodule update --remote # 更新子模块为远程项目最新版本
# 更新子模块分支到远程
git config -f .gitmodules submodule.DbConnector.branch stable
```

### 参考链接
- [Git book # 7.11 Git 工具 - 子模块](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E5%AD%90%E6%A8%A1%E5%9D%97)
- [Git Submodules 介绍（通俗易懂，总结了工作完全够用的 submodule 命令）](https://cloud.tencent.com/developer/article/2136829) 