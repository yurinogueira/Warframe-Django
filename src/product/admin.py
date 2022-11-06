from django.contrib.admin import register, ModelAdmin

from product.models import Product


@register(Product)
class ProductAdmin(ModelAdmin):
    list_per_page = 30
    list_select_related = ("category",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        "name",
        "category",
        "stock",
        "price",
    )
