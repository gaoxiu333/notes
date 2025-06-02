- 添加监控
- 添加单元测试
- seo
- mock 数据
- 优化框架
- 梳理主题，或者尝试动态主题
- 动画？

## 架构问题

## 命名规则

## nextjs SSR 服务数据和客户端数据同步解决方案

草他们的这个世界
https://github.com/QueroDelivery/frontend-development-guidelines/blob/main/style-guide/README.md
https://github.com/QueroDelivery/frontend-development-guidelines/blob/main/feature-guides/leitura-adicional.md
cli
https://github.com/juntossomosmais/time-out-market/tree/main

## 伪大纲

```markdown
伪大纲
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
```
