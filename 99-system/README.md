# 99-system 系统文件夹

这里存放**知识库系统配置和全局辅助工具**，包括模板、脚本、样式和全局导航等。

## 子目录结构

- 99-templates：存放各类笔记模板
- 99-scripts：存放自动化脚本
- 99-styles：存放CSS片段
- 99-MOCs：存放全局内容地图

## 模板系统

模板文件命名规则：`_tpl-[类型]`，如：

- `_tpl-note`：普通笔记模板
- `_tpl-project`：项目笔记模板
- `_tpl-meeting`：会议记录模板
- `_tpl-snippet`：代码片段模板
- `_tpl-tech-cheatsheet`：技术速查表模板

## 脚本功能

- **jd_id**：自动生成Johnny-Decimal编号
  - 用于生成笔记的唯一ID编号
  - 在模板中通过以下代码调用：
    ```
    00.00.0001
    ```

- **update_field**：自动更新元数据中的updated字段
  - 功能：每次保存笔记时自动更新元数据中的updated时间戳
  - 配置方法：
    1. 确保Templater插件已启用
    2. 在Templater设置中配置脚本目录指向`99-system/scripts`
    3. 在需要自动更新时间的模板最后添加以下代码（已注释状态）:
       ```
       
       ```
    4. 取消注释以启用自动更新功能
  - 使用说明详见脚本文件注释

- **move_to_folder**：辅助笔记分类移动
  - 用于将笔记从收集箱移动到适当分类位置
  - 同时保持链接关系

## 样式配置

- 代码块高亮样式
- 技术文档专用格式
- 图谱可视化样式
- ...

## 全局MOC

- MOC-dashboard：知识库总览
- MOC-projects：项目索引
- MOC-areas：领域索引
- MOC-resources：资源索引

## 系统维护

定期执行的系统维护任务：

1. 标签系统整理（每月）
2. 孤岛笔记检查（每周）
3. 过期项目提醒（每周）
4. 知识库健康度检查（每月）

## 自动化说明

### 启用元数据自动更新

1. 打开设置 > 第三方插件 > Templater
2. 在"Script files folder"设置为`99-system/scripts`
3. 勾选"Trigger Templater on file creation"
4. 在模板末尾找到以下代码并取消注释（删除注释符号）：
   ```
   
   ``` 