# Vitest + Playwright 实战速查表

## 项目架构配置

### 目录结构
```
project/
├── src/
│   ├── components/
│   │   ├── Button/
│   │   │   ├── Button.vue
│   │   │   ├── Button.test.js        # 单元测试 (Vitest)
│   │   │   └── Button.spec.js        # 集成测试 (Vitest)
│   ├── utils/
│   │   ├── helpers.js
│   │   └── helpers.test.js           # 工具函数测试 (Vitest)
│   └── stores/
│       ├── user.js
│       └── user.test.js              # 状态管理测试 (Vitest)
├── tests/
│   ├── unit/                         # Vitest 单元测试
│   ├── integration/                  # Vitest 集成测试
│   └── e2e/                          # Playwright E2E 测试
│       ├── auth.spec.js
│       ├── checkout.spec.js
│       └── pages/                    # 页面对象
├── test-utils/
│   ├── vitest-setup.js               # Vitest 全局配置
│   ├── playwright-setup.js           # Playwright 全局配置
│   └── shared-fixtures.js            # 共享测试工具
├── vitest.config.js
└── playwright.config.js
```

### 统一配置策略
```javascript
// vitest.config.js
import { defineConfig } from 'vitest/config'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: ['./test-utils/vitest-setup.js'],
    coverage: {
      reporter: ['text', 'html', 'lcov'],
      exclude: ['tests/e2e/**']  // 排除 E2E 测试
    }
  }
})

// playwright.config.js
export default defineConfig({
  testDir: './tests/e2e',
  fullyParallel: true,
  workers: process.env.CI ? 1 : undefined,
  use: {
    baseURL: process.env.BASE_URL || 'http://localhost:3000',
    trace: 'retain-on-failure'
  },
  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI
  }
})
```

## 测试分层策略

### 1. 单元测试 (Vitest) - 70%
**测试目标：** 纯函数、工具类、业务逻辑

```javascript
// 工具函数测试
describe('formatPrice', () => {
  it.each([
    [1000, '¥1,000.00'],
    [1234.56, '¥1,234.56'],
    [0, '¥0.00']
  ])('应该格式化价格 %d 为 %s', (input, expected) => {
    expect(formatPrice(input)).toBe(expected)
  })
})

// 纯函数测试
describe('calculateDiscount', () => {
  it('应该计算折扣价格', () => {
    const result = calculateDiscount(100, 0.1)
    expect(result).toEqual({
      originalPrice: 100,
      discount: 10,
      finalPrice: 90
    })
  })
})
```

### 2. 集成测试 (Vitest) - 20%
**测试目标：** 组件交互、API 集成、状态管理

```javascript
// 组件集成测试
describe('ShoppingCart 组件', () => {
  it('应该正确处理添加商品流程', async () => {
    const { getByRole, getByText } = render(ShoppingCart, {
      props: { products: mockProducts }
    })
    
    await userEvent.click(getByRole('button', { name: '添加到购物车' }))
    
    expect(getByText('商品已添加')).toBeInTheDocument()
    expect(mockStore.addProduct).toHaveBeenCalledWith(mockProducts[0])
  })
})

// API 集成测试
describe('UserService', () => {
  it('应该处理用户登录', async () => {
    const mockResponse = { token: 'abc123', user: { id: 1 } }
    vi.spyOn(api, 'post').mockResolvedValue(mockResponse)
    
    const result = await userService.login('user@test.com', 'password')
    
    expect(result).toEqual(mockResponse)
    expect(api.post).toHaveBeenCalledWith('/auth/login', {
      email: 'user@test.com',
      password: 'password'
    })
  })
})
```

### 3. 端到端测试 (Playwright) - 10%
**测试目标：** 关键用户流程、跨页面交互

