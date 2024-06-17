from rest_framework import serializers

from marketplace.models import Product
from marketplace.serializers.suppliers import SupplierSerializer
from marketplace.serializers.category_serializer import CategorySerializer


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
