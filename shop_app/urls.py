from django.urls import path
from shop_app.controllers.item_controller import item_list, item_detali
from shop_app.controllers.customer_controller import customer_list, customer_detail
from shop_app.controllers.order_contoller import order_list,order_detail
from shop_app.controllers.order_detail_controller import order_detail_detail , order_detail_list

# from shop_app.controllers.order_contoller import
# from shop_app.controllers.order_detail_controller import

urlpatterns = [
    path('items/', item_list),
    path('items/detail/<int:pk>', item_detali),
    path('customer/', customer_list),
    path('customer/<int:pk>', customer_detail),
    path('order/', order_list),
    path('order/<int:pk>', order_detail),
    path('orderdetail/', order_detail_list),
    path('orderdetail/<int:pk>', order_detail_detail)
]
