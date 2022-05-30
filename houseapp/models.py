from django.db import models

# Create your models here.
class HouseData(models.Model):
    CRIM = models.PositiveIntegerField()
    INDUS = models.PositiveIntegerField()
    NOX = models.PositiveIntegerField()
    DIS = models.PositiveIntegerField()
    RAD = models.PositiveIntegerField()
    TAX = models.PositiveIntegerField()
    B = models.PositiveIntegerField()
    