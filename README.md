# EE308-Ass1-Backend-Project-Directory-Structure

## 📘 项目简介
本项目为 **EE308 First assignment -- front-end and back-end separation contacts programming** —— “联系人管理（Contacts）” 的 **后端部分**。  

- 姓名：Rongze Fan  
- 学号：832301220 / 23126507  
- 项目目标：提供联系人管理的后端服务，包括联系人信息的新增、查询、修改和删除等功能，为前端页面提供稳定的 RESTful API。  
- 技术栈：Python / Django / SQLite

---

## 📂 目录结构

```bash
EE308-Ass1-Backend-Project-Directory-Structure/
│
├── 832301220_concacts_backend/
│   └── src/
│       ├── manage.py            # Django 管理脚本
│       ├── backend/             # Django 项目配置（settings、urls 等）
│       └── contacts/            # 联系人相关应用（models、views、urls 等）
│
├── README.md                    # 项目说明文档（当前文件）
└── codestyle.md                 # 代码规范说明文档


## 🚀快速开始

1️⃣ 克隆项目
git clone https://github.com/FANR888/EE308-Ass1-Backend-Project-Directory-Structure.git

2️⃣ 进入项目目录
cd EE308-Ass1-Backend-Project-Directory-Structure/832301220_concacts_backend/src

3️⃣ （可选）创建并激活虚拟环境
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate

4️⃣ 安装依赖
# 如果有 requirements.txt
pip install -r requirements.txt

# 如果没有，可手动安装 Django
pip install django

5️⃣ 进行数据库迁移
python manage.py migrate

6️⃣ 启动后端服务
python manage.py runserver 0.0.0.0:8000
