# coding: utf-8

from django.contrib.admin import register, ModelAdmin

from core.models import Badge, Image, ListItem, Report, Warframe


@register(Image)
class ImageAdmin(ModelAdmin):
    list_per_page = 30
    search_fields = ("name",)
    list_display = (
        "name",
        "path",
    )


@register(Warframe)
class WarframeAdmin(ModelAdmin):
    list_per_page = 30
    search_fields = ("name",)
    list_display = (
        "name",
        "warframe_type",
    )


@register(Badge)
class BadgeAdmin(ModelAdmin):
    list_per_page = 30
    search_fields = ("name",)
    list_display = ("name",)


@register(Report)
class ReportAdmin(ModelAdmin):
    list_per_page = 30
    search_fields = ("title",)
    list_display = (
        "title",
        "published_in"
    )


@register(ListItem)
class ListItemAdmin(ModelAdmin):
    list_per_page = 30
    search_fields = ("title",)
    list_display = (
        "title",
        "sub_title",
        "item_type",
        "published_in"
    )
