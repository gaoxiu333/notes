---
title: Node开发环境配置
created: 2024-07-22 12:30
updated: 2024-07-22 12:45
type: note
status: active
schema: v1
tags: [topic/backend/nodejs, topic/development/typescript, topic/dev-environment]
---

# Node 配置

## Node.js 版本选择

- 优先使用 LTS (长期支持) 版本
- 使用 nvm 管理多个 Node.js 版本
  ```bash
  # 安装最新的 LTS 版本
  nvm install --lts
  
  # 使用特定 LTS 版本
  nvm use --lts
  ```

## 初始化配置

```bash
# 安装依赖
pnpm add --save-dev eslint @eslint/js @types/eslint__js typescript typescript-eslint
# 使用 @eslint/config 创建 eslint 配置文件
pnpm create @eslint/config
```

## 配置 TypeScript

### 参考资源

- [node-lts-tsconfig](https://github.com/tsconfig/bases/blob/main/bases/node-lts.json) - 官方推荐配置
- [TSconfig Cheat sheet](https://www.totaltypescript.com/tsconfig-cheat-sheet) - 配置清单
- [silver-xu/ts-boilerplate.md](https://gist.github.com/silver-xu/1dcceaa14c4f0253d9637d4811948437) - TS项目模板参考
- [将 TypeScript 与 Node.js 结合使用：初学者指南](https://betterstack.com/community/guides/scaling-nodejs/nodejs-typescript/)

### 基础tsconfig.json示例

```json
{
  "$schema": "https://json.schemastore.org/tsconfig",
  "display": "Node LTS",
  "compilerOptions": {
    "lib": ["es2023"],
    "module": "node16",
    "target": "es2022",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "moduleResolution": "node16"
  }
}
```

### 高级tsconfig.json示例

基于node-lts.json和TSconfig Cheat sheet修改的完整配置：

```json
{
  "$schema": "https://json.schemastore.org/tsconfig",
  "display": "Node LTS",
  "_version": "20.1.0",
  "compilerOptions": {
    /* Base Options: */
    "esModuleInterop": true, // 关于模块解析模块是否兼容简化的 CommonJS 导入方式：https://www.typescriptlang.org/docs/handbook/module-resolution.html
    "skipLibCheck": true, // 性能：跳过检查 .d.ts 文件的类型检查
    "target": "es2022", // 要生成 JS 代码的版本
    "allowJs": true, // 允许导入 JS 代码
    "resolveJsonModule": true, // 允许导入 JSON 文件
    "moduleDetection": "force", // 较为严格的方式，强制将所有文件视为模块
    "isolatedModules": true, //服务于 Babel 等第三方工具，确保每个文件都可以独立编译为模块，同时确保单独编译的文件之间没有依赖关系
    "verbatimModuleSyntax": true, // 强制使用 import type 和 export type

    /* Strictness */
    "strict": true, // 启用所有严格类型检查选项，它同时会启用很多其他选项：关与 JS 的严格模式、any、undefined、null、函数返回值、bind参数、this、switch等的严格检查
    "noUncheckedIndexedAccess": true, // 数组：禁用不检查索引访问
    "noImplicitOverride": true, // 类：禁用子类和父类重名

    /* If transpiling with TypeScript: */
    "module": "NodeNext",
    "moduleResolution": "NodeNext", // 如何解析模块导入的模块
    "outDir": "dist",
    "sourceMap": true,

    /* If your code runs in the DOM: */
    "lib": ["es2022", "dom", "dom.iterable"]
  },
  /* Files: */
  "include": ["src/**/*.ts"],
  "exclude": ["node_modules"]
}
```

## ESLint 配置

### 参考资源

- [typescript-eslint](https://typescript-eslint.io/) - 官方文档与指南

### 安装

```bash
# 使用npm
npm install --save-dev eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin

# 使用yarn
yarn add --dev eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin

# 使用pnpm
pnpm add --save-dev eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
```

### 基础.eslintrc.js配置

```javascript
module.exports = {
  root: true,
  parser: '@typescript-eslint/parser',
  plugins: [
    '@typescript-eslint',
  ],
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
  ],
  rules: {
    // 自定义规则
  }
};
```

### 高级.eslintrc.js配置

```javascript
module.exports = {
  root: true,
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 2021,
    sourceType: 'module',
    project: './tsconfig.json',
  },
  plugins: [
    '@typescript-eslint',
    'import',
    'prettier',
  ],
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:@typescript-eslint/recommended-requiring-type-checking',
    'plugin:import/errors',
    'plugin:import/warnings',
    'plugin:import/typescript',
    'prettier',
    'plugin:prettier/recommended',
  ],
  rules: {
    // TypeScript相关规则
    '@typescript-eslint/explicit-function-return-type': 'warn',
    '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
    '@typescript-eslint/no-explicit-any': 'warn',
    '@typescript-eslint/no-unsafe-assignment': 'warn',
    '@typescript-eslint/no-unsafe-member-access': 'warn',
    '@typescript-eslint/no-unsafe-call': 'warn',
    '@typescript-eslint/no-unsafe-return': 'warn',
    
    // Import规则
    'import/order': [
      'error',
      {
        'groups': [
          'builtin',
          'external',
          'internal',
          'parent',
          'sibling',
          'index'
        ],
        'newlines-between': 'always',
        'alphabetize': {
          'order': 'asc',
          'caseInsensitive': true
        }
      }
    ],
    
    // 通用规则
    'no-console': ['warn', { allow: ['warn', 'error'] }],
    'prettier/prettier': 'error',
  },
  settings: {
    'import/resolver': {
      typescript: {
        alwaysTryTypes: true,
        project: './tsconfig.json',
      },
    },
  },
};
```

### .prettierrc配置示例

```json
{
  "semi": true,
  "trailingComma": "all",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "endOfLine": "auto"
}
```

## 项目初始化

### 使用 TypeScript 创建 Node.js 项目

```bash
# 创建项目目录
mkdir my-node-project
cd my-node-project

# 初始化 npm 项目
npm init -y

# 安装 TypeScript 和类型定义
npm install --save-dev typescript @types/node ts-node

# 创建 TypeScript 配置文件
npx tsc --init

# 安装开发依赖
npm install --save-dev nodemon eslint
```

### package.json 示例配置

```json
{
  "name": "my-node-project",
  "version": "1.0.0",
  "description": "Node.js project with TypeScript",
  "main": "dist/index.js",
  "scripts": {
    "start": "node dist/index.js",
    "dev": "nodemon --exec ts-node src/index.ts",
    "build": "tsc",
    "lint": "eslint . --ext .ts",
    "test": "jest"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "@types/node": "^18.16.0",
    "@typescript-eslint/eslint-plugin": "^5.59.0",
    "@typescript-eslint/parser": "^5.59.0",
    "eslint": "^8.39.0",
    "nodemon": "^2.0.22",
    "ts-node": "^10.9.1",
    "typescript": "^5.0.4"
  }
}
```

## 推荐的项目结构

```
my-node-project/
├── src/                # 源代码目录
│   ├── index.ts        # 应用入口
│   ├── config/         # 配置文件
│   ├── controllers/    # 控制器
│   ├── models/         # 数据模型
│   ├── routes/         # 路由定义
│   ├── services/       # 业务逻辑
│   ├── utils/          # 工具函数
│   └── types/          # 类型定义
├── dist/               # 编译后的JavaScript代码
├── tests/              # 测试文件
├── .eslintrc.js        # ESLint配置
├── .gitignore          # Git忽略文件
├── package.json        # 项目依赖
├── tsconfig.json       # TypeScript配置
└── README.md           # 项目说明
```

## 调试配置

### VS Code 调试配置 (.vscode/launch.json)

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "启动程序",
      "skipFiles": ["<node_internals>/**"],
      "program": "${workspaceFolder}/src/index.ts",
      "preLaunchTask": "tsc: build - tsconfig.json",
      "outFiles": ["${workspaceFolder}/dist/**/*.js"]
    },
    {
      "type": "node",
      "request": "attach",
      "name": "附加到进程",
      "port": 9229
    }
  ]
}
```

## 常见问题与解决方案

1. **TypeScript 路径别名配置**
   
   tsconfig.json:
   ```json
   {
     "compilerOptions": {
       "baseUrl": "./",
       "paths": {
         "@/*": ["src/*"]
       }
     }
   }
   ```
   
   安装模块解析支持:
   ```bash
   npm install --save-dev tsconfig-paths
   ```

2. **支持环境变量**
   
   安装 dotenv:
   ```bash
   npm install dotenv
   npm install --save-dev @types/dotenv
   ```
   
   在入口文件使用:
   ```typescript
   import * as dotenv from 'dotenv';
   dotenv.config();
   ``` 