# Generated by Django 4.1.3 on 2022-12-18 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0002_alter_user_id_tweet_follows"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tweet",
            options={"ordering": ["-time"]},
        ),
        migrations.AlterField(
            model_name="tweet",
            name="likes",
            field=models.IntegerField(default=0),
        ),
    ]
