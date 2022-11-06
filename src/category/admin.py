from django.contrib.admin import register, ModelAdmin

from category.models import Category


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_per_page = 30
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        "name",
        "is_prime",
    )
