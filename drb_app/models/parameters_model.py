from django.db import models


class ParametersModels(models.Model):
    parameter = models.CharField(max_length=20, null=False, blank=False)
    value = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.parameter