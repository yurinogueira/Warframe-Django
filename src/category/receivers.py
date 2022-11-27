from django.utils.text import slugify


def populate_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)
