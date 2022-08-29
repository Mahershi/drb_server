from rest_framework import viewsets
from ..models import BrandModel
from ..serializers import BrandSerializer
from rest_framework.permissions import AllowAny
from ..helper import customResponse


class BrandViewSet(viewsets.ModelViewSet):
    queryset = BrandModel.objects.all()
    permission_classes = [AllowAny]
    serializer_class = BrandSerializer

    def list(self, request, *args, **kwargs):
        resp = super(BrandViewSet, self).list(request, *args, **kwargs)

        return customResponse(success=True, data=resp.data)


