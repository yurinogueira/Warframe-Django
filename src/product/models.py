from decimal import Decimal

from django.db import models


class Product(models.Model):
    category = models.ForeignKey("category.Category", on_delete=models.DO_NOTHING)
    image = models.ForeignKey("core.Image", on_delete=models.CASCADE)
    name = models.CharField(max_length=128, db_index=True, unique=True)
    slug = models.SlugField(max_length=128)

    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=16, decimal_places=2, default=Decimal("0.0"))
    is_available = models.BooleanField(default=False)

    class Meta:
        ordering = ("name",)
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.name
