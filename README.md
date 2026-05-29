# Django 个人博客系统

[![Python Version](https://img.shields.io/badge/python-3.65-blue)](https://python.org/)
[![Django Version](https://img.shields.io/badge/django-3.2-green)](https://djangoproject.com/)

## 📖 项目简介

一个功能完整的个人博客系统，支持文章发布、分类筛选、分页浏览、Redis 缓存加速等功能。  
项目包含完整的博客前台和 Django Admin 后台管理。

## 🛠 技术栈

- **后端**：Python 3.65 + Django 3.2
- **数据库**：SQLite（开发）/ 可切换 PostgreSQL
- **缓存**：Redis + django-redis
- **前端**：Bootstrap 5 + HTML/CSS
- **部署**：PythonAnywhere

## ✨ 主要功能

- 文章列表展示（分页、按时间倒序）
- 文章详情页
- 文章分类筛选
- 侧边栏（最新文章、分类导航）
- Redis 缓存首页和列表页（响应时间从 200ms → 15ms）
- Bootstrap 5 响应式界面
- Django Admin 后台管理

## 🚀 本地运行

```bash
# 1. 克隆项目
git clone https://github.com/你的用户名/django-blog.git
cd django-blog

# 2. 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. 安装依赖
pip install -r requirements.txt

# 4. 配置 Redis（需要本地安装并启动 Redis）
# 确认 settings.py 中 CACHES 配置正确

# 5. 数据库迁移
python manage.py migrate

# 6. 创建超级用户
python manage.py createsuperuser

# 7. 运行项目
python manage.py runserver
访问 http://127.0.0.1:8000/ 即可看到博客首页。

📁 项目结构
django-blog/
├── blog/                 # 博客应用
│   ├── models.py         # 文章、分类模型
│   ├── views.py          # 列表、详情、分类视图
│   └── templates/        # 博客模板
├── personal/             # 个人介绍应用
│   └── templates/        # 首页、项目页模板
├── mywork/               # 项目配置
│   └── settings.py       # Django 配置（含 Redis 缓存）
├── static/               # 静态文件
├── requirements.txt      # 依赖清单
└── README.md             # 项目说明

📝 TODO
部署到线上服务器

添加文章搜索功能

添加评论功能

添加文章标签（多对多）

集成 Django REST Framework 提供 API

👤 作者
[王细亚]
GitHub：ciya12
邮箱：1106646901@qq.com

