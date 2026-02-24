#!/usr/bin/env python3
"""
获取Telegram群组妹纸图的最新图片并发送给用户
"""
import os
import sys
import asyncio
import json
from telethon import TelegramClient
from telethon.sessions import StringSession

async def fetch_and_send_images():
    # API credentials
    api_id = 29654809
    api_hash = '6d671d65274cb41e852228b5d54bef2b'
    session_string = '1BVtsOIgBuz_0YYYWitZ3Omo_6a9YB_qZ1j1cglPZwKkg-Xx-7s7WikeN5-IOrNxDfQ1ZWZ9Ji2PWOjU9PmGxwxs8G1KL02GHQVKkH0w3fEJMBsvykGn6ozrsB24BxR_nQI1c1kc0oAX6LL8RK2mS_-JZvUaguVMxhcxAoKTBKSvzfyG5vwF5gQGvxmjhGFiSDR2k67CVd8LQKy1lq5RnZG3TWdqDr8l7qVP_B3VUBeZ4wPd5KMQYmLNwvdsLHuX8hWfq1V8zoOOsfzF-P1aOJ4nbX6JF0TFvRrqAWgLOYHZ8S30MgYkIFIBoX8y1OH1vRIMx_RYPmAua9PIxu-IqGKMlXJU9yhE='

    # 创建下载目录
    download_dir = '/tmp/mzitu_images'
    os.makedirs(download_dir, exist_ok=True)

    # 创建客户端
    client = TelegramClient(
        StringSession(session_string),
        api_id,
        api_hash
    )

    downloaded_files = []

    try:
        print("正在连接到Telegram...", file=sys.stderr)
        await client.connect()

        if not await client.is_user_authorized():
            print("错误：Session未授权", file=sys.stderr)
            return {
                'success': False,
                'error': 'Session not authorized'
            }

        print("正在获取群组信息...", file=sys.stderr)
        entity = await client.get_entity('Mzitu')
        print(f"找到群组: {entity.title}", file=sys.stderr)

        # 获取最新10条消息
        print("正在获取最新10条消息...", file=sys.stderr)
        messages = []
        async for message in client.iter_messages(entity, limit=10):
            if message.media:
                messages.append(message)

        print(f"找到 {len(messages)} 条包含媒体的消息", file=sys.stderr)

        # 下载图片
        for idx, message in enumerate(messages, 1):
            try:
                # 检查是否是图片
                if hasattr(message.media, 'photo'):
                    print(f"正在下载第{idx}张图片...", file=sys.stderr)

                    # 下载图片
                    file_path = await client.download_media(
                        message,
                        file=f'{download_dir}/{idx}.jpg'
                    )

                    if file_path:
                        downloaded_files.append({
                            'index': idx,
                            'path': file_path,
                            'date': message.date.isoformat() if message.date else None
                        })
                        print(f"✓ 下载成功: {file_path}", file=sys.stderr)
                    else:
                        print(f"✗ 下载失败", file=sys.stderr)

            except Exception as e:
                print(f"下载第{idx}张图片时出错: {e}", file=sys.stderr)
                continue

        return {
            'success': True,
            'count': len(downloaded_files),
            'files': downloaded_files
        }

    except Exception as e:
        import traceback
        print(f"错误: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return {
            'success': False,
            'error': str(e),
            'type': type(e).__name__
        }
    finally:
        await client.disconnect()

if __name__ == '__main__':
    result = asyncio.get_event_loop().run_until_complete(fetch_and_send_images())
    print(json.dumps(result, ensure_ascii=False, indent=2))
