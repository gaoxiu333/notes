# npm 备忘录

Owner: xiu gao

# npm 备忘录

## npm install

官方文档：[npm install](https://docs.npmjs.com/cli/v10/commands/npm-install)

默认安装在`dependencies`，通过参数控制安装的位置

- `P, --save-prod`：`dependencies`.这是默认值，除非`D`或`O`存在。
- `D, --save-dev`：`devDependencies`.
- `O, --save-optional`：`optionalDependencies`.
- `-no-save`：防止保存到`dependencies`.

附加参数

- `E, --save-exact`：保存精确的版本，不会使用 npm 的默认 semver 范围运算符。
- `B, --save-bundle`：同时添加到`bundleDependencies`列表中。