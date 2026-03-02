from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

router = APIRouter()

# 模拟数据库
novels_db = []

class NovelCreate(BaseModel):
    title: str
    author: Optional[str] = None
    content: str

class Novel(BaseModel):
    id: int
    title: str
    author: Optional[str]
    content: str
    created_at: datetime
    updated_at: datetime

@router.get("/list")
async def get_novels():
    """获取小说列表"""
    return novels_db

@router.post("/upload")
async def upload_novel(file: UploadFile = File(...), title: str = None):
    """上传小说文件"""
    content = await file.read()
    
    novel = {
        "id": len(novels_db) + 1,
        "title": title or file.filename,
        "content": content.decode('utf-8'),
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
    novels_db.append(novel)
    
    return {"message": "上传成功", "novel_id": novel["id"]}

@router.post("/create", response_model=Novel)
async def create_novel(novel: NovelCreate):
    """创建小说"""
    now = datetime.now()
    new_novel = Novel(
        id=len(novels_db) + 1,
        title=novel.title,
        author=novel.author,
        content=novel.content,
        created_at=now,
        updated_at=now
    )
    novels_db.append(new_novel)
    return new_novel

@router.get("/{novel_id}")
async def get_novel(novel_id: int):
    """获取小说详情"""
    for novel in novels_db:
        if novel.id == novel_id:
            return novel
    raise HTTPException(status_code=404, detail="小说不存在")

@router.delete("/{novel_id}")
async def delete_novel(novel_id: int):
    """删除小说"""
    global novels_db
    novels_db = [n for n in novels_db if n.id != novel_id]
    return {"message": "删除成功"}
