#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const os = require('os');

/**
 * Chrome 书签读取器
 * 支持读取和解析 Chrome 浏览器的书签数据
 */
class ChromeBookmarksReader {
  constructor() {
    this.bookmarksPath = this.getBookmarksPath();
  }

  /**
   * 获取 Chrome 书签文件路径
   * @returns {string} 书签文件路径
   */
  getBookmarksPath() {
    const platform = os.platform();
    const homeDir = os.homedir();
    
    let bookmarksPath;
    
    switch (platform) {
      case 'darwin': // macOS
        bookmarksPath = path.join(homeDir, 'Library/Application Support/Google/Chrome/Default/Bookmarks');
        break;
      case 'win32': // Windows
        bookmarksPath = path.join(homeDir, 'AppData/Local/Google/Chrome/User Data/Default/Bookmarks');
        break;
      case 'linux': // Linux
        bookmarksPath = path.join(homeDir, '.config/google-chrome/Default/Bookmarks');
        break;
      default:
        throw new Error(`不支持的操作系统: ${platform}`);
    }
    
    return bookmarksPath;
  }

  /**
   * 检查书签文件是否存在
   * @returns {boolean} 文件是否存在
   */
  bookmarksFileExists() {
    return fs.existsSync(this.bookmarksPath);
  }

  /**
   * 读取书签文件
   * @returns {Object} 解析后的书签数据
   */
  readBookmarks() {
    if (!this.bookmarksFileExists()) {
      throw new Error(`书签文件不存在: ${this.bookmarksPath}`);
    }

    try {
      const bookmarksData = fs.readFileSync(this.bookmarksPath, 'utf8');
      return JSON.parse(bookmarksData);
    } catch (error) {
      throw new Error(`读取书签文件失败: ${error.message}`);
    }
  }

  /**
   * 递归解析书签节点
   * @param {Object} node 书签节点
   * @param {Array} bookmarksList 书签列表
   * @param {string} folderPath 文件夹路径
   */
  parseBookmarkNode(node, bookmarksList = [], folderPath = '') {
    if (node.type === 'url') {
      bookmarksList.push({
        id: node.id,
        name: node.name,
        url: node.url,
        dateAdded: new Date(parseInt(node.date_added) / 1000).toISOString(),
        dateModified: node.date_modified ? new Date(parseInt(node.date_modified) / 1000).toISOString() : null,
        folder: folderPath,
        type: 'bookmark'
      });
    } else if (node.type === 'folder') {
      const currentPath = folderPath ? `${folderPath}/${node.name}` : node.name;
      
      bookmarksList.push({
        id: node.id,
        name: node.name,
        dateAdded: new Date(parseInt(node.date_added) / 1000).toISOString(),
        dateModified: node.date_modified ? new Date(parseInt(node.date_modified) / 1000).toISOString() : null,
        folder: folderPath,
        type: 'folder',
        childrenCount: node.children ? node.children.length : 0
      });

      if (node.children) {
        node.children.forEach(child => {
          this.parseBookmarkNode(child, bookmarksList, currentPath);
        });
      }
    }

    return bookmarksList;
  }

  /**
   * 获取所有书签
   * @returns {Array} 书签列表
   */
  getAllBookmarks() {
    const bookmarksData = this.readBookmarks();
    const bookmarksList = [];

    // Chrome 书签结构包含 bookmark_bar（书签栏）、other（其他书签）、synced（同步书签）
    const roots = bookmarksData.roots;
    
    if (roots.bookmark_bar) {
      this.parseBookmarkNode(roots.bookmark_bar, bookmarksList, '书签栏');
    }
    
    if (roots.other) {
      this.parseBookmarkNode(roots.other, bookmarksList, '其他书签');
    }
    
    if (roots.synced) {
      this.parseBookmarkNode(roots.synced, bookmarksList, '移动设备书签');
    }

    return bookmarksList;
  }

  /**
   * 按类型筛选书签
   * @param {string} type 类型：'bookmark' 或 'folder'
   * @returns {Array} 筛选后的书签列表
   */
  getBookmarksByType(type) {
    const allBookmarks = this.getAllBookmarks();
    return allBookmarks.filter(item => item.type === type);
  }

  /**
   * 按文件夹筛选书签
   * @param {string} folderName 文件夹名称
   * @returns {Array} 筛选后的书签列表
   */
  getBookmarksByFolder(folderName) {
    const allBookmarks = this.getAllBookmarks();
    return allBookmarks.filter(item => item.folder.includes(folderName));
  }

  /**
   * 搜索书签
   * @param {string} keyword 关键词
   * @returns {Array} 搜索结果
   */
  searchBookmarks(keyword) {
    const allBookmarks = this.getAllBookmarks();
    const lowerKeyword = keyword.toLowerCase();
    
    return allBookmarks.filter(item => 
      item.name.toLowerCase().includes(lowerKeyword) ||
      (item.url && item.url.toLowerCase().includes(lowerKeyword)) ||
      item.folder.toLowerCase().includes(lowerKeyword)
    );
  }

