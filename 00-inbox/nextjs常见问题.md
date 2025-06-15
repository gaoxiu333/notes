---
title: nextjs常见问题
jd_id: J00-20250615-2230
created: 2025-06-15 22:30
updated: 2025-06-15 22:30
type: note
status: draft
tags: []
---

# nextjs 常见问题

## 全局状态

nextjs 分为服务端渲染和客户端渲染，这样就导致全局状态状态、缓存等数据问题

1. 围绕 zustand 全局状态的问题
2. 围绕浏览器 localstorage 数据的问题，因为浏览器渲染当然是会遵循和使用本地的缓存数据，如果服务端渲染肯定用不了，这种思想如何转变
   1. 如何解决 客户端渲染需要先读取 本地存储，然后再渲染出现闪烁的问题
   2. 使用 beforeInteractive 预加载数据，避免闪烁
3. 围绕 react-query 缓存的问题
4. 总结：服务端渲染的数据和客户端渲染的数据如何同步
5. 闪烁问题，next-themes 是如何避免客户端和服务端数据同步时的闪烁问题的
6. Hydrate 注入：Next.js + React Query SSR  注水实现方案）
7. 缓存策略+乐观更新+持久化缓存
8. token 传递的问题：使用 cookie 传递 token 为最佳方案
