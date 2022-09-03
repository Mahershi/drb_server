from rest_framework import serializers
from ..models import JuiceModel, JuiceStockModel
from rest_framework.request import Request
from django.http import QueryDict


class JuiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = JuiceModel
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        req: Request = self.context.get('request')
        qp: QueryDict = req.query_params

        if qp.get('store') is not None:
            store = qp.get('store')

            try:
                stock: JuiceStockModel = JuiceStockModel.objects.get(juice__exact=data['id'],
                                                                               store__exact=store)
                data['stock'] = stock.stock
            except:
                data['stock'] = 0

        return data

