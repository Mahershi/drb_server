# Generated by Django 4.1 on 2022-09-08 23:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drb_app", "0013_ordermodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ordermodel",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 9, 8, 23, 35, 38, 182464, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
