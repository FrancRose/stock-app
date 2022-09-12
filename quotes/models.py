
from django.db import models

# Create your models here.

class Stock(models.Model):
    stonks = models.CharField(max_length=10)

    def __str__(self):
        return self.stonks

class  Trade(models.Model):
    symbol = models.CharField('Symbol', max_length=10)
    qty = models.CharField('Quantity', max_length=10000 )

    def __str__(self):
        return self.symbol