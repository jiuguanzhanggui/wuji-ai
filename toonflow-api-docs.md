# Toonflow Backend API 文档

> **版本**: 1.0.0  
> **基础 URL**: `http://localhost:60000` (默认端口)  
> **认证方式**: JWT Token (Bearer Token)

---

## 目录

1. [认证说明](#认证说明)
2. [通用响应格式](#通用响应格式)
3. [API 列表](#api-列表)
   - [用户认证](#用户认证)
   - [项目管理](#项目管理)
   - [大纲/剧本](#大纲剧本)
   - [原文/小说](#原文小说)
   - [分镜管理](#分镜管理)
   - [素材/资产](#素材资产)
   - [视频生成](#视频生成)
   - [任务管理](#任务管理)
   - [系统设置](#系统设置)
   - [提示词管理](#提示词管理)
   - [其他接口](#其他接口)

---

## 认证说明

### Token 获取
通过 `/other/login` 接口登录后获取 Token。

### Token 使用方式
在请求 Header 中携带：
```
Authorization: Bearer <your_token>
```
或在 URL 查询参数中携带：
```
?token=<your_token>
```

### Token 有效期
- 默认有效期：180 天

### 免认证接口
- `/other/login` - 登录接口

---

## 通用响应格式

所有 API 返回统一格式：

```json
{
  "code": 200,
  "data": {},
  "message": "成功"
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| code | number | 状态码 (200=成功，400=客户端错误，401=未授权，404=未找到，500=服务器错误) |
| data | any | 返回数据 |
| message | string | 响应消息 |

---

## API 列表

### 用户认证

#### 1. 用户登录
- **接口**: `POST /other/login`
- **认证**: 不需要
- **描述**: 用户登录获取 Token

**请求参数**:
```json
{
  "username": "string",
  "password": "string"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "name": "admin",
    "id": 1
  },
  "message": "登录成功"
}
```

---

#### 2. 保存用户信息
- **接口**: `POST /user/saveUser`
- **认证**: 需要
- **描述**: 更新用户信息

**请求参数**:
```json
{
  "id": 1,
  "name": "string",
  "password": "string"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "保存设置成功",
  "message": "成功"
}
```

---

#### 3. 获取用户信息
- **接口**: `POST /user/getUser`
- **认证**: 需要
- **描述**: 获取当前用户信息

**请求参数**: 无

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "id": 1,
    "name": "admin"
  },
  "message": "成功"
}
```

---

### 项目管理

#### 4. 获取项目列表
- **接口**: `POST /project/getProject`
- **认证**: 需要
- **描述**: 获取所有项目

**请求参数**: 无

**响应示例**:
```json
{
  "code": 200,
  "data": [
    {
      "id": 1,
      "name": "项目名称",
      "intro": "项目介绍",
      "type": "项目类型",
      "artStyle": "艺术风格",
      "videoRatio": "视频比例",
      "userId": 1,
      "createTime": 1234567890
    }
  ],
  "message": "成功"
}
```

---

#### 5. 获取单个项目
- **接口**: `POST /project/getSingleProject`
- **认证**: 需要
- **描述**: 获取指定项目详情

**请求参数**:
```json
{
  "id": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "id": 1,
    "name": "项目名称",
    "intro": "项目介绍",
    "type": "项目类型",
    "artStyle": "艺术风格",
    "videoRatio": "视频比例"
  },
  "message": "成功"
}
```

---

#### 6. 添加项目
- **接口**: `POST /project/addProject`
- **认证**: 需要
- **描述**: 创建新项目

**请求参数**:
```json
{
  "name": "string",
  "intro": "string",
  "type": "string",
  "artStyle": "string",
  "videoRatio": "string"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "id": 1
  },
  "message": "成功"
}
```

---

#### 7. 更新项目
- **接口**: `POST /project/updateProject`
- **认证**: 需要
- **描述**: 更新项目信息

**请求参数**:
```json
{
  "id": 1,
  "name": "string",
  "intro": "string",
  "type": "string",
  "artStyle": "string",
  "videoRatio": "string"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "更新成功",
  "message": "成功"
}
```

---

#### 8. 删除项目
- **接口**: `POST /project/delProject`
- **认证**: 需要
- **描述**: 删除指定项目

**请求参数**:
```json
{
  "id": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "删除成功",
  "message": "成功"
}
```

---

#### 9. 获取项目数量
- **接口**: `POST /project/getProjectCount`
- **认证**: 需要
- **描述**: 获取项目总数

**请求参数**: 无

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "count": 10
  },
  "message": "成功"
}
```

---

### 大纲/剧本

#### 10. 获取大纲列表
- **接口**: `POST /outline/getOutline`
- **认证**: 需要
- **描述**: 获取指定项目的大纲列表

**请求参数**:
```json
{
  "projectId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": [
    {
      "id": 1,
      "projectId": 1,
      "episode": 1,
      "data": "{\"chapterRange\":[1,2,3]}"
    }
  ],
  "message": "成功"
}
```

---

#### 11. 添加大纲
- **接口**: `POST /outline/addOutline`
- **认证**: 需要
- **描述**: 创建新大纲

**请求参数**:
```json
{
  "projectId": 1,
  "episode": 1,
  "data": "{}"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "id": 1
  },
  "message": "成功"
}
```

---

#### 12. 更新大纲
- **接口**: `POST /outline/updateOutline`
- **认证**: 需要
- **描述**: 更新大纲信息

**请求参数**:
```json
{
  "id": 1,
  "data": "{}"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "更新成功",
  "message": "成功"
}
```

---

#### 13. 删除大纲
- **接口**: `POST /outline/delOutline`
- **认证**: 需要
- **描述**: 删除指定大纲

**请求参数**:
```json
{
  "id": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "删除成功",
  "message": "成功"
}
```

---

#### 14. 获取故事线
- **接口**: `POST /outline/getStoryline`
- **认证**: 需要
- **描述**: 获取项目故事线

**请求参数**:
```json
{
  "projectId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": [
    {
      "id": 1,
      "name": "故事线名称",
      "content": "故事线内容",
      "novelIds": "[1,2,3]"
    }
  ],
  "message": "成功"
}
```

---

#### 15. 更新故事线
- **接口**: `POST /outline/updateStoryline`
- **认证**: 需要
- **描述**: 更新故事线内容

**请求参数**:
```json
{
  "id": 1,
  "name": "string",
  "content": "string",
  "novelIds": "[1,2,3]"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "更新成功",
  "message": "成功"
}
```

---

#### 16. 获取分集剧本
- **接口**: `POST /outline/getPartScript`
- **认证**: 需要
- **描述**: 获取指定分集的剧本内容

**请求参数**:
```json
{
  "outlineId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "content": "剧本内容..."
  },
  "message": "成功"
}
```

---

#### 17. 更新剧本
- **接口**: `POST /outline/updateScript`
- **认证**: 需要
- **描述**: 更新剧本内容

**请求参数**:
```json
{
  "scriptId": 1,
  "content": "string"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "更新成功",
  "message": "成功"
}
```

---

#### 18. 获取历史记录
- **接口**: `POST /outline/getHistory`
- **认证**: 需要
- **描述**: 获取大纲生成历史

**请求参数**:
```json
{
  "projectId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": [
    {
      "id": 1,
      "type": "outline",
      "data": "{}",
      "createTime": 1234567890
    }
  ],
  "message": "成功"
}
```

---

#### 19. 设置历史记录
- **接口**: `POST /outline/setHistory`
- **认证**: 需要
- **描述**: 保存大纲生成历史

**请求参数**:
```json
{
  "projectId": 1,
  "type": "outline",
  "data": "{}"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "保存成功",
  "message": "成功"
}
```

---

#### 20. AI 生成大纲
- **接口**: `POST /outline/agentsOutline`
- **认证**: 需要
- **描述**: 使用 AI 生成大纲

**请求参数**:
```json
{
  "projectId": 1,
  "novelData": {},
  "parameter": {}
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "outlineData": {}
  },
  "message": "成功"
}
```

---

#### 21. 生成剧本
- **接口**: `POST /script/generateScriptApi`
- **认证**: 需要
- **描述**: 根据大纲和原文生成剧本

**请求参数**:
```json
{
  "outlineId": 1,
  "scriptId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "message": "生成剧本成功"
  },
  "message": "成功"
}
```

---

#### 22. 获取剧本
- **接口**: `POST /script/geScriptApi`
- **认证**: 需要
- **描述**: 获取剧本内容

**请求参数**:
```json
{
  "scriptId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "id": 1,
    "name": "剧本名称",
    "content": "剧本内容...",
    "outlineId": 1
  },
  "message": "成功"
}
```

---

#### 23. 保存剧本
- **接口**: `POST /script/generateScriptSave`
- **认证**: 需要
- **描述**: 保存生成的剧本

**请求参数**:
```json
{
  "scriptId": 1,
  "content": "string"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "保存成功",
  "message": "成功"
}
```

---

### 原文/小说

#### 24. 获取原文列表
- **接口**: `POST /novel/getNovel`
- **认证**: 需要
- **描述**: 获取项目原文/小说章节列表

**请求参数**:
```json
{
  "projectId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": [
    {
      "id": 1,
      "index": 1,
      "reel": "第一卷",
      "chapter": "第一章",
      "chapterData": "章节内容..."
    }
  ],
  "message": "成功"
}
```

---

#### 25. 添加原文
- **接口**: `POST /novel/addNovel`
- **认证**: 需要
- **描述**: 添加小说章节

**请求参数**:
```json
{
  "projectId": 1,
  "reel": "第一卷",
  "chapter": "第一章",
  "chapterData": "章节内容",
  "chapterIndex": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "id": 1
  },
  "message": "成功"
}
```

---

#### 26. 更新原文
- **接口**: `POST /novel/updateNovel`
- **认证**: 需要
- **描述**: 更新小说章节

**请求参数**:
```json
{
  "id": 1,
  "reel": "第一卷",
  "chapter": "第一章",
  "chapterData": "章节内容",
  "chapterIndex": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "更新成功",
  "message": "成功"
}
```

---

#### 27. 删除原文
- **接口**: `POST /novel/delNovel`
- **认证**: 需要
- **描述**: 删除小说章节

**请求参数**:
```json
{
  "id": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "删除成功",
  "message": "成功"
}
```

---

### 分镜管理

#### 28. 获取分镜列表
- **接口**: `POST /storyboard/getStoryboard`
- **认证**: 需要
- **描述**: 获取分镜列表

**请求参数**:
```json
{
  "projectId": 1,
  "assetsId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": [
    {
      "id": 1,
      "filePath": "https://...",
      "prompt": "分镜描述",
      "state": "1"
    }
  ],
  "message": "成功"
}
```

---

#### 29. 生成分镜
- **接口**: `POST /storyboard/generateStoryboardApi`
- **认证**: 需要
- **描述**: AI 生成分镜图

**请求参数**:
```json
{
  "filePath": "string | object",
  "prompt": "string",
  "projectId": 1,
  "assetsId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "id": 1,
    "url": "https://..."
  },
  "message": "成功"
}
```

---

#### 30. 保存分镜
- **接口**: `POST /storyboard/saveStoryboard`
- **认证**: 需要
- **描述**: 保存分镜数据

**请求参数**:
```json
{
  "projectId": 1,
  "assetsId": 1,
  "imageData": []
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "保存成功",
  "message": "成功"
}
```

---

#### 31. 删除分镜
- **接口**: `POST /storyboard/delStoryboard`
- **认证**: 需要
- **描述**: 删除分镜

**请求参数**:
```json
{
  "id": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "删除成功",
  "message": "成功"
}
```

---

#### 32. 上传分镜图片
- **接口**: `POST /storyboard/uploadImage`
- **认证**: 需要
- **描述**: 上传分镜图片

**请求参数**: FormData
- `file`: 图片文件
- `projectId`: 项目 ID
- `assetsId`: 资产 ID

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "url": "https://..."
  },
  "message": "成功"
}
```

---

#### 33. 生成分镜视频提示词
- **接口**: `POST /storyboard/generateVideoPrompt`
- **认证**: 需要
- **描述**: 根据分镜生成视频提示词

**请求参数**:
```json
{
  "storyboardId": 1,
  "projectId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "prompt": "视频提示词内容..."
  },
  "message": "成功"
}
```

---

#### 34. 生成分镜镜头图
- **接口**: `POST /storyboard/generateShotImage`
- **认证**: 需要
- **描述**: 生成分镜镜头图片

**请求参数**:
```json
{
  "storyboardId": 1,
  "prompt": "string",
  "projectId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "url": "https://..."
  },
  "message": "成功"
}
```

---

#### 35. 分镜对话
- **接口**: `POST /storyboard/chatStoryboard`
- **认证**: 需要
- **描述**: 分镜 AI 对话/修改

**请求参数**:
```json
{
  "storyboardId": 1,
  "message": "string",
  "history": []
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "reply": "AI 回复内容..."
  },
  "message": "成功"
}
```

---

#### 36. 保留分镜
- **接口**: `POST /storyboard/keepStoryboard`
- **认证**: 需要
- **描述**: 确认保留分镜

**请求参数**:
```json
{
  "storyboardId": 1,
  "keep": true
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "操作成功",
  "message": "成功"
}
```

---

#### 37. 批量评分分镜
- **接口**: `POST /storyboard/batchSuperScoreImage`
- **认证**: 需要
- **描述**: 批量对分镜进行 AI 评分

**请求参数**:
```json
{
  "storyboardIds": [1, 2, 3],
  "projectId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": [
    {
      "id": 1,
      "score": 85,
      "comment": "评分意见..."
    }
  ],
  "message": "成功"
}
```

---

### 素材/资产

#### 38. 获取素材列表
- **接口**: `POST /assets/getAssets`
- **认证**: 需要
- **描述**: 获取项目素材列表

**请求参数**:
```json
{
  "projectId": 1,
  "type": "image | video | audio"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": [
    {
      "id": 1,
      "name": "素材名称",
      "filePath": "https://...",
      "type": "image",
      "projectId": 1,
      "scriptId": 1,
      "prompt": "生成提示词"
    }
  ],
  "message": "成功"
}
```

---

#### 39. 添加素材
- **接口**: `POST /assets/addAssets`
- **认证**: 需要
- **描述**: 添加新素材

**请求参数**:
```json
{
  "projectId": 1,
  "name": "string",
  "type": "string",
  "filePath": "string",
  "prompt": "string",
  "intro": "string"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "id": 1
  },
  "message": "成功"
}
```

---

#### 40. 更新素材
- **接口**: `POST /assets/updateAssets`
- **认证**: 需要
- **描述**: 更新素材信息

**请求参数**:
```json
{
  "id": 1,
  "name": "string",
  "prompt": "string",
  "intro": "string"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "更新成功",
  "message": "成功"
}
```

---

#### 41. 删除素材
- **接口**: `POST /assets/delAssets`
- **认证**: 需要
- **描述**: 删除素材

**请求参数**:
```json
{
  "id": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "删除成功",
  "message": "成功"
}
```

---

#### 42. 删除素材图片
- **接口**: `POST /assets/delAssetsImage`
- **认证**: 需要
- **描述**: 删除素材关联的图片

**请求参数**:
```json
{
  "assetsId": 1,
  "imageId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "删除成功",
  "message": "成功"
}
```

---

#### 43. 保存素材
- **接口**: `POST /assets/saveAssets`
- **认证**: 需要
- **描述**: 保存素材数据

**请求参数**:
```json
{
  "projectId": 1,
  "assetsData": []
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "保存成功",
  "message": "成功"
}
```

---

#### 44. 生成素材
- **接口**: `POST /assets/generateAssets`
- **认证**: 需要
- **描述**: AI 生成素材

**请求参数**:
```json
{
  "projectId": 1,
  "scriptId": 1,
  "prompt": "string",
  "type": "image"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "url": "https://..."
  },
  "message": "成功"
}
```

---

#### 45. 获取图片
- **接口**: `POST /assets/getImage`
- **认证**: 需要
- **描述**: 获取指定图片

**请求参数**:
```json
{
  "imageId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "url": "https://..."
  },
  "message": "成功"
}
```

---

#### 46. 获取分镜素材
- **接口**: `POST /assets/getStoryboard`
- **认证**: 需要
- **描述**: 获取分镜相关素材

**请求参数**:
```json
{
  "projectId": 1,
  "assetsId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": [],
  "message": "成功"
}
```

---

#### 47. 润色提示词
- **接口**: `POST /assets/polishPrompt`
- **认证**: 需要
- **描述**: AI 润色/优化提示词

**请求参数**:
```json
{
  "prompt": "string",
  "type": "image | video"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "polishedPrompt": "优化后的提示词..."
  },
  "message": "成功"
}
```

---

### 视频生成

#### 48. 生成视频
- **接口**: `POST /video/generateVideo`
- **认证**: 需要
- **描述**: 生成视频 (异步处理)

**请求参数**:
```json
{
  "projectId": 1,
  "scriptId": 1,
  "configId": 1,
  "aiConfigId": 1,
  "resolution": "1080p",
  "filePath": ["https://..."],
  "duration": 10,
  "prompt": "视频描述",
  "mode": "startEnd | multi | single | text",
  "audioEnabled": true
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "id": 1,
    "configId": 1
  },
  "message": "成功"
}
```

> **注意**: 视频生成是异步的，接口会立即返回，实际生成在后台进行。可通过任务接口查询状态。

---

#### 49. 获取视频列表
- **接口**: `POST /video/getVideo`
- **认证**: 需要
- **描述**: 获取视频列表

**请求参数**:
```json
{
  "projectId": 1,
  "scriptId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": [
    {
      "id": 1,
      "filePath": "https://...",
      "state": 1,
      "prompt": "视频描述",
      "resolution": "1080p",
      "time": 10,
      "createTime": 1234567890
    }
  ],
  "message": "成功"
}
```

---

#### 50. 添加视频
- **接口**: `POST /video/addVideo`
- **认证**: 需要
- **描述**: 添加视频记录

**请求参数**:
```json
{
  "scriptId": 1,
  "filePath": "string",
  "prompt": "string",
  "resolution": "string",
  "time": 10
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "id": 1
  },
  "message": "成功"
}
```

---

#### 51. 保存视频
- **接口**: `POST /video/saveVideo`
- **认证**: 需要
- **描述**: 保存视频数据

**请求参数**:
```json
{
  "videoId": 1,
  "data": {}
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "保存成功",
  "message": "成功"
}
```

---

#### 52. 获取视频配置列表
- **接口**: `POST /video/getVideoConfigs`
- **认证**: 需要
- **描述**: 获取视频配置列表

**请求参数**:
```json
{
  "projectId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": [
    {
      "id": 1,
      "name": "配置名称",
      "manufacturer": "厂商",
      "model": "模型",
      "duration": 10,
      "resolution": "1080p",
      "mode": "single"
    }
  ],
  "message": "成功"
}
```

---

#### 53. 添加视频配置
- **接口**: `POST /video/addVideoConfig`
- **认证**: 需要
- **描述**: 添加视频配置

**请求参数**:
```json
{
  "projectId": 1,
  "name": "string",
  "manufacturer": "string",
  "model": "string",
  "duration": 10,
  "resolution": "string",
  "mode": "string",
  "audioEnabled": true
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "id": 1
  },
  "message": "成功"
}
```

---

#### 54. 更新视频配置
- **接口**: `POST /video/upDateVideoConfig`
- **认证**: 需要
- **描述**: 更新视频配置

**请求参数**:
```json
{
  "id": 1,
  "name": "string",
  "manufacturer": "string",
  "model": "string",
  "duration": 10,
  "resolution": "string",
  "mode": "string"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "更新成功",
  "message": "成功"
}
```

---

#### 55. 删除视频配置
- **接口**: `POST /video/deleteVideoConfig`
- **认证**: 需要
- **描述**: 删除视频配置

**请求参数**:
```json
{
  "id": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "删除成功",
  "message": "成功"
}
```

---

#### 56. 获取视频分镜
- **接口**: `POST /video/getVideoStoryboards`
- **认证**: 需要
- **描述**: 获取视频关联的分镜

**请求参数**:
```json
{
  "videoId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": [],
  "message": "成功"
}
```

---

#### 57. 修改视频分镜
- **接口**: `POST /video/reviseVideoStoryboards`
- **认证**: 需要
- **描述**: 修改视频分镜配置

**请求参数**:
```json
{
  "videoId": 1,
  "storyboardIds": [1, 2, 3]
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "修改成功",
  "message": "成功"
}
```

---

#### 58. 生成视频提示词
- **接口**: `POST /video/generatePrompt`
- **认证**: 需要
- **描述**: AI 生成视频提示词

**请求参数**:
```json
{
  "scriptId": 1,
  "projectId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "prompt": "生成的视频提示词..."
  },
  "message": "成功"
}
```

---

#### 59. 获取视频模型
- **接口**: `POST /video/getVideoModel`
- **认证**: 需要
- **描述**: 获取可用的视频生成模型

**请求参数**: 无

**响应示例**:
```json
{
  "code": 200,
  "data": [
    {
      "id": 1,
      "manufacturer": "厂商",
      "model": "模型名称"
    }
  ],
  "message": "成功"
}
```

---

#### 60. 获取视频厂商列表
- **接口**: `POST /video/getManufacturer`
- **认证**: 需要
- **描述**: 获取支持的视频厂商

**请求参数**: 无

**响应示例**:
```json
{
  "code": 200,
  "data": ["可灵", "即梦", "Vidu", "Runway"],
  "message": "成功"
}
```

---

### 任务管理

#### 61. 获取任务列表
- **接口**: `GET /task/getTaskApi`
- **认证**: 需要
- **描述**: 获取任务列表 (支持分页和筛选)

**请求参数** (Query Parameters):
```
?projectName=项目名称&taskName=任务名称&state=状态&page=1&limit=10
```

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| projectName | string | 否 | 项目名称筛选 |
| taskName | string | 否 | 任务名称筛选 |
| state | string | 否 | 状态筛选 (0=进行中，1=完成，-1=失败) |
| page | number | 否 | 页码，默认 1 |
| limit | number | 否 | 每页数量，默认 10 |

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "data": [
      {
        "id": 1,
        "name": "任务名称",
        "projectName": 1,
        "prompt": "任务描述",
        "state": "1",
        "startTime": "2024-01-01 10:00:00",
        "endTime": "2024-01-01 10:05:00"
      }
    ],
    "total": 100
  },
  "message": "成功"
}
```

---

#### 62. 获取任务详情
- **接口**: `POST /task/taskDetails`
- **认证**: 需要
- **描述**: 获取任务详细信息

**请求参数**:
```json
{
  "taskId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "id": 1,
    "name": "任务名称",
    "state": "1",
    "result": {},
    "errorReason": null
  },
  "message": "成功"
}
```

---

### 系统设置

#### 63. 获取设置
- **接口**: `POST /setting/getSetting`
- **认证**: 需要
- **描述**: 获取系统设置

**请求参数**: 无

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "id": 1,
    "languageModel": "text-model-id",
    "imageModel": "image-model-id",
    "tokenKey": "jwt-secret"
  },
  "message": "成功"
}
```

---

#### 64. 获取 AI 模型列表
- **接口**: `POST /setting/getAiModelList`
- **认证**: 需要
- **描述**: 获取配置的 AI 模型列表

**请求参数**:
```json
{
  "type": "text | image | video"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "openai": [
      {"label": "gpt-4", "value": "gpt-4"}
    ],
    "anthropic": [
      {"label": "claude-3", "value": "claude-3"}
    ]
  },
  "message": "成功"
}
```

---

#### 65. 获取 AI 模型映射
- **接口**: `POST /setting/getAiModelMap`
- **认证**: 需要
- **描述**: 获取 AI 模型映射关系

**请求参数**: 无

**响应示例**:
```json
{
  "code": 200,
  "data": [
    {
      "id": 1,
      "configId": 1,
      "key": "model-key",
      "name": "模型名称"
    }
  ],
  "message": "成功"
}
```

---

#### 66. 获取视频模型列表
- **接口**: `POST /setting/getVideoModelList`
- **认证**: 需要
- **描述**: 获取视频模型列表

**请求参数**: 无

**响应示例**:
```json
{
  "code": 200,
  "data": [
    {
      "id": 1,
      "manufacturer": "厂商",
      "model": "模型",
      "aspectRatio": "16:9",
      "duration": "5-10s"
    }
  ],
  "message": "成功"
}
```

---

#### 67. 获取视频模型详情
- **接口**: `POST /setting/getVideoModelDetail`
- **认证**: 需要
- **描述**: 获取视频模型详细信息

**请求参数**:
```json
{
  "modelId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "id": 1,
    "manufacturer": "厂商",
    "model": "模型",
    "config": {}
  },
  "message": "成功"
}
```

---

#### 68. 添加模型配置
- **接口**: `POST /setting/addModel`
- **认证**: 需要
- **描述**: 添加 AI 模型配置

**请求参数**:
```json
{
  "type": "text | image | video",
  "manufacturer": "string",
  "model": "string",
  "apiKey": "string",
  "baseUrl": "string"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "id": 1
  },
  "message": "成功"
}
```

---

#### 69. 更新模型配置
- **接口**: `POST /setting/updateModel`
- **认证**: 需要
- **描述**: 更新模型配置

**请求参数**:
```json
{
  "id": 1,
  "apiKey": "string",
  "baseUrl": "string",
  "model": "string"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "更新成功",
  "message": "成功"
}
```

---

#### 70. 删除模型配置
- **接口**: `POST /setting/delModel`
- **认证**: 需要
- **描述**: 删除模型配置

**请求参数**:
```json
{
  "id": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "删除成功",
  "message": "成功"
}
```

---

#### 71. 配置模型
- **接口**: `POST /setting/configurationModel`
- **认证**: 需要
- **描述**: 配置模型映射关系

**请求参数**:
```json
{
  "configId": 1,
  "modelMap": {}
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "配置成功",
  "message": "成功"
}
```

---

#### 72. 获取日志
- **接口**: `POST /setting/getLog`
- **认证**: 需要
- **描述**: 获取系统日志

**请求参数**:
```json
{
  "page": 1,
  "limit": 20,
  "type": "error | info | warning"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "data": [],
    "total": 100
  },
  "message": "成功"
}
```

---

### 提示词管理

#### 73. 获取提示词列表
- **接口**: `GET /prompt/getPrompts`
- **认证**: 需要
- **描述**: 获取系统提示词配置

**请求参数**: 无

**响应示例**:
```json
{
  "code": 200,
  "data": [
    {
      "id": 1,
      "name": "提示词名称",
      "code": "PROMPT_CODE",
      "type": "image",
      "defaultValue": "默认值",
      "customValue": "自定义值",
      "parentCode": "PARENT_CODE"
    }
  ],
  "message": "成功"
}
```

---

#### 74. 更新提示词
- **接口**: `POST /prompt/updatePrompt`
- **认证**: 需要
- **描述**: 更新提示词配置

**请求参数**:
```json
{
  "id": 1,
  "customValue": "string"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": "更新成功",
  "message": "成功"
}
```

---

### 其他接口

#### 75. 获取验证码
- **接口**: `POST /other/getCaptcha`
- **认证**: 不需要
- **描述**: 获取登录验证码

**请求参数**: 无

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "captchaId": "xxx",
    "captchaImage": "base64..."
  },
  "message": "成功"
}
```

---

#### 76. 测试 AI
- **接口**: `POST /other/testAI`
- **认证**: 需要
- **描述**: 测试 AI 连接

**请求参数**:
```json
{
  "type": "text | image | video",
  "configId": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "success": true,
    "message": "连接正常"
  },
  "message": "成功"
}
```

---

#### 77. 测试图片生成
- **接口**: `POST /other/testImage`
- **认证**: 需要
- **描述**: 测试图片生成

**请求参数**:
```json
{
  "configId": 1,
  "prompt": "测试提示词"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "url": "https://..."
  },
  "message": "成功"
}
```

---

#### 78. 测试视频生成
- **接口**: `POST /other/testVideo`
- **认证**: 需要
- **描述**: 测试视频生成

**请求参数**:
```json
{
  "configId": 1,
  "prompt": "测试提示词"
}
```

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "url": "https://..."
  },
  "message": "成功"
}
```

