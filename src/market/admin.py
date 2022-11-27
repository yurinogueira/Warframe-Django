from django.contrib.admin import register, ModelAdmin

from market.models import SellItem


@register(SellItem)
class SellItemAdmin(ModelAdmin):
    list_per_page = 30
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    list_select_related = ("item_type", "image")
    list_display = (
        "name",
        "item_type",
        "price",
    )
