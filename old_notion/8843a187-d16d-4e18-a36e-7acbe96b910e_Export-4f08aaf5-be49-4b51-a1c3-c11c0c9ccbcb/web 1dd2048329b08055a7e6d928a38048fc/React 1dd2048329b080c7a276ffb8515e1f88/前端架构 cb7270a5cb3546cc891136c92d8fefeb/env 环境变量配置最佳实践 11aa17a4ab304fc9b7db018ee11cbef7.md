# env 环境变量配置最佳实践

# **env 环境变量配置最佳实践**

## **目的**

- 给你的库或者应用程序一个更加健壮的环境变量配置。
- 提升开发者体验（DX）
- 解决敏感数据在环境变量中的使用

## **通常做法**

当使用 Vite、Rollup 或 webpack 创建应用程序时，通常需要配置环境变量。例如，Vite、Nextjs 一般通过`.env`文件配置。

## **Vite 配置环境变量**

在使用 Vite 创建项目时，Vite 基于 [dotenv](https://github.com/motdotla/dotenv) 自动加载环境变量。除了 Vite，像 Next.js 也是采用这种方式。

**创建环境文件**

```
.env                 # 默认
.env.local           # 开发
.env.production      # 生产
.env.staging         # 预发布

```

**定义环境变量**

```
// .env
VITE_APP_URL='http://api.default.com'

// .env.local
VITE_APP_URL='http://localhost:3000'

```

- * 使用环境变量**

```tsx
console.log(import.meta.env.VITE_APP_URL)

```

**Typescript提示**

```tsx
// vite-env.d.ts/// <reference types="vite/client" />interface ImportMetaEnv{
  readonly VITE_APP_URL:string
}

interface ImportMeta{
  readonly env:ImportMetaEnv
}

```

**指定环境**

```
vite build --mode production
vite build --mode staging
... 其他环境

```

## **使用`process.env`**

`.env` 能够满足大部分环境变量的需求，但当需要区分环境并且涉及到敏感信息，比如访问令牌时，可能需要使用 `process.env`。

例如，你想要像下面这样设置 node 的环境变量：

```
export ACCESS_TOKEN='abcd123' && npm run dev

```

在代码中通过`process.env`访问：

```tsx
console.log(process.env.ACCESS_TOKEN)// undefined
```

在 Vite 中无法直接访问`process.env`，需要修改`vite.config.ts`：

```tsx
// vite.config.tsexport default defineConfig({
// ... otherdefine: {
    "process.env.ACCESS_TOKEN": JSON.stringify(process.env.ACCESS_TOKEN),
  },
});

```

> 由于 Vite 5 使用了esbuild，因此define需要遵循esbuild.define。
> 

Typescript 提示：

```tsx
// env.d.tsdeclare namespace NodeJS {
  interface ProcessEnv {
    ACCESS_TOKEN?: string;
  }
}

```

然后你代码中的环境变量变成了这样...

```tsx
console.log(import.meta.env.VITE_APP_URL)
console.log(process.env.ACCESS_TOKEN)

```

当项目越来越大，环境变量越来越多时... 回头看这是环境变量是啥... 慢慢的开始有了心智负担

## **封装**

f1封装的好处，就是将`import.meta.env`和`process.env`两者放在一起，统一管理维护。或者你没有使用Vite时，刚好也需要这样的封装。

首先，创建以下文件结构：

```
.
└── src
    └── config
        ├── defineConfig.ts
        ├── envs
        │   ├── local.ts
        │   ├── prod.ts
        │   └── staging.ts
        ├── index.ts
        └── types.ts

```

- `config`保存环境变量的文件夹
- `defineConfig.ts` - 类型帮助函数
- `envs` - 包含要支持的不同环境。
- `index.ts` - 环境变量入口文件
- `types.ts` - 存放环境变量类型

**创建环境变量类型**

```tsx
// config/types.tsexport type AppConfig = {
  apiURL:string
}

```

**创建****`defineConfig`****帮助器**

```tsx
// config/defineConfig.tsimport { AppConfig } from './types'

export function defineConfig(config:AppConfig){
  return config
}

```

> 就像vite.cofing.ts中的defineConfig,给环境变量友好的类型提示，最近越来越多的库使用这种方式。
> 

**定义环境**

```tsx
// config/envs/local.tsimport { defineConfig } from "../defineConfig";

export function createLocalConfig() {
  return defineConfig({
    apiURL: "http://localhost:3000",
  });
}
// config/envs/prod.ts
...

```

**配置入口文件**

```tsx
import { createLocalConfig } from "./envs/local";
import { createProdConfig } from "./envs/prod";
import { createStagingConfig } from "./envs/staging";

export const appConfig = getConfig();

function getConfig() {
//switch (process.env.NODE_ENV) {switch(import.meta.env.MODE)
    case "production":
      return createProdConfig();
    case "staging":
      return createStagingConfig();
    case "local":
      return createLocalConfig();
    default:
      throw new Error(`Invalid APP_ENV "${process.env.APP_ENV}"`);
  }
}

```

> 如果你使用的是 Vite，import.meta.env.MODE 足够了。当然，你也可以使用 process.env.NODE_ENV（Vite 需要配置 define）。
> 

**使用**

```tsx
import {appConfig} from '@/config'

console.log(appConfig.apiURL)

```

**默认值**

如果你有一个环境变量是可选的，或者值关注某个特定环境，那么就需要抽离，并且赋予默认值，这样你只需要修改你关注的环境，其他环境使用默认值。

增加默认值也使你的配置灵活拓展

```tsx
// config/types.tsexport type AppConfig = {
  apiURL:string,
  onlyLocal:boolean,
}

// config/defineConfig.tsimport { AppConfig } from "./types";

type KeysWithFallbackValue = "onlyLocal";

// 定义一个工具类：将类型的部分属性转换为可选type Optional<T, K extends keyof T> = Pick<Partial<T>, K> & Omit<T, K>;

// 定义类型：这个类型Optional转换KeysWithFallbackValue属性为可选type RequiredConfig = Optional<AppConfig, KeysWithFallbackValue>;

// 默认值const defaultConfig: Pick<AppConfig, KeysWithFallbackValue> = {
  onlyLocal: false,
};

export function defineConfig(config: RequiredConfig): AppConfig {
  return {
    ...defaultConfig,
    ...config,
  };
}

```

接下来你可以在你想配置的环境文件中添加`onlyLocal`，而不用关心其他环境变量是否需要配置。

```tsx
// config/envs/local.tsimport { defineConfig } from "../defineConfig";

export function createLocalConfig() {
  return defineConfig({
    apiURL: "http://localhost:3000",
    onlyLocal:true
  });
}
// config/envs/prod.ts
```

完～

## **参考**

- [12factor](https://12factor.net/)