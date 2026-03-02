from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

router = APIRouter()

# 模拟数据库
tasks_db = []

class TaskCreate(BaseModel):
    type: str  # generate_script, generate_storyboard, generate_video, etc.
    target_id: int
    params: Optional[dict] = {}

class Task(BaseModel):
    id: int
    type: str
    target_id: int
    status: str = "pending"  # pending, processing, completed, failed
    result: Optional[dict] = None
    created_at: datetime
    updated_at: datetime

@router.get("/list", response_model=List[Task])
async def get_tasks(status: Optional[str] = None):
    """获取任务列表"""
    if status:
        return [t for t in tasks_db if t.status == status]
    return tasks_db

@router.get("/{task_id}")
async def get_task(task_id: int):
    """获取任务详情"""
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="任务不存在")

@router.post("/create", response_model=Task)
async def create_task(task: TaskCreate):
    """创建任务"""
    now = datetime.now()
    new_task = Task(
        id=len(tasks_db) + 1,
        type=task.type,
        target_id=task.target_id,
        created_at=now,
        updated_at=now
    )
    tasks_db.append(new_task)
    
    # TODO: 异步执行任务
    # asyncio.create_task(execute_task(new_task.id))
    
    return new_task

@router.delete("/{task_id}")
async def delete_task(task_id: int):
    """删除任务"""
    global tasks_db
    tasks_db = [t for t in tasks_db if t.id != task_id]
    return {"message": "删除成功"}

@router.post("/{task_id}/cancel")
async def cancel_task(task_id: int):
    """取消任务"""
    for task in tasks_db:
        if task.id == task_id:
            task.status = "cancelled"
            task.updated_at = datetime.now()
            return task
    raise HTTPException(status_code=404, detail="任务不存在")
