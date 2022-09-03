# Generated by Django 4.1 on 2022-09-03 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drb_app", "0010_alter_disposablemodel_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="disposablemodel",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images"),
        ),
        migrations.AddField(
            model_name="juicemodel",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images"),
        ),
        migrations.AddField(
            model_name="podmodel",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images"),
        ),
    ]