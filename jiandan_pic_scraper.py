#!/usr/bin/env python3
"""
煎蛋随手拍图片爬虫
获取点赞数（OO数）最高的5张图片
"""

import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import json

def scrape_jandan_pic():
    """爬取煎蛋随手拍页面"""
    url = "https://jandan.net/pic"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        response.encoding = 'utf-8'
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 调试：保存HTML
        with open('/tmp/jiandan_debug.html', 'w', encoding='utf-8') as f:
            f.write(response.text[:10000])
        
        # 查找所有图片
        all_imgs = soup.find_all('img')
        print(f"找到 {len(all_imgs)} 个图片标签")
        
        # 查找所有li元素
        all_lis = soup.find_all('li')
        print(f"找到 {len(all_lis)} 个li元素")
        
        # 查找所有包含图片的评论/帖子
        posts = []
        
        # 尝试不同的选择器
        for selector in ['.comment', '.post-item', 'li[data-id]', 'article']:
            elements = soup.select(selector)
            print(f"选择器 '{selector}' 找到 {len(elements)} 个元素")
            
            for el in elements:
                img = el.select_one('img')
                if not img or not img.get('src'):
                    continue
                    
                img_src = img['src']
                
                # 跳过loading图片和广告
                if 'loading.gif' in img_src or 'mw600' not in img_src:
                    continue
                
                # 查找OO数（点赞数）
                text = el.get_text()
                # 尝试多种OO数格式
                oo_match = re.search(r'OO\s*[\(（]?\s*(\d+)', text)
                if not oo_match:
                    oo_match = re.search(r'(\d+)\s*OO', text)
                oo_count = int(oo_match.group(1)) if oo_match else 0
                
                # 查找标题或描述
                title_elem = el.select_one('.title, h3, h4, .text, p, .author')
                title = title_elem.get_text().strip() if title_elem else ''
                title = re.sub(r'\s+', ' ', title)[:80]
                
                posts.append({
                    'oo_count': oo_count,
                    'img_src': img_src,
                    'title': title,
                    'selector': selector,
                    'raw_text': text[:150]
                })
        
        print(f"\n总共找到 {len(posts)} 个帖子")
        
        # 按OO数排序，取前5
        posts.sort(key=lambda x: x['oo_count'], reverse=True)
        top5 = posts[:5]
        
        return top5
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return []

if __name__ == "__main__":
    posts = scrape_jandan_pic()
    
    print(f"\n📷 **煎蛋随手拍 Top 5**\n")
    
    if not posts:
        print("未找到任何帖子，请检查页面结构")
    else:
        for i, post in enumerate(posts, 1):
            print(f"{i}. OO [{post['oo_count']}] - {post['title']}")
            print(f"   链接: {post['img_src']}\n")
