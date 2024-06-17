from rest_framework import serializers
from marketplace.models.product import ProductDetail
from marketplace.serializers.product_serializer import ProductDetailSerializer


class ProductDetailInfoSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer()

    class Meta:
        model = ProductDetail
        fields = '__all__'


class ProductDetailCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'
