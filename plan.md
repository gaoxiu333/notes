# Notion 内容迁移计划

## 一、迁移准备

1. **标签设置**：
   - 添加 `#source/notion` 标签作为来源标签
   - 为每个Notion内容添加符合四大命名空间的标签：
     - `#topic/...`：内容主题标签
     - `#status/...`：内容状态标签（如 draft, active, archived）
     - `#action/...`：行动标签（如 review, revisit）
     - `#lang/...`：编程语言标签（适用于代码片段）

2. **API准备**：
   - 设置Notion API访问权限
   - 准备API调用方法，获取内容并保留元数据

## 二、内容映射

### 文件路径映射

将Notion内容映射到知识库结构：

| Notion内容 | 目标路径 | 内容类型 | 建议标签 |
|------------|----------|----------|----|
| Frontend Dev数据库 | 20-areas/20-01-前端开发/ | 知识领域 | #topic/frontend |
| Nodejs数据库 | 30-resources/code-snippets/backend/node/ | 代码片段 | #topic/backend/nodejs #lang/javascript |
| 常用堆栈 | 30-resources/30-01-前端技术/ | 技术资源 | #topic/frontend/stack |
| CS学习指南 | 30-resources/code-snippets/ (按类型分类) | 代码资源 | #topic/cs |
| Python相关 | 30-resources/code-snippets/backend/python/ | 代码片段 | #topic/backend/python #lang/python |
| 小程序开发 | 30-resources/code-snippets/frontend/wechat-miniprogram/ | 代码片段 | #topic/frontend/miniprogram |
| Git配置/Git Submodules | 30-resources/code-snippets/devops/ | 开发工具 | #topic/devops/git |
| Docker相关内容 | 30-resources/code-snippets/devops/docker/ | 运维知识 | #topic/devops/docker |
| Nginx参考 | 30-resources/code-snippets/devops/ | 服务器配置 | #topic/devops/nginx |
| 算法学习/数据结构 | 30-resources/code-snippets/algorithms/ | 算法资源 | #topic/cs/algorithms #topic/cs/data-structures |
| Linux笔记 | 30-resources/code-snippets/devops/ | 系统知识 | #topic/devops/linux |
| Vue/React配置 | 30-resources/code-snippets/frontend/ | 前端框架 | #topic/frontend/framework |
| 数据库相关 | 30-resources/code-snippets/database/ | 数据库知识 | #topic/database |
| 年度总结 | 90-archive/年度总结/ | 归档内容 | #status/archived |
| 3D/Threejs | 30-resources/code-snippets/frontend/ | 前端技术 | #topic/frontend/3d #lang/javascript |
| Dev environment | 30-resources/tools/ | 开发环境 | #topic/tools/dev-environment |
| 动画 | 30-resources/code-snippets/frontend/css/ | 前端技术 | #topic/frontend/animation #lang/css |

### 内容模板映射

根据不同内容类型，采用适当的Obsidian模板：

| 内容类型 | 适用模板 | 适用范围 |
|----------|----------|----------|
| 普通笔记 | _tpl-note | 一般性知识记录 |
| 代码片段 | _tpl-snippet | 复用的代码片段 |
| 技术速查表 | _tpl-tech-cheatsheet | 技术概览、命令集合 |
| 项目文档 | _tpl-project | 项目描述与计划 |
| 内容地图 | _tpl-moc | 分类内容索引 |

## 三、迁移流程

### 1. 内容获取

- 使用Notion API获取所有页面列表和内容
- 提取页面ID、标题、创建时间、最后编辑时间和内容
- 构建页面层次结构关系

### 2. 内容转换

- 将Notion块结构转换为Markdown格式
- 添加符合知识库标准的YAML前置元数据：
  ```yaml
  ---
  title: 文档标题
  created: YYYY-MM-DD HH:mm  # 从API获取
  updated: YYYY-MM-DD HH:mm  # 从API获取
  type: note/resource/snippet  # 根据内容类型选择
  status: active
  schema: v1  # 使用当前版本
  tags: [source/notion, topic/相关主题, lang/语言类型]
  ---
  ```
