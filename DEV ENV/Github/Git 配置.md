## 全局配置

```bash
git config --list --show-origin # 查看配置
git config --global user.name '你的名字'
git config --global user.email '你的邮箱'
```

## 配置 Github

### Github 生成密钥

```bash
ssh-keygen -t ed25519 -C "your_email@example.com" # 生成密钥
```

### 将 SSH 密钥添加到 ssh-agent

```bash
eval "$(ssh-agent -s)"
```

添加 config

```bash
touch ~/.ssh/config # 生成配置文件
```

配置

```bash
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  HostName ssh.github.com
  User git
  Port 443 # 默认端口22不能走代理，需配置 443
  IdentityFile ~/.ssh/id_ed25519
```

> Port 需要额外注意，初次配置经常连接不上 Github， 就是因为 Port 默认走的 22 端口

添加 ssh-agent

```bash
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
# 或者以下命令不区分操作系统
ssh-add -K ~/.ssh/id_ed25519
```

### 复制 公钥

```bash
pbcopy < ~/.ssh/id_ed25519.pub
# 或者查看手动复制
cat ~/.ssh/id_ed25519.pub
```

## 配置 Gitee

### 生成密钥

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_rsa.gitee -C "Gitee SSH Key"
```

- `-t` key 类型
- `-f` 文件名
- `-C` 注释

配置

```
# gitee
Host gitee.com
    Port 22
    HostName gitee.com
    User git
    IdentityFile ~/.ssh/id_rsa.gitee
```

## 测试

```bash
ssh -T git@gitee.com
ssh -T git@github.com
```





参考链接：

[Github 生成新的密钥](https://docs.github.com/zh/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
## cheat sheet

- [github  cheat sheet](https://github.github.com/training-kit/downloads/zh_CN/github-git-cheat-sheet/)
- [https://www.zhoulujun.cn/html/tools/VCS/git/402.html](https://www.zhoulujun.cn/html/tools/VCS/git/402.html)


## Q

本地仓库如何关联一个新的远程仓库？


## 参考

[github 支持](https://support.github.com/)





`