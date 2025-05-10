# useContext

useContext 是 React 提供的一个 Hook，用于直接从上下文中获取共享的数据，而无需逐层通过 props 传递。它通常与 createContext 和 Context Provider 一起使用，用于管理全局状态或跨组件共享数据。

**核心功能**

- `createContext` 创建一个上下文对象，用于存储全局状态或方法
- `useContext` 从上下文获取数据

**使用步骤**

1. 创建 Context
    - 使用 `createContext` 创建一个上下文对象
2. 定义 Provider
    - 创建一个 `ThemeProvider` 组件，用于提供共享的状态和方法
    - value **属性**：定义要共享的数据（如 theme 和 toggleTheme 方法）。
3. 消费 Context
    - 使用 `useContext` 在子组件中获取上下文的值
4. 何时使用？
    - 跨组件共享状态：例如主题、语言、认证信息等
    - 避免繁琐的 props 传递：通过上下文，子组件可以直接访问数据，而无需一层层通过父组件传递 props。

## 示例

```tsx
import React, { createContext, useState, useContext } from 'react';

// 1. 创建 Context
const ThemeContext = createContext();

function ThemeProvider({ children }) {
  // 2. 定义共享的状态和方法
  const [theme, setTheme] = useState('light');

  const toggleTheme = () => {
    setTheme(prevTheme => (prevTheme === 'light' ? 'dark' : 'light'));
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

function ThemeSwitcher() {
  // 3. 使用 useContext 获取上下文
  const { theme, toggleTheme } = useContext(ThemeContext);

  return (
    <div
      style={{
        background: theme === 'light' ? '#fff' : '#333',
        color: theme === 'light' ? '#000' : '#fff',
        padding: '20px',
        textAlign: 'center',
      }}
    >
      <p>当前主题：{theme}</p>
      <button onClick={toggleTheme}>切换主题</button>
    </div>
  );
}

function App() {
  return (
    <ThemeProvider>
      <ThemeSwitcher />
    </ThemeProvider>
  );
}

export default App;
```