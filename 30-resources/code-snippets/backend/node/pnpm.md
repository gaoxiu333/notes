---
title: pnpm
created: 2024-04-22 11:45
updated: 2025-01-09 03:41
type: resource
status: active
schema: v1
tags: [source/notion, topic/backend/nodejs, topic/devops/package-manager, lang/javascript]
---

# pnpm

快速、节省空间的包管理器

### 安装

- 使用[Corepack](https://nodejs.org/api/corepack.html)安装 `since 16.13`
- 使用 npm 安装
- [独立安装](https://pnpm.io/zh/installation#%E4%BD%BF%E7%94%A8%E7%8B%AC%E7%AB%8B%E8%84%9A%E6%9C%AC%E5%AE%89%E8%A3%85)
- [CI 安装](https://pnpm.io/zh/continuous-integration)

```shell
# Corepack
corepack enable 
# 开启 pnmp & yarn ｜ 默认最稳定版本对应的预定义版本
corepack prepare pnpm@latest --activate
# 指定最新版本
corepack install pnpm@latest # node>21.x 安装# npm
npm i -g pnpm
```

### 执行命令

- `pnpx|pnpm dlx -> npx`
- `pnpm create|pnpm dlx -> npm exec`

```shell
pnpm dlx # 相当于 npx
```

### 配置

pnpm 使用 [npm 的配置](https://docs.npmjs.com/misc/config) 格式，因此设置配置的方式与 npm 相同，使用的配置文件是同一个？？

```shell
pnpm config set **
```

### 过滤

过滤是什么？有什么作用，有哪些应用场景？

关于 npm 的详细配置文件，在 pnpm 官网有解释：[参考](https://pnpm.io/zh/package_json)

- package.json
- .npmrc
- pnpm-workspace.yaml
- .pnpmfile.cjs

## 命令行补全

workspaces

- 在pnpm中只需要创建`pnpm-workspace.yaml`,添加

## workspaces

```
pnpm init
npm init -w ./packages/a # 初始化一个子工作空间
npm install abbrev -w a  # 给工作空间a添加依赖
# or
pnpm a add -D loadsh
```

### 子项目相互依赖

1. 更新使用着项目`package.json`

2. 被使用几的配置`main`等字段，指定入口文件，比如一个ts项目

### 配置

- 使用`package.json`中的`workspaces`字段
- `pnpm-workspace.yaml`文件

```json
// package.json 
"workspaces": [  
  "packages/l-react",  
  "packages/learn-react"
]

// pnpm-workspace.yaml
packages:  
  - 'apps/*'  
  - 'packages/*'
```

### 约束

```
npm pkg set type='mpdule' # ES6 模块
npm pkg set engines.node =">=21" # node版本 大于21
npm pkg set engines.pnpm=>'=3'
# or? 下面这个是corepack的
npm pkg set mangePackage='pnpm' # ..
```

TODO

https://dev.to/vinomanick/create-a-monorepo-using-pnpm-workspace-1ebn

```
这个命令和 npx eslint init 的区别
  pnpm create @eslint/config
```

## link

指定到全局，或者指定路径，指定路径太麻烦了，不是吗

```bash
cd ~/target/projecta
pnpm link --global
cd ~/your/projectb
pnpm link projecta

# 查看
pnpm list --global --depth 0
# 卸载
pnpm unlink <package-name> --global
# 试了一下 unlink 无效，最后使用的是 remove 卸载了
```

## file: 协议

```bash
{
  "dependencies": {
    "react": "file:../path-to-local/react",
    "react-dom": "file:../path-to-local/react-dom"
  }
}
``` 