```javascript
// 用户关键流程测试
test('完整购买流程', async ({ page }) => {
  await page.goto('/products')
  
  // 选择商品
  await page.getByRole('button', { name: '购买' }).first().click()
  
  // 添加到购物车
  await page.getByRole('button', { name: '添加到购物车' }).click()
  await expect(page.getByText('已添加到购物车')).toBeVisible()
  
  // 结账流程
  await page.getByRole('link', { name: '购物车' }).click()
  await page.getByRole('button', { name: '结账' }).click()
  
  // 填写收货信息
  await page.getByLabel('收货地址').fill('北京市朝阳区...')
  await page.getByRole('button', { name: '确认订单' }).click()
  
  // 验证订单成功
  await expect(page).toHaveURL(/\/order\/success/)
  await expect(page.getByText('订单创建成功')).toBeVisible()
})
```

## 场景应对策略

### 🔐 认证测试
```javascript
// Vitest: 认证逻辑单元测试
describe('AuthStore', () => {
  it('应该正确处理登录状态', () => {
    const store = useAuthStore()
    
    store.login({ token: 'abc123', user: { id: 1 } })
    
    expect(store.isAuthenticated).toBe(true)
    expect(store.user.id).toBe(1)
    expect(localStorage.getItem('token')).toBe('abc123')
  })
})

// Playwright: 登录流程 E2E 测试
import { test as base } from '@playwright/test'

// 创建认证 fixture
const test = base.extend({
  authenticatedPage: async ({ page }, use) => {
    await page.goto('/login')
    await page.getByLabel('邮箱').fill('admin@test.com')
    await page.getByLabel('密码').fill('password123')
    await page.getByRole('button', { name: '登录' }).click()
    await page.waitForURL('/dashboard')
    await use(page)
  }
})

test('已登录用户访问个人中心', async ({ authenticatedPage }) => {
  await authenticatedPage.goto('/profile')
  await expect(authenticatedPage.getByText('个人信息')).toBeVisible()
})
```

### 🌐 API 集成测试
```javascript
// Vitest: API Service 测试
describe('ProductAPI', () => {
  beforeEach(() => {
    fetchMock.resetMocks()
  })

  it('应该处理获取商品列表', async () => {
    const mockProducts = [{ id: 1, name: '商品1' }]
    fetchMock.mockResponseOnce(JSON.stringify(mockProducts))
    
    const products = await productAPI.getProducts()
    
    expect(products).toEqual(mockProducts)
    expect(fetch).toHaveBeenCalledWith('/api/products')
  })

  it('应该处理 API 错误', async () => {
    fetchMock.mockRejectOnce(new Error('网络错误'))
    
    await expect(productAPI.getProducts()).rejects.toThrow('网络错误')
  })
})

// Playwright: API 响应测试
test('商品列表加载', async ({ page }) => {
  // 拦截 API 请求
  await page.route('**/api/products', async route => {
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify([
        { id: 1, name: '测试商品', price: 99 }
      ])
    })
  })
  
  await page.goto('/products')
  await expect(page.getByText('测试商品')).toBeVisible()
  await expect(page.getByText('¥99')).toBeVisible()
})
```

### 📱 响应式设计测试
```javascript
// Vitest: 响应式工具函数测试
describe('useResponsive', () => {
  it('应该检测屏幕尺寸', () => {
    // 模拟窗口尺寸
    Object.defineProperty(window, 'innerWidth', {
      writable: true,
      configurable: true,
      value: 768
    })
    
    const { isMobile, isTablet } = useResponsive()
    
    expect(isMobile.value).toBe(false)
    expect(isTablet.value).toBe(true)
  })
})

// Playwright: 响应式 UI 测试
const devices = ['iPhone 12', 'iPad', 'Desktop Chrome']

devices.forEach(deviceName => {
  test(`${deviceName} 响应式布局`, async ({ page, context }) => {
    await context.newPage({
      ...devices[deviceName]
    })
    
    await page.goto('/')
    
    if (deviceName.includes('iPhone')) {
      await expect(page.getByTestId('mobile-menu')).toBeVisible()
      await expect(page.getByTestId('desktop-nav')).toBeHidden()
    } else {
      await expect(page.getByTestId('desktop-nav')).toBeVisible()
      await expect(page.getByTestId('mobile-menu')).toBeHidden()
    }
  })
})
```

