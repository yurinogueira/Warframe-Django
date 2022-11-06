# Generated by Django 4.1.2 on 2022-11-06 00:48

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0003_listitem"),
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=128, unique=True)),
                ("slug", models.SlugField(max_length=128)),
                ("stock", models.IntegerField(default=0)),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=Decimal("0.0"), max_digits=16
                    ),
                ),
                ("is_available", models.BooleanField(default=False)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="category.category",
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.image"
                    ),
                ),
            ],
            options={
                "verbose_name": "Produto",
                "verbose_name_plural": "Produtos",
                "ordering": ("name",),
            },
        ),
    ]