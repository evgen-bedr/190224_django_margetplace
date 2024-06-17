from rest_framework import serializers
from marketplace.models import Order
from marketplace.serializers.customer_serializer import CustomerSerializer


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('order_date',)


class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('order_date',)
