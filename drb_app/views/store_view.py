from rest_framework import viewsets
from ..models import StoreModel
from ..serializers import StoreSerializer
from rest_framework.permissions import AllowAny
from ..helper import customResponse


class StoreViewSet(viewsets.ModelViewSet):
    queryset = StoreModel.objects.all()
    permission_classes = [AllowAny]
    serializer_class = StoreSerializer

    def list(self, request, *args, **kwargs):
        resp = super(StoreViewSet, self).list(request, *args, **kwargs)
        return customResponse(success=True, data=resp.data)
