from django.db import models

class TestModel(models.Model):
    data = models.CharField(max_length=20)