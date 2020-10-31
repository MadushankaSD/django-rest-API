from django.db import models
from shop_app.entity.order import Order
from shop_app.entity.item import Item


class OrderDetail(models.Model):
    order_id = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    item_id = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
    qty = models.IntegerField()
