from django.db import models


class DiscountModel(models.Model):
    discount_price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    discount_qty = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return str(self.discount_qty) + ' for ' + str(self.discount_price)