  /**
   * 导出书签到文件
   * @param {string} outputPath 输出文件路径
   * @param {string} format 格式：'json', 'csv', 'html', 'markdown'
   */
  exportBookmarks(outputPath, format = 'json') {
    const bookmarks = this.getAllBookmarks();
    
    switch (format.toLowerCase()) {
      case 'json':
        this.exportToJSON(bookmarks, outputPath);
        break;
      case 'csv':
        this.exportToCSV(bookmarks, outputPath);
        break;
      case 'html':
        this.exportToHTML(bookmarks, outputPath);
        break;
      case 'markdown':
      case 'md':
        this.exportToMarkdown(bookmarks, outputPath);
        break;
      default:
        throw new Error(`不支持的导出格式: ${format}`);
    }
    
    console.log(`书签已导出到: ${outputPath}`);
  }

  /**
   * 导出为 JSON 格式
   */
  exportToJSON(bookmarks, outputPath) {
    fs.writeFileSync(outputPath, JSON.stringify(bookmarks, null, 2), 'utf8');
  }

  /**
   * 导出为 CSV 格式
   */
  exportToCSV(bookmarks, outputPath) {
    const headers = ['名称', '类型', '网址', '文件夹', '添加时间', '修改时间'];
    const csvContent = [
      headers.join(','),
      ...bookmarks.map(bookmark => [
        `"${bookmark.name}"`,
        bookmark.type,
        `"${bookmark.url || ''}"`,
        `"${bookmark.folder}"`,
        bookmark.dateAdded,
        bookmark.dateModified || ''
      ].join(','))
    ].join('\n');
    
    fs.writeFileSync(outputPath, csvContent, 'utf8');
  }

  /**
   * 导出为 HTML 格式
   */
  exportToHTML(bookmarks, outputPath) {
    const htmlContent = `
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Chrome 书签导出</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .folder { font-weight: bold; color: #333; margin: 10px 0; }
        .bookmark { margin-left: 20px; margin: 5px 0; }
        .bookmark a { text-decoration: none; color: #1a0dab; }
        .bookmark a:hover { text-decoration: underline; }
        .meta { color: #666; font-size: 12px; }
    </style>
</head>
<body>
    <h1>Chrome 书签</h1>
    ${bookmarks.map(item => {
      if (item.type === 'folder') {
        return `<div class="folder">📁 ${item.name}</div>`;
      } else {
        return `<div class="bookmark">
          <a href="${item.url}" target="_blank">${item.name}</a>
          <div class="meta">添加时间: ${item.dateAdded} | 文件夹: ${item.folder}</div>
        </div>`;
      }
    }).join('')}
</body>
</html>`;
    
    fs.writeFileSync(outputPath, htmlContent, 'utf8');
  }

  /**
   * 导出为 Markdown 格式
   */
  exportToMarkdown(bookmarks, outputPath) {
    // 构建层级结构
    const structure = this.buildHierarchicalStructure(bookmarks);
    
    let markdownContent = `# Chrome 书签\n\n`;
    markdownContent += `> 导出时间: ${new Date().toLocaleString()}\n\n`;
    
    // 生成 Markdown 内容
    markdownContent += this.generateMarkdownFromStructure(structure);
    
    fs.writeFileSync(outputPath, markdownContent, 'utf8');
  }

  /**
   * 构建层级结构用于 Markdown 导出
   */
  buildHierarchicalStructure(bookmarks) {
    const structure = {
      '书签栏': { folders: {}, bookmarks: [] },
      '其他书签': { folders: {}, bookmarks: [] },
      '移动设备书签': { folders: {}, bookmarks: [] }
    };

    bookmarks.forEach(item => {
      const rootFolder = item.folder.split('/')[0];
      const pathParts = item.folder.split('/').slice(1);
      
      if (!structure[rootFolder]) {
        structure[rootFolder] = { folders: {}, bookmarks: [] };
      }

      let currentLevel = structure[rootFolder];
      
      // 构建文件夹层级
      pathParts.forEach(folderName => {
        if (folderName && !currentLevel.folders[folderName]) {
          currentLevel.folders[folderName] = { folders: {}, bookmarks: [] };
        }
        if (folderName) {
          currentLevel = currentLevel.folders[folderName];
        }
      });

      // 添加书签
      if (item.type === 'bookmark') {
        currentLevel.bookmarks.push(item);
      }
    });

    return structure;
  }

