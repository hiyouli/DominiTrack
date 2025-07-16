# domains/models.py

from django.db import models
from django.contrib.auth.models import User # 引入Django的User模型
from django.utils import timezone

class Domain(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='domains', verbose_name="所有者")
    name = models.CharField(max_length=255, unique=True, verbose_name="域名")
    registration_date = models.DateField(null=True, blank=True, verbose_name="注册日期")
    expiration_date = models.DateField(verbose_name="到期日期")
    auto_lookup_enabled = models.BooleanField(default=True, verbose_name="启用WHOIS自动查询")
    last_lookup_date = models.DateTimeField(null=True, blank=True, verbose_name="最后查询日期")
    notes = models.TextField(blank=True, verbose_name="备注")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def days_until_expiration(self):
        """计算距离到期还剩多少天"""
        today = timezone.now().date()
        remaining_days = (self.expiration_date - today).days
        return remaining_days

    @property
    def status(self):
        """根据到期日期返回域名状态"""
        days = self.days_until_expiration()
        if days < 0:
            return "已过期"
        elif days <= 30: # 假设30天内视为即将到期
            return "即将到期"
        else:
            return "正常"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "域名"
        verbose_name_plural = "域名"
        ordering = ['expiration_date'] # 默认按到期日期排序