
在前端开发中，Linters 是一类工具，用于检查和纠正代码中的潜在问题，以确保代码风格一致、语法正确、最佳实践等。以下是一些常见的前端开发中使用的 Linters：

1. **ESLint：**
    
    - **语言支持：** JavaScript、TypeScript
    - **功能：** 用于检查 JavaScript 和 TypeScript 代码的潜在问题，支持自定义规则，有广泛的社区支持。ESLint 可以检查代码质量、风格、最佳实践等方面。
2. **TSLint（已弃用）：**
    
    - **语言支持：** TypeScript
    - **功能：** 用于检查 TypeScript 代码的潜在问题。然而，自 TypeScript 2019 年发布版本3.7.5起，TypeScript 团队决定不再支持 TSLint，并建议使用 ESLint 来代替。
3. **Stylelint：**
    
    - **语言支持：** CSS、SCSS、Less
    - **功能：** 用于检查样式表（CSS、SCSS、Less）中的潜在问题，支持自定义规则，有助于保持样式表的一致性。
4. **Prettier：**
    
    - **语言支持：** JavaScript、TypeScript、CSS、JSON、Markdown 等
    - **功能：** 不仅是一个 Linter，而是一个代码格式化工具。Prettier 负责统一代码风格，确保整个项目中的代码风格一致。
5. **ESLint-plugin-Vue：**
    
    - **语言支持：** Vue.js 单文件组件
    - **功能：** 是 ESLint 的插件，专门用于检查 Vue.js 单文件组件中的潜在问题，确保 Vue 项目中的代码质量。
6. **HTMLHint：**
    
    - **语言支持：** HTML
    - **功能：** 用于检查 HTML 代码中的潜在问题，包括语法错误、性能优化、最佳实践等方面。

这些工具可以独立使用，也可以结合使用，以确保前端代码的质量和一致性。在项目中集成 Linters 通常是很好的实践，它有助于团队保持一致的代码风格，并尽早发现并修复潜在的问题。

> 补充：`.editorconfig` 用来统一不同编辑器的代码格式

## Prettier

Prettier 是一个强大的代码格式化工具，它有许多优势，特别适用于维护一致的代码风格和提高开发者工作效率。

## 快速开始

#### 安装

```bash
pnpm add -D --save-exact prettier
# 查看帮助
npx prettier --help 
```

### 配置文件

生成一个`.prettierrc`配置文件：如果是Vite创建的项目，推荐`.mjs`后缀，使用js语法格式，方便添加注释。

```js
// ES 风格
// .prettierrc.mjs 
export default {

}
// CommonJs 风格
// .prettierrc.cjs
module.exports = {

}
```

> 配置文件参考: [参考地址](https://json.schemastore.org/prettierrc)
> `editorconfig` 配置会被转换成相应的prettier 配置，但是会被`.prettierrc` 中相应的配置覆盖。
### 执行命令

- `--write` - 格式化本地文件
- `--check` - 只检查代码不格式化
- `--list-different` - 输出为格式化文件列表
- `--config` - 指定配置文件，默认会读取`.prettierrc`，不需要指定

```bash
# 格式化 src 内的所有文件
npx prettier src --write
```


## 集成

[官方推荐的 Linters 集成](https://prettier.io/docs/en/related-projects)
### Linters集成

使用 Prettier 解决代码格式问题，使用 Linter 解决代码质量问题；但是 Linters 不仅包含代码质量规则，也会包含一些代码风格规则，这导致有一些规则会和 Prettier 冲突。幸运的是可以通过插件关闭 Linters 与 Prettier 冲突或不必要的规则：

#### ESLint

-  [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier) - 可以关闭`ESlint`相关规则（仅格式）

> 但是配置完了之后，Prettier和ESLint只能各自执行；想要一次将代码质量检查和代码格式化两个工具同时执行，需要用到`eslint-plugin-prettier`插件，将 Prettier集成到 ESlint 中，虽然方便但是会比较慢一点。


[推荐配置](https://github.com/prettier/eslint-plugin-prettier#recommended-configuration)

```bash
# 配置完 eslint-plugin-prettier 执行：
npx eslint src --fix
```

#### stylelint

- stylelint-prettier - 将prettier集成到 stylelint 中
### 编辑器

#### Visual Studio Code

- `Prettier - Code formatter`
#### WebStorm

[参考](https://prettier.io/docs/en/webstorm)
#### Vim

[参考](https://prettier.io/docs/en/vim)



### Git

#### 依赖 

- lint-staged
- husky
- simple-git-hooks
- commitlint
- [semantic-release](https://github.com/semantic-release/semantic-release)

`simple-git-hooks` 和 `husky` 都可以用于管理 Git 钩子，执行相应的脚本。这里选用前者，因为它更简单。


#### `simple-git-hooks`

安装

```bash
pnpm add simple-git-hooks -D

# 如果以前配置过 hooks 或者遇到问题，可以删除以前的 hooks；也配置过可以跳过
git config core.hooksPath .git/hooks/
rm -rf .git/hooks

# 更新 ./git/hooks
npx simple-git-hooks
```

package.json 配置使用

```json
{
	  "simple-git-hooks": {
	      "pre-commit": "npx lint-staged",
		}
}
```

配置

```json
"check": "tsc --incremental --noEmit",
{
 "simple-git-hooks": {
    "pre-commit": "pnpm lint-staged && pnpm check",
    "commit-msg": "node scripts/verifyCommit.js"
  },
  "lint-staged": {
    "*.{js,json}": [
      "prettier --write"
    ],
    "*.ts?(x)": [
      "eslint",
      "prettier --parser=typescript --write"
    ]
  },
}
```

使用 `--no-verify` 跳过hooks

```bash
git commit -m "any commit" --no-verify
```

#### lint-staged

主要用途是在代码提交之前，只对暂存区中的文件进行代码检查或其他操作，以确保即将提交的代码是符合规范的。

```bash
# 安装完后在 simple-git-hooks 进行配置。
pnpm add lint-staged -D

```

如果是 `monorepo` 仓库，在子项目的根目录添加配置文件`.lintstagedrc.json`

```json
{ "*.md": "prettier --write" }
```

> lint-staged 会发现与每个暂存文件最接近的配置


#### TODO

`commit-msg` - 究竟是自定义实现还是使用现成的？

### 打包工具




