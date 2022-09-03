from rest_framework import serializers
from ..models import DisposableModel, DisposableStockModel
from rest_framework.request import Request
from django.http import QueryDict


class DisposableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisposableModel
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        req: Request = self.context.get('request')
        qp: QueryDict = req.query_params


        if qp.get('store') is not None:
            store = qp.get('store')

            try:
                stock: DisposableStockModel = DisposableStockModel.objects.get(disposable__exact=data['id'], store__exact=store)
                data['stock'] = stock.stock
            except:
                data['stock'] = 0

        return data

