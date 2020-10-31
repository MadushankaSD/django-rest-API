from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    unit_price = models.FloatField()
    qty = models.IntegerField()

    def __str__(self):
        return self.description