from django.dispatch import receiver
from django.db.models import signals
from django.utils.text import slugify

from product.models import Product


@receiver(signals.pre_save, sender=Product)
def populate_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.brand_name)