### 🛒 电商业务流程
```javascript
// Vitest: 购物车逻辑测试
describe('CartStore', () => {
  it('应该正确计算总价', () => {
    const cart = useCartStore()
    
    cart.addItem({ id: 1, price: 100, quantity: 2 })
    cart.addItem({ id: 2, price: 50, quantity: 1 })
    
    expect(cart.total).toBe(250)
    expect(cart.itemCount).toBe(3)
  })

  it('应该应用优惠券', () => {
    const cart = useCartStore()
    cart.addItem({ id: 1, price: 100, quantity: 1 })
    
    cart.applyCoupon({ code: 'SAVE10', discount: 0.1 })
    
    expect(cart.total).toBe(90)
    expect(cart.appliedCoupon.code).toBe('SAVE10')
  })
})

// Playwright: 完整购买流程
test('用户购买商品流程', async ({ page }) => {
  // 登录
  await page.goto('/login')
  await page.getByLabel('邮箱').fill('buyer@test.com')
  await page.getByLabel('密码').fill('password')
  await page.getByRole('button', { name: '登录' }).click()
  
  // 浏览商品
  await page.goto('/products')
  await page.getByText('MacBook Pro').click()
  
  // 添加到购物车
  await page.getByRole('button', { name: '立即购买' }).click()
  await page.getByRole('button', { name: '添加到购物车' }).click()
  
  // 查看购物车
  await page.getByRole('link', { name: '购物车(1)' }).click()
  await expect(page.getByText('MacBook Pro')).toBeVisible()
  
  // 结账
  await page.getByRole('button', { name: '去结算' }).click()
  
  // 填写地址
  await page.getByLabel('收货人').fill('张三')
  await page.getByLabel('手机号').fill('13800138000')
  await page.getByLabel('详细地址').fill('北京市朝阳区xxx')
  
  // 选择支付方式
  await page.getByLabel('支付宝').check()
  
  // 提交订单
  await page.getByRole('button', { name: '提交订单' }).click()
  
  // 验证订单成功
  await expect(page).toHaveURL(/\/order\/\d+/)
  await expect(page.getByText('订单提交成功')).toBeVisible()
})
```

### 🎨 UI 组件测试
```javascript
// Vitest: 组件单元测试
describe('Button 组件', () => {
  it('应该渲染不同类型的按钮', () => {
    const { container } = render(Button, {
      props: { type: 'primary', size: 'large' }
    })
    
    const button = container.querySelector('button')
    expect(button).toHaveClass('btn-primary', 'btn-large')
  })

  it('应该处理点击事件', async () => {
    const handleClick = vi.fn()
    const { getByRole } = render(Button, {
      props: { onClick: handleClick }
    })
    
    await userEvent.click(getByRole('button'))
    expect(handleClick).toHaveBeenCalled()
  })

  it('禁用状态下不应该触发点击', async () => {
    const handleClick = vi.fn()
    const { getByRole } = render(Button, {
      props: { disabled: true, onClick: handleClick }
    })
    
    await userEvent.click(getByRole('button'))
    expect(handleClick).not.toHaveBeenCalled()
  })
})

// Playwright: 组件交互测试
test('模态框组件交互', async ({ page }) => {
  await page.goto('/components/modal')
  
  // 打开模态框
  await page.getByRole('button', { name: '打开模态框' }).click()
  await expect(page.getByRole('dialog')).toBeVisible()
  
  // 点击遮罩关闭
  await page.locator('.modal-overlay').click()
  await expect(page.getByRole('dialog')).toBeHidden()
  
  // ESC 键关闭
  await page.getByRole('button', { name: '打开模态框' }).click()
  await page.keyboard.press('Escape')
  await expect(page.getByRole('dialog')).toBeHidden()
  
  // 确认按钮关闭
  await page.getByRole('button', { name: '打开模态框' }).click()
  await page.getByRole('button', { name: '确认' }).click()
  await expect(page.getByRole('dialog')).toBeHidden()
})
```

