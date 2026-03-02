from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

router = APIRouter()

# 模拟数据库
projects_db = []

class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None
    novel_id: Optional[str] = None

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class Project(BaseModel):
    id: int
    name: str
    description: Optional[str]
    status: str = "draft"
    created_at: datetime
    updated_at: datetime

@router.get("/list", response_model=List[Project])
async def get_projects():
    """获取项目列表"""
    return projects_db

@router.get("/count")
async def get_project_count():
    """获取项目数量"""
    return {"count": len(projects_db)}

@router.post("/add", response_model=Project)
async def add_project(project: ProjectCreate):
    """添加项目"""
    now = datetime.now()
    new_project = Project(
        id=len(projects_db) + 1,
        name=project.name,
        description=project.description,
        created_at=now,
        updated_at=now
    )
    projects_db.append(new_project)
    return new_project

@router.get("/{project_id}")
async def get_project(project_id: int):
    """获取单个项目"""
    for project in projects_db:
        if project.id == project_id:
            return project
    raise HTTPException(status_code=404, detail="项目不存在")

@router.put("/{project_id}")
async def update_project(project_id: int, project: ProjectUpdate):
    """更新项目"""
    for p in projects_db:
        if p.id == project_id:
            if project.name:
                p.name = project.name
            if project.description:
                p.description = project.description
            if project.status:
                p.status = project.status
            p.updated_at = datetime.now()
            return p
    raise HTTPException(status_code=404, detail="项目不存在")

@router.delete("/{project_id}")
async def delete_project(project_id: int):
    """删除项目"""
    global projects_db
    projects_db = [p for p in projects_db if p.id != project_id]
    return {"message": "删除成功"}
