---
title: TypeScript类型系统
jd_id: J00-20250615-2025
created: 2025-06-15 20:25
updated: 2025-06-15 20:25
type: note
status: draft
tags: []
---

# 📌 TypeScript 项目类型系统设计规范

> 本篇由 AI 生成，感觉不太实用但是可以稍微补一下空白，仅供参考
> 注意：
> 1. 现在的类型大多数就近原则
> 2. 对于全局的类型，像拓展 vite 的类型、全局变量等，可能还需要再考虑进行一些实践

## 📁 类型目录结构

```
src/
  types/
    api/               # 接口请求/响应相关类型
    models/            # 业务模型
    common/            # 通用基础类型
    third-party/       # 第三方类型封装
    constants/         # 常量对象（替代 enums）
    index.ts           # 汇总导出
```

## 📖 类型划分规则

| 分类    | 说明                | 示例                                     |
| :---- | :---------------- | :------------------------------------- |
| 基础类型  | 通用复用型             | `Pagination`、`ResponseStatus`          |
| 业务模型  | 代表具体业务对象          | `User`、`Order`                         |
| 接口类型  | 与后端接口请求/响应相关      | `UserListRequest`、`UserDetailResponse` |
| 常量类型  | 有限集合值、固定常量对象      | `UserStatus` (as const 对象)             |
| 第三方类型 | 封装外部库类型声明，便于管理与替换 | `AxiosResponse<T>`                     |

## 📙 类型命名规范

* 接口请求类型：`xxxRequest`
* 接口响应类型：`xxxResponse`
* 业务模型类型：`xxxModel`
* 常量对象：`xxx` (as const 对象)
* 常量对象对应类型：`xxxType`

## 📆 接口响应统一封装

```ts
export type ApiResponse<T = any> = {
  code: number;
  message: string;
  data: T;
};
```

## 📚 类型使用规范

* 所有类型集中放置在 `src/types/`
* 禁止在组件、服务内定义临时类型
* 常量对象统一放在 `constants/` 目录
* 第三方类型统一封装在 `third-party/`
* 所有类型通过 `index.ts` 汇总统一导出
* 保留 `constants.ts` 或独立 `constants/` 目录管理常量对象
* 可扩展性良好

## 📦 推荐常量对象写法（替代 enum）

```ts
// constants/user-status.ts
export const UserStatus = {
  ACTIVE: 'active',
  DISABLED: 'disabled',
  PENDING: 'pending',
} as const;

export type UserStatusType = typeof UserStatus[keyof typeof UserStatus];
```

## ✅ 自查 Checklist

* [x] 类型集中放置在 `src/types/`
* [x] 类型按功能模块分类清晰
* [x] 命名规范统一
* [x] 接口响应统一封装 `ApiResponse<T>`
* [x] 禁止组件/服务内定义临时类型
* [x] 常量对象集中管理
* [x] 第三方类型封装
* [x] 类型集中导出
* [x] 常量对象用 as const 替代 enum
* [x] 可扩展性良好

