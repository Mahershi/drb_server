from rest_framework import serializers
from ..models import PodModel, PodStockModel
from rest_framework.request import Request
from django.http import QueryDict


class PodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodModel
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        req: Request = self.context.get('request')
        qp: QueryDict = req.query_params

        if qp.get('store') is not None:
            store = qp.get('store')

            try:
                stock: PodStockModel = PodStockModel.objects.get(pod__exact=data['id'],
                                                                               store__exact=store)
                data['stock'] = stock.stock
            except:
                data['stock'] = 0

        return data

