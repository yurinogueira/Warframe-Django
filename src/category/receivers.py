from django.dispatch import receiver
from django.db.models import signals
from django.utils.text import slugify

from category.models import Category


@receiver(signals.pre_save, sender=Category)
def populate_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.brand_name)
