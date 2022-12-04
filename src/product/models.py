from decimal import Decimal

from django.db import models


class Product(models.Model):
    item_type = models.ForeignKey(
        "category.Category",
        related_name="products",
        on_delete=models.CASCADE
    )
    name = models.CharField("Nome", max_length=64, db_index=True, unique=True)
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=16, decimal_places=2, default=Decimal("0.0"))
    partial_price = models.DecimalField(max_digits=16, decimal_places=2, default=Decimal("0.0"))

    class Meta:
        ordering = ("name",)
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self) -> str:
        return str(self.name)
