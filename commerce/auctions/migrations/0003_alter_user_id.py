# Generated by Django 4.1.3 on 2022-11-24 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "auctions",
            "0002_user_creditcard_alter_user_email_alter_user_password_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]