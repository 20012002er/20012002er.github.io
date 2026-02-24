#!/usr/bin/env python3
import requests
import urllib3
import os
import sys

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 图片列表（按点赞数排序）
images = [
    ("133赞", "https://wangmoyuimg.cdn.dfyun.com.cn/large/6d435d20e61fa4223a6b96b50f90b4b4.jpg"),
    ("106赞", "https://wangmoyuimg.cdn.dfyun.com.cn/large/fa980e130afc461627e96de9bcf13774.jpg"),
    ("82赞", "https://wangmoyuimg.cdn.dfyun.com.cn/large/86cd96387cd9a515ca52cd341cf626cb.jpg"),
    ("81赞", "https://wangmoyuimg.cdn.dfyun.com.cn/large/affe71d86da23eb16c0f62326d1b30e9.jpg"),
    ("79赞", "https://wangmoyuimg.cdn.dfyun.com.cn/large/f6d7f8c078c9259c9b4a4c443678cd35.jpg"),
    ("76赞", "http://totoimg.cdn.dfyun.com.cn/large/005GRSw2gy1i9zf7q9s88j30em0iw412.jpg"),
    ("64赞", "https://wangmoyuimg.cdn.dfyun.com.cn/large/91132fc3cc3cb0feba56e9a8095185f0.jpg"),
    ("57赞", "https://wangmoyuimg.cdn.dfyun.com.cn/large/89bb3526b5da0efd2db827a9b9c82cb2.png"),
    ("55赞", "https://wangmoyuimg.cdn.dfyun.com.cn/large/fc8fca347b907a8b965d6c8e645a021b.jpg"),
    ("54赞", "https://wangmoyuimg.cdn.dfyun.com.cn/large/7f8f077491961aed69a0b9ecb9d6ce4d.jpg"),
]

output_dir = "/root/.openclaw/workspace/jiandan_images"
os.makedirs(output_dir, exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': 'https://jandan.net/',
}

def download_image(name, url):
    try:
        # 提取文件扩展名
        ext = url.split('.')[-1].split('?')[0]
        filename = f"jiandan_{name.replace('赞', 'likes')}.{ext}"
        filepath = os.path.join(output_dir, filename)
        
        # 尝试下载
        response = requests.get(url, headers=headers, verify=False, timeout=30)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"✓ 下载成功: {filename} ({len(response.content)} bytes)")
            return True
        else:
            print(f"✗ 下载失败: {name} (HTTP {response.status_code})")
            return False
    except Exception as e:
        print(f"✗ 下载失败: {name} ({str(e)})")
        return False

if __name__ == "__main__":
    print("开始下载煎蛋网高点赞图片...")
    success_count = 0
    
    for name, url in images:
        if download_image(name, url):
            success_count += 1
    
    print(f"\n下载完成: {success_count}/{len(images)} 张图片")
    sys.exit(0 if success_count == len(images) else 1)
