from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
import os

router = APIRouter()

# 模拟数据库
assets_db = []
ASSETS_DIR = "assets"

class AssetCreate(BaseModel):
    type: str  # image, video, audio
    name: str
    url: str

class Asset(BaseModel):
    id: int
    type: str
    name: str
    url: str
    created_at: datetime

@router.get("/list")
async def get_assets(asset_type: Optional[str] = None):
    """获取素材列表"""
    if asset_type:
        return [a for a in assets_db if a.type == asset_type]
    return assets_db

@router.get("/image/list")
async def get_images():
    """获取图片列表"""
    return [a for a in assets_db if a.type == "image"]

@router.get("/storyboard/list")
async def get_storyboard_assets():
    """获取分镜素材列表"""
    return [a for a in assets_db if a.type == "storyboard"]

@router.post("/upload")
async def upload_asset(file: UploadFile = File(...), name: str = None, asset_type: str = "image"):
    """上传素材"""
    os.makedirs(ASSETS_DIR, exist_ok=True)
    
    file_path = os.path.join(ASSETS_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    asset = {
        "id": len(assets_db) + 1,
        "type": asset_type,
        "name": name or file.filename,
        "url": f"/{file_path}",
        "created_at": datetime.now()
    }
    assets_db.append(asset)
    
    return {"message": "上传成功", "asset": asset}

@router.post("/generate")
async def generate_asset(prompt: str, asset_type: str = "image"):
    """AI 生成素材"""
    # TODO: 调用 AI 生成素材
    return {
        "message": "素材生成中",
        "prompt": prompt,
        "type": asset_type,
        "status": "processing"
    }

@router.post("/save")
async def save_asset(asset_id: int):
    """保存素材"""
    return {"message": "素材已保存", "asset_id": asset_id}

@router.delete("/{asset_id}")
async def delete_asset(asset_id: int):
    """删除素材"""
    global assets_db
    assets_db = [a for a in assets_db if a.id != asset_id]
    return {"message": "删除成功"}

@router.put("/{asset_id}")
async def update_asset(asset_id: int, name: str = None):
    """更新素材"""
    for a in assets_db:
        if a.id == asset_id:
            if name:
                a.name = name
            return a
    raise HTTPException(status_code=404, detail="素材不存在")
