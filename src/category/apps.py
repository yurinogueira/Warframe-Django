from django.apps import AppConfig
from django.db.models.signals import pre_save


class CategoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "category"

    def ready(self):
        from .models import Category
        from .receivers import (
            populate_slug
        )

        pre_save.connect(populate_slug, sender=Category)
