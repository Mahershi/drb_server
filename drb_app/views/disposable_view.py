from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.permissions import AllowAny
from ..models import DisposableModel
from ..serializers import DisposableSerializer
from ..helper import customResponse
from django.http import QueryDict



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



