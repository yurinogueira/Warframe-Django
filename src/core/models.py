from django.db import models

from core.behaviors import Orderable
from core.choices import WARFRAME_TYPE, COMMON, ITEM_TYPE, HOME_ITEM


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


class Badge(Orderable):
    name = models.CharField("Nome", max_length=32)
    css_class = models.CharField("Classe do CSS", max_length=64)

    @property
    def css_classes(self):
        return f"badge {self.css_class}"

    class Meta:
        ordering = ("position",)
        verbose_name = "Badge"
        verbose_name_plural = "Badges"

    def __str__(self) -> str:
        return str(self.name)


class Report(Orderable):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    title = models.CharField("Título", max_length=128)
    published_in = models.CharField("Publicação", max_length=64)
    message = models.TextField("Mensagem")
    badges = models.ManyToManyField(Badge)

    class Meta:
        ordering = ("position",)
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"

    def __str__(self) -> str:
        return str(self.title)


class ListItem(Orderable):
    title = models.CharField("Título", max_length=128, null=True, blank=True)
    sub_title = models.CharField("Título", max_length=128, null=True, blank=True)
    published_in = models.CharField("Publicação", max_length=64, null=True, blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
    item_type = models.CharField(
        max_length=8,
        choices=ITEM_TYPE,
        default=HOME_ITEM,
        verbose_name="Tipo de Item",
    )

    class Meta:
        ordering = ("position",)
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self) -> str:
        return str(self.title)

