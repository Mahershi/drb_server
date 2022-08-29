from rest_framework import viewsets
from ..models import CategoryModel
from ..serializers import CategorySerializer
from rest_framework.permissions import AllowAny
from ..helper import customResponse


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        resp = super(CategoryViewSet, self).list(request, *args, **kwargs)

        return customResponse(success=True, data=resp.data)


