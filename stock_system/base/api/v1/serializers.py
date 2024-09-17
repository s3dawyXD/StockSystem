from rest_framework import serializers
from ...models import Order, OrderData, Product


class OrderDataSerializer(serializers.Serializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source="product"
    )
    quantity = serializers.IntegerField()

    def to_representation(self, instance):
        respresentation = super().to_representation(instance)
        respresentation["product"] = instance.product.name
        return respresentation


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderProductsSerializer(serializers.Serializer):
    products = OrderDataSerializer(many=True, required=True, allow_empty=False)

    def create(self, validated_data):
        products = validated_data.get("products", [])
        order_obj = (
            Order.objects.create()
        )  # in future we can add extra info about order (created_by, brach, etc.)
        for od in products:
            OrderData.objects.create(**od, order=order_obj)
        return OrderSerializer(order_obj).data


class ListOrderSerializer(serializers.ModelSerializer):
    order_data = OrderDataSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ("id", "created_at", "order_data")
