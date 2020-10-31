from django.db import models
from shop_app.entity.customer import Customer


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
