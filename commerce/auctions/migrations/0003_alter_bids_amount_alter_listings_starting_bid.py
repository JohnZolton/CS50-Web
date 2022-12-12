# Generated by Django 4.1.3 on 2022-12-09 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0002_watchlist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bids",
            name="amount",
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name="listings",
            name="Starting_bid",
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
