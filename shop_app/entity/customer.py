from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    telephone = models.IntegerField()
    email = models.EmailField(max_length=50, null=True)
