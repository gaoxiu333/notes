---
title: Node版本与包管理
created: 2024-07-22 13:00
updated: 2024-07-22 13:00
type: note
status: active
schema: v1
tags: [topic/backend/nodejs, topic/dev-environment, topic/package-manager]
---

# Node.js 版本与包管理

## Node.js 版本管理

Node.js的快速迭代使得不同项目可能需要不同版本的Node.js。版本管理工具可以帮助开发者在多个Node.js版本之间轻松切换。

### nvm (Node Version Manager)

nvm是最流行的Node.js版本管理工具之一，可在Unix/macOS系统上使用。

#### 安装

```bash
# macOS/Linux
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
# 或
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash

# Windows
# 使用nvm-windows: https://github.com/coreybutler/nvm-windows
```

#### 常用命令

```bash
# 列出所有可用的Node.js版本
nvm ls-remote

# 安装特定版本
nvm install 18.17.1

# 安装最新LTS版本
nvm install --lts

# 使用特定版本
nvm use 18.17.1

# 设置默认版本
nvm alias default 18.17.1

# 列出已安装的版本
nvm ls

# 运行特定版本的Node.js（不切换当前版本）
nvm exec 16.20.0 node app.js

# 查看当前使用的版本
nvm current
```

### fnm (Fast Node Manager)

fnm是一个更快的Node.js版本管理工具，使用Rust编写，速度比nvm快很多。

#### 安装

```bash
# macOS (使用Homebrew)
brew install fnm

# 使用curl (Linux/macOS)
curl -fsSL https://fnm.vercel.app/install | bash

# Windows (使用Scoop)
scoop install fnm
```

#### 常用命令

```bash
# 安装特定版本
fnm install 18.17.1

# 安装并使用最新LTS版本
fnm install --lts
fnm use lts-latest

# 使用特定版本
fnm use 18.17.1

# 设置默认版本
fnm default 18.17.1

# 列出已安装的版本
fnm list

# 查看当前使用的版本
fnm current
```

### 项目级Node.js版本配置

在项目根目录创建`.nvmrc`或`.node-version`文件，指定项目使用的Node.js版本，方便团队协作和CI/CD配置。

```bash
# 创建.nvmrc文件 (nvm和fnm都支持)
echo "18.17.1" > .nvmrc

# 进入项目目录后自动切换版本
# nvm
nvm use

# fnm
fnm use
```

## 包管理器

Node.js生态系统中有多种包管理器，每种都有其特点和适用场景。

### npm (Node Package Manager)

npm是Node.js默认的包管理器，随Node.js一起安装。

#### 基本命令

```bash
# 初始化项目
npm init -y

# 安装依赖
npm install [package]
npm i [package]

# 安装开发依赖
npm install --save-dev [package]
npm i -D [package]

# 全局安装
npm install -g [package]

# 运行脚本
npm run [script-name]

# 发布包
npm publish
```

#### npm配置

```bash
# 查看配置
npm config list

# 设置镜像源
npm config set registry https://registry.npmmirror.com

# 设置作用域镜像源
npm config set @myorg:registry https://registry.myorg.com
```

#### 常用npm镜像

| 名称 | 地址 | 说明 |
| --- | --- | --- |
| npm官方 | https://registry.npmjs.org | 默认源 |
| 淘宝镜像 | https://registry.npmmirror.com | 国内推荐 |
| GitHub | https://npm.pkg.github.com | GitHub包 |

### yarn

Yarn是Facebook推出的替代npm的包管理器，提供更快的安装速度和更好的依赖锁定。

#### 安装

```bash
# 使用npm全局安装
npm install -g yarn

# 使用corepack (Node.js 16.10+)
corepack enable
corepack prepare yarn@stable --activate
```

#### 基本命令

```bash
# 初始化项目
yarn init -y

# 安装所有依赖
yarn
yarn install

# 安装特定依赖
yarn add [package]

# 安装开发依赖
yarn add --dev [package]
yarn add -D [package]

# 全局安装
yarn global add [package]

# 运行脚本
yarn [script-name]

# 升级依赖
yarn upgrade [package]
```

#### yarn配置

```bash
# 查看配置
yarn config list

# 设置镜像源
yarn config set registry https://registry.npmmirror.com
```

### pnpm

pnpm是性能优秀的包管理器，通过硬链接共享依赖，大幅节省磁盘空间和安装时间。

#### 安装

```bash
# 使用npm全局安装
npm install -g pnpm

# 使用corepack (Node.js 16.10+)
corepack enable
corepack prepare pnpm@latest --activate
```

#### 基本命令

