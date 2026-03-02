from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

router = APIRouter()

# 模拟数据库
outlines_db = []

class OutlineCreate(BaseModel):
    novel_id: int
    title: str
    content: str

class Outline(BaseModel):
    id: int
    novel_id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

@router.get("/list")
async def get_outlines(novel_id: Optional[int] = None):
    """获取大纲列表"""
    if novel_id:
        return [o for o in outlines_db if o.novel_id == novel_id]
    return outlines_db

@router.post("/generate")
async def generate_outline(novel_id: int):
    """AI 生成大纲"""
    # TODO: 调用 AI 生成大纲
    return {
        "message": "大纲生成中",
        "novel_id": novel_id,
        "status": "processing"
    }

@router.post("/create", response_model=Outline)
async def create_outline(outline: OutlineCreate):
    """创建大纲"""
    now = datetime.now()
    new_outline = Outline(
        id=len(outlines_db) + 1,
        novel_id=outline.novel_id,
        title=outline.title,
        content=outline.content,
        created_at=now,
        updated_at=now
    )
    outlines_db.append(new_outline)
    return new_outline

@router.get("/{outline_id}")
async def get_outline(outline_id: int):
    """获取大纲详情"""
    for outline in outlines_db:
        if outline.id == outline_id:
            return outline
    raise HTTPException(status_code=404, detail="大纲不存在")

@router.put("/{outline_id}")
async def update_outline(outline_id: int, content: str):
    """更新大纲"""
    for o in outlines_db:
        if o.id == outline_id:
            o.content = content
            o.updated_at = datetime.now()
            return o
    raise HTTPException(status_code=404, detail="大纲不存在")
