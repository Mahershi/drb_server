from django.db import models


class StockModel(models.Model):
    store = models.ForeignKey('StoreModel', on_delete=models.SET_NULL, null=True)
    stock = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return self.store.__str__() + ' ' + str(self.stock)