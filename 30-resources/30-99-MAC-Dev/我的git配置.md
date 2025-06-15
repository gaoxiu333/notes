## 工具

**commitizen**

```
brew install commitizen
brew install pre-commit
```

初始化

```bash
cz init # 全选了默认
```

## 全局忽略

```bash
# 查看配置
git config --global --get core.excludesfile

# 配置
git config --global core.excludesfile ~/.gitignore
```

## commit 规范

```bash
# 复制配置 自己电脑的根目录有相关的规范
cp ~/.pre-commit-config.yaml .pre-commit-config.yaml

# 复制cz配置
cp ~/.cz.json .cz.json

# 项目里执行 安装 commit 钩子
pre-commit install --hook-type commit-msg
```
