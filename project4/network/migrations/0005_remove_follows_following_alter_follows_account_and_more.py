# Generated by Django 4.1.3 on 2022-12-18 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0004_alter_follows_followers_alter_follows_following"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="follows",
            name="following",
        ),
        migrations.AlterField(
            model_name="follows",
            name="account",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="follows",
            name="followers",
            field=models.ManyToManyField(
                default=0, related_name="follower", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
