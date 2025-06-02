# TypeScript React 快速参考手册

> 这是基于[React TypeScript Cheat Sheet](https://react-typescript-cheatsheet.netlify.app/)的备忘录

## 📚 目录

- [基础设置](#基础设置)
- [组件类型定义](#组件类型定义)
- [Props 类型模式](#props-类型模式)
- [Hooks 类型使用](#hooks-类型使用)
- [事件处理](#事件处理)
- [高级模式](#高级模式)
- [实用工具类型](#实用工具类型)
- [故障排除](#故障排除)

---

## 基础设置

### 项目初始化

```bash
# 使用 Create React App
npx create-react-app my-app --template typescript

# 或使用 Vite
npm create vite@latest my-app -- --template react-ts
```

### 基本 tsconfig.json 配置

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["DOM", "DOM.Iterable", "ES6"],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
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

## 组件类型定义

### 函数组件（推荐）

```tsx
// 基本函数组件
interface Props {
  name: string;
  age?: number;
}

const UserCard = ({ name, age = 18 }: Props) => {
  return (
    <div>
      <h2>{name}</h2>
      <p>年龄: {age}</p>
    </div>
  );
};

// 使用 React.FC（可选，但不是必须的）
const UserCard: React.FC<Props> = ({ name, age = 18 }) => {
  return (
    <div>
      <h2>{name}</h2>
      <p>年龄: {age}</p>
    </div>
  );
};
```

### 类组件

```tsx
interface Props {
  title: string;
}

interface State {
  count: number;
}

class Counter extends React.Component<Props, State> {
  state: State = {
    count: 0,
  };

  increment = () => {
    this.setState((state) => ({ count: state.count + 1 }));
  };

  render() {
    return (
      <div>
        <h2>{this.props.title}</h2>
        <p>计数: {this.state.count}</p>
        <button onClick={this.increment}>增加</button>
      </div>
    );
  }
}
```

---

## Props 类型模式

### 基础类型集合

```tsx
interface ComponentProps {
  // 基础类型
  message: string;
  count: number;
  isVisible: boolean;
  tags: string[];

  // 对象类型
  user: {
    id: number;
    name: string;
    email?: string;
  };

  // 对象数组
  users: Array<{
    id: number;
    name: string;
  }>;

  // 字符串字面量联合
  status: "loading" | "success" | "error";

  // 可选属性
  className?: string;

  // 函数类型
  onClick: () => void;
  onUserSelect: (user: User) => void;
  onChange: (value: string) => void;
}
```

### Children 类型

```tsx
interface Props {
  // 最常用：接受任何可渲染内容
  children: React.ReactNode;

  // 只接受单个 React 元素
  children: React.ReactElement;

  // 函数作为 children
  children: (data: string) => React.ReactNode;

  // 可选 children
  children?: React.ReactNode;
}

// 使用示例
const Container = ({ children }: { children: React.ReactNode }) => (
  <div className="container">{children}</div>
);
```

### 样式和事件 Props

```tsx
interface StyleProps {
  // CSS 样式对象
  style?: React.CSSProperties;

  // CSS 类名
  className?: string;

  // 事件处理器
  onClick?: React.MouseEventHandler<HTMLButtonElement>;
  onChange?: React.ChangeEventHandler<HTMLInputElement>;
  onSubmit?: React.FormEventHandler<HTMLFormElement>;
}
```

### 继承 HTML 属性

```tsx
// 继承 button 的所有原生属性
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary";
  loading?: boolean;
}

const Button = ({
  variant = "primary",
  loading,
  children,
  ...props
}: ButtonProps) => (
  <button
    className={`btn btn-${variant} ${loading ? "loading" : ""}`}
    disabled={loading}
    {...props}
  >
    {children}
  </button>
);

// 使用 ComponentProps 提取现有组件的 props
type MyButtonProps = React.ComponentProps<typeof Button>;
```

---

## Hooks 类型使用

### useState

```tsx
// 基础类型自动推断
const [count, setCount] = useState(0); // number
const [name, setName] = useState(""); // string

// 联合类型
const [status, setStatus] = useState<"idle" | "loading" | "error">("idle");

// 对象状态
interface User {
  id: number;
  name: string;
  email: string;
}

const [user, setUser] = useState<User | null>(null);

// 数组状态
const [items, setItems] = useState<string[]>([]);

// 使用类型断言（谨慎使用）
const [user, setUser] = useState<User>({} as User);
```

### useRef

```tsx
// DOM 元素引用
const inputRef = useRef<HTMLInputElement>(null);

useEffect(() => {
  if (inputRef.current) {
    inputRef.current.focus();
  }
}, []);

// 可变值引用
const countRef = useRef<number>(0);
const timerRef = useRef<NodeJS.Timeout | null>(null);

// 确保非空的 ref（谨慎使用）
const divRef = useRef<HTMLDivElement>(null!);
```

### useCallback 和 useMemo

```tsx
// useCallback
const handleClick = useCallback((id: number) => {
  console.log("Clicked:", id);
}, []);

const handleSubmit = useCallback((event: React.FormEvent<HTMLFormElement>) => {
  event.preventDefault();
  // 处理提交
}, []);

// useMemo
const expensiveValue = useMemo(() => computeExpensiveValue(data), [data]);

const sortedUsers = useMemo(
  (): User[] => users.sort((a, b) => a.name.localeCompare(b.name)),
  [users]
);
```

### useReducer

```tsx
interface State {
  count: number;
  loading: boolean;
}

type Action =
  | { type: "increment" }
  | { type: "decrement" }
  | { type: "setLoading"; payload: boolean }
  | { type: "reset"; payload: number };

const reducer = (state: State, action: Action): State => {
  switch (action.type) {
    case "increment":
      return { ...state, count: state.count + 1 };
    case "decrement":
      return { ...state, count: state.count - 1 };
    case "setLoading":
      return { ...state, loading: action.payload };
    case "reset":
      return { ...state, count: action.payload };
    default:
      return state;
  }
};

const Counter = () => {
  const [state, dispatch] = useReducer(reducer, { count: 0, loading: false });

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: "increment" })}>+</button>
      <button onClick={() => dispatch({ type: "decrement" })}>-</button>
    </div>
  );
};
```

### useContext

```tsx
// 创建 Context
interface ThemeContextType {
  theme: "light" | "dark";
  toggleTheme: () => void;
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

// 自定义 Hook 确保类型安全
const useTheme = () => {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error("useTheme must be used within a ThemeProvider");
  }
  return context;
};

// Provider 组件
const ThemeProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [theme, setTheme] = useState<"light" | "dark">("light");

  const toggleTheme = () => {
    setTheme((prev) => (prev === "light" ? "dark" : "light"));
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};
```

### 自定义 Hooks

```tsx
// 自定义 Hook 示例
function useLocalStorage<T>(key: string, initialValue: T) {
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      return initialValue;
    }
  });

  const setValue = (value: T | ((val: T) => T)) => {
    try {
      const valueToStore =
        value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(error);
    }
  };

  return [storedValue, setValue] as const;
}

// 使用
const [name, setName] = useLocalStorage<string>("name", "");
```

---

## 事件处理

### 常见事件类型

```tsx
const EventExamples = () => {
  // 鼠标事件
  const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
    console.log("Button clicked", e.currentTarget);
  };

  // 键盘事件
  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      console.log("Enter pressed");
    }
  };

  // 表单事件
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    console.log("Input value:", e.target.value);
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log("Form submitted");
  };

  // 焦点事件
  const handleFocus = (e: React.FocusEvent<HTMLInputElement>) => {
    console.log("Input focused");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        onChange={handleChange}
        onKeyPress={handleKeyPress}
        onFocus={handleFocus}
      />
      <button onClick={handleClick}>提交</button>
    </form>
  );
};
```

### 事件处理器类型定义方式

```tsx
interface Props {
  // 方式 1: 直接定义函数签名
  onClick: (event: React.MouseEvent<HTMLButtonElement>) => void;

  // 方式 2: 使用 React 提供的事件处理器类型
  onClick: React.MouseEventHandler<HTMLButtonElement>;
  onChange: React.ChangeEventHandler<HTMLInputElement>;
  onSubmit: React.FormEventHandler<HTMLFormElement>;
}
```

### 表单处理

```tsx
interface FormData {
  email: string;
  password: string;
}

const LoginForm = () => {
  const [formData, setFormData] = useState<FormData>({
    email: "",
    password: "",
  });

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    // 类型断言访问表单字段
    const target = e.target as typeof e.target & {
      email: { value: string };
      password: { value: string };
    };

    const email = target.email.value;
    const password = target.password.value;

    console.log({ email, password });
  };

  const handleChange =
    (field: keyof FormData) => (e: React.ChangeEvent<HTMLInputElement>) => {
      setFormData((prev) => ({
        ...prev,
        [field]: e.target.value,
      }));
    };

  return (
    <form onSubmit={handleSubmit}>
      <input
        name="email"
        type="email"
        value={formData.email}
        onChange={handleChange("email")}
      />
      <input
        name="password"
        type="password"
        value={formData.password}
        onChange={handleChange("password")}
      />
      <button type="submit">登录</button>
    </form>
  );
};
```

---

## 高级模式

### 泛型组件

```tsx
// 基础泛型组件
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

// 使用泛型组件
const UserList = () => {
  const users = [
    { id: 1, name: "Alice" },
    { id: 2, name: "Bob" },
  ];

  return <List items={users} renderItem={(user) => <span>{user.name}</span>} />;
};

// 带约束的泛型
interface SelectProps<T extends { id: string | number; label: string }> {
  options: T[];
  value?: T;
  onChange: (option: T) => void;
}

function Select<T extends { id: string | number; label: string }>({
  options,
  value,
  onChange,
}: SelectProps<T>) {
  return (
    <select
      value={value?.id}
      onChange={(e) => {
        const option = options.find(
          (opt) => opt.id.toString() === e.target.value
        );
        if (option) onChange(option);
      }}
    >
      {options.map((option) => (
        <option key={option.id} value={option.id}>
          {option.label}
        </option>
      ))}
    </select>
  );
}
```

### 条件类型和类型收窄

```tsx
// 条件渲染的类型处理
interface LoadingProps {
  loading: true;
}

interface LoadedProps {
  loading: false;
  data: string[];
}

type DataComponentProps = LoadingProps | LoadedProps;

const DataComponent = (props: DataComponentProps) => {
  if (props.loading) {
    return <div>Loading...</div>;
  }

  // TypeScript 知道这里 props.loading 是 false，所以 data 可用
  return (
    <ul>
      {props.data.map((item) => (
        <li key={item}>{item}</li>
      ))}
    </ul>
  );
};

// 使用判别联合类型
type ApiResponse<T> =
  | { status: "loading" }
  | { status: "error"; error: string }
  | { status: "success"; data: T };

const ApiComponent = <T,>({ response }: { response: ApiResponse<T> }) => {
  switch (response.status) {
    case "loading":
      return <div>Loading...</div>;
    case "error":
      return <div>Error: {response.error}</div>;
    case "success":
      return <div>Data loaded: {JSON.stringify(response.data)}</div>;
  }
};
```

### 多态组件（as prop）

```tsx
interface BoxProps {
  as?: React.ElementType;
  children: React.ReactNode;
  className?: string;
}

const Box = ({ as: Component = "div", children, ...props }: BoxProps) => {
  return <Component {...props}>{children}</Component>;
};

// 使用
const Example = () => (
  <div>
    <Box>默认 div</Box>
    <Box as="span">span 元素</Box>
    <Box as="button" onClick={() => console.log("clicked")}>
      button 元素
    </Box>
  </div>
);
```

### 包装组件

```tsx
// 包装 HTML 元素
interface CustomButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary";
  size?: "small" | "medium" | "large";
}

const CustomButton = ({
  variant = "primary",
  size = "medium",
  className = "",
  children,
  ...props
}: CustomButtonProps) => {
  const classes = `btn btn-${variant} btn-${size} ${className}`.trim();

  return (
    <button className={classes} {...props}>
      {children}
    </button>
  );
};

// 包装其他组件
interface EnhancedComponentProps
  extends React.ComponentProps<typeof SomeComponent> {
  enhanced?: boolean;
}

const EnhancedComponent = ({ enhanced, ...props }: EnhancedComponentProps) => {
  if (enhanced) {
    return (
      <div className="enhanced">
        <SomeComponent {...props} />
      </div>
    );
  }
  return <SomeComponent {...props} />;
};
```

---

## 实用工具类型

### React 内置工具类型

```tsx
// 提取组件的 props 类型
type ButtonProps = React.ComponentProps<"button">;
type CustomComponentProps = React.ComponentProps<typeof CustomComponent>;

// ref 相关
type ButtonPropsWithRef = React.ComponentPropsWithRef<"button">;
type ButtonPropsWithoutRef = React.ComponentPropsWithoutRef<"button">;

// 元素类型
type ButtonElement = React.ReactElement<React.ComponentProps<"button">>;

// CSS 属性
const styles: React.CSSProperties = {
  backgroundColor: "#f0f0f0",
  padding: "1rem",
  borderRadius: "4px",
};

// 事件类型提取
type InputChangeEvent = React.ChangeEvent<HTMLInputElement>;
type ButtonClickEvent = React.MouseEvent<HTMLButtonElement>;
```

### 自定义工具类型

```tsx
// 让所有属性可选
type Partial<T> = {
  [P in keyof T]?: T[P];
};

// 让所有属性必选
type Required<T> = {
  [P in keyof T]-?: T[P];
};

// 选择特定属性
type Pick<T, K extends keyof T> = {
  [P in K]: T[P];
};

// 排除特定属性
type Omit<T, K extends keyof T> = Pick<T, Exclude<keyof T, K>>;

// 实用示例
interface User {
  id: number;
  name: string;
  email: string;
  password: string;
}

type PublicUser = Omit<User, "password">; // 排除密码
type UserUpdate = Partial<Pick<User, "name" | "email">>; // 只能更新名字和邮箱，且都是可选的
type NewUser = Omit<User, "id">; // 创建用户时不需要 id

// 深度 Partial
type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};

// 非空类型
type NonNullable<T> = T extends null | undefined ? never : T;
```

### 条件类型

```tsx
// 基础条件类型
type IsString<T> = T extends string ? true : false;

// 提取函数返回类型
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

// 提取数组元素类型
type ArrayElement<T> = T extends (infer U)[] ? U : never;

// 实用示例
type ApiFunction = () => Promise<{ data: string; status: number }>;
type ApiReturnType = ReturnType<ApiFunction>; // Promise<{ data: string; status: number }>

type StringArray = string[];
type StringType = ArrayElement<StringArray>; // string
```

---

## 故障排除

### 常见错误和解决方案

#### 1. Object is possibly 'null' 错误

```tsx
// 错误示例
const Component = () => {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // 错误：Object is possibly 'null'
    ref.current.focus();
  }, []);
};

// 解决方案 1：类型检查
const Component = () => {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (ref.current) {
      ref.current.focus();
    }
  }, []);
};

// 解决方案 2：非空断言（确定不为 null 时使用）
const Component = () => {
  const ref = useRef<HTMLDivElement>(null!);

  useEffect(() => {
    ref.current.focus(); // 不会报错，但要确保 ref 已赋值
  }, []);
};
```

#### 2. 函数参数隐式 any 类型

```tsx
// 错误示例
const handleClick = useCallback((e) => {
  // 参数 'e' 隐式具有 'any' 类型
  console.log(e.target);
}, []);

// 解决方案：明确指定参数类型
const handleClick = useCallback((e: React.MouseEvent<HTMLButtonElement>) => {
  console.log(e.target);
}, []);

// 或使用事件处理器类型
const handleClick: React.MouseEventHandler<HTMLButtonElement> = useCallback(
  (e) => {
    console.log(e.target);
  },
  []
);
```

#### 3. 类型 {} 缺少属性

```tsx
// 错误示例
interface User {
  id: number;
  name: string;
}

const user: User = {}; // 错误：类型 '{}' 缺少类型 'User' 中的属性

// 解决方案 1：提供所有必需属性
const user: User = {
  id: 1,
  name: "John",
};

// 解决方案 2：使用 Partial
const partialUser: Partial<User> = {};

// 解决方案 3：类型断言（谨慎使用）
const user = {} as User;
```

#### 4. 联合类型属性访问错误

```tsx
// 错误示例
type Response =
  | { status: "success"; data: string }
  | { status: "error"; message: string };

const handleResponse = (response: Response) => {
  // 错误：类型上不存在属性 'data'
  console.log(response.data);
};

// 解决方案：使用类型守卫
const handleResponse = (response: Response) => {
  if (response.status === "success") {
    console.log(response.data); // 现在可以访问 data
  } else {
    console.log(response.message); // 这里可以访问 message
  }
};
```

### 性能优化相关类型

```tsx
// memo 的类型使用
interface Props {
  name: string;
  items: string[];
}

const MemoizedComponent = React.memo<Props>(({ name, items }) => {
  return (
    <div>
      <h3>{name}</h3>
      <ul>
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </div>
  );
});

// 自定义比较函数
const MemoizedWithCustomCompare = React.memo<Props>(
  ({ name, items }) => {
    return (
      <div>
        <h3>{name}</h3>
        <ul>
          {items.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      </div>
    );
  },
  (prevProps, nextProps) => {
    return (
      prevProps.name === nextProps.name &&
      prevProps.items.length === nextProps.items.length
    );
  }
);

// forwardRef 的类型
interface ButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
}

const FancyButton = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ children, onClick }, ref) => (
    <button ref={ref} className="fancy-button" onClick={onClick}>
      {children}
    </button>
  )
);

// 使用 forwardRef 组件
const Parent = () => {
  const buttonRef = useRef<HTMLButtonElement>(null);

  return <FancyButton ref={buttonRef}>Click me</FancyButton>;
};
```

### 最佳实践建议

#### 1. 优先使用类型推断

```tsx
// 好：利用类型推断
const [count, setCount] = useState(0); // 自动推断为 number
const [items, setItems] = useState<string[]>([]); // 需要明确指定

// 避免：不必要的类型注解
const [count, setCount] = useState<number>(0); // 冗余的类型注解
```

#### 2. 使用 const assertions

```tsx
// 好：使用 const assertions
const themes = ["light", "dark"] as const;
type Theme = (typeof themes)[number]; // 'light' | 'dark'

const config = {
  api: {
    baseUrl: "https://api.example.com",
    version: "v1",
  },
} as const;

// 避免：丢失字面量类型
const themes = ["light", "dark"]; // string[]
```

#### 3. 合理使用 unknown 代替 any

```tsx
// 好：使用 unknown 进行类型检查
const processApiResponse = (response: unknown) => {
  if (typeof response === "object" && response !== null && "data" in response) {
    const data = (response as { data: any }).data;
    return data;
  }
  throw new Error("Invalid response format");
};

// 避免：直接使用 any
const processApiResponse = (response: any) => {
  return response.data; // 失去类型安全
};
```

#### 4. 创建可复用的类型定义

```tsx
// 创建通用类型文件 types/common.ts
export interface ApiResponse<T> {
  data: T;
  message: string;
  status: number;
}

export interface PaginatedResponse<T> extends ApiResponse<T[]> {
  pagination: {
    page: number;
    limit: number;
    total: number;
  };
}

export type AsyncState<T> =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; error: string };

// 在组件中使用
import { ApiResponse, AsyncState } from "../types/common";

interface User {
  id: number;
  name: string;
  email: string;
}

const UserComponent = () => {
  const [userState, setUserState] = useState<AsyncState<User>>({
    status: "idle",
  });

  // ...组件逻辑
};
```

#### 5. 环境声明文件

```tsx
// types/global.d.ts - 全局类型声明
declare global {
  interface Window {
    gtag: (...args: any[]) => void;
  }
}

// types/modules.d.ts - 模块声明
declare module "*.svg" {
  const content: React.FunctionComponent<React.SVGAttributes<SVGElement>>;
  export default content;
}

declare module "*.module.css" {
  const classes: { readonly [key: string]: string };
  export default classes;
}

// types/api.d.ts - API 相关类型
export interface ApiError {
  code: string;
  message: string;
  details?: Record<string, any>;
}

export interface ApiConfig {
  baseURL: string;
  timeout: number;
  headers?: Record<string, string>;
}
```

---

## 📖 扩展阅读

- [TypeScript 官方文档](https://www.typescriptlang.org/docs/)
- [React TypeScript 官方文档](https://react.dev/learn/typescript)
- [@types/react 源码](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/react)
- [TypeScript 实用工具类型](https://www.typescriptlang.org/docs/handbook/utility-types.html)

---

## 🎯 总结

这份 cheatsheet 涵盖了 TypeScript + React 开发中最常见的模式和最佳实践：

- **基础设置**：项目配置和基本组件类型定义
- **Props 模式**：覆盖各种 props 类型定义场景
- **Hooks 使用**：每个常用 Hook 的类型处理方法
- **事件处理**：表单和用户交互的类型安全处理
- **高级模式**：泛型、条件类型、多态组件等高级用法
- **工具类型**：提高开发效率的实用类型工具
- **故障排除**：常见问题的解决方案和最佳实践

记住：TypeScript 的目标是让代码更安全、更易维护。刚开始可能觉得复杂，但随着经验积累，你会发现它让开发过程更加高效和可靠！
