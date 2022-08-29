from rest_framework import serializers
from ..models import DiscountModel


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountModel
        fields = '__all__'
