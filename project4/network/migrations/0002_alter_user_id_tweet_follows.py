# Generated by Django 4.1.3 on 2022-12-18 00:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name="tweet",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("tweet", models.TextField(max_length=140)),
                ("time", models.DateTimeField(auto_now_add=True)),
                ("likes", models.IntegerField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="follows",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "followers",
                    models.ManyToManyField(
                        related_name="following", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "following",
                    models.ManyToManyField(
                        related_name="followers", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
