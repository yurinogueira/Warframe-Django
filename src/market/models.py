from django.db import models

from category.models import Category
from core.models import Image


class SellItem(models.Model):
    item_type = models.ForeignKey(
        Category,
        related_name="items",
        on_delete=models.CASCADE
    )
    name = models.CharField("Nome", max_length=64, db_index=True)
    description = models.CharField("Desrição", max_length=256)
    slug = models.SlugField(max_length=64)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self) -> str:
        return str(self.name)
