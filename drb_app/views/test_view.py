from django.http import HttpResponse
from rest_framework import viewsets
from ..models import TestModel, UserModel
from rest_framework.permissions import  AllowAny
from ..serializers import TestSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action, permission_classes


class TestViewSet(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    permission_classes = [AllowAny]
    serializer_class = TestSerializer

    def list(self, request, *args, **kwargs):
        return HttpResponse("Loaded")





