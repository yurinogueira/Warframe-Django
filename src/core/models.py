from django.db import models

from core.behaviors import Orderable
from core.choices import WARFRAME_TYPE, COMMON


class Image(models.Model):
    name = models.CharField("Nome", max_length=128)
    path = models.CharField("Caminho", max_length=256)

    class Meta:
        ordering = ("name",)
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens"

    def __str__(self) -> str:
        return str(self.name)


class Warframe(Orderable):
    name = models.CharField("Nome", max_length=128)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    warframe_type = models.CharField(
        max_length=8,
        choices=WARFRAME_TYPE,
        default=COMMON,
        verbose_name="Tipo de Warframe",
    )

    class Meta:
        ordering = ("position",)
        verbose_name = "Warframe"
        verbose_name_plural = "Warframes"

    def __str__(self) -> str:
        return str(self.name)
