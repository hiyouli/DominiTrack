# dominitrack_project/Dockerfile

# 使用 Python 官方镜像作为基础
FROM python:3.9-slim-buster

# 设置工作目录
WORKDIR /app

# 禁用 pip 缓存，加快构建速度
ENV PIP_NO_CACHE_DIR 1

# 复制 requirements.txt 到工作目录，并安装依赖
# 注意：此时我们还没有 requirements.txt，但先留着，后续我们会生成
COPY requirements.txt /app/
RUN pip install -r requirements.txt --no-warn-script-location

# 复制整个 Django 项目到容器的 /app 目录
COPY . /app/

# 暴露端口
EXPOSE 8000

# 默认启动命令（会被 docker-compose.yml 中的 command 覆盖）
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]