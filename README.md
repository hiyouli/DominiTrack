# DominiTrack: 您的智能域名守护者 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Workflow Status](https://img.shields.io/badge/Build-Passing-brightgreen)](https://github.com/hiyouli/DominiTrack/actions) [![Technology Stack](https://img.shields.io/badge/Backend-Django-green.svg)](https://www.djangoproject.com/)
[![Technology Stack](https://img.shields.io/badge/Frontend-Vue.js-42b983.svg)](https://vuejs.org/)
[![Technology Stack](https://img.shields.io/badge/Database-PostgreSQL-336791.svg)](https://www.postgresql.org/)
[![Technology Stack](https://img.shields.io/badge/TaskQueue-Celery-blue.svg)](https://docs.celeryq.dev/)

---

## ✨ 项目简介

您是否曾因忘记域名到期日而导致网站下线？或是担心辛苦经营的品牌域名被他人抢注？

**DominiTrack** 正是为解决这一痛点而生！它是一款强大而灵活的开源域名管理与到期提醒系统。通过 DominiTrack，您可以轻松录入并跟踪名下的所有域名，系统将自动监测到期时间，并在关键时刻通过多种渠道（如邮件、微信、Telegram）向您发送个性化提醒，确保您的域名永不掉线，资产安全无虞。

**DominiTrack 的目标是成为您值得信赖的域名资产管理中心。**

## 🌟 核心功能

* **集中式域名管理：**
    * 直观的仪表盘，一览所有域名的状态、到期日期和剩余天数。
    * 轻松添加、编辑和删除域名信息。
* **智能 WHOIS 查询：**
    * 在添加域名时自动查询 WHOIS 信息，智能获取到期日期（支持手动覆盖）。
    * 定期后台自动查询（未来功能），确保数据始终最新。
* **多渠道到期提醒：**
    * **电子邮件通知：** 可定制的提醒时间点（例如到期前90天、30天、7天、1天）。
    * **微信提醒（待集成）：** 通过微信公众号或企业微信推送即时通知。
    * **Telegram 机器人提醒（待集成）：** 将提醒直接发送到您的 Telegram 账户。
    * （未来可扩展短信、Webhook 等更多通知方式。）
* **用户友好的界面：** 清晰、简洁、响应式的设计，无论在桌面还是移动设备上都能轻松操作。
* **灵活的配置：** 自定义提醒间隔和偏好设置，满足您的个性化需求。

## 🛠️ 技术栈

DominiTrack 采用现代化的全栈技术架构，确保高性能、可扩展性和易维护性：

* **后端：**
    * **Python 3.9+**
    * **Django 5.2+：** 强大的 Web 框架，提供完整的 MVC 架构和 ORM。
    * **Django REST Framework：** 快速构建健壮的 RESTful API。
    * **Celery：** 分布式任务队列，用于处理后台任务（如 WHOIS 查询、发送提醒）。
    * **Redis：** Celery 的消息代理和结果存储。
    * **python-whois：** 用于域名 WHOIS 信息查询。
* **前端：**
    * **Vue.js 3+：** 渐进式 JavaScript 框架，构建交互式用户界面。
    * **Vue CLI：** 快速搭建和管理 Vue.js 项目。
    * **Axios：** 强大的 HTTP 客户端，用于前后端数据交互。
* **数据库：**
    * **PostgreSQL：** 稳定、可靠、功能强大的开源关系型数据库。
* **容器化：**
    * **Docker & Docker Compose：** 简化开发环境搭建和生产环境部署，提供一致的运行环境。

## 🚀 快速启动 (面向开发者)

本指南将帮助您在本地搭建 DominiTrack 开发环境。我们强烈推荐使用 Docker Compose 进行开发，以简化依赖管理。

### 前置条件

在开始之前，请确保您的系统已安装以下软件：

* **Git：** 版本控制工具。
* **Docker Desktop：** 包含 Docker Engine 和 Docker Compose，用于运行容器化服务。请确保已启用虚拟化支持（如 Intel VT-x 或 AMD-V）。
* **Python 3.9+：** 用于后端开发和管理虚拟环境。
* **Node.js 16+ (LTS)：** 包含 npm，用于前端开发。

### 💻 本地开发环境设置

1.  **克隆仓库：**

    ```bash
    git clone [https://github.com/hiyouli/DominiTrack.git](https://github.com/hiyouli/DominiTrack.git)
    cd DominiTrack
    ```

2.  **创建 `.env` 文件：**
    在项目根目录 (`DominiTrack/`) 创建一个 `.env` 文件，用于存放敏感信息和环境变量。
    **请务必将 `您的SECRET_KEY` 替换为通过 `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` 生成的密钥！**

    ```env
    # .env

    # Django SECRET_KEY (请替换为您实际生成的密钥！)
    SECRET_KEY=您的SECRET_KEY

    # 数据库配置，与 docker-compose.yml 中的 db 服务配置一致
    DB_NAME=dominitrack_db
    DB_USER=dominitrack_user
    DB_PASSWORD=dominitrack_password
    DB_HOST=db
    DB_PORT=5432

    # Celery 配置
    CELERY_BROKER_URL=redis://redis:6379/0
    CELERY_RESULT_BACKEND=redis://redis:6379/0
    ```

3.  **安装 Python 依赖 & 配置 Django：**

    a. **创建并激活 Python 虚拟环境：**

    ```bash
    # 创建虚拟环境
    python -m venv venv

    # 激活虚拟环境 (Windows)
    .\venv\Scripts\activate
    # 激活虚拟环境 (macOS/Linux)
    # source venv/bin/activate
    ```

    b. **安装后端依赖：**

    ```bash
    pip install django djangorestframework python-dotenv python-whois celery redis
    ```

    c. **生成 `requirements.txt`：**

    ```bash
    pip freeze > requirements.txt
    ```

    d. **配置 Django `settings.py`：**
    请确保 `dominitrack_project/settings.py` 文件已更新，以从 `.env` 文件中加载 `SECRET_KEY` 和数据库配置，并添加了 `rest_framework` 和 `domains` 到 `INSTALLED_APPS`。**此 README 不包含 `settings.py` 的完整内容，请参考项目文件。**

    e. **运行 Django 数据库迁移并创建超级用户：**

    ```bash
    python manage.py migrate
    python manage.py createsuperuser # 创建管理员账户，用于登录 /admin/
    ```

4.  **配置前端 `vue.config.js`：**
    在 `frontend/` 目录下创建 `vue.config.js` 文件（如果不存在），并确保其包含开发代理配置，以便在开发模式下解决前后端跨域问题：

    ```javascript
    // frontend/vue.config.js

    module.exports = {
      devServer: {
        proxy: {
          '/api': { // 当前端请求以 /api 开头时
            target: 'http://backend:8000', // 转发到后端 Docker 容器的地址
            changeOrigin: true, // 改变源，使其看起来像是从后端发出的请求
            ws: true, // 启用 websocket 代理
            pathRewrite: { '^/api': '' } // 重写路径，将 /api 去掉再转发
          }
        },
        host: '0.0.0.0',
        port: 8080,
        client: {
          webSocketURL: 'ws://0.0.0.0:8080/ws',
        },
        allowedHosts: ['all'],
      }
    };
    ```

5.  **配置 Dockerfile 和 Docker Compose：**
    确保以下文件已正确配置：
    * `docker-compose.yml` (在项目根目录)
    * `dominitrack_project/Dockerfile` (后端服务的 Dockerfile)
    * `frontend/Dockerfile.dev` (前端开发服务的 Dockerfile)

    **Docker Compose 配置小贴士：**
    如果您在中国大陆，且拉取 Docker 镜像遇到网络问题（如 `context deadline exceeded` 或 `403 Forbidden`），请在 Docker Desktop 的 `Settings` -> `Docker Engine` 中配置**镜像加速器**。推荐使用阿里云、网易等提供的加速服务，并**确保在运行 Docker 命令时关闭所有 VPN/代理**。

    示例 Docker Engine 配置 (仅供参考，**请替换为您专属的加速器地址**):
    ```json
    {
      "registry-mirrors": [
        "[https://xxxxxxx.mirror.aliyuncs.com](https://xxxxxxx.mirror.aliyuncs.com)"
      ],
      "ipv6": false, // 如果您遇到 IPv6 连接问题，可以考虑添加
      "builder": {
        "gc": {
          "defaultKeepStorage": "20GB",
          "enabled": true
        }
      },
      "experimental": false
    }
    ```

### 启动项目

在项目根目录下，运行：

```bash
docker compose up --build
```

* 此命令将构建 Docker 镜像，并启动 db (PostgreSQL), redis, backend (Django) 和 frontend (Vue.js) 服务。

* 第一次启动可能需要一些时间来下载基础镜像和安装依赖。

#### 访问应用
当所有服务成功启动后：

* 前端应用 (通过 Nginx 代理访问)： http://dominitrack.yourdomain.com/ (替换为您的实际域名)

* 后端管理后台 (通过 Nginx 代理访问)： http://dominitrack.yourdomain.com/admin/ (替换为您的实际域名)

* Django REST Framework API 根目录 (通过 Nginx 代理访问)： http://dominitrack.yourdomain.com/api/ (替换为您的实际域名)

### 🚀🚀 快速部署指南 (面向宝塔面板用户，通过 Docker)

如果您是服务器新手，或习惯使用宝塔面板管理服务器，以下步骤将指导您快速通过 Docker 部署 DominiTrack。

#### 前置条件

* 一台云服务器（Linux 系统，如 CentOS/Ubuntu/Debian）。
* 已安装 **宝塔面板 (BT-Panel)**。
* 在宝塔面板的 **“软件商店”** 中，已安装 **“Docker 管理器”**。

#### 部署步骤

1.  **下载 DominiTrack 项目代码到服务器：**
    a. 登录您的宝塔面板。
    b. 在左侧菜单中选择 **“文件”**。
    c. 导航到您希望存放项目的目录，例如 `/www/wwwroot/`。
    d. 点击顶部导航的 **“远程下载”**。
    e. 粘贴 DominiTrack 的 GitHub 仓库地址：`https://github.com/hiyouli/DominiTrack/archive/refs/heads/main.zip` (直接下载 master 分支的 zip 包)。
    f. 下载完成后，在宝塔文件管理界面中找到 `DominiTrack-main.zip` 并 **解压**。
    g. 将解压后的文件夹重命名为 `DominiTrack` (或者您喜欢的名称)。进入此目录。

2.  **配置 `.env` 环境变量文件：**
    a. 在宝塔文件管理中，进入您刚刚解压的 `DominiTrack` 目录。
    b. 找到 `.env` 文件（如果不存在，请新建一个）。
    c. **编辑该文件，替换 `SECRET_KEY` 为一个您自己生成的随机密钥**（可在本地命令行使用 `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` 生成），并**保留**其他数据库配置信息。

    ```env
    # .env

    # Django SECRET_KEY (请替换为您自己生成的安全密钥！)
    SECRET_KEY=您的随机生成的密钥

    # 数据库配置，保持不变
    DB_NAME=dominitrack_db
    DB_USER=dominitrack_user
    DB_PASSWORD=dominitrack_password
    DB_HOST=db
    DB_PORT=5432

    # Celery 配置
    CELERY_BROKER_URL=redis://redis:6379/0
    CELERY_RESULT_BACKEND=redis://redis:6379/0
    ```

3.  **使用宝塔 Docker 管理器启动服务：**
    a. 在宝塔面板左侧菜单选择 **“Docker”** -> **“Docker 管理器”**。
    b. 点击 **“Compose 管理”** 标签页。
    c. 点击右侧的 **“添加 Compose”**。
    d. **项目名称：** 填写 `DominiTrack` (或您的项目目录名)。
    e. **Compose YML文件路径：** 点击“选择”，导航到您刚才解压的 `DominiTrack` 目录，选择里面的 `docker-compose.yml` 文件。
    f. **勾选 “开启”**。
    g. 点击 **“提交”**。
    h. 宝塔将开始拉取 Docker 镜像、构建项目并启动所有服务。这个过程可能需要几分钟甚至更长时间（取决于您的服务器网络）。您可以在 **“日志”** 选项卡中查看启动进度。

4.  **初始化数据库 (首次部署重要！)：**
    项目启动后，您需要对 Django 数据库进行初始化。
    a. 在宝塔面板左侧菜单选择 **“Docker”** -> **“Docker 管理器”**。
    b. 在 **“容器列表”** 中找到名为 `dominitrack_backend_1` (或类似 `项目名_backend_1`) 的容器。
    c. 点击该容器右侧的 **“终端”** 按钮。
    d. 在容器终端中，依次执行以下命令：
        * **运行数据库迁移：**
          ```bash
          python manage.py migrate
          ```
        * **创建 Django 超级管理员账户：**
          ```bash
          python manage.py createsuperuser
          ```
          按照提示输入用户名、邮箱和密码。这是您将来登录后端管理后台的账号。

5.  **配置 Nginx 反向代理 (通过域名访问)：**
    为了通过域名访问您的 DominiTrack，您需要设置反向代理。
    a. 确保您已经有一个域名解析到了您的服务器 IP 地址（例如 `dominitrack.yourdomain.com`）。
    b. 在宝塔面板左侧菜单选择 **“网站”** -> **“添加站点”**。
    c. **域名：** 填写您的前端域名（例如 `dominitrack.yourdomain.com`）。
    d. **根目录：** 随意选择一个空目录，因为 Docker 容器会处理内容。
    e. **PHP版本：** 选择“纯静态”或任意版本，不重要。
    f. 点击 **“提交”**。
    g. 站点创建成功后，点击该网站右侧的 **“设置”**。
    h. 选择 **“反向代理”** 选项卡。
    i. **启用反向代理。**
    j. **代理名称：** `dominitrack_frontend_proxy`。
    k. **目标URL：** `http://127.0.0.1:8080` (注意这里是 `127.0.0.1`，因为 Nginx 和 Docker 容器都在同一台服务器上)。
    l. **发送域名：** `localhost`。
    m. **勾选 “发送真实IP”**。
    n. 点击 **“保存”**。

    o. **配置后端 API 代理：**
    再次点击刚才设置的网站（例如 `dominitrack.yourdomain.com`）右侧的 **“设置”**。
    p. 选择 **“配置文件”** 选项卡。
    q. 找到 `location /` 块的上方，添加一个新的 `location` 块用于代理 `/api/` 请求到后端：

    ```nginx
    # 在 location / { ... } 块的上方添加
    location /api/ {
        proxy_pass [http://127.0.0.1:8000](http://127.0.0.1:8000); # 代理到后端 Django 服务的端口
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    ```
    r. 点击 **“保存”**。

6.  **开启 Celery 后台任务（可选）：**
    为了让 WHOIS 查询和提醒功能自动运行，您需要在服务器上单独启动 Celery Worker 和 Celery Beat。
    这通常需要通过 SSH 连接到服务器，进入项目目录，然后运行：
    ```bash
    # 进入项目目录 (例如 /www/wwwroot/DominiTrack)
    cd /www/wwwroot/DominiTrack

    # (可选) 如果你还没有激活虚拟环境，或者想在宿主机运行
    # source venv/bin/activate

    # 启动 Celery Worker
    # 注意: 你需要确保 celery 和 redis 已经安装在你的虚拟环境 (或宿主机) 中
    # 或者通过 Docker Compose 启动 Celery 服务 (更推荐的做法，未来会完善 docker-compose.yml)
    # python -m celery -A dominitrack_project worker -l info
    
    # 启动 Celery Beat (用于定时任务)
    # python -m celery -A dominitrack_project beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
    ```
    **注意：** 目前提供的 `docker-compose.yml` 还没有包含 Celery Worker 和 Beat 服务。这将在未来完善。在 Docker Compose 中添加这两个服务后，它们会随 `docker compose up` 自动启动。

---

## 📋 TODO & 未来计划
我们对 DominiTrack 的未来充满了期待：

* 用户认证系统完善： 实现完整的用户注册、登录、密码找回流程。

* 前端界面开发： 完成域名列表展示、添加/编辑域名表单、用户设置等核心页面。

* WHOIS 定时更新： 使用 Celery Beat 定时触发 WHOIS 查询，自动更新域名到期日期。

* 多渠道提醒集成： 实现邮件、微信、Telegram 的自动化提醒功能。

* 国际化 (i18n)： 支持多语言。

* SSL 证书监控： 跟踪 SSL 证书的到期日期并提供提醒。

* DNS 记录监控： 监测域名 DNS 记录的变更。

* Uptime 监控： 简单的网站可用性监测。

* 更强大的数据分析和报告。

## 🤝 如何贡献
我们欢迎所有对域名管理感兴趣的开发者加入 DominiTrack 的开发！无论您是想提交 Bug 报告、提出功能建议，还是贡献代码，都非常感谢。

1. Fork 仓库。

2. 创建您的功能分支 (git checkout -b feature/AmazingFeature)。

3. 提交您的更改 (git commit -m 'feat: Add AmazingFeature')。

4. 推送到您的分支 (git push origin feature/AmazingFeature)。

5. 提交 Pull Request。

请确保您的代码风格符合项目规范，并为新功能编写测试。

## 📜 许可证
本项目采用 MIT 许可证开源。详情请参阅 LICENSE 文件。

## 📧 联系我们
如果您有任何问题或建议，欢迎通过 GitHub Issues 提出。

感谢您对 DominiTrack 的支持！我们共同打造一个更便捷的域名管理世界！
