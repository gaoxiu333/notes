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

---

## 全局状态

Next.js 分为服务端渲染和客户端渲染，这样就导致全局状态、缓存等数据问题。

## 1️⃣ Zustand 全局状态问题

- Zustand 在服务端渲染和客户端渲染的场景下，如何保证全局状态的一致性？
- Zustand 状态持久化时，如何与 `localStorage` 或 `sessionStorage` 配合使用？
- 当服务端渲染无法访问 `localStorage`，客户端需要读取本地缓存，状态如何协调？

---

## 2️⃣ 浏览器 localStorage 数据问题

- 浏览器渲染天然依赖本地缓存，而服务端渲染无法使用，如何在开发思路上理解这两者差异？
- 客户端渲染过程中，先读取 `localStorage`，再渲染页面，容易出现闪烁，如何避免？
- 使用 `<Script strategy="beforeInteractive">` 预加载 `localStorage` 数据，能否彻底解决闪烁问题？有哪些限制？

---

## 3️⃣ React Query 缓存问题

- React Query 的缓存策略应如何设计？
- 缓存数据在多端渲染（SSR + CSR）过程中，如何防止内容不一致或 hydration 警告？
- React Query 的缓存是否适合长期持久化？适合放在哪种本地存储方案中？

---

## 4️⃣ 服务端渲染和客户端渲染数据同步问题

- 服务端渲染返回的数据如何与客户端的缓存或本地状态同步，避免内容闪烁或 hydration 警告？
- 客户端是否应优先以服务端数据为准，再统一同步本地缓存？

---

## 5️⃣ 页面闪烁问题

- `next-themes` 是如何在服务端渲染和客户端渲染切换过程中，避免主题闪烁问题的？
- 它具体在哪个阶段完成主题同步，避免页面跳变？

---

## 6️⃣ Hydrate 注入问题

- Next.js + React Query SSR 中，Hydrate 注水的具体流程是什么？
- Hydrate 注入过程中，服务端数据如何覆盖客户端缓存？顺序和时机是什么？

---

## 7️⃣ 缓存策略、乐观更新与持久化缓存问题

- 前端数据请求与更新过程中，缓存策略应该如何定义？
- 乐观更新（Optimistic Update）在实际场景中，如何与本地缓存和 React Query 缓存协调？
- 缓存是否需要持久化？适合存在哪？持久化缓存和实时数据请求如何权衡？

---

## 8️⃣ Token 传递问题

- 前端 token 传递，为什么 cookie 是最优方案？
- cookie 传递 token 和 `localStorage` / `sessionStorage` 存储 token 相比，有哪些安全性和同步性差异？
- token 传递问题：使用 cookie 传递 token 为最佳方案

---

> [!info]
> **核心思想：区分环境，同步状态**
>
> Next.js 的核心在于它横跨了两个截然不同的运行环境：**服务器（Node.js）** 和 **客户端（浏览器）**。理解这一点是解决所有问题的基础。
>
> - **服务端**：没有 `window`、`document`、`localStorage` 等浏览器特有的 API。它负责为每个请求生成初始的 HTML。
> - **客户端**：拥有完整的浏览器环境。它会"接管"从服务器发送过来的 HTML，并使其具有交互性，这个过程称为 **Hydration (注水)**。
>
> 你遇到的所有问题的本质，都是由于这两个环境之间 **状态和数据不一致** 造成的。因此，解决问题的核心思路就是：**在服务端准备好初始数据，在客户端安全地接收并同步这些数据。**

---

## Zustand 与全局状态

> [!tip] > **Zustand 本身是一个非常轻量级的客户端状态管理库。**

**问题本质**：如果在服务端创建了一个 store，那么这个 store 实例会在多个用户请求之间共享，导致数据污染。

**解决方案**：不要在全局作用域创建唯一的 store 实例，而是在每个请求或每次渲染时，在组件内部创建或初始化 store。

**正确实践：**

1. **为每个请求创建独立的 Store**：在 App Router 中，在组件内部直接使用 `createStore`，确保每次渲染都有一个新的 store 实例。
2. **Context Provider 模式**：创建 Context Provider，在其中初始化 store，并通过 context 传递给子组件，确保服务端每个请求都有独立 store。

```jsx
// bad - 全局共享，会污染
import { create } from 'zustand'
export const useSharedStore = create((set) => ({ ... }))

// good - 在组件内部使用或通过 context
import { createContext, useContext, useRef } from 'react'
import { createStore, useStore } from 'zustand'

const StoreContext = createContext()

export const StoreProvider = ({ children }) => {
  const storeRef = useRef()
  if (!storeRef.current) {
    storeRef.current = createStore((set) => ({ ... }))
  }
  return (
    <StoreContext.Provider value={storeRef.current}>
      {children}
    </StoreContext.Provider>
  )
}

export const useMyStore = (selector) => {
  const store = useContext(StoreContext)
  if (!store) {
    throw new Error('Missing StoreProvider')
  }
  return useStore(store, selector)
}
```

---

## LocalStorage 与浏览器 API