### 📊 数据可视化测试
```javascript
// Vitest: 图表数据处理测试
describe('ChartDataProcessor', () => {
  it('应该转换销售数据格式', () => {
    const rawData = [
      { date: '2024-01-01', sales: 1000 },
      { date: '2024-01-02', sales: 1200 }
    ]
    
    const chartData = processChartData(rawData)
    
    expect(chartData).toEqual([
      { x: '01-01', y: 1000 },
      { x: '01-02', y: 1200 }
    ])
  })

  it('应该计算趋势', () => {
    const data = [100, 120, 110, 130]
    const trend = calculateTrend(data)
    
    expect(trend.direction).toBe('up')
    expect(trend.percentage).toBe(30)
  })
})

// Playwright: 图表渲染和交互测试
test('销售数据图表', async ({ page }) => {
  await page.goto('/dashboard/analytics')
  
  // 等待图表加载
  await page.waitForSelector('canvas', { state: 'visible' })
  
  // 检查图表存在
  await expect(page.locator('canvas')).toBeVisible()
  
  // 测试图表交互
  const canvas = page.locator('canvas')
  await canvas.hover()
  
  // 检查工具提示
  await expect(page.getByText('销售额: ¥')).toBeVisible()
  
  // 测试日期筛选
  await page.getByLabel('开始日期').fill('2024-01-01')
  await page.getByLabel('结束日期').fill('2024-01-31')
  await page.getByRole('button', { name: '应用筛选' }).click()
  
  // 等待图表更新
  await page.waitForLoadState('networkidle')
  
  // 验证数据更新
  await expect(page.getByText('2024年1月数据')).toBeVisible()
})
```

## 性能测试策略

### Vitest 性能测试
```javascript
describe('性能测试', () => {
  it('大数据量处理性能', () => {
    const largeArray = Array.from({ length: 10000 }, (_, i) => i)
    
    const start = performance.now()
    const result = processLargeData(largeArray)
    const end = performance.now()
    
    expect(end - start).toBeLessThan(100) // 100ms 内完成
    expect(result).toHaveLength(10000)
  })

  it('内存使用测试', () => {
    const initialMemory = process.memoryUsage().heapUsed
    
    // 执行可能造成内存泄漏的操作
    for (let i = 0; i < 1000; i++) {
      createLargeObject()
    }
    
    // 强制垃圾回收
    if (global.gc) global.gc()
    
    const finalMemory = process.memoryUsage().heapUsed
    const memoryIncrease = finalMemory - initialMemory
    
    expect(memoryIncrease).toBeLessThan(10 * 1024 * 1024) // 10MB
  })
})
```

### Playwright 性能测试
```javascript
test('页面加载性能', async ({ page }) => {
  // 开始性能监控
  await page.addInitScript(() => {
    window.performanceMetrics = {
      navigationStart: performance.timing.navigationStart,
      loadComplete: 0,
      firstPaint: 0
    }
  })
  
  const start = Date.now()
  await page.goto('/')
  
  // 等待页面完全加载
  await page.waitForLoadState('networkidle')
  const loadTime = Date.now() - start
  
  // 检查加载时间
  expect(loadTime).toBeLessThan(3000) // 3秒内加载
  
  // 检查 Core Web Vitals
  const metrics = await page.evaluate(() => {
    return new Promise(resolve => {
      new PerformanceObserver(list => {
        const entries = list.getEntries()
        const lcp = entries.find(entry => entry.entryType === 'largest-contentful-paint')
        const fid = entries.find(entry => entry.entryType === 'first-input')
        
        resolve({
          lcp: lcp?.startTime,
          fid: fid?.processingStart - fid?.startTime
        })
      }).observe({ entryTypes: ['largest-contentful-paint', 'first-input'] })
    })
  })
  
  if (metrics.lcp) expect(metrics.lcp).toBeLessThan(2500) // LCP < 2.5s
  if (metrics.fid) expect(metrics.fid).toBeLessThan(100)  // FID < 100ms
})
```

