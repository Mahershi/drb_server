from django.db import models
import datetime

class StoreModel(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=True)
    date_created = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.name