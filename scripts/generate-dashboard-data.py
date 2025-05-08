#!/usr/bin/env python3
# 自动生成仪表板数据脚本

import os
import re
import json
import datetime
import yaml
from pathlib import Path
from collections import Counter, defaultdict

class DashboardGenerator:
    def __init__(self, notes_dir="."):
        self.notes_dir = Path(notes_dir)
        
    def extract_frontmatter(self, content):
        """从笔记内容中提取YAML前置元数据"""
        pattern = r'^---\n(.*?)\n---'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            try:
                return yaml.safe_load(match.group(1))
            except:
                return {}
        return {}
    
    def find_notes_by_subject(self, subject_prefix):
        """查找特定主题领域的笔记"""
        matching_notes = []
        
        for note_path in self.notes_dir.glob("**/*.md"):
            with open(note_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            frontmatter = self.extract_frontmatter(content)
            tags = frontmatter.get('tags', [])
            
            if any(tag.startswith(subject_prefix) for tag in tags):
                note_info = {
                    'path': str(note_path.relative_to(self.notes_dir)),
                    'title': frontmatter.get('title', note_path.stem.replace('-', ' ').title()),
                    'date': frontmatter.get('date', 'Unknown'),
                    'updated': frontmatter.get('updated', frontmatter.get('date', 'Unknown')),
                    'status': frontmatter.get('status', 'Unknown'),
                    'tags': tags
                }
                matching_notes.append(note_info)
        
        return matching_notes
    
    def get_recently_edited(self, subject_notes, limit=5):
        """获取最近编辑的笔记"""
        # 按更新日期排序
        recent_notes = sorted(
            subject_notes, 
            key=lambda x: x.get('updated', '1900-01-01') if x.get('updated') else '1900-01-01',
            reverse=True
        )
        return recent_notes[:limit]
    
    def get_subject_stats(self, subject_notes):
        """获取主题统计信息"""
        total_notes = len(subject_notes)
        tags_counter = Counter()
        statuses = Counter()
        subtopics = defaultdict(int)
        
        for note in subject_notes:
            # 计算状态分布
            statuses[note.get('status', 'unknown')] += 1
            
            # 计算标签分布
            for tag in note.get('tags', []):
                tags_counter[tag] += 1
                
                # 提取子主题
                if tag.startswith('subject/') and '/' in tag[8:]:
                    subtopic = tag.split('/', 2)[1]
                    subtopics[subtopic] += 1
        
        return {
            'total_notes': total_notes,
            'statuses': dict(statuses),
            'common_tags': dict(tags_counter.most_common(10)),
            'subtopics': dict(subtopics)
        }
    
    def find_active_projects(self, subject_prefix):
        """查找与主题相关的活跃项目"""
        projects = []
        
        # 查找Projects目录中的项目笔记
        for project_path in self.notes_dir.glob("Projects/**/*.md"):
            with open(project_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            frontmatter = self.extract_frontmatter(content)
            tags = frontmatter.get('tags', [])
            
            # 检查是否与主题相关
            if any(tag.startswith(subject_prefix) for tag in tags):
                project_info = {
                    'path': str(project_path.relative_to(self.notes_dir)),
                    'title': frontmatter.get('title', project_path.stem.replace('-', ' ').title()),
                    'status': frontmatter.get('status', 'Unknown'),
                    'progress': self._extract_progress(content),
                    'due': frontmatter.get('due', 'Unspecified')
                }
                projects.append(project_info)
        
        # 按状态分组
        active_projects = [p for p in projects if p['status'] == 'active']
        planned_projects = [p for p in projects if p['status'] == 'planned']
        completed_projects = [p for p in projects if p['status'] == 'completed']
        
        return {
            'active': active_projects,
            'planned': planned_projects,
            'completed': completed_projects
        }
    
    def _extract_progress(self, content):
        """尝试从内容中提取进度信息"""
        progress_match = re.search(r'进度[：:]\s*(\d+)%', content)
        if progress_match:
            return int(progress_match.group(1))
        
        # 尝试计算任务完成比例
        total_tasks = len(re.findall(r'- \[[ x]\]', content))
        if total_tasks > 0:
            completed_tasks = len(re.findall(r'- \[x\]', content))
            return int(completed_tasks / total_tasks * 100)
            
        return None
    
    def generate_dashboard_data(self, subject, output_file=None):
        """为特定主题生成仪表板数据"""
        subject_prefix = f"subject/{subject}"
        
        # 收集数据
        subject_notes = self.find_notes_by_subject(subject_prefix)
        stats = self.get_subject_stats(subject_notes)
        recent_notes = self.get_recently_edited(subject_notes)
        projects = self.find_active_projects(subject_prefix)
        
        # 组装仪表板数据
        dashboard_data = {
            'generated_at': datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
            'subject': subject,
            'stats': stats,
            'recent_notes': recent_notes,
            'projects': projects
        }
        
        # 写入文件或返回数据
        if output_file:
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(dashboard_data, f, ensure_ascii=False, indent=2, default=str)
            
            print(f"已生成仪表板数据: {output_path}")
        
        return dashboard_data

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="生成笔记仪表板数据")
    parser.add_argument("subject", help="主题领域 (如 frontend, backend, ai)")
    parser.add_argument("--output", "-o", help="输出JSON文件路径")
    args = parser.parse_args()
    
    generator = DashboardGenerator()
    generator.generate_dashboard_data(args.subject, args.output) 