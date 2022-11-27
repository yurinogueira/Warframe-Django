from decimal import Decimal

from django.db import models
from django.utils import timezone

from core.models import Image


class SellItem(models.Model):
    item_type = models.ForeignKey(
        "category.Category",
        related_name="items",
        on_delete=models.CASCADE
    )
    name = models.CharField("Nome", max_length=64, db_index=True, unique=True)
    description = models.CharField("Desrição", max_length=256)
    slug = models.SlugField(max_length=64)
    stock = models.IntegerField(default=0)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=16, decimal_places=2, default=Decimal("0.0"))
    is_available = models.BooleanField(default=False)
    created_at = models.DateTimeField("Criado em", default=timezone.localtime)

    @property
    def available(self):
        return "Sim" if self.is_available else "Não"

    class Meta:
        ordering = ("name",)
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self) -> str:
        return str(self.name)
