from rest_framework import viewsets
from ..models import ParametersModels
from ..serializers import ParameterSerializer
from rest_framework.permissions import AllowAny
from ..helper import customResponse


class ParameterViewSet(viewsets.ModelViewSet):
    queryset = ParametersModels.objects.all()
    serializer_class = ParameterSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        resp = super(ParameterViewSet, self).list(request, *args, **kwargs)
        return customResponse(success=True, data=resp.data)