# React 项目 Feature-Sliced Design (FSD) 结构规范

## 项目结构总览

```
📦 src
 ┣ 📂 app                  # 应用入口
 ┣ 📂 processes            # 跨页面流程 (可选)
 ┣ 📂 pages                # 页面
 ┣ 📂 widgets              # 可重用UI块
 ┣ 📂 features             # 功能
 ┣ 📂 entities             # 业务实体
 ┗ 📂 shared               # 共享代码
```

## 一、基本规则

1. **单向依赖原则**: 各层只能导入位于自己层级之下的模块，不能导入同级或上级模块
2. **层级封装**: 每一层的切片应高内聚、低耦合，对外暴露清晰的公共API
3. **按业务领域而非技术关注点组织代码**

## 二、层级定义与内容

### 1. App (应用层)

- **职责**: 应用初始化、全局提供者、路由设置、全局样式
- **常见分段**:
  - `app/providers/` - React Context提供者
  - `app/styles/` - 全局样式设置
  - `app/router/` - React Router配置
  - `app/store/` - Redux 根存储设置

```jsx
// app/providers/index.tsx 示例
import { QueryProvider } from './query';
import { StoreProvider } from './store';
import { ThemeProvider } from './theme';

export const AppProviders = ({ children }) => (
  <QueryProvider>
    <StoreProvider>
      <ThemeProvider>
        {children}
      </ThemeProvider>
    </StoreProvider>
  </QueryProvider>
);
```

### 2. Pages (页面层)

- **职责**: 定义应用的路由页面
- **组织**: 每个页面一个切片，不同页面间不应相互依赖
- **常见分段**:
  - `ui/` - 页面组件
  - `model/` - 页面状态逻辑
  - `api/` - 页面数据获取

```jsx
// pages/article-edit/ui/ArticleEditPage.tsx 示例
import { useLoaderData } from 'react-router-dom';
import { EditForm } from '../ui/EditForm';
import { TagsInput } from 'features/tags';
import { Button } from 'shared/ui/button';

export function ArticleEditPage() {
  const { article } = useLoaderData();
  return (
    <div className="editor-page">
      <EditForm defaultValues={article} />
    </div>
  );
}
```

### 3. Widgets (组件层)

- **职责**: 复杂UI块，可在多个页面复用
- **组织**: 每个组件块一个切片
- **常见分段**:
  - `ui/` - 组件UI
  - `model/` - 组件状态逻辑

```jsx
// widgets/header/ui/Header.tsx 示例
import { Logo } from './Logo';
import { Navigation } from './Navigation';
import { UserMenu } from 'features/auth';

export function Header() {
  return (
    <header>
      <Logo />
      <Navigation />
      <UserMenu />
    </header>
  );
}
```

### 4. Features (功能层)

- **职责**: 实现具体业务功能，如登录、点赞等
- **组织**: 每个功能一个切片
- **常见分段**:
  - `ui/` - 功能UI组件
  - `model/` - 功能业务逻辑
  - `api/` - 功能API交互

```jsx
// features/auth/ui/LoginForm.tsx 示例
import { useForm } from 'react-hook-form';
import { useLoginMutation } from '../api/login';
import { Button } from 'shared/ui/button';
import { TextField } from 'shared/ui/text-field';

export function LoginForm() {
  const { register, handleSubmit } = useForm();
  const login = useLoginMutation();
  
  const onSubmit = (data) => {
    login.mutate(data);
  };
  
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <TextField {...register('email')} label="邮箱" />
      <TextField {...register('password')} type="password" label="密码" />
      <Button type="submit" loading={login.isLoading}>登录</Button>
    </form>
  );
}
```

### 5. Entities (实体层)

- **职责**: 定义业务实体，如用户、文章等
- **组织**: 每个实体一个切片
- **常见分段**:
  - `ui/` - 实体UI组件
  - `model/` - 实体类型和状态逻辑
  - `api/` - 实体API交互

```jsx
// entities/article/ui/ArticleCard.tsx 示例
import { format } from 'date-fns';
import { Link } from 'react-router-dom';
import type { Article } from '../model/types';

interface ArticleCardProps {
  article: Article;
}

export function ArticleCard({ article }: ArticleCardProps) {
  return (
    <div className="article-card">
      <h2>{article.title}</h2>
      <p>{article.description}</p>
      <span>{format(new Date(article.createdAt), 'yyyy-MM-dd')}</span>
      <Link to={`/articles/${article.id}`}>阅读更多</Link>
    </div>
  );
}
```

### 6. Shared (共享层)

- **职责**: 共享UI组件、工具函数、API客户端等
- **组织**: 直接按分段组织，无切片
- **常见分段**:
  - `ui/` - UI组件库
  - `api/` - API客户端配置
  - `lib/` - 工具函数
  - `config/` - 环境配置

```jsx
// shared/ui/button/index.tsx 示例
import cn from 'classnames';
import './Button.css';

export type ButtonProps = {
  children: React.ReactNode;
  variant?: 'primary' | 'secondary' | 'outline';
  size?: 'sm' | 'md' | 'lg';
  loading?: boolean;
  disabled?: boolean;
} & React.ButtonHTMLAttributes<HTMLButtonElement>;

export function Button({ 
  children, 
  variant = 'primary', 
  size = 'md',
  loading,
  disabled,
  className,
  ...props 
}: ButtonProps) {
  return (
    <button
      className={cn('button', `button--${variant}`, `button--${size}`, className)}
      disabled={disabled || loading}
      {...props}
    >
      {loading ? <span className="spinner" /> : children}
    </button>
  );
}
```

