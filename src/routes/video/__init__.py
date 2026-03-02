from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

router = APIRouter()

# 模拟数据库
videos_db = []

class VideoCreate(BaseModel):
    storyboard_id: int
    name: str

class Video(BaseModel):
    id: int
    storyboard_id: int
    name: str
    url: Optional[str] = None
    status: str = "pending"  # pending, processing, completed, failed
    created_at: datetime
    updated_at: datetime

@router.get("/list")
async def get_videos(storyboard_id: Optional[int] = None):
    """获取视频列表"""
    if storyboard_id:
        return [v for v in videos_db if v.storyboard_id == storyboard_id]
    return videos_db

@router.post("/generate")
async def generate_video(storyboard_id: int):
    """AI 生成视频"""
    # TODO: 调用 AI 生成视频 (Veo, Seedance 等)
    return {
        "message": "视频生成中",
        "storyboard_id": storyboard_id,
        "status": "processing"
    }

@router.post("/create", response_model=Video)
async def create_video(video: VideoCreate):
    """创建视频"""
    now = datetime.now()
    new_video = Video(
        id=len(videos_db) + 1,
        storyboard_id=video.storyboard_id,
        name=video.name,
        created_at=now,
        updated_at=now
    )
    videos_db.append(new_video)
    return new_video

@router.get("/{video_id}")
async def get_video(video_id: int):
    """获取视频详情"""
    for video in videos_db:
        if video.id == video_id:
            return video
    raise HTTPException(status_code=404, detail="视频不存在")

@router.delete("/{video_id}")
async def delete_video(video_id: int):
    """删除视频"""
    global videos_db
    videos_db = [v for v in videos_db if v.id != video_id]
    return {"message": "删除成功"}

@router.post("/{video_id}/test")
async def test_video(video_id: int):
    """测试视频"""
    return {"message": "视频测试成功", "video_id": video_id}
