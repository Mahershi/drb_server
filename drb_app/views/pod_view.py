from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.permissions import AllowAny
from ..models import PodModel
from ..serializers import PodSerializer
from ..helper import customResponse
from django.http import QueryDict
from rest_framework.decorators import action


class PodViewSet(viewsets.ModelViewSet):
    queryset = PodModel.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PodSerializer

    def list(self, request: Request, *args, **kwargs):
        qp: QueryDict = request.query_params
        if qp.get('product') is not None:
            product = qp.get('product')
            self.queryset = self.queryset.filter(product__exact=product)

        resp = super(PodViewSet, self).list(request, *args, **kwargs)
        return customResponse(success=True, data=resp.data)

    @action(methods=['GET'], detail=False)
    def get_pod(self, request: Request, *args, **kwargs):
        qp: QueryDict = request.query_params
        if qp.get('flavour') is None:
            return customResponse(success=False)
        else:
            try:
                pod: PodModel = PodModel.objects.get(pk=qp.get('flavour'))
                serializer = PodSerializer(pod, many=False, context={'request': request})
                # print(serializer.data)
                return customResponse(success=True, data=serializer.data)
            except Exception as e:
                return customResponse(success=False)

