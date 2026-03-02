#!/bin/bash

# Toonflow Python 启动脚本

echo "🎬 Toonflow - AI 短剧工厂"
echo "========================="

# 检查 Python 版本
python_version=$(python3 --version 2>&1)
echo "Python: $python_version"

# 检查虚拟环境
if [ ! -d "venv" ]; then
    echo "创建虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
echo "安装依赖..."
pip install -r requirements.txt -q

# 检查 .env 文件
if [ ! -f ".env" ]; then
    echo "创建 .env 文件..."
    cp .env.example .env
    echo "请编辑 .env 文件配置 API Key"
fi

# 启动服务
echo "启动服务..."
echo "API 文档：http://localhost:8000/api/docs"
echo "========================="

python main.py
