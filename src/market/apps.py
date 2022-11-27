from django.apps import AppConfig
from django.db.models.signals import pre_save


class MarketConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "market"

    def ready(self):
        from .models import SellItem
        from .receivers import (
            populate_slug
        )

        pre_save.connect(populate_slug, sender=SellItem)
