# Feature-Sliced Design (FSD) 架构要点总结

参考来源：[Feature-Sliced Design](https://feature-sliced.github.io/documentation/)

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

映射器是接受 DTO 进行转换的函数，应该位于 DTO 定义附近。实践中，如果请求和 DTO 在`shared/api`中定义，那么映射器也应该放在那里：

```ts
// shared/api/songs.ts
import type { ArtistDTO } from "./artists";

interface SongDTO {
  id: number;
  title: string;
  disc_no: number;
  artist_ids: Array<ArtistDTO["id"]>;
}

interface Song {
  id: string;
  title: string;
  /** 歌曲完整标题，包括光盘编号。 */
  fullTitle: string;
  artistIds: Array<string>;
}

function adaptSongDTO(dto: SongDTO): Song {
  return {
    id: String(dto.id),
    title: dto.title,
    fullTitle: `${dto.disc_no} / ${dto.title}`,
    artistIds: dto.artist_ids.map(String),
  };
}

export function listSongs() {
  return fetch("/api/songs").then(async (res) =>
    (await res.json()).map(adaptSongDTO)
  );
}
```

#### 2.4 全局类型和 Redux

全局类型是在整个应用中使用的类型。基于它们需要了解的内容，有两种全局类型：

1. 不具有任何应用特定性的通用类型
2. 需要了解整个应用的类型

第一种情况很简单 - 将类型放在 Shared 中的适当分段中。例如，如果有用于分析的全局变量接口，可以将其放在`shared/analytics`中。

第二种情况通常在使用无 RTK 的 Redux 项目中遇到。最终存储类型只有在添加所有 reducer 后才可用，但这个存储类型需要在整个应用中使用的选择器中可用。

建议的解决方案是在 Shared 和 App 层之间创建隐式依赖。这两种类型`RootState`和`AppDispatch`不太可能改变，Redux 开发人员会熟悉它们。

在 TypeScript 中，可以通过将类型声明为全局来实现：

```ts
// app/store/index.ts
/* 与之前代码块相同的内容... */

declare type RootState = ReturnType<typeof rootReducer>;
declare type AppDispatch = typeof store.dispatch;
```

```ts
// shared/store/index.ts
import {
  useDispatch,
  useSelector,
  type TypedUseSelectorHook,
} from "react-redux";

export const useAppDispatch = useDispatch.withTypes<AppDispatch>();
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;
```

#### 2.5 枚举

枚举的一般规则是它们应该**定义在尽可能靠近使用位置的地方**。当枚举表示特定于单个功能的值时，它应该在同一功能中定义。

分段的选择也应该由使用位置决定。例如，如果您的枚举包含屏幕上 toast 的位置，它应该放在`ui`分段中。如果它表示后端操作的加载状态，它应该放在`api`分段中。

有些枚举在整个项目中都是通用的，如一般后端响应状态或设计系统标记。在这种情况下，可以将它们放在 Shared 中，并根据枚举表示的内容选择分段(`api`表示响应状态，`ui`表示设计标记等)。

#### 2.6 类型验证模式和 Zod

如果您想验证数据是否符合特定形状或约束，可以定义验证模式。在 TypeScript 中，Zod 是一个用于此任务的流行库。验证模式也应尽可能与使用它们的代码位于同一位置。

验证模式与映射器类似，它们接受数据传输对象并解析它，如果解析失败则产生错误。

最常见的验证情况之一是来自后端的数据。通常，当数据不符合模式时，您希望请求失败，因此将模式放在与请求函数相同的位置是有意义的，通常是`api`分段。

如果您的数据通过用户输入获得，如表单，验证应该在数据输入时进行。您可以将模式放在`ui`分段中，紧挨着表单组件，或者在`model`分段中，如果`ui`分段太拥挤。

#### 2.7 组件 props 和 context 的类型

通常，最好将 props 或 context 接口保存在使用它们的组件或 context 的同一文件中。如果您使用单文件组件的框架，如 Vue 或 Svelte，并且无法在同一文件中定义 props 接口，或者想在多个组件之间共享该接口，请在同一文件夹中创建一个单独的文件，通常是`ui`分段。

以下是使用 JSX(React 或 Solid)的示例：

```tsx
// pages/home/ui/RecentActions.tsx
interface RecentActionsProps {
  actions: Array<{ id: string; text: string }>;
}

export function RecentActions({ actions }: RecentActionsProps) {
  /* … */
}
```

以下是为 Vue 存储在单独文件中的接口示例：

```ts
// pages/home/ui/RecentActionsProps.ts
export interface RecentActionsProps {
  actions: Array<{ id: string; text: string }>;
}
```

```vue
// pages/home/ui/RecentActions.vue
<script setup lang="ts">
import type { RecentActionsProps } from "./RecentActionsProps";

const props = defineProps<RecentActionsProps>();
</script>
```

#### 2.8 环境声明文件(`*.d.ts`)

某些包，例如 Vite 或 ts-reset，需要环境声明文件才能在整个应用中工作。通常，它们不大也不复杂，因此通常不需要任何架构，将它们放在`src/`文件夹中就可以了。为了使`src`更有组织性，您可以将它们保存在 App 层的`app/ambient/`中。

其他包根本没有类型，您可能想将它们声明为无类型或者甚至为它们编写自己的类型。这些类型的好地方是`shared/lib`，在`shared/lib/untyped-packages`这样的文件夹中。在那里创建一个`%LIBRARY_NAME%.d.ts`文件并声明您需要的类型：

```ts
// shared/lib/untyped-packages/use-react-screenshot.d.ts
// 此库没有类型，我们不想费心编写自己的类型。
declare module "use-react-screenshot";
```

#### 2.9 类型的自动生成

从外部源自动生成类型是很常见的，例如从 OpenAPI 模式生成后端类型。在这种情况下，在代码库中为这些类型创建一个专门的位置，比如`shared/api/openapi`。理想情况下，您还应该在该文件夹中包含一个 README，描述这些文件是什么，如何重新生成它们等。

### 3. 页面布局

页面布局是前端应用程序的基础结构部分：

- **布局存储位置**:

  - 单页面专用布局可放在相应的`pages/<page-name>/ui`中
  - 跨多个页面重用的布局可放在`widgets/layouts`中
  - 高度可配置的通用布局可放在`shared/ui`中

- **在布局中使用 widgets**:
  - Widgets 可以被嵌入在布局中，但布局不应依赖于特定 widget 的实现细节
  - 可以通过插槽或渲染道具模式将 widgets 注入到布局中

这种组织方式使布局更加灵活且可重用，同时保持关注点分离。

## 基本概念

1. **FSD 定义**：一种面向业务特性的前端架构方法论，将代码按照业务功能而非技术关注点组织。

2. **核心结构**：
   - **层级 (Layers)**：顶层目录，最多 7 层
   - **切片 (Slices)**：层内按业务领域划分的子目录
   - **分段 (Segments)**：切片内按用途划分的代码

## 基本示例

以下是实施 FSD 的简单项目示例：

```
📁 app
📁 pages
📁 shared
```

这些顶层文件夹称为"层"。让我们深入了解：

```
📂 app
  📁 routes
  📁 analytics
📂 pages
  📁 home
  📂 article-reader
    📁 ui
    📁 api
  📁 settings
📂 shared
  📁 ui
  📁 api
```

`📂 pages`内的文件夹称为"切片"，它们按领域（在本例中是按页面）划分层。

`📂 app`、`📂 shared`和`📂 pages/article-reader`内的文件夹称为"分段"，它们按技术用途划分切片（或层），即代码的用途。

## 层级结构（自上而下）

1. **app 层**：

   - 应用初始化逻辑
   - 提供者 (Providers)、路由器、全局样式
   - 作为应用入口点

2. **processes 层**（可选，已弃用）：

   - 处理跨页面流程
   - 如多步骤注册
   - 被视为已弃用但仍可能使用

3. **pages 层**：

   - 包含应用的页面
   - 或嵌套路由中的页面大部分内容

4. **widgets 层**：

   - 页面上使用的独立 UI 组件
   - 大型自包含功能块或 UI，通常提供完整用例

5. **features 层**（可选）：

   - 处理具有业务价值的用户场景
   - 产品功能的可复用实现
   - 如点赞、评论、产品评级等

6. **entities 层**（可选）：

   - 表示业务实体
   - 如用户、评论、商品等

7. **shared 层**：
   - 可复用且不与特定业务逻辑相关的组件和工具
   - 包括 UI 组件库、axios 配置、应用配置、通用帮助函数等

**注意**：

- **App** 和 **Shared** 层与其他层不同，它们没有切片，直接划分为分段。
- 其他所有层 — **Entities**、**Features**、**Widgets** 和 **Pages**，保持先创建切片，然后在切片内创建分段的结构。
- 层的重要技巧是，一个层上的模块只能了解并导入严格在其下方的层的模块。

## 切片 (Slices) 详解

切片是 FSD 组织层次结构中的第二级，主要目的是按照产品、业务或应用意义对代码进行分组。

1. **命名非标准化**：

   - 切片名称由应用的业务领域直接决定
   - 例如，照片库可能有`photo`、`effects`、`gallery-page`等切片
   - 社交网络可能需要`post`、`comments`、`news-feed`等切片

2. **特殊层级例外**：

   - `Shared`层和`App`层不包含切片
   - 原因：Shared 不应包含任何业务逻辑；App 仅包含整个应用的代码，无需拆分

3. **零耦合与高内聚**：

   - 切片应该是独立的、高内聚的代码文件组
   - 理想切片与同层其他切片相互独立（零耦合）
   - 包含与其主要目标相关的大部分代码（高内聚）

4. **切片导入规则**：

   - 切片中的模块（文件）只能导入位于严格低于其层级的其他切片
   - 切片不能使用同一层上的其他切片，这有助于高内聚和低耦合

5. **公共 API 规则**：

   - 每个切片必须包含公共 API 定义
   - 切片外的模块只能引用该切片的公共 API，而非切片的内部文件结构

6. **切片分组**：
   - 密切相关的切片可以在文件夹中结构化分组
   - 但应遵循与其他切片相同的隔离规则
   - 文件夹内不应有共享代码

## 分段 (Segments) 详解

分段是组织层次结构中的第三级也是最终级别，目的是按技术性质对代码进行分组。

1. **标准化分段名称**：

   - `ui` - 与 UI 显示相关的所有内容：UI 组件、日期格式化程序、样式等
   - `api` - 后端交互：请求函数、数据类型、映射器等
   - `model` - 数据模型：模式、接口、存储和业务逻辑
   - `lib` - 此切片上其他模块需要的库代码
   - `config` - 配置文件和功能标志

2. **自定义分段**：
   - 可以创建自定义分段
   - 最常见的自定义分段位置是 App 层和 Shared 层（不使用切片的层）
   - 分段名称应描述内容的目的，而非本质
   - 例如，`components`、`hooks`和`types`是不好的分段名称，因为它们在查找代码时没有太大帮助

## 公共 API 详解

公共 API 是切片等模块组与使用它的代码之间的"契约"，同时作为"门户"，只允许通过公共 API 访问特定对象。

1. **实现方式**：

   - 通常以带有重新导出(re-exports)的索引文件(index.js)实现
   - 示例：
     ```js
     // pages/auth/index.js
     export { LoginPage } from "./ui/LoginPage";
     export { RegisterPage } from "./ui/RegisterPage";
     ```

2. **好的公共 API 特点**：

   - 保护应用其余部分不受切片内部结构变化（如重构）的影响
   - 当切片行为发生破坏性变化时，公共 API 也应该相应变化
   - 只暴露切片中必要的部分

3. **避免的做法**：

   - 不要使用通配符重新导出所有内容
   - 错误示例：
     ```js
     // ❌ 不好的做法
     export * from "./ui/Comment";
     export * from "./model/comments";
     ```
   - 这会损害切片的可发现性，使集成更加困难，并可能意外暴露模块内部实现

4. **跨导入的公共 API**：

   - 用于同一层不同切片需要互相导入的情况
   - 使用特殊的`@x`符号表示特定切片之间的 API
   - 示例目录结构：
     ```
     📂 entities
       📂 A
         📂 @x
           📄 B.ts  // 专门为entities/B/中的代码提供的API
         📄 index.ts  // 常规公共API
     ```
   - 导入示例：
     ```js
     import type { EntityA } from "entities/A/@x/B";
     ```
   - 注意：尽量减少跨导入，且仅在实体层(Entities)使用此表示法

5. **索引文件的常见问题**：

   - **循环导入**：

     - 当两个或多个文件互相导入形成环路时
     - 可能导致打包器处理困难和运行时错误
     - 避免方法：
       - 同一切片内使用相对导入并写明完整导入路径
       - 不同切片间使用绝对导入(例如使用别名)

   - **大型 bundle 和 Shared 层中的 tree-shaking 问题**：

     - 打包器在处理重新导出所有内容的索引文件时可能难以进行 tree-shaking
     - 特别影响`shared/ui`和`shared/lib`
     - 解决方案：为每个组件或库提供单独的索引文件
     - 示例导入：
       ```js
       import { Button } from "@/shared/ui/button";
       import { TextField } from "@/shared/ui/text-field";
       ```

   - **无法真正防止绕过公共 API**：

     - 索引文件不能真正禁止直接导入
     - 推荐使用 Steiger 等架构检查工具自动捕获这些问题

   - **大型项目中打包器性能降低**：
     - 解决方案：
       - 为`shared/ui`和`shared/lib`中的组件/库使用单独的索引文件
       - 避免在有切片的层的分段中使用索引文件
       - 对于大型项目，考虑拆分为 monorepo 结构，每个包作为独立的 FSD 根目录

## 实际案例：构建 Conduit 应用

为了更好地理解 FSD 的应用，让我们通过一个名为 Conduit 的 Medium 克隆应用来学习。本案例将展示如何将理论应用到实践中。

### 1. 识别页面 - 规划 Pages 层

首先，我们识别应用中的主要页面：

```
📂 pages/
  📁 feed/        // 文章列表（首页）
  📁 sign-in/     // 登录页面
  📁 article-read/ // 文章阅读页面
  📁 article-edit/ // 文章编辑页面
  📁 profile/     // 用户资料页面
  📁 settings/    // 用户设置页面
```

根据 FSD 的导入规则，这些页面不能相互引用代码，因为它们位于同一层级。

### 2. 分析页面细节 - 创建分段

以 Feed 页面（文章列表）为例，我们可以识别出几个动态区域：

1. 登录链接和登录状态指示
2. 标签列表（用于过滤文章）
3. 文章列表（带有点赞按钮）

对于标签列表功能，我们需要：

- 获取可用标签（API 交互）
- 渲染每个标签（用户界面）
- 存储选定的标签（客户端存储）

在 FSD 中，我们按目的使用分段对代码进行分离：

```
📂 pages/feed/
  📂 api/      // 后端交互
    📄 getTags.ts
    📄 getArticles.ts
    📄 likeArticle.ts
  📂 ui/       // 渲染和外观
    📄 TagList.tsx
    📄 ArticleList.tsx
    📄 TabList.tsx
    📄 Pagination.tsx
  📂 model/    // 存储和业务逻辑
    📄 store.ts
    📄 selectors.ts
```

### 3. 提取共享代码 - 使用 Shared 层

某些代码在整个应用中保持不变：UI 组件库、API 客户端配置等。这些代码放在 Shared 层中：

```
📂 shared/
  📂 ui/       // UI组件库
    📄 Button.tsx
    📄 Input.tsx
    📄 Modal.tsx
  📂 api/      // API客户端配置
    📄 apiClient.ts
    📄 endpoints.ts
  📂 config/   // 环境变量解析
    📄 env.ts
  📂 i18n/     // 语言支持配置
    📄 config.ts
  📂 router/   // 路由原语和常量
    📄 routes.ts
```

Shared 层不同于其他层，因为它直接包含分段而非切片。分段的命名应该描述目的（为什么），而非本质（是什么）。避免使用"components"、"hooks"等名称，因为它们没有传达内容的用途。

### 4. 定义公共 API - 创建索引文件

每个切片或分段需要定义一个公共 API，通常通过`index.js`文件实现：

```
// pages/feed/index.js
export { FeedPage } from "./ui/FeedPage";
export { loader } from "./api/loader";

// shared/ui/index.js
export { Button } from "./Button";
export { Input } from "./Input";
export { Modal } from "./Modal";
```

对于 Shared 层，通常为每个分段定义单独的公共 API，而不是为整个 Shared 层定义一个索引。

### 5. 处理 UI 大型重用块 - Widgets 层

对于在多个页面中重用的大型 UI 块（如页眉），我们使用 Widgets 层。例如，一个简单的页眉可能包含：

```
📂 widgets/
  📂 header/
    📂 ui/
      📄 Header.tsx
      📄 Logo.tsx
      📄 Navigation.tsx
    📂 api/
      📄 getUserStatus.ts
    📄 index.ts
```

由于页眉非常简单，只需要请求 API 来确定用户是否已登录，因此可以仅从 Shared 层导入。

### 6. 实际代码示例 - 文章编辑页面

以下是文章编辑页面的实现示例：

```tsx
// pages/article-edit/ui/ArticleEditPage.tsx
import { useActionData, useLoaderData } from "@remix-run/react";
import { type loader } from "../api/loader";
import { FormErrors } from "./FormErrors";
import { TagsInput } from "./TagsInput";

export function ArticleEditPage() {
  const { article } = useLoaderData<typeof loader>();
  const isEditMode = article != null;

  return (
    <div className="editor-page">
      <div className="container page">
        <div className="row">
          <div className="col-md-10 offset-md-1 col-xs-12">
            <FormErrors />
            <form method="post">
              <fieldset>
                <fieldset className="form-group">
                  <input
                    type="text"
                    className="form-control form-control-lg"
                    placeholder="Article Title"
                    name="title"
                    defaultValue={article?.article.title}
                  />
                </fieldset>
                <fieldset className="form-group">
                  <input
                    type="text"
                    className="form-control"
                    placeholder="What's this article about?"
                    name="description"
                    defaultValue={article?.article.description}
                  />
                </fieldset>
                <fieldset className="form-group">
                  <textarea
                    className="form-control"
                    rows={8}
                    placeholder="Write your article (in markdown)"
                    name="body"
                    defaultValue={article?.article.body}
                  ></textarea>
                </fieldset>
                <fieldset className="form-group">
                  <TagsInput
                    name="tags"
                    defaultValue={article?.article.tagList}
                  />
                </fieldset>
                <button
                  className="btn btn-lg pull-xs-right btn-primary"
                  type="submit"
                >
                  {isEditMode ? "Update" : "Publish"} Article
                </button>
              </fieldset>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}
```

整个页面以一种干净、模块化的方式组织，遵循 FSD 的原则：

- 表示层在`ui`分段
- 数据获取在`api`分段
- 数据验证和处理在`model`分段
- 通过公共 API（index 文件）导出必要的组件和函数

## 优势

1. **一致性**：

   - 由于结构标准化，项目变得更加一致，使团队更容易加入新成员

2. **面对变更和重构的稳定性**：

   - 一个层上的模块不能使用同一层或上层的其他模块
   - 这允许您进行隔离修改，而不会对应用的其余部分产生不可预见的后果

3. **逻辑的受控重用**：

   - 根据层级，您可以使代码非常可重用或非常局部化
   - 这在遵循**DRY**原则和实用性之间保持平衡

4. **面向业务和用户需求**：

   - 应用按业务领域拆分，命名中鼓励使用业务语言
   - 这样您可以进行有用的产品工作，而无需完全理解项目中所有其他不相关的部分

5. **组件可轻松替换、添加或删除**
6. **架构标准化**
7. **良好的可扩展性**
8. **与开发技术栈无关**
9. **模块间连接可控，避免意外副作用**
10. **面向业务的架构方法论**

## 劣势

1. 相比其他架构解决方案，入门门槛较高
2. 需要团队意识、文化和概念遵守
3. 问题需立即解决，代码问题和概念偏差立即可见

## 增量采用

如果您有现有的代码库并想迁移到 FSD，建议采用以下策略：

1. **打好基础**：

   - 首先逐模块塑造 App 和 Shared 层，创建基础

2. **分布现有 UI**：

   - 使用广泛的笔触将所有现有 UI 分布在 Widgets 和 Pages 之间
   - 即使它们有违反 FSD 规则的依赖关系也没关系

3. **解决问题并提取实体**：
   - 开始逐步解决导入违规问题
   - 提取 Entities，甚至可能提取 Features

建议在重构过程中避免添加新的大型实体，或者只重构项目的某些部分。

## 关键原则

1. **单向依赖**：

   - 高层只能使用低层的功能，不能反向依赖
   - 例如：feature 不能使用 widget 组件

2. **封装性**：

   - 每个切片自包含其状态、UI 和 API 逻辑
   - 降低依赖性，提高可重构性和可复用性

3. **业务导向**：
   - 按业务价值而非技术关注点组织代码

## 采用情况

已被银行、金融科技、电子商务和 B2B 公司等广泛采用。

## Next.js 集成指南

在使用 Next.js 实现 FSD 架构时，需要解决两个主要冲突：

### 1. Pages 层冲突解决方案

#### 推荐方案：根目录 Pages 文件夹

```
├── pages              # Next.js pages 文件夹
├── src
│   ├── app
│   ├── entities
│   ├── features
│   ├── pages          # FSD pages 文件夹
│   ├── shared
│   ├── widgets
```

- 将 Next.js 的 `pages` 文件夹移至项目根目录
- 在 `src` 文件夹内保持 FSD 结构
- 从 Next.js pages 文件夹导入 FSD pages

#### 替代方案：重命名 FSD Pages 层

```
├── app
├── entities
├── features
├── pages              # Next.js pages 文件夹
├── views              # 重命名后的 FSD pages 文件夹
├── shared
├── widgets
```

- 将 FSD 的 `pages` 层重命名为 `views`
- 在项目 README 中记录此更改
- 保持项目结构不与 Next.js 冲突

### 2. App 层处理

#### Next.js 13 以下版本

由于没有显式的 `app` 文件夹，使用 `_app.tsx`：

```tsx
// app/providers/index.tsx
const App = ({ Component, pageProps }: AppProps) => {
  return (
    <Provider1>
      <Provider2>
        <BaseLayout>
          <Component {...pageProps} />
        </BaseLayout>
      </Provider2>
    </Provider1>
  );
};

export default App;
```

在 `_app.tsx` 中导入：

```tsx
// pages/_app.tsx
import "app/styles/index.scss";
export { default } from "app/providers";
```

#### Next.js App Router (13.4+)

```
├── app                # Next.js app 文件夹
├── pages              # Next.js pages 存根文件夹
│   ├── README.md      # 说明此文件夹存在原因
├── src
│   ├── app            # FSD app 文件夹
│   ├── entities
│   ├── features
│   ├── pages          # FSD pages 文件夹
│   ├── shared
│   ├── widgets
```

- 将 Next.js `app` 文件夹移至项目根目录
- 保留 `pages` 存根文件夹以保持兼容性
- 在 `src` 中维护 FSD 结构

### 3. 其他注意事项

1. **中间件处理**：

   - 必须从 `src` 移至项目根目录
   - Next.js 要求中间件位于根目录，紧邻 `app` 或 `pages`

2. **文档维护**：
   - 重要：记录任何结构变更
   - 特别是在重命名 FSD 层时

这种集成方式允许在遵循 Next.js 约束和要求的同时保持 FSD 的架构优势。

## React Query 集成指南

在使用 React Query 时，需要考虑查询键 (Query Keys) 和变更 (Mutations) 的放置位置，以及如何组织请求。

### 1. 查询键 (Query Keys) 存放位置

#### 解决方案 1 (推荐)：按实体拆分

如果项目已按实体划分，且每个请求对应单个实体，最佳方式是按实体组织。

```
└── src/
    ├── entities/
    |     ├── {entity}/
    |    ...     └── api/
    |                 ├── `{entity}.query`      # 包含键和函数的查询工厂
    |                 ├── `get-{entity}`        # 获取实体的函数
   ...                                         # 其他 CRUD 函数
```

如果实体间存在关联，可使用公共 API 进行交叉导入或考虑替代方案。

#### 替代方案：存放在 Shared 层

在实体拆分不适用的情况下，可以考虑以下结构：

```
└── src/
   ...
    └── shared/
          ├── api/
         ...   ├── `queries`                    # 查询工厂
               |      ├── `document.ts`
               |      ├── `background-jobs.ts`
               |     ...
               └──  index.ts
```

### 2. 变更 (Mutations) 插入位置

不建议将变更与查询混合。有两种选择：

#### 选项 1：在使用位置附近的 `api` 段中定义自定义 Hook

```typescript
// @/features/update-post/api/use-update-title.ts
export const useUpdateTitle = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ id, newTitle }) =>
      apiClient
        .patch(`/posts/${id}`, { title: newTitle })
        .then((data) => console.log(data)),

    onSuccess: (newPost) => {
      queryClient.setQueryData(postsQueries.ids(id), newPost);
    },
  });
};
```

#### 选项 2：在其他地方（Shared 或 Entities）定义变更函数，并在组件中直接使用 `useMutation`

```typescript
// 变更函数定义 (例如: @/shared/api/posts.ts)
export const postApi = {
  createPost: async (data: { title: string; userId: number }) => {
    /*...*/
  },
};

// 组件中使用 (@/pages/post-create/ui/post-create-page.tsx)
import { postApi } from "@/shared/api/posts"; // 或 entities/post

export const CreatePost = () => {
  // ...
  const { mutate, isPending } = useMutation({
    mutationFn: postApi.createPost, // 直接引用
  });
  // ...
};
```

### 3. 请求组织：查询工厂 (Query Factory)

查询工厂是一个对象，其键值为返回查询键列表的函数。

- **推荐使用 React Query v5+ 的 `queryOptions` 工具**

```typescript
// @/entities/post/api/post.queries.ts
import { queryOptions } from "@tanstack/react-query";
// ... 其他导入

export const postQueries = {
  all: () => ["posts"],
  lists: () => [...postQueries.all(), "list"],
  list: (page: number, limit: number) =>
    queryOptions({
      queryKey: [...postQueries.lists(), page, limit],
      queryFn: () => getPosts(page, limit),
      placeholderData: keepPreviousData, // 示例选项
    }),
  // ... 其他查询
};
```

**使用示例：**

```typescript
// @/pages/post-page/ui/post-page.tsx
import { postApi } from "@/entities/post"; // 假设查询工厂导出在 postApi 中
import { useQuery } from "@tanstack/react-query";

export const PostPage = () => {
  const { postId } = useParams<Params>();
  const id = parseInt(postId || "");
  const { data: post, isLoading } = useQuery(
    postApi.postQueries.detail({ id })
  ); // 使用查询工厂
  // ...
};
```

**优势：** 结构化、方便访问、易于重新获取 (refetch)。

### 4. 分页处理

类似地使用查询工厂来处理分页请求。

```typescript
// 查询工厂中定义分页查询
export const postQueries = {
  // ...
  list: (page: number, limit: number) =>
    queryOptions({
      queryKey: [...postQueries.lists(), page, limit],
      queryFn: () => getPosts(page, limit),
      placeholderData: keepPreviousData,
    }),
};

// 组件中使用
export const HomePage = () => {
  const [page, setPage] = useState(1);
  const { data, isLoading } = useQuery(
    postApi.postQueries.list(page, 10) // 使用分页查询
  );
  // ...
};
```

### 5. QueryProvider 设置

- 在 `app/providers` 中创建 `QueryProvider` 组件。
- 在 `shared/api` 中创建 `QueryClient` 实例。

```typescript
// @/shared/api/query-client.ts
import { QueryClient } from "@tanstack/react-query";

export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 5 * 60 * 1000, // 5 minutes
      gcTime: 5 * 60 * 1000,
    },
  },
});

// @/app/providers/query-provider.tsx
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ReactNode } from "react";

export const QueryProvider = ({ children }: { children: ReactNode }) => {
  // 可以直接导入 client 或通过 props 传入
  const client = queryClient;
  return (
    <QueryClientProvider client={client}>
      {children}
      {/* 可以添加 ReactQueryDevtools */}
    </QueryClientProvider>
  );
};
```

### 6. 代码生成

虽然存在代码生成工具，但手动方式更灵活。如果使用生成工具，建议将生成的代码放在 `@/shared/api` 目录中。

### 7. API 客户端 (ApiClient)

建议在 `shared/api` 中使用自定义的 `ApiClient` 类来标准化 API 请求处理、日志记录、头部信息和数据交换格式。

```typescript
// @/shared/api/api-client.ts
import { API_URL } from "@/shared/config";

export class ApiClient {
  private baseUrl: string;

  constructor(url: string) {
    this.baseUrl = url;
  }

  private async handleResponse<TResult>(response: Response): Promise<TResult> {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    try {
      return await response.json();
    } catch (error) {
      throw new Error("Error parsing JSON response");
    }
  }

  public async get<TResult = unknown>(
    endpoint: string,
    queryParams?: Record<string, string | number>
  ): Promise<TResult> {
    // ... 实现 GET 请求
  }

  public async post<TResult = unknown, TData = Record<string, unknown>>(
    endpoint: string,
    body: TData
  ): Promise<TResult> {
    // ... 实现 POST 请求
  }
  // ... 其他方法 (PATCH, DELETE)
}

export const apiClient = new ApiClient(API_URL);
```
