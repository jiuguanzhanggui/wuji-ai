from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

router = APIRouter()

# 模拟数据库
storyboards_db = []

class StoryboardCreate(BaseModel):
    script_id: int
    scene_number: int
    description: str
    image_prompt: str

class Storyboard(BaseModel):
    id: int
    script_id: int
    scene_number: int
    description: str
    image_prompt: str
    images: Optional[List[str]] = []
    created_at: datetime
    updated_at: datetime

@router.get("/list")
async def get_storyboards(script_id: Optional[int] = None):
    """获取分镜列表"""
    if script_id:
        return [s for s in storyboards_db if s.script_id == script_id]
    return storyboards_db

@router.post("/generate")
async def generate_storyboard(script_id: int):
    """AI 生成分镜"""
    # TODO: 调用 AI 生成分镜
    return {
        "message": "分镜生成中",
        "script_id": script_id,
        "status": "processing"
    }

@router.post("/generate-image")
async def generate_storyboard_image(storyboard_id: int):
    """AI 生成分镜图片"""
    # TODO: 调用 AI 生成图片
    return {
        "message": "图片生成中",
        "storyboard_id": storyboard_id,
        "status": "processing"
    }

@router.post("/create", response_model=Storyboard)
async def create_storyboard(storyboard: StoryboardCreate):
    """创建分镜"""
    now = datetime.now()
    new_storyboard = Storyboard(
        id=len(storyboards_db) + 1,
        script_id=storyboard.script_id,
        scene_number=storyboard.scene_number,
        description=storyboard.description,
        image_prompt=storyboard.image_prompt,
        created_at=now,
        updated_at=now
    )
    storyboards_db.append(new_storyboard)
    return new_storyboard

@router.get("/{storyboard_id}")
async def get_storyboard(storyboard_id: int):
    """获取分镜详情"""
    for storyboard in storyboards_db:
        if storyboard.id == storyboard_id:
            return storyboard
    raise HTTPException(status_code=404, detail="分镜不存在")

@router.put("/{storyboard_id}")
async def update_storyboard(storyboard_id: int, description: str, image_prompt: str):
    """更新分镜"""
    for s in storyboards_db:
        if s.id == storyboard_id:
            s.description = description
            s.image_prompt = image_prompt
            s.updated_at = datetime.now()
            return s
    raise HTTPException(status_code=404, detail="分镜不存在")
