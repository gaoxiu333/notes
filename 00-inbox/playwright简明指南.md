# Playwright 入门指南

## 什么是 Playwright？

Playwright 是由 Microsoft 开发的现代端到端测试框架，具有以下特点：
- 支持多浏览器（Chromium、Firefox、Safari）
- 快速可靠的测试执行
- 强大的页面交互 API
- 自动等待机制
- 内置调试工具
- 支持移动端模拟

## 安装

```bash
# 安装 Playwright
npm init playwright@latest

# 或手动安装
npm install -D @playwright/test
npx playwright install
```

安装后会自动创建配置文件和示例测试。

## 基础配置

### playwright.config.js
```javascript
import { defineConfig, devices } from '@playwright/test'

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] },
    },
  ],
  webServer: {
    command: 'npm run start',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
  },
})
```

## 编写第一个测试

### 基础页面测试
```javascript
// tests/homepage.spec.js
import { test, expect } from '@playwright/test'

test('首页基础功能测试', async ({ page }) => {
  // 访问页面
  await page.goto('/')
  
  // 检查页面标题
  await expect(page).toHaveTitle(/首页/)
  
  // 检查页面元素
  await expect(page.getByRole('heading', { name: '欢迎' })).toBeVisible()
  
  // 点击按钮
  await page.getByRole('button', { name: '开始' }).click()
  
  // 检查导航结果
  await expect(page).toHaveURL(/\/dashboard/)
})
```

### 表单交互测试
```javascript
test('用户注册表单', async ({ page }) => {
  await page.goto('/register')
  
  // 填写表单
  await page.getByLabel('用户名').fill('testuser')
  await page.getByLabel('邮箱').fill('test@example.com')
  await page.getByLabel('密码').fill('password123')
  await page.getByLabel('确认密码').fill('password123')
  
  // 选择复选框
  await page.getByLabel('同意条款').check()
  
  // 提交表单
  await page.getByRole('button', { name: '注册' }).click()
  
  // 验证成功消息
  await expect(page.getByText('注册成功')).toBeVisible()
})
```

## 元素定位策略

### 推荐的定位方法
```javascript
// 1. 通过角色定位（最推荐）
await page.getByRole('button', { name: '提交' })
await page.getByRole('textbox', { name: '用户名' })
await page.getByRole('link', { name: '首页' })

// 2. 通过标签文本定位
await page.getByLabel('密码')
await page.getByPlaceholder('请输入邮箱')

// 3. 通过文本内容定位
await page.getByText('登录')
await page.getByText('欢迎回来', { exact: true })

// 4. 通过测试 ID 定位
await page.getByTestId('submit-button')

// 5. CSS 选择器（不推荐，但有时必要）
await page.locator('.submit-btn')
await page.locator('#username')
```

### 复杂定位
```javascript
// 组合定位
await page.getByRole('listitem').filter({ hasText: '产品A' })
  .getByRole('button', { name: '购买' }).click()

// 第 n 个元素
await page.getByRole('button').nth(2)

// 第一个和最后一个
await page.getByRole('listitem').first()
await page.getByRole('listitem').last()

// 包含特定子元素
await page.locator('tr').filter({ has: page.getByText('John') })
```

## 常用操作

### 页面操作
```javascript
// 导航
await page.goto('/dashboard')
await page.goBack()
await page.goForward()
await page.reload()

// 等待
await page.waitForLoadState('networkidle')
await page.waitForSelector('.loading', { state: 'hidden' })
await page.waitForFunction(() => window.jQuery !== undefined)

// 截图
await page.screenshot({ path: 'screenshot.png' })
await page.screenshot({ path: 'fullpage.png', fullPage: true })
```

