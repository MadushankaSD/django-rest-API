from rest_framework import serializers
from shop_app.entity.order_detail import Order_detail


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_detail
        fields = "__all__"
