from django.db.models import signals
from django.dispatch import receiver
from django.utils.text import slugify

from market.models import SellItem


@receiver(signals.pre_save, sender=SellItem)
def populate_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.brand_name)
