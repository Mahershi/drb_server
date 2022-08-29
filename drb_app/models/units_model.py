from django.db import models


class UnitsModel(models.Model):
    unit_label = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.unit_label