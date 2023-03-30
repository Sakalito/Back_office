# Generated by Django 4.1.7 on 2023-03-29 14:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="stockmoveitemmodel",
            name="quantity",
        ),
        migrations.AddField(
            model_name="stockmoveitemmodel",
            name="amount",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="stockmovemodel",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2023, 3, 29, 16, 1, 48, 132399)
            ),
        ),
    ]