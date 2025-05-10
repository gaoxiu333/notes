# React TypeScript 规范指南

## 目录
- [简介](#简介)
- [基础类型使用](#基础类型使用)
- [组件类型定义](#组件类型定义)
- [Props 类型定义](#props-类型定义)
- [Hooks 类型定义](#hooks-类型定义)
- [事件处理类型](#事件处理类型)
- [状态管理](#状态管理)
- [常见问题与解决方案](#常见问题与解决方案)
- [代码风格与最佳实践](#代码风格与最佳实践)
- [工具配置](#工具配置)

## 简介

TypeScript 为 React 开发提供了静态类型检查，提高了代码质量和可维护性。本文档提供了在 React 项目中使用 TypeScript 的最佳实践和规范指南。

## 基础类型使用

### 基本类型

```typescript
// 基础类型
const stringVar: string = "Hello";
const numberVar: number = 42;
const booleanVar: boolean = true;
const undefinedVar: undefined = undefined;
const nullVar: null = null;

// 数组
const stringArray: string[] = ["a", "b", "c"];
const numberArray: Array<number> = [1, 2, 3];

// 元组
const tuple: [string, number] = ["age", 25];

// 枚举
enum Direction {
  Up = "UP",
  Down = "DOWN",
  Left = "LEFT",
  Right = "RIGHT"
}

// 对象
interface User {
  name: string;
  age: number;
}

const user: User = {
  name: "张三",
  age: 30
};
```

### 联合类型与交叉类型

```typescript
// 联合类型
type StringOrNumber = string | number;
const id: StringOrNumber = "abc123"; // 或 123

// 交叉类型
interface HasName {
  name: string;
}

interface HasAge {
  age: number;
}

type Person = HasName & HasAge;
const person: Person = { name: "李四", age: 25 };
```

## 组件类型定义

### 函数组件

```typescript
// 使用 React.FC (不推荐)
import React from 'react';

interface GreetingProps {
  name: string;
}

const Greeting: React.FC<GreetingProps> = ({ name }) => {
  return <h1>你好, {name}!</h1>;
};

// 更推荐的方式
const BetterGreeting = ({ name }: GreetingProps) => {
  return <h1>你好, {name}!</h1>;
};
```

### 类组件

```typescript
import React, { Component } from 'react';

interface CounterProps {
  initialCount: number;
}

interface CounterState {
  count: number;
}

class Counter extends Component<CounterProps, CounterState> {
  constructor(props: CounterProps) {
    super(props);
    this.state = {
      count: props.initialCount
    };
  }

  increment = () => {
    this.setState(prevState => ({
      count: prevState.count + 1
    }));
  };

  render() {
    return (
      <div>
        <p>计数: {this.state.count}</p>
        <button onClick={this.increment}>增加</button>
      </div>
    );
  }
}
```

## Props 类型定义

### 必选与可选属性

```typescript
interface UserCardProps {
  name: string;            // 必选
  age: number;             // 必选
  email?: string;          // 可选
  onProfileClick?: () => void; // 可选函数
}

const UserCard = ({ name, age, email, onProfileClick }: UserCardProps) => {
  return (
    <div onClick={onProfileClick}>
      <h2>{name}</h2>
      <p>年龄: {age}</p>
      {email && <p>邮箱: {email}</p>}
    </div>
  );
};
```

### 子组件类型

```typescript
interface ContainerProps {
  children: React.ReactNode;
}

const Container = ({ children }: ContainerProps) => {
  return <div className="container">{children}</div>;
};
```

### 默认 Props

```typescript
interface ButtonProps {
  label: string;
  primary?: boolean;
  disabled?: boolean;
}

const Button = ({ 
  label, 
  primary = false, 
  disabled = false 
}: ButtonProps) => {
  return (
    <button 
      className={primary ? 'primary-button' : 'secondary-button'} 
      disabled={disabled}
    >
      {label}
    </button>
  );
};
```

## Hooks 类型定义

### useState

```typescript
import { useState } from 'react';

// 简单类型
const [count, setCount] = useState<number>(0);

// 复杂类型
interface User {
  id: number;
  name: string;
  email: string;
}

const [user, setUser] = useState<User | null>(null);

// 另一种写法，让 TypeScript 自动推导
const [user, setUser] = useState<User>({
  id: 1,
  name: '王五',
  email: 'wang@example.com'
});
```

### useEffect

```typescript
import { useEffect, useState } from 'react';

interface User {
  id: number;
  name: string;
}

const UserProfile = ({ userId }: { userId: number }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const response = await fetch(`/api/users/${userId}`);
        const data = await response.json();
        setUser(data);
      } catch (error) {
        console.error('Failed to fetch user:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchUser();
  }, [userId]);

  if (loading) return <div>加载中...</div>;
  if (!user) return <div>用户不存在</div>;

  return (
    <div>
      <h1>{user.name}</h1>
      <p>ID: {user.id}</p>
    </div>
  );
};
```

### useRef

```typescript
import { useRef, useEffect } from 'react';

const AutoFocusInput = () => {
  // DOM元素引用
  const inputRef = useRef<HTMLInputElement>(null);
  
  // 普通值引用
  const countRef = useRef<number>(0);

  useEffect(() => {
    // 安全的可选链操作
    inputRef.current?.focus();
    
    // 增加计数，不会触发重新渲染
    countRef.current += 1;
  }, []);

  return (
    <div>
      <input ref={inputRef} type="text" />
      <p>组件渲染次数: {countRef.current}</p>
    </div>
  );
};
```

### useContext

```typescript
import { createContext, useContext, useState } from 'react';

interface ThemeContextType {
  isDark: boolean;
  toggleTheme: () => void;
}

// 创建上下文并提供默认值
const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

// 提供者组件
export const ThemeProvider = ({ children }: { children: React.ReactNode }) => {
  const [isDark, setIsDark] = useState(false);
  
  const toggleTheme = () => {
    setIsDark(prev => !prev);
  };

  const value = { isDark, toggleTheme };
  
  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
};

// 自定义Hook使用上下文
export const useTheme = (): ThemeContextType => {
  const context = useContext(ThemeContext);
  if (context === undefined) {
    throw new Error('useTheme must be used within a ThemeProvider');
  }
  return context;
};

// 使用
const ThemedButton = () => {
  const { isDark, toggleTheme } = useTheme();
  
  return (
    <button
      onClick={toggleTheme}
      style={{
        backgroundColor: isDark ? '#333' : '#f0f0f0',
        color: isDark ? '#fff' : '#000'
      }}
    >
      切换主题
    </button>
  );
};
```

## 事件处理类型

### DOM 事件

```typescript
import React from 'react';

const Form = () => {
  // 鼠标事件
  const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
    console.log('按钮被点击', e.currentTarget);
  };

  // 表单事件
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log('表单提交');
  };

  // 输入事件
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    console.log('输入值:', e.target.value);
  };

  // 键盘事件
  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      console.log('按下回车键');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="text" 
        onChange={handleChange}
        onKeyDown={handleKeyDown}
      />
      <button type="submit" onClick={handleClick}>
        提交
      </button>
    </form>
  );
};
```

### 自定义事件处理器

```typescript
interface ItemProps {
  id: number;
  name: string;
  onItemClick: (id: number, name: string) => void;
}

const Item = ({ id, name, onItemClick }: ItemProps) => {
  return (
    <div onClick={() => onItemClick(id, name)}>
      {name}
    </div>
  );
};

// 使用组件
const ItemList = () => {
  const handleItemClick = (id: number, name: string) => {
    console.log(`选择了项目 ${id}: ${name}`);
  };

  return (
    <div>
      <Item id={1} name="项目1" onItemClick={handleItemClick} />
      <Item id={2} name="项目2" onItemClick={handleItemClick} />
    </div>
  );
};
```

## 状态管理

### 全局状态类型 (使用 Context)

```typescript
import React, { createContext, useContext, useReducer, ReactNode } from 'react';

// 状态接口
interface AppState {
  count: number;
  user: {
    name: string;
    loggedIn: boolean;
  };
}

// 初始状态
const initialState: AppState = {
  count: 0,
  user: {
    name: '',
    loggedIn: false
  }
};

// 动作类型
type Action = 
  | { type: 'INCREMENT' }
  | { type: 'DECREMENT' }
  | { type: 'LOGIN'; payload: string }
  | { type: 'LOGOUT' };

// reducer 函数
const reducer = (state: AppState, action: Action): AppState => {
  switch (action.type) {
    case 'INCREMENT':
      return { ...state, count: state.count + 1 };
    case 'DECREMENT':
      return { ...state, count: state.count - 1 };
    case 'LOGIN':
      return { 
        ...state, 
        user: { name: action.payload, loggedIn: true } 
      };
    case 'LOGOUT':
      return { 
        ...state, 
        user: { name: '', loggedIn: false } 
      };
    default:
      return state;
  }
};

// 创建上下文
interface AppContextProps {
  state: AppState;
  dispatch: React.Dispatch<Action>;
}

const AppContext = createContext<AppContextProps | undefined>(undefined);

// 提供者组件
export const AppProvider = ({ children }: { children: ReactNode }) => {
  const [state, dispatch] = useReducer(reducer, initialState);
  
  return (
    <AppContext.Provider value={{ state, dispatch }}>
      {children}
    </AppContext.Provider>
  );
};

// 自定义Hook
export const useAppContext = () => {
  const context = useContext(AppContext);
  if (context === undefined) {
    throw new Error('useAppContext must be used within an AppProvider');
  }
  return context;
};
```

## 常见问题与解决方案

### 类型断言

```typescript
// 使用 as 断言
const element = document.getElementById('root') as HTMLDivElement;

// 使用尖括号语法 (不推荐用于JSX)
const count = <number>someValue;

// 非空断言
function process(value: string | null) {
  // 断言 value 不为 null
  const length = value!.length;
}
```

### 类型守卫

```typescript
// 类型谓词
interface Bird {
  fly(): void;
  layEggs(): void;
}

interface Fish {
  swim(): void;
  layEggs(): void;
}

function isFish(pet: Fish | Bird): pet is Fish {
  return (pet as Fish).swim !== undefined;
}

function move(pet: Fish | Bird) {
  if (isFish(pet)) {
    // 此时 TypeScript 知道 pet 是 Fish 类型
    pet.swim();
  } else {
    // 此时 TypeScript 知道 pet 是 Bird 类型
    pet.fly();
  }
}

// 使用 instanceof
function logValue(x: Date | string) {
  if (x instanceof Date) {
    console.log(x.toUTCString());
  } else {
    console.log(x.toUpperCase());
  }
}

// 使用 typeof
function padLeft(value: string, padding: string | number) {
  if (typeof padding === "number") {
    return " ".repeat(padding) + value;
  }
  return padding + value;
}
```

### 泛型组件

```typescript
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
}

function List<T>({ items, renderItem }: ListProps<T>) {
  return (
    <ul>
      {items.map((item, index) => (
        <li key={index}>{renderItem(item)}</li>
      ))}
    </ul>
  );
}

// 使用组件
interface User {
  id: number;
  name: string;
}

const users: User[] = [
  { id: 1, name: '张三' },
  { id: 2, name: '李四' }
];

const App = () => (
  <List<User>
    items={users}
    renderItem={(user) => <span>{user.name}</span>}
  />
);
```

## 代码风格与最佳实践

### 避免不良习惯

1. 不启用 `"strict": true` 
2. 使用 `||` 代替 Nullish 合并运算符 `??` 作为默认值
3. 使用 `any` 而不是 `unknown` 处理API响应
4. 使用 `as` 断言替代类型守卫
5. 在测试中过度使用 `as any`
6. 使用可选属性而非通过接口扩展建模组合
7. 使用一个字母的泛型名称
8. 非布尔类型检查 `if (nonboolean)`
9. 使用双感叹号 `if (!!nonboolean)`
10. 使用 `!= null` 检查 `null` 和 `undefined`

### 推荐的实践

```typescript
// 使用联合类型代替可选属性
// 不好的方式
interface User {
  name: string;
  email?: string;
  phone?: string;
}

// 更好的方式
interface UserBase {
  name: string;
}

interface UserWithEmail extends UserBase {
  email: string;
  phone?: never;
}

interface UserWithPhone extends UserBase {
  email?: never;
  phone: string;
}

type User = UserWithEmail | UserWithPhone | UserBase;

// 使用 ?? 而非 ||
// 不好的方式
const count = props.count || 0; // 当 count 为 0 时会返回默认值

// 好的方式
const count = props.count ?? 0; // 只有当 count 为 null 或 undefined 时返回默认值

// 使用 unknown 而非 any
// 不好的方式
const fetchData = async (): Promise<any> => {
  const response = await fetch('/api/data');
  return response.json();
};

// 好的方式
interface ApiResponse {
  id: number;
  name: string;
}

const fetchData = async (): Promise<unknown> => {
  const response = await fetch('/api/data');
  return response.json();
};

// 使用类型守卫安全地使用结果
const getData = async () => {
  const data = await fetchData();
  
  // 类型守卫确保数据结构正确
  if (isApiResponse(data)) {
    console.log(data.name);
  }
};

// 类型守卫函数
function isApiResponse(data: unknown): data is ApiResponse {
  return (
    typeof data === 'object' && 
    data !== null && 
    'id' in data && 
    'name' in data
  );
}
```

## 工具配置

### ESLint 配置

```javascript
// .eslintrc.js
module.exports = {
  env: {
    es6: true,
    node: true,
    jest: true,
  },
  extends: "eslint:recommended",
  parser: "@typescript-eslint/parser",
  plugins: ["@typescript-eslint"],
  parserOptions: {
    ecmaVersion: 2017,
    sourceType: "module",
  },
  rules: {
    indent: ["error", 2],
    "linebreak-style": ["error", "unix"],
    quotes: ["error", "single"],
    "no-console": "warn",
    "no-unused-vars": "off",
    "@typescript-eslint/no-unused-vars": [
      "error",
      { vars: "all", args: "after-used", ignoreRestSiblings: false },
    ],
    "@typescript-eslint/explicit-function-return-type": "warn",
    "no-empty": "warn",
  },
};
```

### tsconfig.json 配置

```json
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": ["src"]
}
```

---

> 参考资料：[React TypeScript Cheatsheets](https://github.com/typescript-cheatsheets/react)
