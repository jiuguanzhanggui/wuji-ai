from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

# 模拟数据库
users_db = {
    "admin": {
        "username": "admin",
        "password": "admin123",  # 生产环境应该加密
        "role": "admin"
    }
}

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    username: str
    role: str
    token: Optional[str] = None

@router.post("/login", response_model=UserResponse)
async def login(user: UserLogin):
    """用户登录"""
    if user.username not in users_db:
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    
    db_user = users_db[user.username]
    if db_user["password"] != user.password:
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    
    # 生成简单 token (生产环境应该使用 JWT)
    token = f"token_{user.username}"
    
    return UserResponse(
        username=db_user["username"],
        role=db_user["role"],
        token=token
    )

@router.get("/info")
async def get_user_info():
    """获取当前用户信息"""
    return {
        "username": "admin",
        "role": "admin"
    }

@router.post("/logout")
async def logout():
    """用户登出"""
    return {"message": "登出成功"}

@router.get("/list")
async def get_user_list():
    """获取用户列表"""
    return {
        "users": [
            {"username": "admin", "role": "admin"}
        ]
    }
