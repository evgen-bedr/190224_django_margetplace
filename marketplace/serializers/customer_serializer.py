import re

from rest_framework import serializers

from marketplace.models import Customer
from marketplace.serializers.address_serializers import AddressSerializer
from marketplace.models import Address


class CustomerSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    deleted = serializers.BooleanField(read_only=True)
    deleted_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
        # read_only_fields = ['date_joined', 'deleted', 'deleted_at']


class CustomerCreateUpdateSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(read_only=True)
    deleted = serializers.BooleanField(read_only=True)
    deleted_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
        # exclude = ['date_joined', 'deleted', 'deleted_at']

    def validate_phone_number(self, value):
        if not re.match(r"^\d{10,15}$", value):
            return serializers.ValidationError(
                "The phone must contains only digits. The length must be between 10 and 15"
            )

        return value
