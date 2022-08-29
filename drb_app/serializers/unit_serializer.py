from rest_framework import serializers
from ..models import UnitsModel


class UnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitsModel
        fields = '__all__'