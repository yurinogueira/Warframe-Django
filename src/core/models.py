from django.db import models

from core.behaviors import Timestampable


class Image(Timestampable):
    name = models.CharField("Nome", max_length=128)
    path = models.CharField("Caminho", max_length=256)

    class Meta:
        ordering = ("name",)
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens"

    def __str__(self) -> str:
        return str(self.name)
