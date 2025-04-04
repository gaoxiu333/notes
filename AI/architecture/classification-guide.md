# 知识分类指南

## 1. 分类体系

### 1.1 主要分类维度

1. **领域分类**
   - AI/机器学习
   - Web开发
   - 工程实践
   - 工具使用

2. **内容类型**
   - 概念解释
   - 技术教程
   - 最佳实践
   - 工具指南
   - 参考资料

3. **难度等级**
   - 入门 (🟢)
   - 基础 (🟡)
   - 进阶 (🟠)
   - 专家 (🔴)

### 1.2 标签规范

```yaml
---
domain: [AI, Web开发, 工程实践, 工具使用]
type: [概念, 教程, 实践, 工具, 参考]
level: [入门, 基础, 进阶, 专家]
tech: [具体技术标签]
status: [草稿, 审核中, 已发布]
---
```

## 2. 文件命名规范

### 2.1 通用规则
- 使用kebab-case
- 避免特殊字符
- 使用有意义的描述性名称

### 2.2 命名模式
```
[主题]-[子主题]-[具体内容].md
```

示例：
- ai-prompt-engineering-basics.md
- web-react-hooks-guide.md
- tools-git-workflow.md

## 3. 目录组织

### 3.1 标准目录结构
```
主题/
├── README.md
├── 基础/
│   ├── 概念/
│   ├── 教程/
│   └── 实践/
├── 进阶/
│   ├── 技术/
│   ├── 方法/
│   └── 案例/
└── 资源/
    ├── 工具/
    ├── 参考/
    └── 模板/
```

### 3.2 README.md模板
```markdown
# [主题名称]

## 简介
[主题简要说明]

## 目录结构
[文件树形图]

## 快速开始
[入门指南]

## 重要文档
[核心文档链接]
```

## 4. 内容组织规范

### 4.1 文档结构
1. **标题区域**
   - 文档标题
   - 元数据（tags, category等）
   - 简短描述

2. **主体内容**
   - 目标/简介
   - 主要内容
   - 示例/演示
   - 注意事项

3. **补充信息**
   - 相关链接
   - 参考资料
   - 更新记录

### 4.2 内容质量标准
- ✓ 确保信息准确性
- ✓ 保持结构一致性
- ✓ 提供实践示例
- ✓ 包含必要说明
- ✓ 及时更新维护

## 5. 知识关联

### 5.1 内部链接
使用相对路径：
```markdown
[相关主题](../相关主题.md)
```

### 5.2 知识图谱
- 使用Mermaid绘制关系图
- 标注关键连接点
- 保持图谱更新

### 5.3 索引维护
- 主题索引
- 标签索引
- 技术栈索引

## 6. 维护流程

### 6.1 内容更新
1. 定期检查过期内容
2. 补充新的实践经验
3. 更新相关链接
4. 优化内容结构

### 6.2 质量控制
- 内容审查清单
- 格式规范检查
- 链接有效性验证
- 分类准确性确认

## 7. 最佳实践

### 7.1 文档编写
- 使用清晰的语言
- 提供具体示例
- 包含实践建议
- 注明参考来源

### 7.2 分类管理
- 避免过深的层级
- 保持分类简洁
- 定期整理归档
- 及时更新索引

## 8. 更新日志

- 2024-04-03：创建文档
- 2024-04-03：完善分类规范
