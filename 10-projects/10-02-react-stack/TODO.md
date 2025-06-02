- 添加监控
- 添加单元测试
- seo
- mock 数据
- 优化框架
- 梳理主题，或者尝试动态主题
- 动画？

> 自己的架构总结：
> 按照 FSD
> 1. 就近原则
> 2. 使用段和切片
> 3. 段是什么，怎么定义
> 4. 切片是约定俗成的功能行文件命名后者技术特征的文件命名

## mws

在 nextjs 的客户端中还不支持

**如何解决 客户端渲染需要先读取 本地存储，然后再渲染出现闪烁的问题**！！！
但是 theme 是如何解决闪烁问题的？？？



## 架构问题
1. 使用 FSD
如果一开始就使用 FSD 就会存在特性模块如何分的问题，尤其是 API 的抽象，很难以开始就划分好，没有良好的规范，后期很容易变成交叉引用，最后变成灾难？
2. 使用传统 feature 模式
如果趋势区域稳定，可以逐渐过渡到 FSD吧？

> 项目开始使用传统方式，按照功能和技术点组织架构，项目逐渐复杂，可以考虑使用就近原则向 FSD
> 项目架构设计没有银弹，随着项目的迭代逐渐演变和改进


## 命名规则

## 基本命名风格

### 1. **camelCase（驼峰命名）**

- **格式**：首字母小写，后续单词首字母大写
- **示例**：`userProfile.js`、`handleSubmit.ts`、`apiClient.ts`
- **适用**：JavaScript变量、函数、配置文件

### 2. **PascalCase（帕斯卡命名）**

- **格式**：每个单词首字母都大写
- **示例**：`UserProfile.tsx`、`LoginForm.jsx`、`ApiService.ts`
- **适用**：React组件、类名、构造函数

### 3. **kebab-case（短横线命名）**

- **格式**：单词间用短横线连接，全小写
- **示例**：`user-profile.css`、`login-form.html`、`api-client.js`
- **适用**：CSS文件、HTML文件、某些配置文件

### 4. **snake_case（下划线命名）**

- **格式**：单词间用下划线连接，全小写
- **示例**：`user_profile.py`、`api_config.json`
- **适用**：Python文件、数据库相关、某些配置文件

### 5. **SCREAMING_SNAKE_CASE（全大写下划线）**

- **格式**：全大写，下划线分隔
- **示例**：`API_CONFIG.js`、`CONSTANTS.ts`
- **适用**：常量文件、环境配置

```bash
# 这个能写成一个博客么？
`这是一个非常重要的状态管理策略问题。用户想了解Zustand和React Query的使用场景和边界，这涉及到：
1. 客户端状态 vs 服务端状态的区别
```

## Cookies 和 jwt token

如果坚持使用 jwt token，推荐使用 middlewhere 给服务器组件传递token
）但是 next-theme到底是如何解决的？


## nextjs SSR 服务数据和客户端数据同步解决方案
1. Hydrate 注入（Next.js + React Query SSR 注水实现方案）
2. 缓存策略+乐观更新+持久化缓存

- 没有 commit 规范工具（commitlint）
- - 缺少 React Testing Library 配置



需要 cli、linters 很之前就一直想要的！！


草他们的这个世界
https://github.com/QueroDelivery/frontend-development-guidelines/blob/main/style-guide/README.md
https://github.com/QueroDelivery/frontend-development-guidelines/blob/main/feature-guides/leitura-adicional.md
cli
https://github.com/juntossomosmais/time-out-market/tree/main


## 伪大纲

```markdown
## Architecture(架构)
- [File Name](https://juntossomosmais.github.io/frontend-guideline/#21-file-name)
- [Folder Architecture](https://juntossomosmais.github.io/frontend-guideline/#22-folder-architecture)
- guidelines(指南)
## 架构策略
- 演进路径->随着项目的拓展，简单的基于类型的结构变得难以管理
- 基于类型、基于功能

概念
- SoC（关注点分离）feature 下进行关注点分离，实行按技术进行原子化分组
- - **核心思想**: 在一个模块内部，将不同类型的代码（如 UI、状态管理、API 调用、工具函数等）分离开。

几种常见的文件夹分组模式
**按文件类型分组 (Type-Based Structure)**

- 描述：基于文件的技术性质进行组织，例如在 `src/` 目录下创建顶层的 `components/`、`hooks/`、`services/`、`pages/` 等文件夹。
**按功能/模块分组 (Feature-Based Structure)**

- 描述：基于应用的特性或业务领域来组织文件，例如 `src/features/authentication/`、`src/features/dashboard/`、`src/features/user-profile/`。每个功能文件夹内部再包含其自身的组件、Hooks、服务等。

高级组件结构化：原子设计 (Atomic Design)
原子设计是一种用于创建设计系统的方法论，它将用户界面分解为五个不同的层级，从而构建出系统化、可扩展的 UI 组件库 。
**命名约定：**

- 组件使用帕斯卡命名法 (PascalCase)，例如 `UserProfile.tsx` 。  
    
- 函数、Hooks、变量使用驼峰命名法 (camelCase)，例如 `useFetchData.ts`, `formatDate.ts` 。

再来一个 伪大纲
**1. 按功能/领域组织 (Feature/Domain-Driven Organization):**
**2. 清晰的模块边界和依赖管理 (Clear Module Boundaries and Dependency Management):**
**3. 分离关注点 (Separation of Concerns - SoC):**
**4. 可复用/共享代码的明确位置 (Clear Location for Reusable/Shared Code):**
**5. 命名约定和一致性 (Naming Conventions and Consistency):**
**6. 可测试性 (Testability):**
**7. 可扩展性和可维护性 (Scalability and Maintainability):**

维护指南
- **模块化**: 代码主要组织在 `src` 文件夹下，并按功能模块（features）进行划分，以实现高内聚和低耦合。
- **功能文件夹结构**: 每个功能模块（feature）可以包含 `api`, `assets`, `components`, `hooks`, `stores`, `types`, `utils` 等子文件夹，按需创建。
- **禁止跨功能导入**: 不建议在不同功能模块之间直接导入，应在应用层面组合功能。ESLint 被用来强制执行此规则以及单向代码库架构（共享 -> 功能 -> 应用）。
- **单向代码库架构**: 代码流向应为单向：共享模块 -> 功能模块 -> 应用层

还伪
前端分层

  

## 开发环境

  

1. 工具

2. 配置

3. node版本管理等

  

## React 技术栈

  

1. 文件结构

2. 规范

3. 技术栈推荐

4. 参考文档

5. checklist

  

## 工具链

  

1. eslint

2. git

3. 等

```


另一重要的考虑点：熵减

AI 协助
```
根据社区的 checklist 检查文章的完整性
react Screaming Architecture （尖叫设计模式）


获取 react  最新生态和最佳实践的资源

  

以英文资料为主 确保有深度
```