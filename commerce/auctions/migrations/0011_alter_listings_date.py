# Generated by Django 4.1.3 on 2022-11-25 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0010_alter_listings_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listings",
            name="date",
            field=models.DateField(),
        ),
    ]
