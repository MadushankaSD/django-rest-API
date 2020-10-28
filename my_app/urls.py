from django.urls import path
from .views import item_list , item_detali

urlpatterns = [
    path('items/', item_list),
    path('items/detail/<int:pk>', item_detali),
]