## 错误处理和调试

### 调试配置
```javascript
// test-utils/debug-helpers.js
export const debugTest = {
  // Vitest 调试
  logState: (state, label = 'State') => {
    if (process.env.DEBUG_TESTS) {
      console.log(`🐛 ${label}:`, JSON.stringify(state, null, 2))
    }
  },
  
  // Playwright 调试
  screenshot: async (page, name) => {
    if (process.env.DEBUG_TESTS) {
      await page.screenshot({ 
        path: `debug-screenshots/${name}-${Date.now()}.png` 
      })
    }
  },
  
  // 通用调试
  time: (label) => {
    if (process.env.DEBUG_TESTS) {
      console.time(label)
      return () => console.timeEnd(label)
    }
    return () => {}
  }
}
```

### 错误恢复策略
```javascript
// Playwright 重试和错误处理
test('带自动重试的测试', async ({ page }) => {
  test.setTimeout(30000) // 30秒超时
  
  for (let attempt = 0; attempt < 3; attempt++) {
    try {
      await page.goto('/')
      await page.getByRole('button', { name: '加载数据' }).click()
      await expect(page.getByText('数据加载完成')).toBeVisible({ timeout: 10000 })
      break // 成功则跳出循环
    } catch (error) {
      if (attempt === 2) throw error // 最后一次尝试失败则抛出错误
      
      console.log(`尝试 ${attempt + 1} 失败，重试中...`)
      await page.reload()
      await page.waitForTimeout(1000)
    }
  }
})
```

## CI/CD 集成

### GitHub Actions 配置
```yaml
name: Tests
on: [push, pull_request]

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '18'
      - run: npm ci
      - run: npm run test:unit
      - run: npm run test:coverage
      - uses: codecov/codecov-action@v3

  e2e-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '18'
      - run: npm ci
      - run: npx playwright install
      - run: npm run test:e2e
      - uses: actions/upload-artifact@v3
        if: failure()
        with:
          name: playwright-report
          path: playwright-report/
```

### 环境变量管理
```javascript
// test-utils/env-config.js
export const testConfig = {
  vitest: {
    baseURL: process.env.VITE_TEST_BASE_URL || 'http://localhost:3000',
    apiURL: process.env.VITE_TEST_API_URL || 'http://localhost:8080/api',
    timeout: parseInt(process.env.VITE_TEST_TIMEOUT) || 5000
  },
  playwright: {
    baseURL: process.env.PLAYWRIGHT_BASE_URL || 'http://localhost:3000',
    headless: process.env.CI === 'true',
    slowMo: process.env.SLOW_MO ? parseInt(process.env.SLOW_MO) : 0
  }
}
```

## 总结

**测试策略分配：**
- **70% 单元测试 (Vitest)** - 快速反馈，高覆盖率
- **20% 集成测试 (Vitest)** - 模块间交互验证  
- **10% E2E 测试 (Playwright)** - 关键用户流程保障

**工具选择原则：**
- **Vitest** - 逻辑测试、组件测试、API 测试
- **Playwright** - 用户体验测试、跨浏览器测试、视觉测试

**最佳实践：**
1. 🏗️ **分层测试** - 不同层次使用不同工具
2. 🔧 **共享工具** - 统一测试工具和辅助函数
3. 📊 **性能监控** - 集成性能测试到 CI/CD
4. 🐛 **调试友好** - 完善的调试和错误处理机制
5. 🚀 **CI/CD 集成** - 自动化测试流程