### 表单操作
```javascript
// 输入文本
await page.getByLabel('搜索').fill('关键词')
await page.getByLabel('描述').type('这是一段描述', { delay: 100 })

// 选择下拉菜单
await page.getByLabel('城市').selectOption('北京')
await page.getByLabel('城市').selectOption({ label: '上海' })

// 文件上传
await page.getByLabel('上传文件').setInputFiles('path/to/file.pdf')
await page.getByLabel('上传文件').setInputFiles(['file1.pdf', 'file2.pdf'])

// 复选框和单选框
await page.getByLabel('记住我').check()
await page.getByLabel('记住我').uncheck()
await page.getByLabel('男').check() // 单选框
```

### 鼠标和键盘操作
```javascript
// 鼠标操作
await page.getByText('右键菜单').click({ button: 'right' })
await page.getByText('双击').dblclick()
await page.getByText('悬停').hover()

// 拖拽
await page.getByText('拖拽源').dragTo(page.getByText('拖拽目标'))

// 键盘操作
await page.keyboard.press('Enter')
await page.keyboard.press('Control+A')
await page.keyboard.type('Hello World')
```

## 断言方法

### 页面断言
```javascript
// 页面标题和 URL
await expect(page).toHaveTitle('页面标题')
await expect(page).toHaveURL('https://example.com/page')
await expect(page).toHaveURL(/\/dashboard$/)

// 页面截图对比
await expect(page).toHaveScreenshot('homepage.png')
```

### 元素断言
```javascript
// 可见性
await expect(page.getByText('欢迎')).toBeVisible()
await expect(page.getByText('加载中')).toBeHidden()

// 元素状态
await expect(page.getByLabel('同意条款')).toBeChecked()
await expect(page.getByRole('button', { name: '提交' })).toBeEnabled()
await expect(page.getByRole('button', { name: '保存' })).toBeDisabled()

// 文本内容
await expect(page.getByText('用户名')).toHaveText('用户名')
await expect(page.getByLabel('描述')).toHaveValue('这是描述')
await expect(page.getByText('总价')).toContainText('¥99')

// 属性检查
await expect(page.getByRole('link')).toHaveAttribute('href', '/home')
await expect(page.getByLabel('邮箱')).toHaveAttribute('type', 'email')

// 元素数量
await expect(page.getByRole('listitem')).toHaveCount(5)
```

## 高级功能

### 拦截网络请求
```javascript
test('API 请求拦截', async ({ page }) => {
  // 拦截 API 请求并返回模拟数据
  await page.route('**/api/users', async route => {
    const json = [
      { id: 1, name: '张三' },
      { id: 2, name: '李四' }
    ]
    await route.fulfill({ json })
  })
  
  await page.goto('/users')
  await expect(page.getByText('张三')).toBeVisible()
})

// 等待特定请求
test('等待 API 响应', async ({ page }) => {
  const responsePromise = page.waitForResponse('**/api/data')
  await page.getByRole('button', { name: '加载数据' }).click()
  const response = await responsePromise
  expect(response.status()).toBe(200)
})
```

### 多页面处理
```javascript
test('新窗口处理', async ({ context, page }) => {
  // 等待新页面打开
  const pagePromise = context.waitForEvent('page')
  await page.getByText('在新窗口打开').click()
  const newPage = await pagePromise
  
  await expect(newPage.getByText('新页面内容')).toBeVisible()
  await newPage.close()
})
```

### 存储状态
```javascript
// 保存登录状态
test('保存用户状态', async ({ page }) => {
  await page.goto('/login')
  await page.getByLabel('用户名').fill('admin')
  await page.getByLabel('密码').fill('password')
  await page.getByRole('button', { name: '登录' }).click()
  
  // 保存认证状态
  await page.context().storageState({ path: 'auth.json' })
})

// 配置文件中使用保存的状态
// playwright.config.js
{
  name: 'logged-in',
  use: { 
    ...devices['Desktop Chrome'],
    storageState: 'auth.json'
  },
}
```

## 调试技巧

