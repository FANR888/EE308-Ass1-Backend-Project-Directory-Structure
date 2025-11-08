# ✨ 后端代码规范（Code Style）

**来源**：  
本项目代码风格主要参考并遵循以下官方与大公司规范整理：

* **Python 官方：** [PEP 8 – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* **Django 官方文档：** [Coding style（编码风格）](https://docs.djangoproject.com/en/stable/internals/contributing/writing-code/coding-style/)
* **Google：** [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

本文件在不与上述规范冲突的前提下，对项目中常用的约定做了精简与本地化说明。**若本文件未明确说明的情况，一律以 PEP 8 与 Django 官方文档为准。**

---

## 1. 📂 项目与文件结构

| 结构项 | 规范 | 示例 |
| :--- | :--- | :--- |
| **顶层目录** | 使用 `<StudentID>_concacts_backend/` 结构。 | `123456_concacts_backend/` |
| **源代码目录** | 所有源代码应放在 `src/` 目录下。 | `src/manage.py`, `src/backend/` |
| **Django App 命名** | 使用**小写+下划线**。 | `contacts`, `user_profile` |
| **文件管理** | 不在项目中保留无用文件、临时文件（如 `*.pyc`, `__pycache__`, IDE配置），统一通过 `.gitignore` 忽略。 | |

**Django 文件结构：**
```bash
EE308-Ass1-Backend-Project-Directory-Structure/
│
├── 832301220_concacts_backend/
│   └── src/
│       ├── manage.py            # Django 管理脚本
│       ├── backend/             # Django 项目配置（settings、urls 等）
│       └── contacts/            # 联系人相关应用（models、views、urls 等）
├── requirements.txt             # 项目依赖包文档
├── README.md                    # 项目说明文档
└── codestyle.md                 # 代码规范说明文档（当前文件）
```


## 2. 📝 命名规范

整体遵循 **PEP 8** 的命名规则：

| 结构项 | 规范 | 示例 |
| :--- | :--- | :--- |
| **模块/文件名** | 全小写，必要时用下划线分隔。 | ✅ `views.py`, `utils.py`, `contact_service.py` |
| **包名** | 全小写，尽量简短。 | ✅ `contacts`, `api`, `common` |
| **类名** | **PascalCase**（每个单词首字母大写）。 | ✅ `Contact`, `ContactService`, `ContactSerializer` |
| **函数/方法名** | **snake_case**（小写 + 下划线）。 | ✅ `create_contact()`, `get_contact_list()` |
| **变量名** | **snake_case**，语义清晰，避免单字母。 | ✅ `contact_id`, `phone_number` |
| **常量名** | **全大写 + 下划线**。 | ✅ `DEFAULT_PAGE_SIZE = 20` |

### Django 特定命名
* **Model 类名：** **单数形式**，例如 `Contact`。
* **Model 字段：** **snake_case**，例如 `phone_number = models.CharField(...)`。
* **URL name：** **小写+下划线**，例如 `name="contacts-list"`。

## 3. 📐 代码格式（缩进、行宽、空行）

### 缩进
* 使用 **4 个空格** 缩进，**不允许使用 TAB**。

### 最大行宽
* **普通代码：** 每行不超过 **79 个字符**。
* **文档字符串和注释：** 建议不超过 **72 字符**。

### 空行
* **顶层函数、类之间：** 使用 **2 行空行** 分隔。
* **类中的方法之间：** 使用 **1 行空行** 分隔。
* 逻辑上无关的代码块之间，适当加入空行增强可读性。

### 空格使用
* **二元运算符两侧加空格：** `a + b`, `x == 1`。
* **函数调用括号前不加空格：** `func(arg1, arg2)`。
* **列表/字典内部逗号后加空格：**
    * ✅ `[1, 2, 3]`
    * ✅ `{"name": "Tom", "age": 18}`

### 换行
* 行过长时优先使用 **圆括号、方括号、花括号** 自动换行：

```python
contacts = [
    contact
    for contact in queryset
    if contact.is_active
]



