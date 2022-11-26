from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, db_index=True, unique=True)
    slug = models.SlugField(max_length=64)
    is_prime = models.BooleanField(default=False)

    @property
    def prime(self):
        return "Sim" if self.is_prime else "Não"

    class Meta:
        ordering = ("name",)
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name
