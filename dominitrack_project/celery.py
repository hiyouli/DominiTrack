# dominitrack_project/celery.py

import os
from celery import Celery

# 设置 Django 的 settings 模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dominitrack_project.settings')

# 创建 Celery 应用实例
app = Celery('dominitrack_project')

# 从 Django 的 settings 文件中加载配置（以 'CELERY_' 开头的配置）
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动发现 Django 应用中的 tasks.py 文件
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')