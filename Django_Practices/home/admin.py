from django.contrib import admin
from .models import User


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'phone', 'city', 'created_at', 'is_active']
    search_fields = ['full_name', 'email']
    list_filter = ['city']