### 调试模式
```bash
# 以调试模式运行测试
npx playwright test --debug

# 运行特定测试
npx playwright test tests/login.spec.js --debug

# 以慢动作模式运行
npx playwright test --headed --slowMo=1000
```

### 代码中的调试
```javascript
test('调试测试', async ({ page }) => {
  await page.goto('/')
  
  // 在浏览器中暂停执行
  await page.pause()
  
  // 启动调试器
  await page.getByText('登录').click()
})
```

### 生成测试代码
```bash
# 录制用户操作生成测试代码
npx playwright codegen https://example.com

# 指定浏览器录制
npx playwright codegen --browser=firefox https://example.com
```

## 常用命令

```bash
# 运行所有测试
npx playwright test

# 运行特定文件
npx playwright test tests/login.spec.js

# 运行特定浏览器
npx playwright test --project=chromium

# 并行运行
npx playwright test --workers=4

# 生成 HTML 报告
npx playwright test --reporter=html

# 显示测试结果
npx playwright show-report

# 更新截图
npx playwright test --update-snapshots

# 安装浏览器
npx playwright install

# 检查安装
npx playwright doctor
```

## 最佳实践与实用技巧

### 1. 页面对象模型 (POM)
```javascript
// pages/LoginPage.js
export class LoginPage {
  constructor(page) {
    this.page = page
    this.usernameInput = page.getByLabel('用户名')
    this.passwordInput = page.getByLabel('密码')
    this.loginButton = page.getByRole('button', { name: '登录' })
    this.errorMessage = page.getByTestId('error-message')
  }

  async goto() {
    await this.page.goto('/login')
  }

  async login(username, password) {
    await this.usernameInput.fill(username)
    await this.passwordInput.fill(password)
    await this.loginButton.click()
  }

  async getErrorMessage() {
    return await this.errorMessage.textContent()
  }
}

// 在测试中使用
import { LoginPage } from '../pages/LoginPage'

test('登录功能', async ({ page }) => {
  const loginPage = new LoginPage(page)
  await loginPage.goto()
  await loginPage.login('admin', 'password')
  await expect(page).toHaveURL('/dashboard')
})
```

### 2. 测试数据管理
```javascript
// data/testData.js
export const users = {
  admin: {
    username: 'admin',
    password: 'admin123',
    email: 'admin@example.com'
  },
  regular: {
    username: 'user',
    password: 'user123',
    email: 'user@example.com'
  }
}

export const products = [
  { name: '笔记本电脑', price: 5999, category: '电子产品' },
  { name: '咖啡杯', price: 29, category: '生活用品' }
]

// 在测试中使用
import { users, products } from '../data/testData'

test('使用测试数据', async ({ page }) => {
  const user = users.admin
  await loginPage.login(user.username, user.password)
})
```

### 3. 自定义 Fixture
```javascript
// fixtures/auth.js
import { test as base } from '@playwright/test'
import { LoginPage } from '../pages/LoginPage'

export const test = base.extend({
  // 自动登录的 fixture
  authenticatedPage: async ({ page }, use) => {
    const loginPage = new LoginPage(page)
    await loginPage.goto()
    await loginPage.login('admin', 'password123')
    await page.waitForURL('/dashboard')
    await use(page)
  }
})

// 使用自定义 fixture
test('需要登录的测试', async ({ authenticatedPage }) => {
  // 页面已经是登录状态
  await expect(authenticatedPage.getByText('欢迎，管理员')).toBeVisible()
})
```

### 4. 环境配置
```javascript
// playwright.config.js
export default defineConfig({
  projects: [
    {
      name: 'development',
      use: { 
        baseURL: 'http://localhost:3000',
        trace: 'on'
      },
    },
    {
      name: 'staging',
      use: { 
        baseURL: 'https://staging.example.com',
        trace: 'retain-on-failure'
      },
    },
    {
      name: 'production',
      use: { 
        baseURL: 'https://example.com',
        trace: 'retain-on-failure'
      },
    }
  ]
})

// 运行特定环境
// npx playwright test --project=staging
```