## 三、React 特有规范

### 1. React Query 集成

- **查询键与函数**:
  - 实体相关查询放在 `entities/<entity>/api/<entity>.queries.ts`
  - 共用查询工厂放在 `shared/api/queries/`

```typescript
// entities/post/api/post.queries.ts 示例
import { queryOptions } from '@tanstack/react-query';

export const postQueries = {
  all: () => ['posts'],
  lists: () => [...postQueries.all(), 'list'],
  list: (page: number, limit: number) => queryOptions({
    queryKey: [...postQueries.lists(), page, limit],
    queryFn: () => getPosts(page, limit),
  }),
  detail: (id: number) => queryOptions({
    queryKey: [...postQueries.all(), id],
    queryFn: () => getPost(id),
  }),
};
```

### 2. 组件与Hooks

- **组件放置**: 
  - 切片特定组件放在对应切片的 `ui/` 分段
  - 通用组件放在 `shared/ui/<组件名>/`
- **自定义Hooks**:
  - 切片特定hooks放在对应切片的 `model/` 分段
  - 通用hooks放在 `shared/lib/hooks/`

### 3. 路由处理

- 路由配置放在 `app/router/`
- 页面组件从 `pages/<page-name>` 导入

```jsx
// app/router/index.tsx 示例
import { createBrowserRouter } from 'react-router-dom';
import { HomePage } from 'pages/home';
import { ArticleReadPage, loader as articleLoader } from 'pages/article-read';
import { ArticleEditPage } from 'pages/article-edit';
import { NotFoundPage } from 'pages/not-found';

export const router = createBrowserRouter([
  {
    path: '/',
    element: <HomePage />,
  },
  {
    path: '/articles/:id',
    element: <ArticleReadPage />,
    loader: articleLoader,
  },
  {
    path: '/articles/:id/edit',
    element: <ArticleEditPage />,
  },
  {
    path: '*',
    element: <NotFoundPage />,
  },
]);
```

## 四、类型管理规范

### 1. 业务实体类型

- 定义在 `entities/<entity>/model/types.ts`
- 公共API通过 `entities/<entity>/index.ts` 导出

```typescript
// entities/article/model/types.ts 示例
export interface Article {
  id: number;
  title: string;
  description: string;
  body: string;
  tagList: string[];
  createdAt: string;
  updatedAt: string;
  author: {
    username: string;
    bio: string;
    image: string;
  };
}
```

### 2. 公共API导出

- 使用命名导出，避免通配符导出
- 只导出必要的类型和组件

```typescript
// entities/article/index.ts 示例
export { ArticleCard } from './ui/ArticleCard';
export { ArticleList } from './ui/ArticleList';
export { articleQueries } from './api/article.queries';
export type { Article } from './model/types';
```

### 3. API类型和映射

- API类型(DTO)定义在各自切片的 `api/` 分段
- 映射函数也放在同一位置

```typescript
// entities/article/api/types.ts 示例
export interface ArticleDTO {
  id: number;
  title: string;
  description: string;
  body: string;
  tagList: string[];
  createdAt: string;
  updatedAt: string;
  author: {
    username: string;
    bio: string;
    image: string;
  };
}

// entities/article/api/mappers.ts
import type { ArticleDTO } from './types';
import type { Article } from '../model/types';

export function mapArticleFromDTO(dto: ArticleDTO): Article {
  return {
    ...dto,
    // 任何必要的转换
  };
}
```

## 五、导入规则

1. **同一切片内**: 使用相对路径导入
```typescript
// ✅ 正确: 从同一切片导入
import { ArticleCard } from '../ui/ArticleCard';
```

2. **跨切片导入**: 使用绝对路径(别名)导入，只能导入低层公共API
```typescript
// ✅ 正确: 从低层导入
import { Button } from 'shared/ui/button';
import { User } from 'entities/user';

// ❌ 错误: 从同层导入
import { Profile } from 'entities/profile';

// ❌ 错误: 从高层导入
import { ArticlePage } from 'pages/article';
```

3. **跨实体导入**: 使用 `@x` 特殊符号
```typescript
// entities/article/model/types.ts
import type { User } from 'entities/user/@x/article';
```

## 六、Next.js 集成注意事项

若使用Next.js，考虑以下调整:

1. **文件结构**:
   - 将Next.js的 `pages` 文件夹移至项目根目录
   - 在 `src` 内保持FSD结构
   - 从Next.js pages导入FSD pages

2. **App Router(13.4+)**:
   - 将 `app` 文件夹放在根目录，保留存根 `pages` 文件夹
   - FSD `app` 层放在 `src/app`

## 七、项目启动指南

创建新React项目时，建议按以下步骤实施FSD:

1. 创建基础层级结构
```bash
mkdir -p src/{app,pages,widgets,features,entities,shared/{ui,api,lib,config}}
```

2. 配置别名(使用webpack, vite或craco)
```js
// vite.config.js 示例
export default {
  resolve: {
    alias: {
      'app': '/src/app',
      'pages': '/src/pages',
      'widgets': '/src/widgets',
      'features': '/src/features',
      'entities': '/src/entities',
      'shared': '/src/shared',
    },
  },
}
```

3. 启动应用开发，按需创建切片和分段 