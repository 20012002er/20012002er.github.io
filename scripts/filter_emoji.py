#!/usr/bin/env python3
"""
过滤MD文件中的emoji表情，确保MySQL兼容性
移除所有emoji和特殊Unicode字符，保留常规文本
"""

import re
import sys
import os

def filter_emoji_from_file(file_path):
    """
    过滤文件中的emoji表情
    
    Args:
        file_path: MD文件路径
    
    Returns:
        bool: 成功返回True，失败返回False
    """
    if not os.path.exists(file_path):
        print(f"❌ 文件不存在: {file_path}", file=sys.stderr)
        return False
    
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_size = len(content)
        
        # 定义emoji的正则表达式模式
        # 覆盖所有主要emoji Unicode范围
        emoji_pattern = re.compile(
            '['
            '\U0001F600-\U0001F64F'  # emoticons (表情)
            '\U0001F300-\U0001F5FF'  # symbols & pictographs (符号和象形文字)
            '\U0001F680-\U0001F6FF'  # transport & map symbols (交通和地图符号)
            '\U0001F1E0-\U0001F1FF'  # flags (国旗)
            '\U00002702-\U000027B0'  # dingbats (装饰符号)
            '\U000024C2-\U0001F251'  # 其他符号
            '\U0001F900-\U0001F9FF'  # supplemental symbols (补充符号)
            '\U0001FA70-\U0001FAFF'  # symbols and pictographs extended-A (扩展符号A)
            '\U00002600-\U000026FF'  # misc symbols (杂项符号)
            '\U0000FE0F'             # variation selector (变体选择器)
            '\U0001F300-\U0001F9FF'  # 全面覆盖emoji范围
            ']+',
            flags=re.UNICODE
        )
        
        # 过滤emoji
        filtered_content = emoji_pattern.sub('', content)
        
        # 清理多余的空行（emoji移除后可能留下）
        filtered_content = re.sub(r'\n\s*\n\s*\n', '\n\n', filtered_content)
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(filtered_content)
        
        filtered_size = len(filtered_content)
        removed = original_size - filtered_size
        
        print(f"✅ Emoji过滤完成: {file_path}")
        print(f"   移除字符数: {removed}")
        print(f"   原始大小: {original_size} → 过滤后: {filtered_size}")
        
        return True
        
    except Exception as e:
        print(f"❌ 过滤失败: {e}", file=sys.stderr)
        return False

def main():
    if len(sys.argv) != 2:
        print("用法: python3 filter_emoji.py <文件路径>")
        print("示例: python3 filter_emoji.py /app/data/daily/20260224/20260224-ainews.md")
        sys.exit(1)
    
    file_path = sys.argv[1]
    success = filter_emoji_from_file(file_path)
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
