# Generated by Django 4.1 on 2022-09-03 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("drb_app", "0008_podstockmodel_juicestockmodel"),
    ]

    operations = [
        migrations.RenameField(
            model_name="juicestockmodel", old_name="disposable", new_name="juice",
        ),
        migrations.RenameField(
            model_name="podstockmodel", old_name="disposable", new_name="pod",
        ),
    ]
