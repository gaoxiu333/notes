---
title: Git快速指南
created: {{date:YYYY-MM-DD HH:mm}}
updated: {{date:YYYY-MM-DD HH:mm}}
type: note
status: active
schema: v1
tags: [topic/devops, topic/git, topic/version-control, action/reference]
---

# Git快速指南

## 基本配置

```bash
# 全局配置
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 项目特定配置
git config user.name "Your Name"
git config user.email "your.email@example.com"

# 查看配置
git config --list
```

## 基本工作流

```bash
# 初始化仓库
git init

# 克隆仓库
git clone <repository-url>

# 查看状态
git status

# 添加文件到暂存区
git add <file>       # 添加指定文件
git add .            # 添加所有修改

# 提交更改
git commit -m "提交信息"
git commit -am "提交信息"  # 合并add和commit

# 拉取远程更改
git pull

# 推送到远程
git push
git push -u origin <branch>  # 首次推送
```

## 分支操作

```bash
# 查看分支
git branch           # 本地分支
git branch -r        # 远程分支
git branch -a        # 所有分支

# 创建分支
git branch <branch-name>
git checkout -b <branch-name>  # 创建并切换

# 切换分支
git checkout <branch-name>
git switch <branch-name>  # Git 2.23+

# 合并分支
git merge <branch-name>

# 变基
git rebase <branch-name>

# 删除分支
git branch -d <branch-name>    # 安全删除
git branch -D <branch-name>    # 强制删除
```

## .gitignore

.gitignore文件用于指定Git应忽略的文件和目录。

```
# 文件类型
*.log
*.tmp
*.swp

# 特定文件
config.json
secrets.yml

# 目录
node_modules/
dist/
build/
.cache/

# 特例（不忽略）
!important.log
```

## Git子模块

Git子模块允许将一个Git仓库作为另一个Git仓库的子目录。

```bash
# 添加子模块
git submodule add <repository-url> <path>

# 初始化子模块
git submodule init
git submodule update

# 获取所有子模块
git submodule update --init --recursive

# 更新所有子模块
git submodule update --remote

# 克隆包含子模块的仓库
git clone --recursive <repository-url>
```

## 高级操作

### 历史查看

```bash
# 查看提交历史
git log
git log --oneline  # 简洁模式
git log --graph    # 图形化显示
git log -p <file>  # 查看文件的修改历史

# 查看文件修改
git diff           # 工作目录vs暂存区
git diff --staged  # 暂存区vs最近提交
git diff <commit1> <commit2>  # 比较两次提交
```

### 撤销修改

```bash
# 撤销工作目录修改
git checkout -- <file>
git restore <file>  # Git 2.23+

# 撤销暂存区修改
git reset HEAD <file>
git restore --staged <file>  # Git 2.23+

# 撤销提交
git revert <commit>  # 创建新提交来撤销
git reset --soft HEAD~1  # 撤销最后一次提交但保留更改
git reset --hard HEAD~1  # 撤销最后一次提交并丢弃更改
```

### 暂存修改

```bash
# 暂存当前工作
git stash
git stash save "工作描述"

# 查看暂存列表
git stash list

# 应用暂存
git stash apply    # 应用最近的暂存但不删除
git stash pop      # 应用最近的暂存并删除
git stash apply stash@{n}  # 应用特定暂存

# 删除暂存
git stash drop stash@{n}
git stash clear    # 删除所有暂存
```

## 常见工作场景

### 切换分支但保留修改
```bash
git stash
git checkout <other-branch>
git stash pop
```

### 创建和应用补丁
```bash
# 创建补丁
git diff > changes.patch

# 应用补丁
git apply changes.patch
```

### 查找引入Bug的提交
```bash
git bisect start
git bisect bad    # 当前版本有bug
git bisect good <known-good-commit>  # 指定一个好的版本
# Git会自动二分查找，每次告诉它good或bad
# 找到后
git bisect reset
```

## Git工作流模型

### GitFlow
- `master`: 生产环境代码
- `develop`: 开发环境代码
- `feature/*`: 功能分支
- `release/*`: 发布准备分支
- `hotfix/*`: 紧急修复分支

### GitHub Flow
- `main`: 主分支，始终可部署
- 从main创建功能分支
- 创建Pull Request讨论变更
- 合并到main并部署

## 相关链接

- [[Git配置]] - 详细的Git配置指南
- [[Git-ignore]] - .gitignore模板与技巧
- [[Git-Submodules]] - 子模块详解与最佳实践 