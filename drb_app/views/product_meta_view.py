from django.http import QueryDict
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
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

    @action(methods=['GET'], detail=False)
    def get_new(self, request, *args, **kwargs):
        qp: QueryDict = request.query_params
        if qp.get('cat_id') is not None:
            cat_id = qp.get('cat_id')
            self.queryset = self.queryset.filter(category__exact=cat_id).order_by('-date_created')
            serializer = self.serializer_class(self.queryset, many=True)
            return customResponse(success=True, data=serializer.data)
        else:
            return customResponse(success=False)


    @action(methods=['GET'], detail=False)
    def on_sale(self, request, *args, **kwargs):
        qp: QueryDict = request.query_params
        if qp.get('cat_id') is not None:
            cat_id = qp.get('cat_id')
            self.queryset = self.queryset.filter(category__exact=cat_id, on_sale__exact=True).order_by('-date_created')
            serializer = self.serializer_class(self.queryset, many=True)
            return customResponse(success=True, data=serializer.data)
        else:
            return customResponse(success=False)

    @action(methods=['GET'], detail=False)
    def popular(self, request, *args, **kwargs):
        qp: QueryDict = request.query_params
        if qp.get('cat_id') is not None:
            cat_id = qp.get('cat_id')
            self.queryset = self.queryset.filter(category__exact=cat_id, popular__exact=True).order_by('-date_created')
            serializer = self.serializer_class(self.queryset, many=True)
            return customResponse(success=True, data=serializer.data)
        else:
            return customResponse(success=False)

    @action(methods=['GET'], detail=False)
    def strong(self, request, *args, **kwargs):
        qp: QueryDict = request.query_params
        if qp.get('cat_id') is not None:
            cat_id = qp.get('cat_id')
            self.queryset = self.queryset.filter(category__exact=cat_id, strong__exact=True).order_by('-date_created')
            serializer = self.serializer_class(self.queryset, many=True)
            return customResponse(success=True, data=serializer.data)
        else:
            return customResponse(success=False)

