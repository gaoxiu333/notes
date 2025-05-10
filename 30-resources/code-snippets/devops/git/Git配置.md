---
title: Git配置
created: 2024-04-22 12:27
updated: 2025-02-26 07:06
type: resource
status: active
schema: v1
tags: [source/notion, topic/devops/git, lang/shell]
---

# Git 配置

## 全局配置

```shell
git config --list --show-origin 
# 查看配置
git config --global user.name '你的名字'
git config --global user.email '你的邮箱'
```

## 配置 Github

### Github 生成密钥

SSH 密钥类型：

- [ED25519](https://docs.gitlab.com/ee/user/ssh.html#ed25519-ssh-keys)
- [ED25519_SK](https://docs.gitlab.com/ee/user/ssh.html#ed25519_sk-ssh-keys)
- [ECDSA_SK](https://docs.gitlab.com/ee/user/ssh.html#ecdsa_sk-ssh-keys)
- [RSA](https://docs.gitlab.com/ee/user/ssh.html#rsa-ssh-keys)

```shell
ssh-keygen -t ed25519 -C "your_email@example.com" # 生成密钥
```

### 将 SSH 密钥添加到 ssh-agent

```shell
eval "$(ssh-agent -s)"
```

添加 config

```shell
touch ~/.ssh/config # 生成配置文件
```

配置

```shell
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  HostName ssh.github.com
  User git
  Port 443 # 默认端口22不能走代理，需配置 443  IdentityFile ~/.ssh/id_ed25519
```

> Port 需要额外注意，初次配置经常连接不上 Github， 就是因为 Port 默认走的 22 端口

添加 ssh-agent

```shell
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
# 或者以下命令不区分操作系统ssh-add -K ~/.ssh/id_ed25519
```

### 复制 公钥

```shell
pbcopy < ~/.ssh/id_ed25519.pub
# 或者查看手动复制cat ~/.ssh/id_ed25519.pub
```

## 配置 Gitee

### 生成密钥

```shell
ssh-keygen -t ed25519 -f ~/.ssh/id_rsa.gitee -C "Gitee SSH Key"
```

- `t` key 类型
- `f` 文件名
- `C` 注释

配置

```
# gitee
Host gitee.com
    Port 22
    HostName gitee.com
    User git
    IdentityFile ~/.ssh/id_rsa.gitee
```

## 配置 gitlab

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_rsa.robo -C "Robo SSH Key"
ssh-keygen -t ed25519 -f ~/.ssh/id_rsa.xdf -C "xdf SSH Key"
```

配置

```bash
# gitlab
Host robo.space
    Port 22
    HostName gitlab-uat.robo.space
    User git
    IdentityFile ~/.ssh/id_rsa.robo
```

## 测试

```shell
ssh -T git@gitee.com
ssh -T git@github.com
```

## Git Credential Manager

[Git Credential Manager](https://github.com/git-ecosystem/git-credential-manager)(GCM) 是安全存储凭据并通过 HTTPS 连接到 GitHub 的另一种方法；

```
brew install --cask git-credential-manager
```

> 在mac上只需要安装就行了，不需要其他任何操作。

## Git flow

[Git flow](https://docs.github.com/en/get-started/using-github/github-flow)：轻量级的、基于分支的工作流程

参考链接：

[Github 生成新的密钥](https://docs.github.com/zh/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

## Git 切换远程仓库

```bash
git remote -v # 查看远程仓库
git remote set-url origin <new-repo-url>. # 更换远程仓库
```

## cheat sheet

- [github cheat sheet](https://github.github.com/training-kit/downloads/zh_CN/github-git-cheat-sheet/)
- https://www.zhoulujun.cn/html/tools/VCS/git/402.html

## 参考

[github 支持](https://support.github.com/)

[git-cheatsheet](https://gist.github.com/eashish93/3eca6a90fef1ea6e586b7ec211ff72a5?ref=dailydev) 