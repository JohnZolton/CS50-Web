# Generated by Django 4.1.3 on 2022-11-25 01:29

import datetime
from django.db import migrations, models
from django import utils

class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0012_alter_bids_bid_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bids",
            name="bid_time",
            field=models.TimeField(
                default=utils.timezone.now
            ),
        ),
        migrations.AlterField(
            model_name="comments",
            name="comment_time",
            field=models.TimeField(
                default=utils.timezone.now
            ),
        ),
        migrations.AlterField(
            model_name="listings",
            name="date",
            field=models.DateField(
                default=utils.timezone.now
            ),
        ),
    ]
