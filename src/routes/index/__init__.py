from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_index():
    """获取首页信息"""
    return {
        "message": "Welcome to Toonflow API",
        "version": "1.0.0"
    }

@router.get("/info")
async def get_info():
    """获取系统信息"""
    return {
        "name": "Toonflow",
        "description": "AI 短剧工厂",
        "features": [
            "角色生成",
            "剧本生成", 
            "分镜制作",
            "视频合成"
        ]
    }
