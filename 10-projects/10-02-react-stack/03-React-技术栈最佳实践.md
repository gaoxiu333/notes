---
title: React-技术栈最佳实践
jd_id: J00-20250514-2235
created: 2025-05-14 22:35
updated: 2025-05-14 22:37
type: note
status: draft
tags: [topic/react, topic/frontend/best-practices, topic/monorepo]
---

# React 技术栈最佳实践指南

## Monorepo 方案选择

根据团队规模和项目特点，推荐以下两种主流方案：

### Nx

- 适用场景：中大型团队
- 特点：支持前后端项目统一管理
- 优势：完整的工具链和扩展生态

### Turborepo

- 适用场景：小到中型团队
- 特点：前端项目优先（特别适合 React + Next.js）
- 优势：配置简单，学习曲线平缓

## 工程化最佳实践

### 环境变量管理

推荐技术栈：

- TypeScript + Zod：类型安全
- dotenv：环境变量管理（Next.js 项目内置）
- Turbo：构建系统

### 项目初始化流程

1. 使用 Turborepo 创建基础项目

```bash
pnpm dlx create-turbo@latest
```

2. 添加 Next.js 应用

```bash
cd apps
pnpm dlx create-next-app@latest --use-pnpm
```

### 依赖管理要点

常见问题：多项目间的依赖版本冲突

解决方案（按推荐度排序）：

1. 使用 `syncpack` 检查和修复依赖 【推荐】
2. 在根目录统一管理公共依赖
3. 使用 `pnpm.overrides` 强制统一版本
4. 配置 `.npmrc` 防止自动安装不同版本

### Eslint

需要分别配置 `tsconfig.json` 、 `eslint.config.ts` 、 `prettier.config.mjs`

- `TypeScript`
- `Eslint`
- `Prettier`
- `eslint-config-prettier` - 关闭所有可能与 Prettier 冲突的 ESLint 规则
- `eslint-plugin-prettier` - 将 Prettier 作为 ESLint 规则运行，在 ESLint 中显示 Prettier 错误

## ShadCN

### 主题

- 建议使用`CSS variables`作为主题系统，`utility classes` 需要更多的 CSS 类名
> 如何构建自己的设计系统呢？

## 注意事项

- 项目初始化阶段的配置（如 ESLint）需要特别关注
- 建议记录项目搭建过程中遇到的问题和解决方案
- 参考优秀实践：[bulletproof-react](https://github.com/alan2207/bulletproof-react)
