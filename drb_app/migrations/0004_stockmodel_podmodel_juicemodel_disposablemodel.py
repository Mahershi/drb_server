# Generated by Django 4.1 on 2022-08-29 21:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("drb_app", "0003_productmetamodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="StockModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stock", models.IntegerField(default=0)),
                (
                    "store",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="drb_app.storemodel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PodModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("flavour", models.CharField(max_length=30)),
                ("description", models.CharField(max_length=100)),
                ("empty", models.BooleanField(default=False)),
                ("date_created", models.DateField(default=datetime.date(2022, 8, 29))),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="drb_app.productmetamodel",
                    ),
                ),
                (
                    "stock",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="drb_app.stockmodel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JuiceModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("flavour", models.CharField(max_length=30)),
                ("description", models.CharField(max_length=100)),
                ("date_created", models.DateField(default=datetime.date(2022, 8, 29))),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="drb_app.productmetamodel",
                    ),
                ),
                (
                    "stock",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="drb_app.stockmodel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DisposableModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("flavour", models.CharField(max_length=30)),
                ("description", models.CharField(max_length=100)),
                ("date_created", models.DateField(default=datetime.date(2022, 8, 29))),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="drb_app.productmetamodel",
                    ),
                ),
                (
                    "stock",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="drb_app.stockmodel",
                    ),
                ),
            ],
        ),
    ]
