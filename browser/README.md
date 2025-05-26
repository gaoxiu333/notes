# Chrome 书签读取器

一个用于读取和解析 Chrome 浏览器书签的 Node.js 工具。支持跨平台使用（macOS、Windows、Linux），提供多种导出格式和强大的搜索功能。

## 功能特性

- 🔍 **跨平台支持** - 自动检测操作系统并定位 Chrome 书签文件
- 📚 **完整解析** - 解析所有书签和文件夹结构
- 🔎 **智能搜索** - 根据名称、URL 或文件夹路径搜索书签
- 📊 **统计分析** - 显示书签统计信息和分布情况
- 💾 **多格式导出** - 支持 JSON、CSV、HTML 格式导出
- 🎯 **灵活筛选** - 按类型、文件夹筛选书签

## 安装和使用

### 基本使用

```bash
# 进入 browser 目录
cd browser

# 查看所有书签
node chrome-bookmarks-reader.js list

# 或者使用 npm scripts
npm run list
```

### 命令行选项

```bash
# 列出所有书签和文件夹
node chrome-bookmarks-reader.js list

# 只显示文件夹
node chrome-bookmarks-reader.js folders

# 搜索书签
node chrome-bookmarks-reader.js search "github"

# 导出书签（支持 json、csv、html 格式）
node chrome-bookmarks-reader.js export json bookmarks.json
node chrome-bookmarks-reader.js export csv bookmarks.csv
node chrome-bookmarks-reader.js export html bookmarks.html

# 显示统计信息
node chrome-bookmarks-reader.js stats

# 显示帮助信息
node chrome-bookmarks-reader.js help
```

### 使用 npm scripts

```bash
npm run list      # 列出所有书签
npm run folders   # 显示文件夹
npm run stats     # 显示统计信息
npm run help      # 显示帮助信息
```

## 编程使用

可以将此工具作为模块在其他 Node.js 项目中使用：

```javascript
const ChromeBookmarksReader = require('./chrome-bookmarks-reader');

const reader = new ChromeBookmarksReader();

// 检查书签文件是否存在
if (reader.bookmarksFileExists()) {
  // 获取所有书签
  const bookmarks = reader.getAllBookmarks();
  console.log('总书签数:', bookmarks.length);

  // 搜索书签
  const results = reader.searchBookmarks('github');
  console.log('搜索结果:', results);

  // 按类型筛选
  const folders = reader.getBookmarksByType('folder');
  const links = reader.getBookmarksByType('bookmark');

  // 导出书签
  reader.exportBookmarks('my-bookmarks.json', 'json');
  
  // 显示统计信息
  reader.showStatistics();
}
```

## Chrome 书签文件位置

工具会自动根据操作系统查找 Chrome 书签文件：

- **macOS**: `~/Library/Application Support/Google/Chrome/Default/Bookmarks`
- **Windows**: `~/AppData/Local/Google/Chrome/User Data/Default/Bookmarks`
- **Linux**: `~/.config/google-chrome/Default/Bookmarks`

## 书签数据结构

每个书签项包含以下信息：

```javascript
{
  id: "书签ID",
  name: "书签名称",
  url: "书签URL（仅书签类型有此字段）",
  type: "bookmark" | "folder",
  folder: "所在文件夹路径",
  dateAdded: "添加时间（ISO格式）",
  dateModified: "修改时间（ISO格式）",
  childrenCount: "子项数量（仅文件夹类型有此字段）"
}
```

## 导出格式

### JSON 格式
标准的 JSON 数组，包含完整的书签信息，适合程序处理。

### CSV 格式
包含以下列：名称、类型、网址、文件夹、添加时间、修改时间。

### HTML 格式
生成美观的 HTML 页面，包含可点击的链接和样式，适合在浏览器中查看。

## 注意事项

1. **Chrome 需要关闭** - 读取书签文件时，建议关闭 Chrome 浏览器以确保文件不被锁定
2. **权限问题** - 确保 Node.js 进程有权限访问 Chrome 用户数据目录
3. **文件编码** - Chrome 书签文件使用 UTF-8 编码，工具会正确处理中文等非 ASCII 字符

## 系统要求

- Node.js 12.0.0 或更高版本
- 已安装并使用过 Chrome 浏览器

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！ 