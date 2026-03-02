from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

router = APIRouter()

# 模拟数据库
prompts_db = []

class PromptCreate(BaseModel):
    type: str  # image, video, script
    content: str
    name: Optional[str] = None

class Prompt(BaseModel):
    id: int
    type: str
    name: str
    content: str
    created_at: datetime

@router.get("/list", response_model=List[Prompt])
async def get_prompts(prompt_type: Optional[str] = None):
    """获取提示词列表"""
    if prompt_type:
        return [p for p in prompts_db if p.type == prompt_type]
    return prompts_db

@router.post("/create", response_model=Prompt)
async def create_prompt(prompt: PromptCreate):
    """创建提示词"""
    new_prompt = Prompt(
        id=len(prompts_db) + 1,
        type=prompt.type,
        name=prompt.name or f"Prompt_{len(prompts_db) + 1}",
        content=prompt.content,
        created_at=datetime.now()
    )
    prompts_db.append(new_prompt)
    return new_prompt

@router.put("/{prompt_id}")
async def update_prompt(prompt_id: int, content: str):
    """更新提示词"""
    for p in prompts_db:
        if p.id == prompt_id:
            p.content = content
            return p
    raise HTTPException(status_code=404, detail="提示词不存在")

@router.delete("/{prompt_id}")
async def delete_prompt(prompt_id: int):
    """删除提示词"""
    global prompts_db
    prompts_db = [p for p in prompts_db if p.id != prompt_id]
    return {"message": "删除成功"}

@router.post("/polish")
async def polish_prompt(content: str):
    """AI 优化提示词"""
    # TODO: 调用 AI 优化提示词
    return {
        "message": "提示词优化中",
        "original": content,
        "status": "processing"
    }
