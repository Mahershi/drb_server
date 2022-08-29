from rest_framework import serializers
from ..models import ParametersModels


class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParametersModels
        fields = '__all__'
