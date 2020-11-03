from shop_app.entity.order_detail import OrderDetail
from shop_app.serializers.order_detail_serializer import OrderDetailSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def order_detail_list(request):
    if request.method == 'GET':
        try:
            orders = OrderDetail.objects.all()
        except:
            pass
        serializer = OrderDetailSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def order_detail_detail(request, pk):
    try:
        orders = OrderDetail.objects.get(pk=pk)
    except OrderDetail.DoseNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderDetailSerializer(orders)
        return Response(serializer.data, status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = OrderDetailSerializer(orders, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        orders.delete()
        return Response(status.HTTP_204_NO_CONTENT)
