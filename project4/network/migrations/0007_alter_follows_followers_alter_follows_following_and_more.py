# Generated by Django 4.1.3 on 2022-12-19 23:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0006_follows_following"),
    ]

    operations = [
        migrations.AlterField(
            model_name="follows",
            name="followers",
            field=models.ManyToManyField(
                default=None, related_name="follower", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="follows",
            name="following",
            field=models.ManyToManyField(
                default=None, related_name="isfollowing", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.RemoveField(
            model_name="tweet",
            name="likes",
        ),
        migrations.AddField(
            model_name="tweet",
            name="likes",
            field=models.ManyToManyField(
                default=None, related_name="likers", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
