from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from ..models import DiscountModel
from ..serializers import DiscountSerializer
from ..helper import customResponse


class DiscountViewSet(viewsets.ModelViewSet):
    serializer_class = DiscountSerializer
    queryset = DiscountModel.objects.all()
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        resp = super(DiscountViewSet, self).list(request, *args, **kwargs)
        return customResponse(success=True, data=resp.data)
