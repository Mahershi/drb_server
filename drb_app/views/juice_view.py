from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.permissions import AllowAny
from ..models import JuiceModel
from ..serializers import JuiceSerializer
from ..helper import customResponse
from django.http import QueryDict
from rest_framework.decorators import action


class JuiceViewSet(viewsets.ModelViewSet):
    queryset = JuiceModel.objects.all()
    permission_classes = [AllowAny]
    serializer_class = JuiceSerializer

    def list(self, request: Request, *args, **kwargs):
        qp: QueryDict = request.query_params
        if qp.get('product') is not None:
            product = qp.get('product')
            self.queryset = self.queryset.filter(product__exact=product)

        resp = super(JuiceViewSet, self).list(request, *args, **kwargs)
        return customResponse(success=True, data=resp.data)

    @action(methods=['GET'], detail=False)
    def get_juice(self, request: Request, *args, **kwargs):
        qp: QueryDict = request.query_params
        if qp.get('flavour') is None:
            return customResponse(success=False)
        else:
            try:
                juice: JuiceModel = JuiceModel.objects.get(pk=qp.get('flavour'))
                serializer = JuiceSerializer(juice, many=False, context={'request': request})
                # print(serializer.data)
                return customResponse(success=True, data=serializer.data)
            except Exception as e:
                return customResponse(success=False)



