# domains/serializers.py

from rest_framework import serializers
from .models import Domain

class DomainSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username') # 添加所有者用户名（只读）
    days_until_expiration = serializers.ReadOnlyField() # 添加到期剩余天数（只读）
    status = serializers.ReadOnlyField() # 添加状态（只读）

    class Meta:
        model = Domain
        fields = [
            'id', 'owner', 'owner_username', 'name', 'registration_date',
            'expiration_date', 'auto_lookup_enabled', 'last_lookup_date',
            'notes', 'created_at', 'updated_at', 'days_until_expiration', 'status'
        ]
        read_only_fields = ['owner', 'last_lookup_date', 'created_at', 'updated_at'] # 这些字段只读