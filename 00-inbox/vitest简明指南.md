# Vitest 入门指南

## 什么是 Vitest？

Vitest 是一个基于 Vite 的现代 JavaScript 测试框架，具有以下特点：
- 极快的执行速度
- 与 Vite 生态系统无缝集成
- 兼容 Jest API
- 支持 TypeScript 开箱即用
- 内置代码覆盖率

## 安装

```bash
# 使用 npm
npm install -D vitest

# 使用 yarn
yarn add -D vitest

# 使用 pnpm
pnpm add -D vitest
```

## 基础配置

### package.json 配置
```json
{
  "scripts": {
    "test": "vitest",
    "test:run": "vitest run",
    "test:coverage": "vitest --coverage"
  }
}
```

### vitest.config.js（可选）
```javascript
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    globals: true,
    environment: 'jsdom', // 或 'node'、'happy-dom'
    setupFiles: './src/test/setup.js'
  }
})
```

## 编写第一个测试

### 基础函数示例
```javascript
// src/utils/math.js
export function add(a, b) {
  return a + b
}

export function multiply(a, b) {
  return a * b
}
```

### 测试文件
```javascript
// src/utils/math.test.js
import { describe, it, expect } from 'vitest'
import { add, multiply } from './math.js'

describe('数学工具函数', () => {
  it('应该正确相加两个数字', () => {
    expect(add(2, 3)).toBe(5)
    expect(add(-1, 1)).toBe(0)
  })

  it('应该正确相乘两个数字', () => {
    expect(multiply(3, 4)).toBe(12)
    expect(multiply(0, 5)).toBe(0)
  })
})
```

## 常用断言方法

```javascript
// 基础断言
expect(value).toBe(expected)           // 严格相等
expect(value).toEqual(expected)        // 深度相等
expect(value).toBeTruthy()             // 真值
expect(value).toBeFalsy()              // 假值
expect(value).toBeNull()               // null
expect(value).toBeUndefined()          // undefined

// 数字断言
expect(value).toBeGreaterThan(3)       // 大于
expect(value).toBeCloseTo(0.3)         // 浮点数近似

// 字符串断言
expect(string).toContain('substring')   // 包含子串
expect(string).toMatch(/pattern/)       // 正则匹配

// 数组断言
expect(array).toContain(item)          // 包含元素
expect(array).toHaveLength(3)          // 长度检查

// 异常断言
expect(() => {
  throw new Error('错误')
}).toThrow('错误')
```

## 异步测试

### Promise 测试
```javascript
import { it, expect } from 'vitest'

// 返回 Promise
it('异步函数测试', async () => {
  const result = await fetchData()
  expect(result).toBe('data')
})

// 测试 Promise 拒绝
it('应该抛出错误', async () => {
  await expect(fetchDataWithError()).rejects.toThrow('网络错误')
})
```

### 回调函数测试
```javascript
import { it, expect } from 'vitest'

it('回调函数测试', (done) => {
  fetchDataWithCallback((error, data) => {
    expect(error).toBeNull()
    expect(data).toBe('result')
    done()
  })
})
```

## Mock 功能

### 函数 Mock
```javascript
import { vi, it, expect } from 'vitest'

it('Mock 函数测试', () => {
  const mockFn = vi.fn()
  mockFn('arg1', 'arg2')
  
  expect(mockFn).toHaveBeenCalled()
  expect(mockFn).toHaveBeenCalledWith('arg1', 'arg2')
  expect(mockFn).toHaveBeenCalledTimes(1)
})
```

### 模块 Mock
```javascript
import { vi, beforeEach } from 'vitest'

// Mock 整个模块
vi.mock('./api', () => ({
  fetchUser: vi.fn(() => Promise.resolve({ id: 1, name: '张三' }))
}))

// Mock 部分模块
vi.mock('./utils', async () => {
  const actual = await vi.importActual('./utils')
  return {
    ...actual,
    getCurrentTime: vi.fn(() => '2024-01-01')
  }
})
```

## 生命周期钩子

