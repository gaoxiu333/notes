---
title: vue admin 堆栈
created: 2024-05-04 00:36
updated: 2024-05-29 10:36
type: resource
status: active
schema: v1
tags: [source/notion, topic/frontend/vue, topic/frontend/admin, lang/javascript]
---

# vue admin 堆栈

## 初始化

```bash
pnpm create vue@latest
```

## 添加 antd

```bash
pnpm add ant-design-vue@latest 
```

- 注册 antd 组件

推荐全局部分注册，但是为了省事儿，一般都是全局完整注册（如果是全局完整注册，该如何优化呢？）

## 定制主题

- 预设算法 - antd 内置的三套主题
- `theme.defaultAlgorithm` - 默认
- `theme.darkAlgoritm` - 暗色
- `theme.compactAlgorithm` - 紧凑
- [API](https://antdv.com/docs/vue/customize-theme-cn#api) - 如果需要颗粒度比较细的定制，请参考

## 已使用堆栈

- [unplugin-icons](https://github.com/unplugin/unplugin-icons) - 可以使用 iconify 的图标

## 堆栈合集

**UI 框架**

- [UnoCSS](https://github.com/antfu/unocss) - 高性能且极具灵活性的即时原子化 CSS 引擎

**Icons**

- [Iconify](https://iconify.design/) - 使用任意的图标集，浏览：[🔍Icônes](https://icones.netlify.app/)

**插件**

- `unplugin-vue-components` - 自动加载组件
- `unplugin-auto-import` - 直接使用 Composition API 等，无需导入
- `vite-plugin-pwa` - PWA
- [Vue I18n](https://github.com/intlify/vue-i18n-next) - 国际化
- [VueUse](https://github.com/antfu/vueuse) - 实用的 Composition API 工具合集
- `@vueuse/head` - 响应式地操作文档头信息
- `vite-plugin-vue-devtools` - 旨在增强Vue开发者体验的Vite插件

**编码风格**

- 使用 Composition API 地 `<script setup>` SFC 语法
- [ESLint](https://eslint.org/) 配置为 [@antfu/eslint-config](https://github.com/antfu/eslint-config), 单引号, 无分号.

**开发工具**

- [TypeScript](https://www.typescriptlang.org/)
- [Vitest](https://github.com/vitest-dev/vitest) - 基于 Vite 的单元测试框架
- [Cypress](https://cypress.io/) - E2E 测试
- [pnpm](https://pnpm.js.org/) - 快, 节省磁盘空间的包管理器
- `vite-ssg` - 服务端生成
- [VS Code 扩展](https://github.com/antfu-collective/vitesse/blob/main/.vscode/extensions.json)

## 参考

- [vitesse](https://github.com/antfu-collective/vitesse) - 入门模版
- [UI lib picker](https://ui-libs.vercel.app/) - vue ui组件库
- [awesome-vite-vue3](https://github.com/vitejs/awesome-vite?tab=readme-ov-file#vue-3)

## TODO

- 关于 router 定义，还是看一下 [vue-router](https://github.com/vuejs/router/tree/main) 的 playground，效果更好。 