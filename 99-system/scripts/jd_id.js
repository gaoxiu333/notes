/**
 * 为笔记生成Johnny-Decimal ID
 * 使用方法: <% tp.user.jd_id() %>
 * 生成格式: JXX-YYYYMMDD-HHMM，符合PKM规范
 */

function getJDId() {
    try {
        // 获取文件路径
        const filePath = this.app.workspace.getActiveFile().path;
        
        // 检查文件是否已有JD ID
        const fileCache = this.app.metadataCache.getFileCache(this.app.workspace.getActiveFile());
        if (fileCache && fileCache.frontmatter && fileCache.frontmatter.jd_id) {
            return fileCache.frontmatter.jd_id;
        }
        
        // 分析路径以生成ID
        const pathSegments = filePath.split('/');
        
        // 如果路径不包含至少一个目录，则使用默认值
        if (pathSegments.length <= 1) {
            return "J00-" + moment().format("YYYYMMDD-HHmm");
        }
        
        // 获取顶级目录
        const topFolder = pathSegments[0];
        
        // 获取顶级目录的编号部分（如"00"、"10"等）
        const folderMatch = topFolder.match(/^(\d{2})/);
        const folderNum = folderMatch ? folderMatch[1] : "00";
        
        // 生成当前时间戳部分
        const timestamp = moment().format("YYYYMMDD-HHmm");
        
        // 返回格式为 JXX-YYYYMMDD-HHMM 的ID
        return `J${folderNum}-${timestamp}`;
    } catch (error) {
        console.error("生成JD ID时出错:", error);
        return "J00-" + moment().format("YYYYMMDD-HHmm"); // 返回默认值作为备选
    }
}

module.exports = getJDId; 