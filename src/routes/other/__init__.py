from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/captcha")
async def get_captcha():
    """获取验证码"""
    # TODO: 生成验证码
    return {
        "captcha": "1234",
        "captcha_id": "test_id"
    }

@router.post("/login")
async def login(username: str, password: str, captcha: str):
    """登录"""
    # TODO: 实现登录逻辑
    return {
        "message": "登录成功",
        "token": "test_token"
    }

@router.post("/delete-all")
async def delete_all_data():
    """删除所有数据"""
    # TODO: 删除所有数据
    return {"message": "所有数据已删除"}

@router.post("/clear-database")
async def clear_database():
    """清空数据库"""
    # TODO: 清空数据库
    return {"message": "数据库已清空"}

@router.get("/test")
async def test_api():
    """测试 API"""
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat()
    }
