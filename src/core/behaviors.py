from django.db import models


class Orderable(models.Model):
    position = models.PositiveSmallIntegerField("Posição", default=0)

    class Meta:
        abstract = True
