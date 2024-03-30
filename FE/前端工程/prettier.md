# prettier 入门

Prettier 是一个固执己见的代码格式化程序，支持：

- JavaScript(包括试验性功能)
- JSX
- TypeScript
- CSS、Less、SCSS
- HTML
- JSON
- Markdown
- YAML

## 疑问？

- Prettier 与 Linters

  - ESlint
  - TSlint
  - stylelint

  > 参考：[Prettier 与 Linters](https://prettier.io/docs/en/comparison)
  >
  > 主要区别为：
  >
  > - 格式规则
  > - 代码质量规则
  > - Prettier 进行格式化，linter 捕获错误

## 基本原理

- Strings - 单引号、双引号
  - 默认双引号
- Empty lines - 空行
  - 多行空行折叠为一行
  - 开头和结尾空行被删除（文件总是以一个换行符结尾）
- Multi-line objedcts - 多行对象
  - 对象中第一个属性与花括号换行则为多行对象
  - 对象第一个属性紧挨着花括号，则为单行对象
- Decorators - 装饰器
- Semicolons - 分号
- Print width - 格式化代码宽度
- JSX
  - return 默认加上了 ()
- Comments - 注释
  - 使用`eslint-disable`、`/* istanbul ignore next */`代替`eslint-disable-line`、`eslint-disable-next-line`

## 安装

```bash
npm i --save-dev --save-exact prettier
echo {}> .prettierrc.json
touch .prettierignore # 将基于 .gitignore .eslintignore
npx prettier . --write # 格式化所有内容 文件为 glob 语法
```

## 编辑器配置

## Linters 集成

- Eslint - [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier#installation) 关闭所有不必要或者可能与 Prettier 冲突的 ESlint 规则

- Stylelint - [stylelint-config-prettier](https://github.com/prettier/stylelint-config-prettier) 和上面类似

- ESLint

  - [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier) 关闭可能与 Prettier 冲突的 ESLint 规则
  - [eslint-plugin-prettier](https://github.com/prettier/eslint-plugin-prettier) 将 Prettier 作为 ESLint 规则运行，并报告错误
  - [prettier-eslint](https://github.com/prettier/prettier-eslint) 根据 Prettier 规则进行格式化代码
  - [prettier-standard](https://github.com/sheerun/prettier-standard) 使用 standard 规则格式化代码

- stylelint

  - [stylelint-config-prettier](https://github.com/prettier/stylelint-config-prettier) 关闭可能与 Prettier 冲突的规则
  - [stylelint-prettier](https://github.com/prettier/stylelint-prettier) 将 Prettier 作为 stylelint 规则运行，并报告错误
  - [prettier-stylelint](https://github.com/hugomrdias/prettier-stylelint) 将 Prettier 作为规则，并自动修复

  > 参考：
  >
  > [相关项目](https://prettier.io/docs/en/related-projects)
  >
  > [ESLint 和 Prettier 推荐配置](https://github.com/prettier/eslint-plugin-prettier#recommended-configuration)

## Git hooks

1. 安装 husky 和 lint-staged

   ```bash
   npm install --save-dev husky lint-staged
   npx husky install
   npm pkg set scripts.prepare="husky install"
   npx husky add .husky/pre-commit "npx lint-staged"
   ```

2. 修改 package.json

   ```json
   {
     "lint-staged": {
       "**/*": "prettier --write --ignore-unknown"
     }
   }
   ```

   > 如果您使用 ESLint，请确保 lint-staged 在 Prettier 之前运行它，而不是之后。
   >
   > 参考： [预提交挂钩](https://prettier.io/docs/en/precommit)

## 忽略代码

- `.prettierignore` 文件

  ```
  # 默认忽略以下文件
  **/.git
  **/.svn
  **/.hg
  **/node_modules # --with-node-modules 参数会启用该文件的格式化
  ```

- `--ignore-path` CLI 忽略参数

- 注释方式忽略

  ```bash
  # js
  // prettier-ignore
  # jsx
  {/* prettier-ignore */}
  # HTML
  <!-- prettier-ignore -->
  <!-- prettier-ignore-attribute -->
  <!-- prettier-ignore-attribute (mouseup) -->
  # CSS
  /* prettier-ignore */
  # Markdown
  <!-- prettier-ignore -->
  ```

- 更多方式，请参考官网