from django.db import models
import datetime


class CategoryModel(models.Model):
    category = models.CharField(max_length=20, null=False, blank=False)
    date_created = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.category