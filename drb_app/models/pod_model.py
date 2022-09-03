from django.db import models
import datetime


class PodModel(models.Model):
    product = models.ForeignKey('ProductMetaModel', on_delete=models.SET_NULL, null=True)
    flavour = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)
    empty = models.BooleanField(default=False)
    # stock = models.ForeignKey('StockModel', on_delete=models.SET_NULL, null=True)
    date_created = models.DateField(default=datetime.date.today())

    image = models.ImageField(upload_to='images', null=True, blank=True)


    def __str__(self):
        return self.product.__str__() + ": " + self.flavour
