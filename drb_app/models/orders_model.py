from django.db import models
import datetime
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField


class OrderModel(models.Model):
    product = models.ForeignKey('ProductMetaModel', on_delete=models.SET_NULL, null=True, blank=False)
    flavour = ArrayField(models.CharField(null=False, blank=False, max_length=10))
    store = models.ForeignKey('StoreModel', on_delete=models.SET_NULL, null=True, blank=False)
    flav_count = ArrayField(models.IntegerField(null=True))
    subtotal = models.DecimalField(decimal_places=2, max_digits=6, default=0.0)
    tax = models.DecimalField(decimal_places=2, max_digits=6, default=0.0)
    total = models.DecimalField(decimal_places=2, max_digits=6, default=0.0)
    qty = models.IntegerField(default=0)

    date_created = models.DateTimeField(default=datetime.datetime.now(tz=timezone.utc))
