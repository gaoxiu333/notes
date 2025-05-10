# zustand

## 创建 Store

```jsx
import { create } from 'zustand'

type State = {
  count: number
  increment: () => void
  reset: () => void
}

// 创建 Store
const useStore = create<State>((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
  reset: () => set({ count: 0 }),
}))
```

## 平面更新

```jsx
const state = useStore() // 获取整个状态对象
const count = useStore((state) => state.count) // 只订阅 count 变化**(优化建议)**

// 平面更新
const increment = useStore((state) => state.increment)

```

**完整示例**

```jsx
import { create } from 'zustand'

type State = {
  firstName: string
  lastName: string
}

type Action = {
  updateFirstName: (firstName: State['firstName']) => void
  updateLastName: (lastName: State['lastName']) => void
}

// Create your store, which includes both state and (optionally) actions
const usePersonStore = create<State & Action>((set) => ({
  firstName: '',
  lastName: '',
  updateFirstName: (firstName) => set(() => ({ firstName: firstName })),
  updateLastName: (lastName) => set(() => ({ lastName: lastName })),
}))

// In consuming app
function App() {
  // "select" the needed state and actions, in this case, the firstName value
  // and the action updateFirstName
  const firstName = usePersonStore((state) => state.firstName)
  const updateFirstName = usePersonStore((state) => state.updateFirstName)

  return (
    <main>
      <label>
        First name
        <input
          // Update the "firstName" state
          onChange={(e) => updateFirstName(e.currentTarget.value)}
          value={firstName}
        />
      </label>

      <p>
        Hello, <strong>{firstName}!</strong>
      </p>
    </main>
  )
}

```

## 深层嵌套对象

- 正常方法：因为是不可变更对象，需要不断的**浅拷贝每一层（像Reux那样）**
    - 注意：zustand 做了优化，第一个级别不需要浅拷贝
    - 禁用自动合并： `set((state)⇒newState,true)`
- 使用middleware： `immer`
- [参考集成文档](https://zustand.docs.pmnd.rs/integrations/immer-middleware)

## 自动创建选择器

写法优化（非必要优化），可以封装 `createSelectors` 或者使用 `createStore`

example: [https://codesandbox.io/p/sandbox/zustand-auto-generate-selectors-forked-rl8v5e](https://codesandbox.io/p/sandbox/zustand-auto-generate-selectors-forked-rl8v5e)

```jsx
import { createStore } from 'zustand'

interface BearState {
  bears: number
  increase: (by: number) => void
  increment: () => void
}

const store = createStore<BearState>((set) => ({
  bears: 0,
  increase: (by) => set((state) => ({ bears: state.bears + by })),
  increment: () => set((state) => ({ bears: state.bears + 1 })),
}))

const useBearStore = createSelectors(store)

// get the property
const bears = useBearStore.use.bears()

// get the action
const increment = useBearStore.use.increment()
```

## TypeScript

https://zustand.docs.pmnd.rs/guides/typescript

## 使用 storage 初始化数据

https://zustand.docs.pmnd.rs/integrations/persisting-store-data

## API & Hook&中间件

https://zustand.docs.pmnd.rs/apis/create-store

- `createStore`
    - 非react环境下使用store

[https://zustand.docs.pmnd.rs/hooks/use-shallow](https://zustand.docs.pmnd.rs/hooks/use-shallow)

https://zustand.docs.pmnd.rs/middlewares/combine

## 中间件

- combine
    - 模块坏store
- devtools
- immer
- persist
- 异步

持久化数据