---

#### 79. 清除数据库
- **接口**: `POST /other/clearDatabase`
- **认证**: 需要
- **描述**: 清除数据库所有数据 (**危险操作**)

**请求参数**: 无

**响应示例**:
```json
{
  "code": 200,
  "data": "清除成功",
  "message": "成功"
}
```

---

#### 80. 删除所有数据
- **接口**: `POST /other/deleteAllData`
- **认证**: 需要
- **描述**: 删除所有业务数据 (**危险操作**)

**请求参数**: 无

**响应示例**:
```json
{
  "code": 200,
  "data": "删除成功",
  "message": "成功"
}
```

---

#### 81. 首页接口
- **接口**: `GET /index`
- **认证**: 需要
- **描述**: 获取首页/仪表板数据

**请求参数**: 无

**响应示例**:
```json
{
  "code": 200,
  "data": {
    "projectCount": 10,
    "videoCount": 50,
    "taskCount": 100
  },
  "message": "成功"
}
```

---

## 数据库表结构参考

| 表名 | 说明 |
|------|------|
| t_user | 用户表 |
| t_project | 项目表 |
| t_outline | 大纲表 |
| t_script | 剧本表 |
| t_novel | 小说/原文表 |
| t_storyline | 故事线表 |
| t_assets | 素材/资产表 |
| t_image | 图片表 |
| t_storyboard | 分镜表 |
| t_video | 视频表 |
| t_videoConfig | 视频配置表 |
| t_config | AI 模型配置表 |
| t_textModel | 文本模型表 |
| t_imageModel | 图片模型表 |
| t_videoModel | 视频模型表 |
| t_taskList | 任务列表表 |
| t_prompts | 提示词配置表 |
| t_setting | 系统设置表 |
| t_chatHistory | 对话历史表 |
| t_aiModelMap | AI 模型映射表 |

---

## 错误码说明

| 状态码 | 说明 |
|--------|------|
| 200 | 成功 |
| 400 | 客户端错误 (参数错误、请求格式错误等) |
| 401 | 未授权 (Token 缺失或无效) |
| 404 | 资源未找到 |
| 500 | 服务器内部错误 |

---

## 注意事项

1. **Token 安全**: 请妥善保管 Token，不要泄露
2. **异步任务**: 视频生成等耗时操作采用异步处理，需通过任务接口查询状态
3. **文件大小**: 上传文件限制为 100MB
4. **并发限制**: 建议控制并发请求数量
5. **数据备份**: 执行删除操作前请做好数据备份

---

*文档生成时间: 2026-03-03*
