---
title: "Feature-Sliced Design架构"
date: 2024-07-18
tags: 
  - type/concept
  - subject/frontend
  - topic/architecture
  - topic/react
status: active
---

# Feature-Sliced Design (FSD) 架构要点总结

参考来源：[Feature-Sliced Design](https://feature-sliced.github.io/documentation/)

## FSD 项目结构速览

```
📦 src
 ┣ 📂 app                  # 应用入口 (App Layer)
 ┃ ┣ 📂 providers          # 应用级别提供者
 ┃ ┣ 📂 styles             # 全局样式
 ┃ ┣ 📂 store              # 根 store 配置
 ┃ ┣ 📂 routes             # 路由配置
 ┃ ┗ 📄 index.ts           # 应用入口点
 ┃
 ┣ 📂 processes            # 跨页面流程 (Processes Layer - 可选)
 ┃ ┣ 📂 authentication     # 认证流程
 ┃ ┃ ┣ 📂 ui               # 流程 UI 组件
 ┃ ┃ ┣ 📂 model            # 流程业务逻辑
 ┃ ┃ ┗ 📄 index.ts         # 公共 API
 ┃
 ┣ 📂 pages                # 页面 (Pages Layer)
 ┃ ┣ 📂 home               # 首页
 ┃ ┃ ┣ 📂 ui               # 页面 UI 组件
 ┃ ┃ ┣ 📂 model            # 页面业务逻辑
 ┃ ┃ ┣ 📂 api              # 页面 API 请求
 ┃ ┃ ┗ 📄 index.ts         # 公共 API
 ┃ ┣ 📂 article-read       # 文章阅读页
 ┃ ┃ ┣ 📂 ui               # 页面 UI 组件
 ┃ ┃ ┣ 📂 model            # 页面业务逻辑
 ┃ ┃ ┣ 📂 api              # 页面 API 请求
 ┃ ┃ ┗ 📄 index.ts         # 公共 API
 ┃
 ┣ 📂 widgets              # 可重用 UI 块 (Widgets Layer)
 ┃ ┣ 📂 header             # 页头组件
 ┃ ┃ ┣ 📂 ui               # 组件 UI
 ┃ ┃ ┣ 📂 model            # 组件业务逻辑
 ┃ ┃ ┗ 📄 index.ts         # 公共 API
 ┃ ┣ 📂 footer             # 页脚组件
 ┃ ┃ ┣ 📂 ui               # 组件 UI
 ┃ ┃ ┗ 📄 index.ts         # 公共 API
 ┃
 ┣ 📂 features             # 功能 (Features Layer)
 ┃ ┣ 📂 auth               # 认证功能
 ┃ ┃ ┣ 📂 ui               # 功能 UI 组件
 ┃ ┃ ┣ 📂 model            # 功能业务逻辑
 ┃ ┃ ┣ 📂 api              # 功能 API 请求
 ┃ ┃ ┗ 📄 index.ts         # 公共 API
 ┃ ┣ 📂 article-like       # 文章点赞功能
 ┃ ┃ ┣ 📂 ui               # 功能 UI 组件
 ┃ ┃ ┣ 📂 model            # 功能业务逻辑
 ┃ ┃ ┣ 📂 api              # 功能 API 请求
 ┃ ┃ ┗ 📄 index.ts         # 公共 API
 ┃
 ┣ 📂 entities             # 业务实体 (Entities Layer)
 ┃ ┣ 📂 user               # 用户实体
 ┃ ┃ ┣ 📂 ui               # 实体 UI 组件
 ┃ ┃ ┣ 📂 model            # 实体业务逻辑
 ┃ ┃ ┣ 📂 api              # 实体 API 请求
 ┃ ┃ ┣ 📂 @x               # 跨导入 API
 ┃ ┃ ┃ ┗ 📄 article.ts     # 为 article 实体提供的 API
 ┃ ┃ ┗ 📄 index.ts         # 公共 API
 ┃ ┣ 📂 article            # 文章实体
 ┃ ┃ ┣ 📂 ui               # 实体 UI 组件
 ┃ ┃ ┣ 📂 model            # 实体业务逻辑
 ┃ ┃ ┣ 📂 api              # 实体 API 请求
 ┃ ┃ ┣ 📂 lib              # 实体特定库
 ┃ ┃ ┗ 📄 index.ts         # 公共 API
 ┃
 ┗ 📂 shared               # 共享代码 (Shared Layer)
   ┣ 📂 ui                 # UI 组件库
   ┃ ┣ 📂 button           # 按钮组件
   ┃ ┃ ┗ 📄 index.ts       # 组件公共 API
   ┃ ┣ 📂 input            # 输入组件
   ┃ ┃ ┗ 📄 index.ts       # 组件公共 API
   ┣ 📂 api                # API 客户端配置
   ┃ ┣ 📄 api-client.ts    # API 客户端
   ┃ ┗ 📄 query-client.ts  # 查询客户端 (React Query)
   ┣ 📂 config             # 环境配置
   ┣ 📂 lib                # 工具库
   ┗ 📂 i18n               # 国际化
```

## 概述

**Feature-Sliced Design (FSD)** 是一种用于搭建前端应用的架构方法论。简而言之，它是一套组织代码的规则和约定。该方法论的主要目的是使项目在面对不断变化的业务需求时更加可理解和稳定。

除了一系列约定外，FSD 还是一个工具链。它包括检查项目架构的代码检查工具、通过 CLI 或 IDE 的文件夹生成器，以及丰富的示例库。

## 适用场景

FSD 可以在任何规模的项目和团队中实施。如果满足以下条件，它适合您的项目：

- 您正在做**前端**（网页、移动端、桌面端等 UI）
- 您正在构建**应用程序**，而非库

仅此而已！对于使用何种编程语言、UI 框架或状态管理器没有限制。您还可以逐步采用 FSD，在单体仓库中使用它，并通过将应用程序拆分为多个包并在其中单独实施 FSD 来扩展规模。

如果您已经有了一个架构并考虑切换到 FSD，请确保当前架构在您的团队中**正在造成麻烦**。例如，如果您的项目变得太大且相互连接，难以高效实施新功能，或者您预期会有许多新成员加入团队。如果当前架构运行良好，可能不值得更改。但如果您确实决定迁移，请参阅增量采用部分以获取指导。

## 常见示例案例

FSD 架构可以灵活应对多种常见的前端开发场景。以下是一些典型的应用案例：

### 1. 认证逻辑

认证是大多数应用程序的核心功能，在 FSD 中，认证逻辑可以按以下方式组织：

- **表单处理**: 登录、注册表单可放在`features/auth`中
- **双因素认证(2FA)**: 可作为单独的`features/2fa`或 auth 特性的一部分
- **OAuth 集成**: 社交媒体登录可放在`features/oauth`
- **令牌存储**: 可放在`entities/session`的 model 分段中
- **令牌刷新**: 自动刷新逻辑可放在`entities/session`或`features/auth`中

这种分解使认证逻辑更易于维护和测试，同时保持代码的高内聚性。

### 2. 类型管理

在 TypeScript 项目中，类型定义的位置和组织方式是重要的架构决策：

#### 2.1 工具类型

工具类型是那些本身没有太多意义，通常与其他类型一起使用的类型。例如：

```ts
type ArrayValues<T extends readonly unknown[]> = T[number];
```

要在项目中使用这些工具类型，您可以：

- 安装类型库，如`type-fest`
- 在`shared/lib`中创建自己的类型库，如`shared/lib/utility-types`

不要高估工具类型的潜在可重用性。仅仅因为它可以被重用，并不意味着它会被重用。有些工具类型放在它们被需要的地方附近就可以了：

```
📂 pages
  📂 home
    📂 api
      📄 ArrayValues.ts (工具类型)
      📄 getMemoryUsageMetrics.ts (使用工具类型的代码)
```

> ⚠️ 避免创建`shared/types`文件夹，或向切片添加`types`分段。"类型"这一类别类似于"组件"或"钩子"，它描述的是内容的本质，而不是用途。分段应描述代码的目的，而非本质。

#### 2.2 业务实体及其交叉引用

应用中最重要的类型是业务实体的类型，即应用处理的现实世界对象。例如，在音乐流媒体应用中，您可能有业务实体*Song*、*Album*等。

业务实体通常来自后端，因此第一步是为后端响应定义类型。为每个端点创建请求函数并为其响应定义类型是很方便的。为了额外的类型安全，您可能想使用如 Zod 这样的模式验证库处理响应。

例如，如果将所有请求保存在 Shared 中，可以这样做：

```ts
// shared/api/songs.ts
import type { Artist } from "./artists";

interface Song {
  id: number;
  title: string;
  artists: Array<Artist>;
}

export function listSongs() {
  return fetch("/api/songs").then((res) => res.json() as Promise<Array<Song>>);
}
```

您可能注意到`Song`类型引用了另一个实体`Artist`。这是将请求存储在 Shared 中的好处之一—现实世界的类型往往相互交织。

但按照 FSD 的导入规则，同层次的切片不能相互导入。处理这个问题有两种方法：

1. **参数化类型**

可以让类型接受类型参数作为与其他实体连接的插槽，甚至可以对这些插槽施加约束：

```ts
// entities/song/model/song.ts
interface Song<ArtistType extends { id: string }> {
  id: number;
  title: string;
  artists: Array<ArtistType>;
}
```

这对某些类型比其他类型效果更好。简单的类型如`Cart = { items: Array<Product> }`可以轻松地与任何类型的产品一起工作。更紧密相连的类型，如`Country`和`City`，可能不那么容易分离。

2. **跨导入(但要正确执行)**

要在 FSD 中实现实体之间的跨导入，可以为每个将要交叉导入的切片创建特定的公共 API，使用`@x`记号。例如，如果我们有实体`song`、`artist`和`playlist`，后两者需要引用`song`，我们可以在`song`实体中为它们创建特定的公共 API：

```
📂 entities
  📂 song
    📂 @x
      📄 artist.ts (供`artist`实体导入的公共API)
      📄 playlist.ts (供`playlist`实体导入的公共API)
    📄 index.ts (常规公共API)
```

`entities/song/@x/artist.ts`文件的内容类似于`entities/song/index.ts`：

```ts
// entities/song/@x/artist.ts
export type { Song } from "../model/song.ts";
```

然后`entities/artist/model/artist.ts`可以这样导入`Song`：

```ts
// entities/artist/model/artist.ts
import type { Song } from "entities/song/@x/artist";
export interface Artist {
  name: string;
  songs: Array<Song>;
}
```

通过明确实体之间的连接，我们可以控制相互依赖并保持一定程度的领域分离。

#### 2.3 数据传输对象和映射器

数据传输对象(DTOs)是描述后端数据形状的术语。有时 DTO 可以按原样使用，但有时对前端来说不便。映射器(Mappers)就是将 DTO 转换为更便捷形状的工具。

**DTO 的位置**

如果您的后端类型在单独的包中(例如，前后端共享代码)，只需从中导入 DTO 即可。如果不共享代码，就需要在前端代码库中保存 DTO。

如果请求函数在`shared/api`中，那么 DTO 应该放在那里，紧挨着使用它的函数：

```ts
// shared/api/songs.ts
import type { ArtistDTO } from "./artists";

interface SongDTO {
  id: number;
  title: string;
  artist_ids: Array<ArtistDTO["id"]>;
}

export function listSongs() {
  return fetch("/api/songs").then(
    (res) => res.json() as Promise<Array<SongDTO>>
  );
}
```

**映射器的位置**

映射器是接受 DTO 进行转换的函数，应该位于 DTO 定义附近。实践中，如果请求和 DTO 在`shared/api`中定义，那么映射器也应该放在那里。 