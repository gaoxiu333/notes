#!/usr/bin/env python3
# 批量文件迁移与标准化工具

import os
import re
import shutil
import yaml
import datetime
from pathlib import Path
import argparse
from collections import defaultdict

class NoteMigrator:
    """笔记迁移与标准化工具"""
    
    def __init__(self, source_dir, target_dir, config_file=None):
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.config = self._load_config(config_file)
        self.templates_dir = Path("KnowledgeBase/Templates")
        self.migrated_count = 0
        self.skipped_count = 0
        self.stats = defaultdict(int)
    
    def _load_config(self, config_file):
        """加载迁移配置"""
        default_config = {
            "file_extensions": [".md", ".txt"],
            "exclude_patterns": ["node_modules", ".git", ".obsidian"],
            "default_type": "type/note",
            "default_status": "draft",
            "tag_mappings": {
                "react": "subject/frontend/react",
                "javascript": "subject/frontend/javascript",
                "python": "subject/backend/python",
                "ai": "subject/ai",
                "machine learning": "subject/ai/ml",
                "project": "type/project"
            },
            "content_type_patterns": {
                "type/tutorial": ["step by step", "tutorial", "guide", "how to"],
                "type/concept": ["definition", "what is", "concept of", "understanding"],
                "type/reference": ["cheatsheet", "reference", "quick guide"],
                "type/project": ["project", "implementation", "development"]
            },
            "rename_pattern": "{title}",
            "preserve_original": True
        }
        
        if config_file and Path(config_file).exists():
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    user_config = yaml.safe_load(f)
                    if user_config and isinstance(user_config, dict):
                        for key, value in user_config.items():
                            if key in default_config and isinstance(default_config[key], dict):
                                default_config[key].update(value)
                            else:
                                default_config[key] = value
            except Exception as e:
                print(f"配置文件加载错误: {e}")
                
        return default_config
    
    def _extract_frontmatter(self, content):
        """从笔记内容中提取YAML前置元数据"""
        pattern = r'^---\n(.*?)\n---'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            try:
                return yaml.safe_load(match.group(1)), True
            except:
                return {}, False
        return {}, False
    
    def _detect_content_type(self, content, title):
        """根据内容和标题猜测笔记类型"""
        content_lower = content.lower()
        title_lower = title.lower()
        
        # 检查内容模式
        for note_type, patterns in self.config["content_type_patterns"].items():
            for pattern in patterns:
                if pattern in content_lower or pattern in title_lower:
                    return note_type
        
        # 基于标题中的关键词判断
        if any(word in title_lower for word in ["project", "开发", "实现"]):
            return "type/project"
        elif any(word in title_lower for word in ["tutorial", "guide", "howto", "教程"]):
            return "type/tutorial"
        elif any(word in title_lower for word in ["concept", "概念", "理论", "原理"]):
            return "type/concept"
        elif any(word in title_lower for word in ["cheatsheet", "reference", "速查"]):
            return "type/reference"
        
        # 默认类型
        return self.config["default_type"]
    
    def _detect_subject_tags(self, content, title, existing_tags=None):
        """根据内容和标题猜测主题标签"""
        content_lower = content.lower()
        title_lower = title.lower()
        detected_tags = []
        
        # 首先检查已有标签中是否有可映射的
        if existing_tags:
            for tag in existing_tags:
                if isinstance(tag, str) and tag in self.config["tag_mappings"]:
                    detected_tags.append(self.config["tag_mappings"][tag])
        
        # 检查内容中的关键词
        for keyword, mapped_tag in self.config["tag_mappings"].items():
            if keyword in content_lower or keyword in title_lower:
                if mapped_tag not in detected_tags:
                    detected_tags.append(mapped_tag)
        
        return detected_tags
    
    def _generate_frontmatter(self, original_path, content, original_frontmatter=None):
        """生成标准化的YAML前置元数据"""
        if original_frontmatter is None:
            original_frontmatter = {}
        
        # 提取或生成标题
        title = original_frontmatter.get('title', None)
        if not title:
            # 尝试从文件名或内容中提取标题
            filename = original_path.stem.replace('-', ' ').replace('_', ' ')
            
            # 尝试从内容的第一个标题行提取
            title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
            if title_match:
                title = title_match.group(1)
            else:
                title = filename.title()  # 将文件名转换为标题格式
        
        # 确定创建日期和更新日期
        date = original_frontmatter.get('date', 
                    original_frontmatter.get('created', 
                        datetime.datetime.now().strftime('%Y-%m-%d')))
        
        updated = original_frontmatter.get('updated', date)
        
        # 处理标签
        existing_tags = original_frontmatter.get('tags', [])
        if isinstance(existing_tags, str):
            existing_tags = [tag.strip() for tag in existing_tags.split(',')]
        
        # 确定笔记类型
        note_type = next((tag for tag in existing_tags if tag.startswith('type/')), None)
        if not note_type:
            note_type = self._detect_content_type(content, title)
        
        # 确定主题标签
        subject_tags = self._detect_subject_tags(content, title, existing_tags)
        
        # 合并所有标签
        all_tags = [note_type] + subject_tags
        for tag in existing_tags:
            if not tag.startswith('type/') and tag not in all_tags and tag not in self.config["tag_mappings"]:
                all_tags.append(tag)
        
        # 状态标签
        status = original_frontmatter.get('status', self.config["default_status"])
        
        # 构建前置元数据
        frontmatter = {
            'title': title,
            'date': date,
            'updated': updated,
            'tags': all_tags,
            'status': status
        }
        
        # 保留原始元数据中的其他字段
        for key, value in original_frontmatter.items():
            if key not in frontmatter and key not in ['title', 'date', 'updated', 'tags', 'status']:
                frontmatter[key] = value
        
        return frontmatter, title
    
    def _determine_target_path(self, original_path, frontmatter):
        """确定迁移目标路径"""
        # 获取标签信息辅助决定目标路径
        tags = frontmatter.get('tags', [])
        
        # 默认放在Knowledge/Concepts下
        target_subdir = "KnowledgeBase/Concepts"
        
        # 根据标签确定一个更合适的目录
        subject_tag = next((tag for tag in tags if tag.startswith('subject/')), None)
        type_tag = next((tag for tag in tags if tag.startswith('type/')), None)
        
        # 根据主题标签确定技术目录
        if subject_tag:
            parts = subject_tag.split('/')
            if len(parts) >= 2:
                main_subject = parts[1].capitalize()
                
                if main_subject == 'Frontend':
                    target_subdir = "Technology/Frontend"
                    if len(parts) >= 3:
                        sub_subject = parts[2].capitalize()
                        target_subdir = f"Technology/Frontend/{sub_subject}"
                
                elif main_subject == 'Backend':
                    target_subdir = "Technology/Backend"
                    if len(parts) >= 3:
                        sub_subject = parts[2].capitalize()
                        target_subdir = f"Technology/Backend/{sub_subject}"
                
                elif main_subject == 'Ai':
                    target_subdir = "Technology/AI"
                    if len(parts) >= 3:
                        sub_subject = parts[2].upper() if parts[2] in ['ml', 'llm'] else parts[2].capitalize()
                        target_subdir = f"Technology/AI/{sub_subject}"
        
        # 根据类型标签调整目录
        if type_tag:
            if type_tag == 'type/project':
                status = frontmatter.get('status', 'active')
                if status == 'completed':
                    target_subdir = "Projects/Completed"
                elif status == 'planning':
                    target_subdir = "Projects/Planning"
                else:
                    target_subdir = "Projects/Active"
            
            elif type_tag == 'type/moc':
                target_subdir = "KnowledgeBase/MOCs"
            
            elif type_tag == 'type/reference':
                target_subdir = "Resources/Guides"
            
            elif type_tag == 'type/template':
                target_subdir = "KnowledgeBase/Templates"
        
        # 准备文件名
        title = frontmatter.get('title', original_path.stem)
        # 转换为kebab-case
        filename = re.sub(r'[^\w\s-]', '', title.lower())
        filename = re.sub(r'[\s_]+', '-', filename)
        
        # 确保目标目录存在
        full_target_dir = self.target_dir / target_subdir
        full_target_dir.mkdir(parents=True, exist_ok=True)
        
        # 返回完整的目标路径
        return full_target_dir / f"{filename}.md"
    
    def process_file(self, file_path):
        """处理单个文件"""
        rel_path = file_path.relative_to(self.source_dir)
        
        # 检查是否应该排除该文件
        for pattern in self.config["exclude_patterns"]:
            if pattern in str(rel_path):
                print(f"跳过排除文件: {rel_path}")
                self.skipped_count += 1
                return False
        
        # 检查文件扩展名
        if file_path.suffix.lower() not in self.config["file_extensions"]:
            self.skipped_count += 1
            return False
        
        try:
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 提取前置元数据
            original_frontmatter, has_frontmatter = self._extract_frontmatter(content)
            
            # 生成标准化的前置元数据
            frontmatter, title = self._generate_frontmatter(file_path, content, original_frontmatter)
            
            # 确定目标路径
            target_path = self._determine_target_path(file_path, frontmatter)
            
            # 准备新内容
            yaml_frontmatter = yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False)
            
            if has_frontmatter:
                # 替换原有前置元数据
                new_content = re.sub(r'^---\n.*?\n---\n', f'---\n{yaml_frontmatter}---\n', content, flags=re.DOTALL)
            else:
                # 添加前置元数据
                new_content = f'---\n{yaml_frontmatter}---\n\n{content}'
            
            # 确保目标目录存在
            target_path.parent.mkdir(parents=True, exist_ok=True)
            
            # 写入新文件
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            # 更新统计信息
            self.migrated_count += 1
            
            # 记录分类信息
            note_type = next((tag for tag in frontmatter.get('tags', []) if tag.startswith('type/')), 'untyped')
            self.stats[note_type] += 1
            
            print(f"已迁移: {rel_path} -> {target_path.relative_to(self.target_dir)}")
            return True
            
        except Exception as e:
            print(f"处理文件 {rel_path} 时出错: {e}")
            self.skipped_count += 1
            return False
    
    def migrate_all(self):
        """迁移所有符合条件的文件"""
        print(f"开始从 {self.source_dir} 迁移文件到 {self.target_dir}...")
        
        # 遍历源目录中的所有文件
        for root, _, files in os.walk(self.source_dir):
            root_path = Path(root)
            
            for file in files:
                file_path = root_path / file
                self.process_file(file_path)
        
        # 打印统计信息
        print(f"\n迁移完成！")
        print(f"成功迁移: {self.migrated_count} 文件")
        print(f"跳过文件: {self.skipped_count} 文件")
        print("\n笔记类型统计:")
        for note_type, count in self.stats.items():
            print(f"  {note_type}: {count} 文件")
    
    def generate_migration_report(self, report_path):
        """生成迁移报告"""
        report = f"""# 笔记迁移报告
生成时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}

## 迁移统计
- 源目录: {self.source_dir}
- 目标目录: {self.target_dir}
- 成功迁移: {self.migrated_count} 文件
- 跳过文件: {self.skipped_count} 文件

## 笔记类型统计
"""
        for note_type, count in self.stats.items():
            report += f"- {note_type}: {count} 文件\n"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"迁移报告已生成: {report_path}")

def main():
    parser = argparse.ArgumentParser(description="批量迁移与标准化Markdown笔记")
    parser.add_argument("source", help="源目录路径")
    parser.add_argument("target", help="目标目录路径")
    parser.add_argument("--config", "-c", help="配置文件路径")
    parser.add_argument("--report", "-r", help="生成报告的路径")
    
    args = parser.parse_args()
    
    migrator = NoteMigrator(args.source, args.target, args.config)
    migrator.migrate_all()
    
    if args.report:
        migrator.generate_migration_report(args.report)

if __name__ == "__main__":
    main() 