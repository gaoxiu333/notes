/**
 * 为笔记生成Johnny-Decimal ID
 * 使用方法: <% tp.user.jd_id() %>
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
            return "00.00.0001";
        }
        
        // 获取顶级目录
        const topFolder = pathSegments[0];
        
        // 获取顶级目录的编号部分（如"00"、"10"等）
        const folderMatch = topFolder.match(/^(\d{2})/);
        const folderNum = folderMatch ? folderMatch[1] : "00";
        
        // 如果有二级目录，则使用二级目录的编号
        let subFolderNum = "00";
        if (pathSegments.length > 2) {
            const subFolder = pathSegments[1];
            const subFolderMatch = subFolder.match(/^(\d{2})/);
            subFolderNum = subFolderMatch ? subFolderMatch[1] : "00";
        }
        
        // 为当前路径生成一个基于时间的唯一ID
        const timestamp = new Date().getTime();
        const uniqueId = (timestamp % 10000).toString().padStart(4, '0');
        
        // 最后4位限制为0001-9999
        const itemNum = (uniqueId % 9999) + 1;
        const formattedItemNum = itemNum.toString().padStart(4, '0');
        
        return `${folderNum}.${subFolderNum}.${formattedItemNum}`;
    } catch (error) {
        console.error("生成JD ID时出错:", error);
        return "00.00.0001"; // 返回默认值作为备选
    }
}

module.exports = getJDId; 