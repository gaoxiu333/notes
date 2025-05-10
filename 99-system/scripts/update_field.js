/**
 * 更新文件元数据中的updated字段
 * 
 * ## 功能说明
 * 此脚本自动将笔记YAML前置元数据中的updated字段更新为当前时间，
 * 用于跟踪笔记的最后修改时间。
 * 
 * ## 安装方法
 * 1. 确保此文件位于 99-system/scripts/ 目录下
 * 2. 在Obsidian中启用Templater插件
 * 3. 在Templater设置中，配置"Script files folder"为 99-system/scripts
 * 4. 重启Obsidian或重新加载Templater插件
 * 
 * ## 使用方法
 * 
 * ### 方法一：在模板中自动应用
 * 在模板文件末尾添加以下代码，使创建新笔记时自动更新时间：
 * ```
 * <%* this.app.plugins.plugins["templater-obsidian"].templater.current_functions_object.user.update_field() %>
 * ```
 * 
 * ### 方法二：配置为保存时自动运行
 * 1. 在Templater设置中启用"Trigger Templater on file creation"
 * 2. 在"Folder templates"中配置适当的目录和模板
 * 3. 在模板中加入此脚本调用
 * 
 * ### 方法三：创建快捷命令
 * 1. 在Obsidian设置中找到"Hotkeys"
 * 2. 为"Templater: Open Insert Template modal"设置快捷键
 * 3. 创建一个只包含此脚本调用的简单模板
 * 4. 使用快捷键选择该模板以更新当前笔记的时间戳
 * 
 * ### 方法四：使用文件菜单命令
 * 模板命令也可以通过右键菜单或命令面板执行
 * 
 * ## 注意事项
 * - 此脚本仅更新已有updated字段的笔记
 * - 确保YAML前置元数据格式正确
 * - 时间格式为：YYYY-MM-DD HH:mm
 */

function updateField() {
    try {
        // 获取当前文件的YAML前置元数据
        const activeFile = app.workspace.getActiveFile();
        if (!activeFile) {
            console.log("没有活动文件");
            return;
        }
        
        const cache = app.metadataCache.getFileCache(activeFile);
        if (!cache || !cache.frontmatter) {
            console.log("无法获取文件元数据");
            return;
        }
        
        const yaml = cache.frontmatter;
        
        // 如果元数据存在且有updated字段
        if (yaml && 'updated' in yaml) {
            // 获取当前时间 - 不依赖tp变量
            const now = moment().format("YYYY-MM-DD HH:mm");
            
            // 更新updated字段
            app.fileManager.processFrontMatter(activeFile, fm => {
                fm.updated = now;
                return fm;
            });
            console.log("已更新文件时间戳为:", now);
        } else {
            console.log("文件元数据中没有updated字段");
        }
    } catch (error) {
        console.error("更新时间戳时出错:", error);
    }
}

module.exports = updateField; 