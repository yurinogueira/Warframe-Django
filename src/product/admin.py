from django.contrib.admin import register, ModelAdmin

from product.models import Product


@register(Product)
class ProductAdmin(ModelAdmin):
    list_per_page = 30
    search_fields = ("name",)
    list_select_related = ("item_type",)
    list_display = (
        "name",
        "item_type",
        "price",
    )
