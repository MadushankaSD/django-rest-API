from rest_framework import serializers
from shop_app.entity.item import Item


# (1) Another way to do same task below
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        # fields = ['id', 'name', 'description', 'qty']
        fields = "__all__"

# (2) This is a one way to do Serialize
# class ItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField(primary_key=True)
#     name = serializers.CharField(max_length=100)
#     description = serializers.CharField(max_length=500)
#     qty = serializers.IntegerField()
#     date = serializers.DateTimeField(auto_now_add=True)
#
#     def create(self, validated_data):
#         return Item.objects.create(validated_data)
#
#     def update(self, instance, validated_data):
#         instance.id = validated_data.get('id', instance.id)
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.qty = validated_data.get('qty', instance.qty)
#         instance.date = validated_data.get('date', instance.date)
#         return instance