### 5. 错误处理和重试
```javascript
test('带重试机制的测试', async ({ page }) => {
  // 设置单个测试的重试次数
  test.describe.configure({ retries: 3 })
  
  await page.goto('/')
  
  // 使用软断言，不会立即失败
  await expect.soft(page.getByText('可能不存在的元素')).toBeVisible()
  await expect.soft(page.getByText('另一个元素')).toBeVisible()
  
  // 硬断言，会导致测试失败
  await expect(page.getByText('必须存在的元素')).toBeVisible()
})
```

### 6. 性能测试
```javascript
test('页面加载性能', async ({ page }) => {
  const startTime = Date.now()
  
  await page.goto('/')
  await page.waitForLoadState('networkidle')
  
  const loadTime = Date.now() - startTime
  expect(loadTime).toBeLessThan(3000) // 3秒内加载完成
})

test('网络请求性能', async ({ page }) => {
  const responses = []
  
  page.on('response', response => {
    if (response.url().includes('/api/')) {
      responses.push({
        url: response.url(),
        status: response.status(),
        timing: response.timing()
      })
    }
  })
  
  await page.goto('/dashboard')
  
  // 检查 API 响应时间
  const slowResponses = responses.filter(r => r.timing > 1000)
  expect(slowResponses).toHaveLength(0)
})
```

### 7. 视觉回归测试
```javascript
test('页面视觉回归', async ({ page }) => {
  await page.goto('/')
  
  // 等待动画完成
  await page.waitForTimeout(1000)
  
  // 隐藏动态内容
  await page.addStyleTag({
    content: '.timestamp, .animation { visibility: hidden; }'
  })
  
  // 截图对比
  await expect(page).toHaveScreenshot('homepage.png', {
    fullPage: true,
    animations: 'disabled'
  })
})
```

### 8. 移动端测试
```javascript
test('移动端响应式测试', async ({ page }) => {
  // 设置移动端视口
  await page.setViewportSize({ width: 375, height: 667 })
  
  await page.goto('/')
  
  // 检查移动端菜单
  await expect(page.getByTestId('mobile-menu-button')).toBeVisible()
  await expect(page.getByTestId('desktop-nav')).toBeHidden()
  
  // 测试触摸操作
  await page.getByTestId('mobile-menu-button').tap()
  await expect(page.getByTestId('mobile-menu')).toBeVisible()
})
```

### 9. API 测试集成
```javascript
import { test, expect, request } from '@playwright/test'

test('API 和 UI 集成测试', async ({ page }) => {
  // 先通过 API 创建数据
  const apiContext = await request.newContext()
  const response = await apiContext.post('/api/users', {
    data: { name: '测试用户', email: 'test@example.com' }
  })
  expect(response.ok()).toBeTruthy()
  
  const user = await response.json()
  
  // 然后在 UI 中验证
  await page.goto('/users')
  await expect(page.getByText(user.name)).toBeVisible()
})
```

### 10. 测试报告定制
```javascript
// playwright.config.js
export default defineConfig({
  reporter: [
    ['html'],
    ['json', { outputFile: 'test-results.json' }],
    ['junit', { outputFile: 'test-results.xml' }],
    ['./custom-reporter.js']
  ]
})

// custom-reporter.js
class CustomReporter {
  onTestEnd(test, result) {
    if (result.status === 'failed') {
      console.log(`❌ ${test.title} 失败`)
      console.log(`   错误: ${result.error?.message}`)
    }
  }
}

module.exports = CustomReporter
```

## 总结

Playwright 是一个功能强大的端到端测试框架，特别适合现代 Web 应用测试。通过合理使用页面对象模型、自定义 fixture 和环境配置，可以构建可维护性强的测试套件。结合视觉回归测试、性能监控和 API 集成，能够全面保障应用质量。