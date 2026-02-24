#!/usr/bin/env python3
"""
获取Telegram群组妹纸图的最新图片（仅下载部分）
WhatsApp发送部分由主任务处理
"""
import os
import sys
import asyncio
import json
from telethon import TelegramClient
from telethon.sessions import StringSession

# 配置
API_ID = 29654809
API_HASH = '6d671d65274cb41e852228b5d54bef2b'
SESSION_STRING = '1BVtsOIgBuz_0YYYWitZ3Omo_6a9YB_qZ1j1cglPZwKkg-Xx-7s7WikeN5-IOrNxDfQ1ZWZ9Ji2PWOjU9PmGxwxs8G1KL02GHQVKkH0w3fEJMBsvykGn6ozrsB24BxR_nQI1c1kc0oAX6LL8RK2mS_-JZvUaguVMxhcxAoKTBKSvzfyG5vwF5gQGvxmjhGFiSDR2k67CVd8LQKy1lq5RnZG3TWdqDr8l7qVP_B3VUBeZ4wPd5KMQYmLNwvdsLHuX8hWfq1V8zoOOsfzF-P1aOJ4nbX6JF0TFvRrqAWgLOYHZ8S30MgYkIFIBoX8y1OH1vRIMx_RYPmAua9PIxu-IqGKMlXJU9yhE='

async def download_images():
    # 创建下载目录
    download_dir = '/tmp/mzitu_images'
    os.makedirs(download_dir, exist_ok=True)

    # 创建Telegram客户端
    client = TelegramClient(
        StringSession(SESSION_STRING),
        API_ID,
        API_HASH
    )

    downloaded_files = []

    try:
        print("正在连接到Telegram...", flush=True, file=sys.stderr)
        await client.connect()

        if not await client.is_user_authorized():
            return {'success': False, 'error': 'Session not authorized'}

        print("正在获取群组信息...", flush=True, file=sys.stderr)
        entity = await client.get_entity('Mzitu')

        # 获取最新10条消息
        print("正在获取最新消息...", flush=True, file=sys.stderr)
        messages = []
        async for message in client.iter_messages(entity, limit=10):
            if message.media and hasattr(message.media, 'photo'):
                messages.append(message)

        print(f"找到 {len(messages)} 条图片消息", flush=True, file=sys.stderr)

        if len(messages) == 0:
            return {
                'success': True,
                'count': 0,
                'files': [],
                'message': '没有新的图片消息'
            }

        # 下载图片
        for idx, message in enumerate(messages, 1):
            try:
                print(f"下载第{idx}/{len(messages)}张图片...", flush=True, file=sys.stderr)

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
                    print(f"✓ {file_path}", flush=True, file=sys.stderr)

            except Exception as e:
                print(f"✗ 下载失败: {e}", flush=True, file=sys.stderr)
                continue

        return {
            'success': True,
            'count': len(downloaded_files),
            'files': downloaded_files,
            'download_dir': download_dir,
            'message': f'成功下载{len(downloaded_files)}张图片'
        }

    except Exception as e:
        import traceback
        print(f"错误: {e}", flush=True, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return {
            'success': False,
            'error': str(e)
        }
    finally:
        await client.disconnect()

if __name__ == '__main__':
    result = asyncio.get_event_loop().run_until_complete(download_images())
    print(json.dumps(result, ensure_ascii=False, indent=2))
