# Generated by Django 4.1.3 on 2022-11-29 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0021_rename_item_listings_title_listings_category_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="listings",
            old_name="duration",
            new_name="Duration",
        ),
        migrations.RenameField(
            model_name="listings",
            old_name="seller",
            new_name="Seller",
        ),
    ]