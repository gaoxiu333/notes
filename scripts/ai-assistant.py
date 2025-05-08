#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AI助手脚本 - 与大语言模型协同工作
功能：
1. 自动生成MOC内容摘要
2. 分析笔记间的关联性并提出链接建议
3. 从长文档中提取关键概念
"""

import os
import re
import sys
import json
import argparse
import requests
from pathlib import Path
from typing import List, Dict, Any, Optional

# 配置项
CONFIG = {
    "api_key": os.environ.get("OPENAI_API_KEY", ""),
    "api_base": "https://api.openai.com/v1",
    "model": "gpt-4-turbo",  # 或其他模型
    "prompt_dir": Path(__file__).parent.parent / "KnowledgeBase/Tools/prompts",
    "vault_dir": Path(__file__).parent.parent,  # 笔记库根目录
}

def load_prompt(prompt_name: str) -> str:
    """加载提示词模板"""
    prompt_path = CONFIG["prompt_dir"] / f"{prompt_name}.prompt"
    if not prompt_path.exists():
        raise FileNotFoundError(f"提示词模板文件不存在: {prompt_path}")
    
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()

def call_llm_api(prompt: str, temperature: float = 0.2) -> str:
    """调用大语言模型API"""
    if not CONFIG["api_key"]:
        raise ValueError("未设置API密钥。请设置环境变量OPENAI_API_KEY")
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CONFIG['api_key']}"
    }
    
    payload = {
        "model": CONFIG["model"],
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature
    }
    
    response = requests.post(
        f"{CONFIG['api_base']}/chat/completions", 
        headers=headers, 
        json=payload
    )
    
    if response.status_code != 200:
        print(f"API请求失败: {response.status_code}")
        print(response.text)
        return ""
    
    return response.json()["choices"][0]["message"]["content"]

def extract_yaml_frontmatter(content: str) -> Dict[str, Any]:
    """从笔记内容中提取YAML前置元数据"""
    yaml_pattern = r"^---\n(.*?)\n---"
    match = re.search(yaml_pattern, content, re.DOTALL)
    if not match:
        return {}
    
    # 简单解析YAML（实际使用中可能需要更复杂的解析）
    yaml_text = match.group(1)
    metadata = {}
    
    for line in yaml_text.split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip()
    
    return metadata

def find_markdown_files(directory: Path) -> List[Path]:
    """递归查找目录中的所有Markdown文件"""
    return list(directory.glob("**/*.md"))

def generate_moc_summary(moc_path: str) -> str:
    """生成MOC内容摘要"""
    moc_file = Path(moc_path)
    if not moc_file.exists():
        return f"错误: MOC文件不存在: {moc_path}"
    
    with open(moc_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    prompt_template = load_prompt("summary-generator")
    prompt = prompt_template.format(content=content)
    
    summary = call_llm_api(prompt)
    return summary

def suggest_connections(note_path: str) -> List[Dict[str, str]]:
    """分析笔记并提出关联建议"""
    note_file = Path(note_path)
    if not note_file.exists():
        return [{"error": f"笔记文件不存在: {note_path}"}]
    
    # 读取目标笔记
    with open(note_file, "r", encoding="utf-8") as f:
        target_content = f.read()
    
    # 获取所有其他笔记
    all_notes = find_markdown_files(CONFIG["vault_dir"])
    other_notes = []
    
    # 收集最多10个其他笔记内容（可根据需要调整）
    count = 0
    for note in all_notes:
        if note.resolve() == note_file.resolve():
            continue
        
        if count >= 10:
            break
            
        try:
            with open(note, "r", encoding="utf-8") as f:
                note_content = f.read()
                metadata = extract_yaml_frontmatter(note_content)
                
                other_notes.append({
                    "path": str(note.relative_to(CONFIG["vault_dir"])),
                    "title": metadata.get("title", note.stem),
                    "tags": metadata.get("tags", ""),
                    "content": note_content[:1000]  # 仅使用前1000个字符
                })
                count += 1
        except Exception as e:
            print(f"读取笔记发生错误: {note} - {e}")
    
    # 调用LLM查找关联
    prompt_template = load_prompt("connection-finder")
    prompt = prompt_template.format(
        target_note=target_content,
        other_notes=json.dumps(other_notes, ensure_ascii=False, indent=2)
    )
    
    result = call_llm_api(prompt)
    
    # 尝试将结果解析为JSON
    try:
        connections = json.loads(result)
        return connections
    except:
        return [{"error": "无法解析API结果", "raw_result": result}]

def extract_concepts(document_path: str) -> List[Dict[str, str]]:
    """从长文档中提取关键概念"""
    doc_file = Path(document_path)
    if not doc_file.exists():
        return [{"error": f"文档不存在: {document_path}"}]
    
    with open(doc_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    prompt_template = load_prompt("concept-extractor")
    prompt = prompt_template.format(content=content)
    
    result = call_llm_api(prompt)
    
    # 尝试将结果解析为JSON
    try:
        concepts = json.loads(result)
        return concepts
    except:
        return [{"error": "无法解析API结果", "raw_result": result}]

def main():
    parser = argparse.ArgumentParser(description="AI笔记助手")
    subparsers = parser.add_subparsers(dest="command", help="子命令")
    
    # MOC摘要生成子命令
    moc_parser = subparsers.add_parser("summarize-moc", help="生成MOC内容摘要")
    moc_parser.add_argument("path", help="MOC文件路径")
    
    # 笔记关联分析子命令
    connect_parser = subparsers.add_parser("find-connections", help="分析笔记关联性")
    connect_parser.add_argument("path", help="笔记文件路径")
    
    # 提取关键概念子命令
    concept_parser = subparsers.add_parser("extract-concepts", help="提取关键概念")
    concept_parser.add_argument("path", help="文档文件路径")
    
    args = parser.parse_args()
    
    if args.command == "summarize-moc":
        summary = generate_moc_summary(args.path)
        print(summary)
    
    elif args.command == "find-connections":
        connections = suggest_connections(args.path)
        print(json.dumps(connections, ensure_ascii=False, indent=2))
    
    elif args.command == "extract-concepts":
        concepts = extract_concepts(args.path)
        print(json.dumps(concepts, ensure_ascii=False, indent=2))
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main() 