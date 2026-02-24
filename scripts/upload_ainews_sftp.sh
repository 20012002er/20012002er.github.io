#!/bin/bash

# SFTP上传脚本 - AI新闻日报
# 使用sshpass+sftp进行密码认证上传

set -e

# 配置文件路径
CONFIG_FILE="/root/.openclaw/workspace/config/sftp_config.json"

# 获取当天日期
TODAY=$(date +%Y%m%d)
FILE_PATH="/app/data/daily/${TODAY}/${TODAY}-ainews.md"
FILENAME="${TODAY}-ainews.md"

# 检查文件是否存在
if [ ! -f "$FILE_PATH" ]; then
    echo "Error: 文件不存在 $FILE_PATH"
    exit 1
fi

# 从配置文件读取SFTP信息
HOST=$(jq -r '.host' "$CONFIG_FILE")
PORT=$(jq -r '.port' "$CONFIG_FILE")
USER=$(jq -r '.username' "$CONFIG_FILE")
PASS=$(jq -r '.password' "$CONFIG_FILE")
REMOTE_PATH=$(jq -r '.remote_path' "$CONFIG_FILE")

echo "开始SFTP上传..."
echo "文件: $FILE_PATH"
echo "远程路径: $REMOTE_PATH"
echo "主机: $HOST:$PORT"

# 使用sshpass+sftp批量命令上传（自动关闭连接）
echo "put $FILE_PATH" | sshpass -p "$PASS" sftp -o StrictHostKeyChecking=no -o Port=$PORT "$USER@$HOST:$REMOTE_PATH" 2>&1

if [ $? -eq 0 ]; then
    echo "✅ SFTP上传成功: $FILENAME"
    echo "   → $HOST:$REMOTE_PATH"
    exit 0
else
    echo "❌ SFTP上传失败"
    exit 1
fi
