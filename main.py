"""
Toonflow - AI 短剧工厂 FastAPI 后端
AI 剧本 × AI 影像 × 极速生成
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

# 导入路由
from src.routes.index import index
from src.routes.user import user
from src.routes.project import project
from src.routes.novel import novel
from src.routes.outline import outline
from src.routes.script import script
from src.routes.storyboard import storyboard
from src.routes.assets import assets
from src.routes.video import video
from src.routes.task import task
from src.routes.prompt import prompt
from src.routes.setting import setting
from src.routes.other import other

# 创建 FastAPI 应用
app = FastAPI(
    title="Toonflow API",
    description="AI 短剧工厂 - 从文本到角色，从分镜到视频，0 门槛全流程 AI 化",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境应该限制具体域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(index.router, prefix="/api/index", tags=["首页"])
app.include_router(user.router, prefix="/api/user", tags=["用户"])
app.include_router(project.router, prefix="/api/project", tags=["项目"])
app.include_router(novel.router, prefix="/api/novel", tags=["小说"])
app.include_router(outline.router, prefix="/api/outline", tags=["大纲"])
app.include_router(script.router, prefix="/api/script", tags=["剧本"])
app.include_router(storyboard.router, prefix="/api/storyboard", tags=["分镜"])
app.include_router(assets.router, prefix="/api/assets", tags=["素材"])
app.include_router(video.router, prefix="/api/video", tags=["视频"])
app.include_router(task.router, prefix="/api/task", tags=["任务"])
app.include_router(prompt.router, prefix="/api/prompt", tags=["提示词"])
app.include_router(setting.router, prefix="/api/setting", tags=["设置"])
app.include_router(other.router, prefix="/api/other", tags=["其他"])

# 挂载静态文件目录
if os.path.exists("public"):
    app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get("/")
async def root():
    """API 根路径"""
    return {
        "name": "Toonflow API",
        "version": "1.0.0",
        "description": "AI 短剧工厂 - 从文本到角色，从分镜到视频",
        "docs": "/api/docs"
    }

@app.get("/api/health")
async def health_check():
    """健康检查"""
    return {"status": "ok", "message": "Toonflow API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
