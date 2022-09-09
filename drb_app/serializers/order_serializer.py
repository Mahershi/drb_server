from ..models import OrderModel
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = OrderModel