- 处理内部链接，转换为Obsidian格式 `[[链接]]`

### 3. 内容组织

- 按映射表分类整理内容
- 为主要内容类别创建MOC文件
- 按四大命名空间添加合适的标签
- 更新全局MOC，确保导航完整

### 4. 标签系统应用

按照知识库现有标签体系进行分类：

1. **主题标签 (topic/)**
   - 领域类：`#topic/frontend`、`#topic/backend`、`#topic/devops`
   - 技术类：`#topic/frontend/react`、`#topic/database/mongodb`
   - 概念类：`#topic/cs/algorithms`、`#topic/cs/data-structures`

2. **状态标签 (status/)**
   - `#status/draft` - 初始迁移的内容
   - `#status/active` - 已整理完善的内容
   - `#status/archived` - 历史归档内容

3. **行动标签 (action/)**
   - `#action/revise` - 需要修改完善
   - `#action/migrate` - 正在迁移的内容
   - `#action/review` - 需要复盘回顾

4. **语言标签 (lang/)**
   - `#lang/javascript`、`#lang/typescript`
   - `#lang/python`、`#lang/go`
   - `#lang/css`、`#lang/html`

## 四、迁移执行记录

### 当前迁移进度

已迁移的页面：
1. 常用堆栈 -> `30-resources/30-01-前端技术/常用堆栈/index.md`
2. Vue Admin堆栈 -> `30-resources/30-01-前端技术/常用堆栈/vue-admin-堆栈.md`
3. Node面试题 -> `30-resources/code-snippets/backend/node/node面试题.md`
4. 小程序开发指南 -> `30-resources/code-snippets/frontend/wechat-miniprogram/小程序开发指南.md`
5. 动画 -> `30-resources/code-snippets/frontend/css/动画.md`
6. Git配置 -> `30-resources/code-snippets/devops/git/Git配置.md`
7. node-debug -> `30-resources/code-snippets/backend/node/node-debug.md`
8. pnpm -> `30-resources/code-snippets/backend/node/pnpm.md`
9. yarn -> `30-resources/code-snippets/backend/node/yarn.md`
10. React配置 -> `30-resources/30-01-前端技术/React/React配置.md`

### 迁移内容索引

已创建迁移内容MOC文件：`00-inbox/notion-migration-moc.md`，用于索引和跟踪已迁移的内容。

### 下一步计划

1. 继续使用API方式获取更多Notion页面内容
2. 处理子页面和嵌套内容
3. 补充和完善标签系统
4. 处理页面间链接关系

## 五、验证与完善

1. **基础验证**：
   - 检查元数据格式
   - 验证内部链接
   - 确保标签规范

2. **内容完善**：
   - 标记需要后续完善的内容（`#action/revise`）
   - 添加Dataview查询支持，跟踪迁移内容：
   ```
   ```dataview
   TABLE updated AS "更新时间", status AS "状态", file.folder AS "位置"
   FROM #source/notion
   SORT updated DESC
   ```
   ```

3. **MOC文件创建**：
   - 为每个主要内容领域创建MOC文件
   - 使用`_tpl-moc`模板
   - 连接相关内容和核心概念

## 六、实施步骤

### 阶段1：数据提取
- 开发API调用脚本，获取所有内容
- 存储原始数据，保留结构关系

### 阶段2：内容转换
- 转换为Markdown格式
- 添加符合规范的元数据和标签
- 整理内容到对应目标路径

### 阶段3：整合与验证
- 创建必要的MOC文件
- 验证迁移内容的完整性和正确性
- 更新全局导航，如MOC-dashboard

## 七、注意事项

1. 所有迁移内容必须包含`#source/notion`标签和来源时间信息
2. 保留原始创建和编辑时间
3. 注意API限制，避免频繁请求导致限流
4. 确保内容分类符合知识库PARA+Johnny-Decimal结构
5. 定期使用MOC-health-check评估知识库健康度 