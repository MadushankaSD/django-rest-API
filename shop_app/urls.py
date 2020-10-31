from django.urls import path
from shop_app.controllers.item_controller import item_list , item_detali
# from shop_app.controllers.customer_controller import
# from shop_app.controllers.order_contoller import
# from shop_app.controllers.order_detail_controller import

urlpatterns = [
    path('items/', item_list),
    path('items/detail/<int:pk>', item_detali),
    # path('order',)
]
