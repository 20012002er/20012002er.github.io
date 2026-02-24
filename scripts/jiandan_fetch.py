#!/usr/bin/env python3
"""
煎蛋随手拍热图抓取脚本（使用pyppeteer）
"""
import asyncio
import sys
import os
import json

async def fetch_jiandan_images():
    import pyppeteer

    chromium_path = os.path.expanduser('~/.local/share/pyppeteer/local-chromium/588429/chrome-linux/chrome')

    print("正在启动浏览器...", file=sys.stderr)
    browser = await pyppeteer.launch(
        headless=True,
        executablePath=chromium_path,
        args=[
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage',
            '--disable-gpu',
        ]
    )

    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})

    # 访问随手拍页面
    print("正在访问煎蛋随手拍页面...", file=sys.stderr)
    await page.goto('https://jandan.net/ooxx', {
        'waitUntil': 'networkidle0',
        'timeout': 45000
    })

    print("等待页面加载...", file=sys.stderr)
    await asyncio.sleep(5)

    # 滚动页面触发懒加载
    print("滚动页面加载更多内容...", file=sys.stderr)
    for i in range(3):
        await page.evaluate('window.scrollBy(0, window.innerHeight * 0.8)')
        await asyncio.sleep(2)

    # 回到顶部
    await page.evaluate('window.scrollTo(0, 0)')
    await asyncio.sleep(2)

    # 提取图片
    print("正在提取图片信息...", file=sys.stderr)
    images = await page.evaluate('''
        () => {
            const imgs = [];
            const imgElements = document.querySelectorAll('img');

            imgElements.forEach((img) => {
                const src = img.getAttribute('src');
                if (!src) return;

                if (!src.match(/\.(jpg|jpeg|png|gif|webp)$/i)) return;

                const fullSrc = src.startsWith('http') ? src : ('https:' + src);

                if (!fullSrc.includes('jandan') && !fullSrc.includes('toto.im') && !fullSrc.includes('wangmoyu.com')) return;

                imgs.push({
                    url: fullSrc,
                    title: '随手拍图片',
                    author: '煎蛋用户',
                    oo: 'N/A'
                });
            });

            return imgs.slice(0, 10);
        }
    ''')

    await browser.close()

    return {
        'success': True,
        'count': len(images),
        'images': images
    }

if __name__ == '__main__':
    try:
        result = asyncio.get_event_loop().run_until_complete(fetch_jiandan_images())
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as e:
        print(json.dumps({
            'success': False,
            'error': str(e),
            'type': type(e).__name__
        }, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)
