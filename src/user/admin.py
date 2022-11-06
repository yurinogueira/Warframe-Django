from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user.models import User


@register(User)
class UserAdmin(BaseUserAdmin):
    list_per_page = 30
    search_fields = ("email",)
    list_display = (
        "email",
        "first_name",
        "date_joined",
        "last_login",
    )
    readonly_fields = (
        "last_login",
        "date_joined",
    )
