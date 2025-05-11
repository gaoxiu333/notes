---
title: Monorepo与PNPM实践指南
created: {{date:YYYY-MM-DD HH:mm}}
updated: {{date:YYYY-MM-DD HH:mm}}
type: note
status: active
schema: v1
tags: [topic/backend/nodejs, topic/package-manager, topic/monorepo, topic/pnpm, topic/dev-environment]
---

# Monorepo与PNPM实践指南

## 1. Monorepo概念

Monorepo（单一代码仓库）是一种将多个相关项目放在同一个Git仓库中的开发策略，适用于管理多个功能相近且相互依赖的包或应用。

### 1.1 适用场景

- 当管理多个功能相近，又相互依赖的包时
- 需要跨多个包进行协同更改和调试
- 需要统一构建流程、代码规范和工作流

### 1.2 优缺点分析

**优点**：
- 统一的构建流程和工具链
- 简化的依赖管理
- 方便跨包调试和测试
- 原子提交和版本控制
- 代码共享和复用更简单
- 统一的CI/CD流程

**缺点**：
- 代码仓库体积变大
- 开发单个包时也需要下载整个项目依赖
- 权限控制较复杂
- 构建时间可能较长

## 2. PNPM工作空间实践

与Yarn或NPM工作空间相比，PNPM工作空间的主要优点是公共包不会提升到根目录，从而使所有工作空间包完全隔离，依赖管理更为严格。

### 2.1 环境准备

- 安装pnpm: `npm install -g pnpm`
- Node.js >=18（推荐）

### 2.2 项目初始化

```bash
# 创建项目目录
mkdir pnpm-monorepo
cd pnpm-monorepo

# 初始化项目
pnpm init
git init

# 配置.gitignore
echo -e 'node_modules\ndist' > .gitignore

# 配置Node版本和模块类型
npm pkg set engines.node='>=18'
npm pkg set type='module'

# 创建README
echo '# PNPM Monorepo' > README.md
```

### 2.3 工作空间配置

创建`pnpm-workspace.yaml`文件，定义工作空间结构：

```yaml
packages:
  - 'apps/*'    # 应用程序
  - 'packages/*' # 共享库/包
```

创建项目目录结构：

```bash
mkdir apps packages
```

### 2.4 初始化子项目

```bash
# 创建共享库
cd packages
pnpm create vite lib --template vanilla-ts

# 创建应用程序
cd ../apps
pnpm create vite web-app --template react-ts

# 回到根目录安装依赖
cd ..
pnpm install

# 添加便捷脚本
npm pkg set scripts.lib='pnpm --filter lib'
npm pkg set scripts.webapp='pnpm --filter web-app'
```

## 3. 配置包依赖关系

### 3.1 将共享库配置为库模式

Vite默认以应用模式构建，需要配置为库模式才能被其他项目引用。

1. 安装类型生成插件：

```bash
pnpm --filter lib add vite-plugin-dts -D
```

2. 配置Vite（lib/vite.config.ts）：

```typescript
import { defineConfig } from 'vite'
import { resolve } from 'path'
import dts from 'vite-plugin-dts'

export default defineConfig({
  build: { 
    lib: { 
      entry: resolve(__dirname, 'src/main.ts'), 
      formats: ['es'] 
    } 
  },
  resolve: { 
    alias: { src: resolve('src/') } 
  },
  plugins: [dts()],
})
```

3. 更新lib的package.json：

```json
{
  "main": "./dist/main.js",
  "types": "./dist/main.d.ts",
  "exports": {
    ".": {
      "import": "./dist/main.js",
      "types": "./dist/main.d.ts"
    }
  }
}
```

### 3.2 在应用中引用共享库

1. 更新web-app的package.json，添加工作空间依赖：

```json
{
  "dependencies": {
    "lib": "workspace:*",
    // 其他依赖...
  }
}
```

2. 重新安装依赖：

```bash
pnpm install
```

3. 构建lib包：

```bash
pnpm lib build
```

4. 在web-app中使用lib：

```tsx
import { counter } from 'lib'

function App() {
  const [count, setCount] = useState(0)
  
  return (
    <>
      <button onClick={() => setCount(counter(count, 1))}>
        count: {count}
      </button>
    </>
  )
}
```

## 4. 开发工作流优化

### 4.1 实时开发模式

在积极开发共享库的同时测试应用时，可以使用监视模式：

```bash
# 终端1：以监视模式构建lib
pnpm lib build --watch

# 终端2：启动应用
pnpm webapp dev
```

### 4.2 并行执行命令

使用`pnpm -r`命令在所有包中执行相同的命令：

```bash
# 在所有包中执行构建
pnpm -r run build

# 在所有包中执行测试
pnpm -r run test
```

### 4.3 过滤器语法

PNPM提供了强大的过滤器语法来执行特定包的命令：

```bash
# 执行单个包的命令
pnpm --filter <package-name> <command>

# 执行多个包的命令
pnpm --filter "{package-a,package-b}" <command>

# 执行某个包及其依赖的命令
pnpm --filter <package-name>... <command>

# 执行依赖某个包的所有包的命令
pnpm --filter "...<package-name>" <command>
```

## 5. 版本管理策略

### 5.1 统一版本

所有包使用相同的版本号，适合紧密耦合的项目：

```bash
# 使用Changesets或类似工具更新所有包版本
pnpm add -D @changesets/cli
pnpm changeset
pnpm changeset version
pnpm -r publish
```

### 5.2 独立版本

每个包独立管理版本号，适合相对独立的包：

```bash
# 单独更新和发布特定包
cd packages/my-package
pnpm version patch
pnpm publish
```

## 6. CI/CD配置

GitHub Actions配置示例：

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: pnpm/action-setup@v2
        with:
          version: 8
      - uses: actions/setup-node@v3
        with:
          node-version: 18
          cache: 'pnpm'
      - run: pnpm install
      - run: pnpm -r run build
      - run: pnpm -r run test
```

## 7. 常见问题与解决方案

### 7.1 依赖提升问题

**问题**：某些工具可能需要依赖位于根目录的node_modules中。
**解决方案**：使用pnpm的`pnpm.overrides`或`.npmrc`中的`public-hoist-pattern`。

### 7.2 构建顺序问题

**问题**：相互依赖的包需要按照正确的顺序构建。
**解决方案**：使用`pnpm -r --topo`进行拓扑排序的构建。

### 7.3 TypeScript路径解析

**问题**：TypeScript项目中引用工作空间包时的路径解析。
**解决方案**：配置tsconfig.json中的paths选项。

```json
{
  "compilerOptions": {
    "paths": {
      "lib": ["./node_modules/lib/dist/main"]
    }
  }
}
```

## 8. 最佳实践总结

1. **保持清晰的目录结构**：明确区分应用和库
2. **版本控制**：提交锁文件，确保依赖一致性
3. **明确依赖关系**：使用`workspace:*`语法声明工作空间依赖
4. **共享配置**：将通用配置放在根目录，减少重复
5. **脚本复用**：使用根目录的scripts简化操作
6. **构建优化**：利用增量构建和缓存提高性能

## 9. 参考资源

- [PNPM官方文档](https://pnpm.io/workspaces)
- [Vite库模式构建](https://cn.vitejs.dev/guide/build#library-mode)
- [Monorepo工具比较](https://monorepo.tools/)
- [Changesets版本管理](https://github.com/changesets/changesets)

## 相关链接

- [[Node版本与包管理]] - Node.js包管理器完整指南
- [[项目结构组织]] - 项目结构与组织最佳实践
- [[构建工具]] - 现代前端构建工具对比 