```javascript
import { describe, it, beforeAll, afterAll, beforeEach, afterEach } from 'vitest'

describe('生命周期示例', () => {
  beforeAll(() => {
    // 所有测试前执行一次
    console.log('测试套件开始')
  })

  afterAll(() => {
    // 所有测试后执行一次
    console.log('测试套件结束')
  })

  beforeEach(() => {
    // 每个测试前执行
    console.log('测试开始')
  })

  afterEach(() => {
    // 每个测试后执行
    console.log('测试结束')
  })

  it('测试用例1', () => {
    expect(true).toBe(true)
  })
})
```

## 测试覆盖率

```bash
# 安装覆盖率工具
npm install -D @vitest/coverage-v8

# 运行覆盖率测试
npm run test:coverage
```

配置覆盖率：
```javascript
// vitest.config.js
export default defineConfig({
  test: {
    coverage: {
      provider: 'v8',
      reporter: ['text', 'html', 'lcov'],
      exclude: [
        'node_modules/',
        'src/test/',
        '**/*.test.js'
      ]
    }
  }
})
```

## 常用命令

```bash
# 运行所有测试
vitest

# 运行一次测试（不监听文件变化）
vitest run

# 运行指定文件的测试
vitest math.test.js

# 运行匹配模式的测试
vitest --grep "数学"

# 以监听模式运行
vitest --watch

# 生成覆盖率报告
vitest --coverage

# 在 UI 界面中运行测试
vitest --ui
```

## 最佳实践与实用技巧

### 1. 测试文件组织
```javascript
// 推荐的文件结构
src/
  components/
    Button/
      Button.vue
      Button.test.js          // 组件测试
      Button.stories.js       // Storybook 故事
  utils/
    __tests__/               // 或者集中放在 __tests__ 目录
      math.test.js
      string.test.js
  test/
    setup.js                 // 全局测试配置
    helpers.js               // 测试工具函数
```

### 2. 使用测试工厂函数
```javascript
// 创建测试数据的工厂函数
function createUser(overrides = {}) {
  return {
    id: 1,
    name: '张三',
    email: 'zhangsan@example.com',
    age: 25,
    ...overrides
  }
}

it('应该处理用户数据', () => {
  const user = createUser({ age: 30 })
  expect(processUser(user)).toEqual(expect.objectContaining({
    isAdult: true
  }))
})
```

### 3. 善用 beforeEach 清理和准备
```javascript
describe('用户服务测试', () => {
  let userService
  let mockDatabase

  beforeEach(() => {
    // 每个测试前重新创建实例，确保隔离
    mockDatabase = vi.fn()
    userService = new UserService(mockDatabase)
    
    // 重置所有 mock
    vi.clearAllMocks()
  })
})
```

### 4. 使用自定义匹配器
```javascript
// test/setup.js
import { expect } from 'vitest'

// 自定义匹配器：检查是否为有效邮箱
expect.extend({
  toBeValidEmail(received) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    const pass = emailRegex.test(received)
    
    return {
      pass,
      message: () => `期望 ${received} ${pass ? '不' : ''}是有效邮箱`
    }
  }
})

// 在测试中使用
it('应该验证邮箱格式', () => {
  expect('user@example.com').toBeValidEmail()
})
```

### 5. 条件测试执行
```javascript
import { it, describe, skipIf, runIf } from 'vitest'

// 根据环境跳过测试
describe.skipIf(process.env.NODE_ENV === 'production')('开发环境测试', () => {
  it('开发模式功能测试', () => {
    // 只在开发环境运行
  })
})

// 根据条件运行测试
it.runIf(process.platform === 'linux')('Linux 特定功能', () => {
  // 只在 Linux 系统运行
})

// 跳过特定测试
it.skip('暂时跳过的测试', () => {
  // 这个测试会被跳过
})

// 只运行这个测试（调试时很有用）
it.only('专注测试这一个', () => {
  // 只会运行这个测试
})
```

