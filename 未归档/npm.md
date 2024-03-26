## npx create

```bash
npx jest
pnpm exec jest
npx create-react-app my-app
pnpm dlx create-react-app my-app
```

## pnpm 清除缓存

```bash
pnpm store prune # 会清除所有缓存？
```

## corepack

- `node>14.19`

```bash
# 安装 pnpm
corepack enable pnpm@latest
# 或者
corepack install --global pnpm@latest

# 本地项目操作
corepack install pnpm@latest # 只在本地项目使用
corepack use pnpm@latest # 本地项目使用最新版pnpm安装依赖
corepack use yarn@1.x # 本地项目使用yarn 1.X 最新版本安装依赖
```

