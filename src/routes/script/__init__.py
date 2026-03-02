from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

router = APIRouter()

# 模拟数据库
scripts_db = []

class ScriptCreate(BaseModel):
    outline_id: int
    title: str
    content: str

class Script(BaseModel):
    id: int
    outline_id: int
    title: str
    content: str
    scenes: Optional[List[dict]] = []
    created_at: datetime
    updated_at: datetime

@router.get("/list")
async def get_scripts(outline_id: Optional[int] = None):
    """获取剧本列表"""
    if outline_id:
        return [s for s in scripts_db if s.outline_id == outline_id]
    return scripts_db

@router.post("/generate")
async def generate_script(outline_id: int):
    """AI 生成剧本"""
    # TODO: 调用 AI 生成剧本
    return {
        "message": "剧本生成中",
        "outline_id": outline_id,
        "status": "processing"
    }

@router.post("/create", response_model=Script)
async def create_script(script: ScriptCreate):
    """创建剧本"""
    now = datetime.now()
    new_script = Script(
        id=len(scripts_db) + 1,
        outline_id=script.outline_id,
        title=script.title,
        content=script.content,
        created_at=now,
        updated_at=now
    )
    scripts_db.append(new_script)
    return new_script

@router.get("/{script_id}")
async def get_script(script_id: int):
    """获取剧本详情"""
    for script in scripts_db:
        if script.id == script_id:
            return script
    raise HTTPException(status_code=404, detail="剧本不存在")

@router.put("/{script_id}")
async def update_script(script_id: int, content: str):
    """更新剧本"""
    for s in scripts_db:
        if s.id == script_id:
            s.content = content
            s.updated_at = datetime.now()
            return s
    raise HTTPException(status_code=404, detail="剧本不存在")

@router.post("/{script_id}/save")
async def save_script(script_id: int):
    """保存剧本"""
    return {"message": "剧本已保存", "script_id": script_id}
