#!/usr/bin/env python3
# 自动生成定期回顾文档

import os
import sys
import datetime
import argparse
from pathlib import Path

# 回顾类型配置
REVIEW_TYPES = {
    "daily": {
        "template": "KnowledgeBase/Templates/daily-review-template.md",
        "output_dir": "Daily/Journal",
        "filename_format": "%Y-%m-%d-daily-review.md"
    },
    "weekly": {
        "template": "KnowledgeBase/Templates/weekly-review-template.md",
        "output_dir": "KnowledgeBase/Practice",
        "filename_format": "%Y-W%W-weekly-review.md"
    },
    "monthly": {
        "template": "KnowledgeBase/Templates/monthly-review-template.md",
        "output_dir": "KnowledgeBase/Practice",
        "filename_format": "%Y-%m-monthly-review.md"
    },
    "quarterly": {
        "template": "KnowledgeBase/Templates/quarterly-review-template.md",
        "output_dir": "KnowledgeBase/Practice",
        "filename_format": "%Y-Q%q-quarterly-review.md"
    }
}

def parse_args():
    parser = argparse.ArgumentParser(description="生成定期回顾文档")
    parser.add_argument("review_type", choices=REVIEW_TYPES.keys(), help="回顾类型")
    parser.add_argument("--date", help="指定日期 (YYYY-MM-DD), 默认为今天", default=None)
    return parser.parse_args()

def get_quarter(date):
    """获取日期所在季度"""
    return (date.month - 1) // 3 + 1

def format_filename(template, date):
    """格式化文件名, 支持季度格式"""
    result = date.strftime(template)
    if "%q" in result:
        result = result.replace("%q", str(get_quarter(date)))
    return result

def generate_review(review_type, target_date=None):
    """生成特定类型的回顾文档"""
    if target_date:
        try:
            date = datetime.datetime.strptime(target_date, "%Y-%m-%d")
        except ValueError:
            print("错误: 日期格式应为 YYYY-MM-DD")
            sys.exit(1)
    else:
        date = datetime.datetime.now()
    
    config = REVIEW_TYPES[review_type]
    
    # 确保输出目录存在
    output_dir = Path(config["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 生成输出文件名
    output_file = output_dir / format_filename(config["filename_format"], date)
    
    # 如果文件已存在，确认是否覆盖
    if output_file.exists():
        print(f"警告: 文件 {output_file} 已存在")
        response = input("是否覆盖? (y/n): ").lower()
        if response != 'y':
            print("操作取消")
            sys.exit(0)
    
    # 读取模板
    template_path = Path(config["template"])
    if not template_path.exists():
        print(f"错误: 模板文件 {template_path} 不存在")
        sys.exit(1)
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # 替换模板变量
    replacements = {
        "{{date:YYYY-MM-DD}}": date.strftime("%Y-%m-%d"),
        "{{date:YYYY}}": date.strftime("%Y"),
        "{{date:MM}}": date.strftime("%m"),
        "{{date:DD}}": date.strftime("%d"),
        "{{date:ww}}": date.strftime("%U"),
        "{{quarter}}": str(get_quarter(date)),
        "{{month_name}}": date.strftime("%B")
    }
    
    content = template_content
    for key, value in replacements.items():
        content = content.replace(key, value)
    
    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"已生成{review_type}回顾文档: {output_file}")
    
    # 对于每周回顾，同时生成任务链接
    if review_type == "weekly":
        # 获取本周新增笔记
        print("\n本周新增笔记:")
        os.system(f"find . -name '*.md' -newermt '{(date - datetime.timedelta(days=7)).strftime('%Y-%m-%d')}' -not -path './Daily/*'")
    
    return str(output_file)

if __name__ == "__main__":
    args = parse_args()
    generate_review(args.review_type, args.date) 