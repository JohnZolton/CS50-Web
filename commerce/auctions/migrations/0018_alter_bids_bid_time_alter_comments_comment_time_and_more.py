# Generated by Django 4.1.3 on 2022-11-27 00:07

import datetime
from django.db import migrations, models
from django import utils


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0017_alter_bids_bid_time_alter_bids_id_and_more"),
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
            model_name="comments",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="listings",
            name="date",
            field=models.DateField(
                default=utils.timezone.now
            ),
        ),
    ]