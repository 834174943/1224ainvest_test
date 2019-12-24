from django.db import models

class books1(models.Model):
    name = models.CharField(max_length=20, null=False)
    author = models.CharField(max_length=20, null=False)
    price = models.FloatField()
