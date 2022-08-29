from django.db import models
import datetime


class BrandModel(models.Model):
    brand = models.CharField(max_length=30, null=False, blank=True)
    date_created = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.brand