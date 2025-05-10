# TypeScript 配置

当使用 TypeScript 时，Eslint配置需要 typescript-eslint 的支持。

`typescript-eslint` :

- 允许 Eslint 解析 TypeScript 语法
- 提供了 TypeScript 特有的规则

## 使用

```bash
pnpm add --save-dev eslint @eslint/js @types/eslint__js typescript typescript-eslint
```

- `eslint`
- `@eslint/js`
- `@types/eslint__js`
- `typescript`
- `typescript-eslint`

`eslint.config.js` 配置：

```jsx
// @ts-check

import eslint from '@eslint/js';
import tseslint from 'typescript-eslint';

export default tseslint.config(
  eslint.configs.recommended,
  ...tseslint.configs.recommended,
);
```

- `tseslint.config(...)` - 可选的助手函数，可以代替 JSDoc 类型注释
- `eslint.configs.recommended` - eslint 建议配置
    - 
- `tseslint.configs.recommended` - 关于 TypeScript 代码语法正确性的推荐规则
    - 除此之外还有：
    - `recommentded-type-checked`
    - `strict`  - 包含 `recommended` + 额外规则
    - `styleistic`  - 包含代码风格的配置
    - `base` 、 `all` 、 `only-checked` …