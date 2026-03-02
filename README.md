# Toonflow Python - AI 短剧工厂 FastAPI 后端

基于 **FastAPI** 的 Python 后端实现，保持与原 Node.js 项目相同的文件结构。

## 🚀 快速开始

### 1. 安装依赖

```bash
cd toonflow-python
pip install -r requirements.txt
```

### 2. 配置环境

```bash
cp .env.example .env
# 编辑 .env 文件，填入你的 API Key
```

### 3. 启动服务

```bash
# 开发模式
python main.py

# 或使用 uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 4. 访问 API 文档

- Swagger UI: http://localhost:8000/api/docs
- ReDoc: http://localhost:8000/api/redoc
- API Root: http://localhost:8000

## 📁 项目结构

```
toonflow-python/
├── main.py                    # 应用入口
├── config.py                  # 配置文件
├── database.py                # 数据库配置
├── requirements.txt           # Python 依赖
├── .env.example              # 环境变量示例
└── src/
    ├── routes/               # API 路由
    │   ├── index/           # 首页
    │   ├── user/            # 用户
    │   ├── project/         # 项目
    │   ├── novel/           # 小说
    │   ├── outline/         # 大纲
    │   ├── script/          # 剧本
    │   ├── storyboard/      # 分镜
    │   ├── assets/          # 素材
    │   ├── video/           # 视频
    │   ├── task/            # 任务
    │   ├── prompt/          # 提示词
    │   ├── setting/         # 设置
    │   └── other/           # 其他
    ├── lib/                  # 库函数
    ├── middleware/           # 中间件
    ├── utils/                # 工具函数
    │   └── ai/              # AI 相关工具
    │       ├── text/        # 文本生成
    │       ├── image/       # 图片生成
    │       └── video/       # 视频生成
    └── agents/               # AI Agents
        ├── outlineScript/   # 大纲剧本 Agent
        └── storyboard/      # 分镜 Agent
```

## 🔌 API 端点

| 路由 | 前缀 | 说明 |
|------|------|------|
| index | `/api/index` | 首页信息 |
| user | `/api/user` | 用户登录/管理 |
| project | `/api/project` | 项目管理 |
| novel | `/api/novel` | 小说管理 |
| outline | `/api/outline` | 大纲生成 |
| script | `/api/script` | 剧本生成 |
| storyboard | `/api/storyboard` | 分镜制作 |
| assets | `/api/assets` | 素材管理 |
| video | `/api/video` | 视频生成 |
| task | `/api/task` | 任务管理 |
| prompt | `/api/prompt` | 提示词管理 |
| setting | `/api/setting` | 系统设置 |
| other | `/api/other` | 其他功能 |

## 🔑 核心功能

### 1. 用户系统
- 登录/登出
- 用户信息管理

### 2. 项目管理
- 创建/编辑/删除项目
- 项目列表查询

### 3. AI 创作流程
```
小说 → 大纲 → 剧本 → 分镜 → 视频
```

### 4. AI 服务集成
- OpenAI (GPT, DALL-E)
- Anthropic (Claude)
- 阿里云 (DashScope)
- Google Veo (视频)
- Seedance (视频)

## 📝 待实现功能

以下功能目前返回模拟数据，需要接入实际 AI 服务：

- [ ] AI 大纲生成
- [ ] AI 剧本生成
- [ ] AI 分镜生成
- [ ] AI 图片生成
- [ ] AI 视频生成
- [ ] 提示词优化
- [ ] 数据库持久化

## 🛠️ 开发

### 添加新路由

1. 在 `src/routes/` 下创建新目录
2. 创建 `__init__.py` 定义路由
3. 在 `main.py` 中注册路由

### 接入 AI 服务

在 `src/utils/ai/` 下添加相应的 AI 服务集成：

```python
# src/utils/ai/text/generate.py
from openai import AsyncOpenAI

client = AsyncOpenAI()

async def generate_text(prompt: str):
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
```

## 📄 许可证

AGPL-3.0

---

**Toonflow** - AI 剧本 × AI 影像 × 极速生成 🔥
