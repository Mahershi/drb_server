from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.permissions import AllowAny
from ..models import DisposableModel
from ..serializers import DisposableSerializer
from ..helper import customResponse
from django.http import QueryDict
from rest_framework.decorators import action


class DisposableViewSet(viewsets.ModelViewSet):
    queryset = DisposableModel.objects.all()
    permission_classes = [AllowAny]
    serializer_class = DisposableSerializer

    def list(self, request: Request, *args, **kwargs):
        qp: QueryDict = request.query_params
        if qp.get('product') is not None:
            product = qp.get('product')
            self.queryset = self.queryset.filter(product__exact=product)

        resp = super(DisposableViewSet, self).list(request, *args, **kwargs)
        return customResponse(success=True, data=resp.data)

    @action(methods=['GET'], detail=False)
    def get_disposable(self, request: Request, *args, **kwargs):
        qp: QueryDict = request.query_params
        print(qp)
        if qp.get('flavour') is None:
            return customResponse(success=False)
        else:
            try:
                dispo: DisposableModel = DisposableModel.objects.get(pk=qp.get('flavour'))
                serializer = DisposableSerializer(dispo, many=False, context={'request':request})
                # print(serializer.data)
                print(dispo.flavour)
                return customResponse(success=True, data=serializer.data)
            except Exception as e:
                print(e)
                return customResponse(success=False)

