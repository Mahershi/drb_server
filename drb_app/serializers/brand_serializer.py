from rest_framework import serializers
from ..models import BrandModel


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields =  '__all__'

