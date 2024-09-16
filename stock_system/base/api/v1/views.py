from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

from .serializers import OrderProductsSerializer, ListOrderSerializer
from base.models import Order


class OrderViewset(viewsets.ViewSet):
    authentication_classes = []  # disable authentication
    permission_classes = [permissions.AllowAny]  # disable permission
    serializer_class = OrderProductsSerializer

    def create(self, request, *args, **kwargs):
        serializer = OrderProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(
            {"status": "success", "data": data}, status=status.HTTP_201_CREATED
        )

    def list(self, request, *args, **kwargs):
        queryset = Order.objects.all()
        serializer = ListOrderSerializer(queryset, many=True)
        return Response({"status": "success", "data": serializer.data})
