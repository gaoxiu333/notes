
### 编辑器

**Visual Studio Code 插件**

* [TypeScript Importer](https://marketplace.visualstudio.com/items?itemName=pmneo.tsimporter) - 收集项目中的所有类型定义，敲出`:` 时来进行类型补全

**配置**

搜索'typescript Inlay Hints'，推荐开启:

* Function Like Return Types，显示推导得到的函数返回值类型；
* Parameter Names，显示函数入参的名称；
* Parameter Types，显示函数入参的类型；
* Variable Types，显示变量的类型。

### 编译器工具

* Babel
* SWC
* Sucrase
* nodejs 编译工具
	* esno - 使用ESBuild编译
	* ts-node
	* ts-node-dev

## 支持文件类型

### 支持JSON

`resolveJsonModule:true`
`"moduleResolution": "node"`

> 支持JSON 不仅需要开启`resolveJsonModule`，还需要`moduleResolution`配置为`node`，使用node模块解析策略。

### 支持js文件

`esModuleInterop:true` - 开启 CommonJS 模块的导入

# TS 环境配置

## CLI 命令

```bash
tsc --hlep
tsc --init  # 初始化配置文件 tsconfig.json
tsc --project  # 指定配置文件
tsc --version # 查看 TS 版本

tsc --build # 构建
tsc --clean # 删除所有构建的文件
tsc --dry # 显示？
tsc --verbose # 查看日志详情
tsc --watch # 监听文件变动
```

## 常用配置

- `tsconfig.json`
  - 表示 TS 项目的根目录
- 常用顶层配置
  - `files:[]`、`include:[]`、`exclude:[]`
    - `*` 匹配0或多个字符（不包括目录分隔符）
    - `?` 匹配一个任意字符（不包括目录分隔符）
    - `**/` 递归匹配任意子目录
  - `extends:“继承的配置地址”`
  - `compilerOptions` - 编译选项
