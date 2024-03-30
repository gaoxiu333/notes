快速、节省空间的包管理器

### 安装

- 使用[Corepack](https://nodejs.org/api/corepack.html)安装  `since 16.13`
- 使用 Npm 安装
- [独立安装](https://pnpm.io/zh/installation#%E4%BD%BF%E7%94%A8%E7%8B%AC%E7%AB%8B%E8%84%9A%E6%9C%AC%E5%AE%89%E8%A3%85)
- [CI 安装](https://pnpm.io/zh/continuous-integration)

```bash
# Corepack
corepack enable # 开启 pnmp & yarn ｜ 默认最稳定版本对应的预定义版本
corepack prepare pnpm@latest --activate # 指定最新版本

# npm
npm i -g pnpm
```

### 动态包执行

```bash
pnpm dlx # 相当于 npx
```

### 配置

pnpm 使用 [npm 的配置](https://docs.npmjs.com/misc/config) 格式，因此设置配置的方式与 npm 相同，使用的配置文件是同一个？？

```bash
pnpm config set **
```

### 过滤

过滤是什么？有什么作用，有哪些应用场景？

关于 npm 的详细配置文件，在 pnpm 官网有解释：[参考](https://pnpm.io/zh/package_json)
- package.json
- .npmrc
- pnpm-workspace.yaml
- .pnpmfile.cjs
- 
