# coding: utf-8

from django.contrib.admin import register, ModelAdmin

from core.models import Image


@register(Image)
class ImageAdmin(ModelAdmin):
    list_per_page = 30
    search_fields = ("name",)
    list_display = (
        "name",
        "path",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )