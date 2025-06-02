---
title: Frontend Style Guide
jd_id: J10-20250602-1916
created: 2025-06-02 19:16
updated: 2025-06-02 19:16
type: guide
status: draft
tags: [topic/frontend, topic/react, topic/style-guide, action/todo]
---

# Frontend Style Guide

前端项目代码风格和架构指南，确保代码的一致性、可维护性和可扩展性。

## 1. 文件夹结构

### 核心原则

**模块化**: 代码主要组织在 `src` 文件夹下，并按功能模块（features）进行划分，以实现高内聚和低耦合。

**功能文件夹结构**: 每个功能模块（feature）可以包含 `api`, `assets`, `components`, `hooks`, `stores`, `types`, `utils` 等子文件夹，按需创建。

**禁止跨功能导入**: 不建议在不同功能模块之间直接导入，应在应用层面组合功能。

**单向代码库架构**: 代码流向应为单向：共享模块 → 功能模块 → 应用层

### 目录结构示例

```
src/
├── app/              # 应用程序层（路由入口）
├── assets/           # 全局静态资源
├── components/       # 全局共享组件
├── config/          # 全局配置
├── features/        # 特性模块（核心）
│   └── awesome-feature/
│       ├── api/     # 功能相关API
│       ├── components/ # 功能组件
│       ├── hooks/   # 功能Hooks
│       ├── stores/  # 功能状态
│       ├── types/   # 功能类型
│       └── utils/   # 功能工具
├── hooks/           # 全局共享Hooks
├── lib/             # 第三方库封装
├── stores/          # 全局状态管理
├── testing/         # 测试工具和模拟
├── types/           # 全局类型定义
└── utils/           # 共享工具函数
```

### 按功能/领域组织

代码主目录为 `src/`，核心采用特性/领域驱动（features）分区，提升高内聚、低耦合。

每个功能模块可包含 `api`、`assets`、`components`、`hooks`、`stores`、`types`、`utils` 等子文件夹，按需创建。

## 2. 命名规范

### 文件和文件夹命名

- **文件/文件夹**: 统一采用短横线（kebab-case）
  ```
  ✅ user-profile.component.ts
  ✅ api-client.util.ts
  ✅ auth-store.ts
  
  ❌ UserProfile.component.ts
  ❌ apiClient.util.ts
  ❌ AuthStore.ts
  ```

- **特殊场景**: 常量使用 UPPER_SNAKE_CASE
  ```
  ✅ API_BASE_URL
  ✅ MAX_RETRY_COUNT
  ```

### 组件命名

- **React 组件**: 文件名使用 kebab-case，导出使用 PascalCase
  ```typescript
  // 文件名: user-profile.tsx
  export const UserProfile = () => {
    // 组件实现
  }
  ```

### 函数和变量命名

- **函数**: camelCase
- **变量**: camelCase
- **常量**: UPPER_SNAKE_CASE
- **类型/接口**: PascalCase

```typescript
// ✅ 推荐
const userName = 'john';
const API_BASE_URL = 'https://api.example.com';
function getUserData() { }
interface UserProfile { }
type ApiResponse<T> = { }
```

## 3. 模块边界和依赖管理

### 清晰的模块边界

- 禁止跨功能模块直接导入，需在应用层组合
- 依赖流向单向：共享模块 → 功能模块 → 应用层
- 使用 ESLint 强制执行依赖和架构规范

### 依赖方向规则

```
❌ 错误: features/auth → features/user (跨功能导入)
✅ 正确: features/auth → components/shared (使用共享模块)
✅ 正确: app/pages → features/auth (应用层组合)
```

## 4. 关注点分离

### 组件职责分离

- **展示组件**: 只负责 UI 渲染，接收 props
- **容器组件**: 负责数据获取和状态管理
- **业务逻辑**: 抽取到自定义 hooks 中

### 目录职责

- `components/`: 纯 UI 组件，无副作用
- `hooks/`: 业务逻辑和状态管理
- `stores/`: 全局状态管理
- `api/`: 数据获取和网络请求
- `utils/`: 纯函数工具
- `types/`: 类型定义

## 5. 代码复用策略

### 全局可复用内容

放在 `components`、`hooks`、`lib`、`stores`、`types`、`utils` 等共享目录。

### 功能模块内复用

功能模块内仅暴露自身复用内容，避免全局污染。

### 复用层级

```
1. 应用层 (app/)
   ↑ 使用
2. 功能层 (features/)
   ↑ 使用
3. 共享层 (components/, hooks/, utils/)
```

## 6. 测试策略

### 测试文件组织

- 测试代码与被测模块同目录
- 或在 `src/testing` 统一管理
- 测试文件命名: `*.test.ts` 或 `*.spec.ts`

### 可测试性设计

- 组件、工具函数等设计时考虑可测试性
- 避免复杂依赖
- 使用依赖注入和 mock

## 7. 扩展性和维护性

### 扁平化原则

- 目录结构扁平化，减少嵌套层级
- 降低心智负担
- 本地优先原则：相关代码就近放置

### 按需嵌套

- 项目规模增长时合理分组
- 避免目录臃肿
- 保持清晰的导航路径

## 8. Next.js 适配

### 目录结构调整

- 保持 `src/` 的特性驱动结构
- `app/` 目录仅作为路由入口
- 从 `src/features/` 导入实现

### 路由组织

```
app/
├── (auth)/
│   ├── login/
│   └── register/
├── dashboard/
└── layout.tsx

src/
├── features/
│   ├── auth/
│   └── dashboard/
└── ...
```

## 9. 最佳实践

### 避免的模式

- ❌ 避免使用桶文件（index.js/ts），影响 Tree shaking
- ❌ 避免深层嵌套目录
- ❌ 避免跨功能模块直接导入

### 推荐模式

- ✅ 可组合性优先，提升代码复用性
- ✅ 依赖关系追踪，保持清晰的模块调用图
- ✅ 单一职责原则
- ✅ 显式导入导出

## 10. 工具和强制执行

### ESLint 规则

配置 ESLint 强制执行：
- 依赖方向规则
- 命名约定
- 导入导出规范

### 代码审查检查点

- [ ] 目录结构是否符合规范
- [ ] 命名是否一致
- [ ] 依赖方向是否正确
- [ ] 组件职责是否单一
- [ ] 测试覆盖是否充分

## 参考资料

- [Feature-Sliced Design](https://feature-sliced.github.io/documentation/)
- [bulletproof-react](https://github.com/alan2207/bulletproof-react/blob/master/docs/project-structure.md)
- [Screaming Architecture - Evolution of a React folder structure](https://dev.to/profydev/screaming-architecture-evolution-of-a-react-folder-structure-4g25)