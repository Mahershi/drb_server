from rest_framework import serializers
from ..models import ProductMetaModel
from .brand_serializer import BrandSerializer
from .category_serializer import CategorySerializer
from .discount_serializer import DiscountSerializer
from .unit_serializer import UnitsSerializer


class ProductMetaSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False)
    category = CategorySerializer(many=False)
    discount = DiscountSerializer(many=True)
    nic_unit = UnitsSerializer(many=False)
    size_unit = UnitsSerializer(many=False)

    class Meta:
        model = ProductMetaModel
        fields = '__all__'