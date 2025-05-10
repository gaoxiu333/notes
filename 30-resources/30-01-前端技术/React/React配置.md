---
title: React配置
created: 2024-05-10 16:07
updated: 2024-05-29 10:14
type: resource
status: active
schema: v1
tags: [source/notion, topic/frontend/react, lang/javascript, lang/typescript]
---

# React 配置

## 插件

- `'eslint-plugin-react-hooks'` - 这个 ESLint 插件强制执行[Hooks 规则](https://react.dev/reference/rules/rules-of-hooks)(React 之前需要使用 canary版本)
- `'eslint-plugin-react-refresh'` -  验证您的组件是否可以通过快速刷新安全地更新。
- `'@typescript-eslint/parser'` - 一个 ESLint 解析器，它利用**TypeScript ESTree**来允许 ESLint lint TypeScript 源代码(这个属于 TS lint)
- [eslint-react](https://github.com/Rel1cx/eslint-react) - 刚兴起，很多明星项目在用

## Eslint 官方推荐预设

- `eslint-plugin-react`

[React eslint 最佳实践](https://timjames.dev/blog/the-best-eslint-rules-for-react-projects-30i8)

## 配置草稿

- `pluginJs.configs.recommended` ??
- `typescript-eslint` - 配置 ts
- `eslint-plugin-react/configs/recommended.js` - 配置 React

有 3 个可共享的配置。

- `eslint-plugin-react/configs/all`
- `eslint-plugin-react/configs/recommended`
- `eslint-plugin-react/configs/jsx-runtime`
- Hooks 规则：[eslint-plugin-react-hooks](https://github.com/facebook/react/tree/master/packages/eslint-plugin-react-hooks)
- JSX 可访问性：[eslint-plugin-jsx-a11y](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y)
- React Native：[eslint-plugin-react-native](https://github.com/Intellicode/eslint-plugin-react-native)

**分类** 

```javascript
'react': plugins['@eslint-react'],
'react-dom': plugins['@eslint-react/dom'],
'react-hooks': pluginReactHooks,
'react-hooks-extra': plugins['@eslint-react/hooks-extra'],
'react-naming-convention': plugins['@eslint-react/naming-convention'],
'react-refresh': pluginReactRefresh,
``` 