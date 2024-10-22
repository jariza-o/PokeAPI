from django.contrib import admin
from custom_auth.models import Custom_User
"""
Use:
    Register the User and Message Models for the Admin Panel
"""
@admin.register(Custom_User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'password']