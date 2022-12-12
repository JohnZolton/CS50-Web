# Generated by Django 4.1.3 on 2022-12-10 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0008_alter_listings_winner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listings",
            name="Winner",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Winner",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
