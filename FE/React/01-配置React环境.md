## React 开发环境配置

开始 React 之前，要有个舒适的 React 开发环境，在主观上有个了解。

### 快速开始

1. 使用 [Vite](https://vitejs.dev/guide/) 创建，使用 Vite 创建已经是官方推荐的方式

   ```bash
   npm create vite@latest
   ```

2. 使用 [Create React App](https://create-react-app.dev/)，官方文档中已经没有这一项推荐（不知道为啥）

   ```bash
   npx create-react-app <project-name>
   ```

3. 使用 HTML 快速体验

   请下载此 HTML 页面 [点击下载](https://gist.githubusercontent.com/gaearon/0275b1e1518599bbeafcde4722e79ed1/raw/db72dcbf3384ee1708c4a07d3be79860db04bff0/example.html) ，放在本地 HTML 文件中打开，就可以简单体验了。

4. 其他官方推荐

   参考官方文档：[点击查看](https://react.dev/learn/installation#try-react)

### 编辑器

**编辑器推荐：**

- [VS Code](https://code.visualstudio.com/) - 免费强大；
- [WebStorm](https://www.jetbrains.com/webstorm/) - 收费，更友好，但占内存。

**VS Code 插件：**

- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) - 自动格式化代码

> 当 Perttier 和 ESlint 冲突时，禁用 ESlint 代码格式化预设，或者使用 `prettier --check`。

### 开发者工具

React 团队提供了浏览器工具 React Developer Tools

**特性**

- 可以检查 React 组件
- 修改 Props 和 state
- 查看性能问题

**安装**

- [**Chrome**](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en)
- [**Firefox**](https://addons.mozilla.org/en-US/firefox/addon/react-devtools/)
- [**Edge**](https://microsoftedge.microsoft.com/addons/detail/react-developer-tools/gpphkfbcpidddadnkolkpfckpihlkkil)

Safari 和 移动端需要工具包支持：

```bash
# 安装
npm install react-devtools --no-save # 也可以全局安装  -g
# 启动
npx react-devtools
```