```bash
# 初始化项目
pnpm init

# 安装所有依赖
pnpm install

# 安装特定依赖
pnpm add [package]

# 安装开发依赖
pnpm add -D [package]

# 全局安装
pnpm add -g [package]

# 运行脚本
pnpm [script-name]

# 升级依赖
pnpm update [package]
```

#### pnpm配置

```bash
# 查看配置
pnpm config list

# 设置镜像源
pnpm config set registry https://registry.npmmirror.com
```

## Corepack

Corepack是Node.js官方提供的包管理器版本管理工具，用于确保项目使用指定版本的包管理器。

### 启用Corepack

```bash
# Node.js 16.10+已默认包含Corepack
corepack enable
```

### 配置项目包管理器

在`package.json`中指定包管理器版本：

```json
{
  "name": "my-project",
  "packageManager": "pnpm@8.6.2"
}
```

这样，使用不同包管理器或版本时会收到警告，确保团队使用一致的工具。

## Monorepo管理

Monorepo（单一代码仓库）是一种将多个相关项目放在同一个Git仓库中的开发策略。

### 包管理器对Monorepo的支持

#### npm Workspaces

npm从7.0开始支持工作区功能：

```json
// package.json
{
  "name": "my-monorepo",
  "workspaces": [
    "packages/*"
  ]
}
```

使用命令：

```bash
# 在根目录安装所有依赖
npm install

# 在特定工作区执行命令
npm run test --workspace=package-name

# 在所有工作区执行命令
npm run build --workspaces
```

#### yarn Workspaces

Yarn较早支持Workspaces功能：

```json
// package.json
{
  "name": "my-monorepo",
  "private": true,
  "workspaces": [
    "packages/*"
  ]
}
```

使用命令：

```bash
# 在根目录安装所有依赖
yarn install

# 在特定工作区执行命令
yarn workspace package-name test

# 在所有工作区执行命令
yarn workspaces run build
```

#### pnpm Workspaces

pnpm对Monorepo支持最完善：

```yaml
# pnpm-workspace.yaml
packages:
  - 'packages/*'
  - 'apps/*'
  - '!**/test/**'
```

使用命令：

```bash
# 在根目录安装所有依赖
pnpm install

# 在特定工作区执行命令
pnpm --filter package-name test

# 在所有工作区执行命令
pnpm -r run build

# 安装工作区A作为工作区B的依赖
pnpm --filter B add A
```

### 专用Monorepo工具

除了包管理器自带的Workspace功能外，还有专门的Monorepo管理工具：

- **Lerna**: 最早的Monorepo管理工具，现已与Nx集成
- **Nx**: 功能强大的构建系统和Monorepo管理工具
- **Turborepo**: Vercel开发的高性能构建系统
- **Rush**: Microsoft的企业级Monorepo管理方案

## 依赖管理最佳实践

### 锁文件

不同包管理器使用不同的锁文件格式：

- npm: `package-lock.json`
- yarn: `yarn.lock`
- pnpm: `pnpm-lock.yaml`

**重要提示**: 
- 锁文件应该提交到Git仓库
- 不要混用包管理器，以防锁文件冲突

### 版本控制策略

语义化版本（SemVer）规范：

- **主版本号(Major)**: 不兼容的API变更
- **次版本号(Minor)**: 向后兼容的功能新增
- **修订号(Patch)**: 向后兼容的问题修复

在`package.json`中指定依赖版本：

```json
{
  "dependencies": {
    "exact-version": "1.2.3",         // 精确版本
    "compatible-updates": "^1.2.3",   // 兼容更新 (1.x.x)
    "minor-updates": "~1.2.3",        // 次要更新 (1.2.x)
    "latest": "*"                     // 最新版本 (不推荐)
  }
}
```

### 审核与安全

定期审核依赖安全性：

```bash
# npm
npm audit
npm audit fix

# yarn
yarn audit
yarn audit fix

# pnpm
pnpm audit
pnpm audit fix
```

## 常见问题排查

### 依赖冲突解决

```bash
# npm
npm ls [package-name]
npm dedupe

# yarn
yarn why [package-name]
yarn dedupe

# pnpm
pnpm why [package-name]
pnpm dedupe
```

### 缓存清理

当遇到奇怪的安装问题时，清除缓存可能有帮助：

```bash
# npm
npm cache clean --force

# yarn
yarn cache clean

# pnpm
pnpm store prune
```

## 相关资源

- [nvm GitHub仓库](https://github.com/nvm-sh/nvm)
- [fnm GitHub仓库](https://github.com/Schniz/fnm)
- [npm官方文档](https://docs.npmjs.com/)
- [yarn官方文档](https://yarnpkg.com/)
- [pnpm官方文档](https://pnpm.io/)
- [Corepack文档](https://nodejs.org/api/corepack.html)
- [Monorepo工具比较](https://monorepo.tools/) 