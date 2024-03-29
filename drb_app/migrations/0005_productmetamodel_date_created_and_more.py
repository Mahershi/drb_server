# Generated by Django 4.1 on 2022-08-30 19:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drb_app", "0004_stockmodel_podmodel_juicemodel_disposablemodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="productmetamodel",
            name="date_created",
            field=models.DateField(default=datetime.date(2022, 8, 30)),
        ),
        migrations.AlterField(
            model_name="brandmodel",
            name="date_created",
            field=models.DateField(default=datetime.date(2022, 8, 30)),
        ),
        migrations.AlterField(
            model_name="categorymodel",
            name="date_created",
            field=models.DateField(default=datetime.date(2022, 8, 30)),
        ),
        migrations.AlterField(
            model_name="disposablemodel",
            name="date_created",
            field=models.DateField(default=datetime.date(2022, 8, 30)),
        ),
        migrations.AlterField(
            model_name="juicemodel",
            name="date_created",
            field=models.DateField(default=datetime.date(2022, 8, 30)),
        ),
        migrations.AlterField(
            model_name="podmodel",
            name="date_created",
            field=models.DateField(default=datetime.date(2022, 8, 30)),
        ),
        migrations.AlterField(
            model_name="productmetamodel",
            name="discount",
            field=models.ManyToManyField(
                blank=True, related_name="has_discounts", to="drb_app.discountmodel"
            ),
        ),
        migrations.AlterField(
            model_name="storemodel",
            name="date_created",
            field=models.DateField(default=datetime.date(2022, 8, 30)),
        ),
    ]