**问题本质**：服务端没有 `localStorage`。在 SSR 期间，任何直接调用 `localStorage` 的代码都会报错。即使在客户端，如果组件在 Hydration 完成前就试图访问 `localStorage` 并根据其值渲染，而服务端渲染的 HTML 没有对应的值，就会出现 mismatch，导致页面闪烁。

> [!example] > **闪烁的原因**：
>
> 1. 服务端渲染：生成一个不带 `localStorage` 数据的 HTML（如默认浅色主题）。
> 2. 客户端接收：浏览器立即渲染这个 HTML。
> 3. 客户端 Hydration：React 执行，组件挂载，代码读到 `localStorage` 中存的是深色主题。
> 4. 客户端重渲染：React 立即将组件更新为深色主题。
>
> 这个从 **浅色 -> 深色** 的快速变化，就是你看到的 **闪烁**。

**解决方案：**

1. **延迟到客户端执行**：将所有依赖 `localStorage` 的逻辑都放在 `useEffect` 中。这样可避免服务端报错，但无法解决闪烁。
2. **避免闪烁的最佳实践**：
   - 提供默认值：服务端和首次客户端渲染时，使用统一的默认值。
   - 使用 `useEffect` 同步状态：只在客户端操作 `localStorage`。
   - 抑制 Hydration 警告：对于明知服务端和客户端会不同的属性（如 `className`），可用 `suppressHydrationWarning`。

> [!info] > **next-themes 的解决方案剖析**
>
> - **Cookie 辅助**：主题信息存储在 Cookie 中，服务端渲染时可读取，生成正确的 HTML，从根源消除闪烁。
> - **脚本阻塞渲染**：内联一小段脚本（用 `next/script` 的 `beforeInteractive` 策略），在页面其他部分渲染前，立即读取 `localStorage` 并设置 `<html>` 的 class。
>
> **`beforeInteractive` 的作用**：让 `<script>` 在页面变得可交互前就加载执行，适用于需要在 CSS 解析和 React Hydration 前改变 DOM 的场景。

---

## React Query 与缓存（@tanstack/react-query）

**问题本质**：React Query 主要是客户端缓存库。要在 Next.js 中实现 SSR/SSG，需要将服务端获取的数据"传递"给客户端缓存，这就是 **Hydration (注水)**。

> [!example] > **Hydration (注水) 的工作流程**：
>
> 1. 服务端获取数据：在服务器组件或 `getServerSideProps` 中，创建 `QueryClient` 实例并预取数据。
> 2. 服务端脱水（Dehydration）：调用 `dehydrate(queryClient)`，序列化缓存。
> 3. 通过 props 传递：将序列化后的 JSON 通过页面 props 传递给客户端。
> 4. 客户端注水（Hydration）：客户端用 `<Hydrate state={dehydratedState}>` 初始化缓存。
>
> **效果**：客户端 React Query 发现需要的数据已在缓存中，避免二次请求。

**缓存策略 + 乐观更新 + 持久化缓存**：

- **缓存策略**（`staleTime`, `cacheTime`）：决定数据新鲜度和缓存保留时长。
- **乐观更新**：数据变更时，UI 立即展示成功状态，失败则回滚。
- **持久化缓存**：通过插件（如 `persistQueryClient`），将缓存持久化到 `localStorage` 或 `sessionStorage`，刷新后仍可用。

---

## Token 传递：为什么 Cookie 是最佳方案

**问题本质**：HTTP 无状态。需要机制在不同请求间识别用户身份。

> [!question] > **几种方案对比：**
>
> - **LocalStorage**：
>   - 优点：简单方便。
>   - 缺点：服务端无法访问，安全性风险（易受 XSS 攻击）。
> - **HTTP Header (Authorization: Bearer ...)**：
>   - 优点：RESTful 标准。
>   - 缺点：服务端数据获取需手动解析和附加，繁琐。
> - **Cookie**：
>   - 优点：自动发送，服务端可用，可设置 HttpOnly/Secure/SameSite，安全性高。

**结论**：

> [!info]
> 由于其 **自动性、服务端可用性** 和 **更高的安全性**，**使用设置了 `HttpOnly` 属性的 Cookie 是在 Next.js 应用中传递 Token 的最佳、也是最安全的方案。**

---

## 总结：本质的回归

- **全局状态 (Zustand)**：核心是 **隔离**。确保每个服务端请求都有独立的 store 实例，避免数据污染。
- **浏览器 API (LocalStorage)**：核心是 **同步与时机**。服务端没有这些 API，通过 `useEffect` 在客户端同步，或通过 Cookie 消除闪烁。
- **数据缓存 (React Query)**：核心是 **传递与复用**。通过 **脱水/注水** 机制，将服务端数据"灌"给客户端缓存，避免二次请求。
- **Token 传递**：核心是 **安全与便捷**。`HttpOnly` Cookie 在安全性和跨环境可用性上，完胜其他方案。

> [!success]
> 理解了这些问题的 **本质**，你就能在面对具体场景时，选择最恰当的策略，而不是仅仅记住零散的解决方案。