### 6. 错误边界测试
```javascript
import { it, expect } from 'vitest'

it('应该优雅处理各种错误情况', () => {
  // 测试空值
  expect(() => processData(null)).toThrow('数据不能为空')
  expect(() => processData(undefined)).toThrow('数据不能为空')
  
  // 测试错误类型
  expect(() => processData('invalid')).toThrow('数据格式错误')
  
  // 测试边界值
  expect(() => processData([])).toThrow('数据不能为空数组')
  expect(() => processData({})).toThrow('数据对象不能为空')
})
```

### 7. 快照测试的正确使用
```javascript
import { it, expect } from 'vitest'

it('组件渲染快照', () => {
  const component = render(<UserCard user={createUser()} />)
  
  // 对于 UI 组件，快照测试很有用
  expect(component.container.firstChild).toMatchSnapshot()
})

// 更好的做法：测试特定的输出结构
it('API 响应格式测试', () => {
  const response = formatApiResponse(userData)
  
  expect(response).toMatchObject({
    status: 'success',
    data: expect.objectContaining({
      id: expect.any(Number),
      name: expect.any(String)
    })
  })
})
```

### 8. 性能测试
```javascript
import { it, expect, vi } from 'vitest'

it('函数执行性能测试', () => {
  const start = Date.now()
  
  // 执行需要测试性能的函数
  heavyCalculation(largeDataSet)
  
  const duration = Date.now() - start
  expect(duration).toBeLessThan(1000) // 应该在1秒内完成
})

// 使用 vi.spyOn 监控函数调用次数
it('应该优化函数调用次数', () => {
  const spy = vi.spyOn(expensiveFunction, 'call')
  
  optimizedFunction(data)
  
  expect(spy).toHaveBeenCalledTimes(1) // 确保没有重复调用
})
```

### 9. 并发测试
```javascript
import { it, expect } from 'vitest'

// 设置并发测试
it.concurrent('并发测试1', async () => {
  const result = await asyncOperation1()
  expect(result).toBe('expected1')
})

it.concurrent('并发测试2', async () => {
  const result = await asyncOperation2()
  expect(result).toBe('expected2')
})

// 限制并发数量
describe.concurrent('API 测试', () => {
  // 这些测试会并发运行，但受到 Vitest 配置的并发限制
})
```

### 10. 测试覆盖率优化技巧
```javascript
// vitest.config.js
export default defineConfig({
  test: {
    coverage: {
      // 设置覆盖率阈值
      thresholds: {
        global: {
          statements: 80,
          branches: 80,
          functions: 80,
          lines: 80
        }
      },
      // 排除不需要测试的文件
      exclude: [
        'src/main.js',           // 入口文件
        'src/**/*.config.js',    // 配置文件
        'src/**/*.d.ts',         // 类型定义
        'src/test/**',           // 测试工具
        'src/**/*.stories.js'    // Storybook 文件
      ]
    }
  }
})
```

### 11. 调试技巧
```javascript
// 使用 console.log 调试（但记得删除）
it('调试测试', () => {
  const result = complexFunction(input)
  console.log('调试输出:', result) // 临时调试
  expect(result).toBe(expected)
})

// 使用 debugger（需要 Node.js 调试模式）
it('使用断点调试', () => {
  const data = processData(input)
  debugger // 在这里暂停执行
  expect(data).toEqual(expected)
})

// 运行单个测试文件进行调试
// npm test -- math.test.js
```

### 12. 环境变量测试
```javascript
import { beforeEach, afterEach, it, expect, vi } from 'vitest'

describe('环境变量测试', () => {
  const originalEnv = process.env

  beforeEach(() => {
    // 重置环境变量
    vi.resetModules()
    process.env = { ...originalEnv }
  })

  afterEach(() => {
    // 恢复原始环境变量
    process.env = originalEnv
  })

  it('应该在开发环境下启用调试', () => {
    process.env.NODE_ENV = 'development'
    
    const config = loadConfig()
    expect(config.debug).toBe(true)
  })
})
```

## 总结

Vitest 提供了现代、快速的测试体验，特别适合 Vite 项目。它的 API 与 Jest 兼容，学习成本低，同时提供了更好的性能和开发体验。通过合理使用断言、Mock 和生命周期钩子，可以构建健壮的测试套件。