  /**
   * 从层级结构生成 Markdown 内容
   */
  generateMarkdownFromStructure(structure, level = 2) {
    let content = '';
    
    Object.entries(structure).forEach(([folderName, data]) => {
      if (data.bookmarks.length > 0 || Object.keys(data.folders).length > 0) {
        // 添加文件夹标题
        content += `${'#'.repeat(level)} ${folderName}\n\n`;
        
        // 添加书签
        if (data.bookmarks.length > 0) {
          data.bookmarks
            .sort((a, b) => a.name.localeCompare(b.name))
            .forEach(bookmark => {
              content += `- [${bookmark.name}](${bookmark.url})\n`;
              content += `  > 📅 添加时间: ${bookmark.dateAdded.split('T')[0]}\n\n`;
            });
        }
        
        // 递归处理子文件夹
        if (Object.keys(data.folders).length > 0) {
          content += this.generateMarkdownFromStructure(data.folders, level + 1);
        }
      }
    });
    
    return content;
  }

  /**
   * 显示书签统计信息
   */
  showStatistics() {
    const allBookmarks = this.getAllBookmarks();
    const bookmarks = allBookmarks.filter(item => item.type === 'bookmark');
    const folders = allBookmarks.filter(item => item.type === 'folder');
    
    const folderStats = {};
    bookmarks.forEach(bookmark => {
      const folder = bookmark.folder || '未分类';
      folderStats[folder] = (folderStats[folder] || 0) + 1;
    });

    console.log('\n📊 书签统计信息:');
    console.log(`总书签数: ${bookmarks.length}`);
    console.log(`文件夹数: ${folders.length}`);
    console.log('\n📁 各文件夹书签数量:');
    
    Object.entries(folderStats)
      .sort(([,a], [,b]) => b - a)
      .forEach(([folder, count]) => {
        console.log(`  ${folder}: ${count} 个书签`);
      });
  }
}

// CLI 使用部分
if (require.main === module) {
  const args = process.argv.slice(2);
  const reader = new ChromeBookmarksReader();

  try {
    if (!reader.bookmarksFileExists()) {
      console.error('❌ Chrome 书签文件不存在，请确保 Chrome 浏览器已安装并使用过。');
      console.log(`书签文件路径: ${reader.bookmarksPath}`);
      process.exit(1);
    }

    const command = args[0];
    
    switch (command) {
      case 'list':
      case 'ls':
        const bookmarks = reader.getAllBookmarks();
        console.log(`\n📚 找到 ${bookmarks.length} 个项目:\n`);
        bookmarks.forEach(item => {
          const icon = item.type === 'folder' ? '📁' : '🔖';
          const url = item.url ? ` (${item.url})` : '';
          console.log(`${icon} ${item.name}${url}`);
          console.log(`   文件夹: ${item.folder} | 添加时间: ${item.dateAdded}`);
        });
        break;

      case 'folders':
        const folders = reader.getBookmarksByType('folder');
        console.log(`\n📁 找到 ${folders.length} 个文件夹:\n`);
        folders.forEach(folder => {
          console.log(`📁 ${folder.name} (${folder.childrenCount} 项)`);
          console.log(`   路径: ${folder.folder} | 添加时间: ${folder.dateAdded}`);
        });
        break;

      case 'search':
        const keyword = args[1];
        if (!keyword) {
          console.error('❌ 请提供搜索关键词');
          process.exit(1);
        }
        const results = reader.searchBookmarks(keyword);
        console.log(`\n🔍 搜索 "${keyword}" 的结果 (${results.length} 个):\n`);
        results.forEach(item => {
          const icon = item.type === 'folder' ? '📁' : '🔖';
          const url = item.url ? ` (${item.url})` : '';
          console.log(`${icon} ${item.name}${url}`);
        });
        break;

      case 'export':
        const format = args[1] || 'json';
        const outputPath = args[2] || `bookmarks_export.${format}`;
        reader.exportBookmarks(outputPath, format);
        break;

      case 'stats':
        reader.showStatistics();
        break;

      case 'help':
      case '--help':
      case '-h':
      default:
        console.log(`
📚 Chrome 书签读取器

用法:
  node chrome-bookmarks-reader.js [command] [options]

命令:
  list, ls              列出所有书签和文件夹
  folders               只显示文件夹
  search <keyword>      搜索书签
  export [format] [path] 导出书签 (format: json|csv|html|markdown)
  stats                 显示统计信息
  help                  显示帮助信息

示例:
  node chrome-bookmarks-reader.js list
  node chrome-bookmarks-reader.js search "github"
  node chrome-bookmarks-reader.js export json bookmarks.json
  node chrome-bookmarks-reader.js export html bookmarks.html
  node chrome-bookmarks-reader.js export markdown bookmarks.md
  node chrome-bookmarks-reader.js stats

书签文件位置: ${reader.bookmarksPath}
        `);
        break;
    }
  } catch (error) {
    console.error(`❌ 错误: ${error.message}`);
    process.exit(1);
  }
}

module.exports = ChromeBookmarksReader; 