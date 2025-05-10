# react typescript 实战

## 参考链接

- [TypeScript Cheatsheets React](https://github.com/typescript-cheatsheets/react)

一些不熟悉的概念/语法

- Record

一些专有 API

- React.Dispatch<React.SetStateAction<number>>
- React.RC/React.FunctionComponent
- HTMLDivElement

工具

- [VS Code 插件](https://marketplace.visualstudio.com/items?itemName=paulshen.paul-typescript-toolkit)
- [插件配置](https://x.com/_paulshen/status/1392915279466745857)

## Example

**有用的 React Prop 类型示例**

适用于接受其他 React 组件作为 props 的组件。

```jsx
export declare interface AppProps {
  children?: React.ReactNode; // 最佳选择，接受任何 React 能渲染的内容
  childrenElement: React.JSX.Element; // 一个单独的 React 元素
  style?: React.CSSProperties; // 用于传递样式 props
  onChange?: React.FormEventHandler<HTMLInputElement>; // 表单事件！泛型参数是 event.target 的类型
  props: Props & React.ComponentPropsWithoutRef<"button">; // 模拟所有 button 元素的 props，并显式不转发其 ref
  props2: Props & React.ComponentPropsWithRef<MyButtonWithForwardRef>; // 模拟 MyButtonWithForwardRef 的所有 props，并显式转发其 ref
}
```

## Function Component

- 通常不声明，使用默认的推断
- `React.FC` 和 `React.RFC` 都应不被推荐

```jsx
type AppProps = {
  message: string;
};

const App = ({ message }: AppProps) => <div>{message}</div>;
const App: React.FC<AppProps> = ({ message }) => <div>{message}</div>;
```

## hooks

- 内容 hooks 比较简单
- 自定义hook 记得使用 `as const`
- useRef 的两种类型，DOM元素和普通对象

```jsx
**// useState**
const [user, setUser] = useState<User | null>(null);
**// useCallback**
const memoizedCallback = useCallback(
  (param1: string, param2: number) => {
    console.log(param1, param2)
    return { ok: true }
  },
  [...],
);
// useRef
const intervalRef = useRef<number | null>(null);
const divRef = useRef<HTMLDivElement>(null);
```

自定义hook

- 记得使用 as const
- [详细请查看](https://fettblog.eu/typescript-react/hooks/#useref)
- 示例
    - [https://github.com/mweststrate/use-st8](https://github.com/mweststrate/use-st8)
    - [https://github.com/palmerhq/the-platform](https://github.com/palmerhq/the-platform)
    - [https://github.com/sw-yx/hooks](https://github.com/sw-yx/hooks)

## 表单和事件

- [常见的表单事件类型](https://react-typescript-cheatsheet.netlify.app/docs/basic/getting-started/forms_and_events#list-of-event-types)

```jsx
 onChange = (e: React.FormEvent<HTMLInputElement>): void => {
    this.setState({ text: e.currentTarget.value });
  };
  render() {
    return (
      <div>
        <input type="text" value={this.state.text} onChange={this.onChange} />
      </div>
    );
  }
```

## ForwardRef

- 涉及 props 类型
- 涉及 HTML 元素类型

```jsx
interface Props {
  children?: ReactNode;
  type: "submit" | "button";
}
export type Ref = HTMLButtonElement;

export const FancyButton = forwardRef<Ref, Props>((props, ref) => (
  <button ref={ref} className="MyClassName" type={props.type}>
    {props.children}
  </button>
));
```

## Children

- 一般为 ReactNode

### 1. 组件定义

```
// 函数组件
type Props = {
  message: string;
  children?: React.ReactNode;
};

const MyComponent: React.FC<Props> = ({ message, children }) => {
  return <div>{message}{children}</div>;
};

// 类组件
type State = { count: number };

class ClassComponent extends React.Component<Props, State> {
  state: State = { count: 0 };
  // ...
}
```

---

### 2. Hooks 类型

```
// useState
const [count, setCount] = useState<number>(0);
const [user, setUser] = useState<User | null>(null);

// useEffect
useEffect(() => {
  // side effect
}, [dependencies]);

// useContext
interface ThemeContextType { theme: 'light' | 'dark' }
const ThemeContext = createContext<ThemeContextType | null>(null);
const theme = useContext(ThemeContext)!; // 使用非空断言

// useRef
const inputRef = useRef<HTMLInputElement>(null);
const timerRef = useRef<number | null>(null);
```

---

### 3. 事件处理

```
// 输入事件
const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
  console.log(e.target.value);
};

// 点击事件
const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
  e.preventDefault();
};

// 表单提交
const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
  e.preventDefault();
};
```

---

### 4. 常见类型工具

```
React.ReactNode          // 任何可渲染内容
React.CSSProperties      // 样式对象类型
React.ComponentProps<typeof Component>  // 获取组件 props 类型
React.ComponentType      // 组件类型（用于HOC）
```

---

### 5. 泛型组件

```
type ListProps<T> = {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
};

function List<T>({ items, renderItem }: ListProps<T>) {
  return <div>{items.map(renderItem)}</div>;
}
```

---

### 6. 高阶组件

```
const withLoading = <P extends object>(
  Component: React.ComponentType<P>
) => {
  return (props: P & { isLoading: boolean }) => {
    return props.isLoading
      ? <Spinner />: <Component {...props as P} />;
  };
};
```

---

### 7. 类型声明扩展

```
// 扩展全局类型
declare global {
  interface Window {
    MY_CUSTOM_API: any;
  }
}

// 扩展模块类型
declare module '*.module.css' {
  const classes: { [key: string]: string };
  export default classes;
}
```

---

### 8. 常用实用类型

```
Partial<Props>            // 所有属性变为可选
Readonly<Props>           // 所有属性变为只读
Pick<Props, 'key1' | 'key2'>  // 选择特定属性
Omit<Props, 'keyToOmit'>  // 排除特定属性
```

---

### 9. Context 类型

```
interface ThemeContextType {
  theme: 'light' | 'dark';
  toggleTheme: () => void;
}

const ThemeContext = createContext<ThemeContextType>({
  theme: 'light',
  toggleTheme: () => {},
});

// Provider 使用
<ThemeContext.Provider value={{ theme, toggleTheme }}>
  {children}
</ThemeContext.Provider>
```

---

### 10. React Router 类型

```
import { RouteComponentProps } from 'react-router-dom';

type RouteParams = {
  id: string;
};

type Props = RouteComponentProps<RouteParams>;

const UserPage: React.FC<Props> = ({ match }) => {
  const userId = match.params.id;
  // ...
};
```

---

### 提示：

1. 安装必要类型包：

```
npm install --save-dev @types/react @types/react-dom
```

1. 使用 `strict: true` 模式以获得完整类型检查
2. 对于第三方库，优先使用 `@types/库名` 类型声明
3. 使用 `as` 断言要谨慎，优先考虑正确的类型声明

保存此速查表，可以帮助快速回忆 React + TypeScript 开发中的常见模式。建议结合具体项目的类型需求进行调整和扩展！