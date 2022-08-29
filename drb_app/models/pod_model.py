from django.db import models
import datetime


class PodModel(models.Model):
    product = models.ForeignKey('ProductMetaModel', on_delete=models.SET_NULL, null=True)
    flavour = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    empty = models.BooleanField(default=False)
    stock = models.ForeignKey('StockModel', on_delete=models.SET_NULL, null=True)
    date_created = models.DateField(default=datetime.date.today())
