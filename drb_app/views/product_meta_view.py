from rest_framework.response import Response

from ..models import ProductMetaModel
from ..serializers import ProductMetaSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from ..helper import customResponse


class ProductMetaViewset(viewsets.ModelViewSet):
    queryset = ProductMetaModel.objects.all()
    serializer_class = ProductMetaSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        resp: Response = super(ProductMetaViewset, self).list(request, *args, **kwargs)

        return customResponse(success=True, data=resp.data)

    def retrieve(self, request, *args, **kwargs):
        resp: Response = super(ProductMetaViewset, self).retrieve(request, *args, **kwargs)

        return customResponse(success=True, data=resp.data)