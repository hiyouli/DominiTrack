# domains/admin.py

from django.contrib import admin
from .models import Domain

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'owner', 'expiration_date', 'days_until_expiration',
        'status', 'auto_lookup_enabled', 'last_lookup_date', 'created_at'
    )
    list_filter = ('owner', 'auto_lookup_enabled', 'expiration_date')
    search_fields = ('name', 'notes')
    date_hierarchy = 'expiration_date'
    ordering = ('expiration_date',)
    readonly_fields = ('created_at', 'updated_at', 'last_lookup_date') # 这些字段在后台只读