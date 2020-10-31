from django.contrib import admin
from shop_app.entity.order_detail import OrderDetail
from shop_app.entity.order import Order
from shop_app.entity.customer import Customer
from shop_app.entity.item import Item
# Register your models here.

admin.site.register(Item)
admin.site.register(OrderDetail)
admin.site.register(Order)
admin.site.register(Customer)

