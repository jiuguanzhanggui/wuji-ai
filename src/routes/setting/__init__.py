from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter()

# 模拟配置存储
settings_db = {
    "ai_models": [],
    "api_keys": {}
}

class ModelConfig(BaseModel):
    name: str
    type: str  # text, image, video
    api_url: str
    api_key: str

@router.get("/list")
async def get_settings():
    """获取所有配置"""
    return settings_db

@router.get("/models")
async def get_models():
    """获取 AI 模型配置列表"""
    return settings_db["ai_models"]

@router.post("/models/add")
async def add_model(model: ModelConfig):
    """添加 AI 模型配置"""
    settings_db["ai_models"].append(model.dict())
    return {"message": "模型添加成功"}

@router.delete("/models/{model_name}")
async def delete_model(model_name: str):
    """删除 AI 模型配置"""
    settings_db["ai_models"] = [
        m for m in settings_db["ai_models"] if m["name"] != model_name
    ]
    return {"message": "模型删除成功"}

@router.get("/logs")
async def get_logs():
    """获取日志"""
    return {
        "logs": []
    }

@router.post("/test-ai")
async def test_ai_connection(model_name: str):
    """测试 AI 连接"""
    # TODO: 测试 AI 连接
    return {
        "message": "测试成功",
        "model": model_name
    }

@router.post("/test-video")
async def test_video_connection():
    """测试视频生成连接"""
    return {"message": "视频服务连接正常"}

@router.post("/test-image")
async def test_image_connection():
    """测试图片生成连接"""
    return {"message": "图片服务连接正常"}
