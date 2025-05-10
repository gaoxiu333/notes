# Git ignore

# Git ignore

创建一个全局的 `.gitignore` 文件

```bash
touch ~/.gitignore
```

忽略内容

```bash
# 文件夹视图文件.DS_StoreDesktop.ini# 缩略图缓存._*Thumbs.db# 可能出现在外部磁盘文件上.Spotlight-V100.Trashes# 编译的 python 文件*.pyc# 编译的 C++ 文件*.out# 特定的应用程序文件venvnode_modules.sass-cache
```

指定全局忽略文件

```bash
git config --global core.excludesfile ~/.gitignore
```

## 参考

- [macOS.gitignore](https://github.com/github/gitignore/blob/main/Global/macOS.gitignore)
- [gitignore.io](https://www.gitignore.io/)