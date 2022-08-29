from rest_framework import viewsets
from ..models import UserModel
from ..serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request, QueryDict
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from ..helper import customResponse
from rest_framework.decorators import action, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = IsAuthenticated
    queryset = UserModel.objects.all()

    def get_permissions(self):
        print(self.action)
        if self.action == 'create' or self.action == 'exists' or self.action == 'login':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAuthenticated, ]

        return super().get_permissions()

    @action(methods=['POST'], detail=False)
    def login(self, request: Request):
        data = request.data
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            serializer_data = UserSerializer(user, many=False).data
            serializer_data.pop('password')
            resp = {
                "user": serializer_data,
                "token": token.key
            }
            return customResponse(True, resp)
        else:
            return customResponse(False)

    @action(detail=False, methods=['POST', 'GET'], )
    def exists(self, request: Request, pk=None):
        data = request.data
        print(str(data))
        username = data.get('username')
        # print(email)
        try:
            user: UserModel = UserModel.objects.filter(username__exact=username).get()
            serializer = UserSerializer(user, many=False)
            resp = serializer.data
            resp.pop('password')
            token, created = Token.objects.get_or_create(user=user)
            print(token.key)
            resp = {
                'token': token.key,
                'user': resp,
            }
            return customResponse(True, resp)
        except Exception as e:
            print(e)
            return customResponse(False, {"error": str(e)})

    def create(self, request, *args, **kwargs):
        # return customResponse(False, {"error": "Method Not Allowed"})
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            user = UserModel.objects.get_by_natural_key(serializer.validated_data.get('username'))
            token, created = Token.objects.get_or_create(user=user)
            data = serializer.data
            data.pop('password')
            resp = {
                'token': token.key,
                'user': data
            }
            return customResponse(True, resp)
        except:
            return customResponse(False,)


class CreateExistingToken(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        for user in UserModel.objects.all():
            Token.objects.get_or_create(user=user)

        return Response(
            {
                "success": "true"
            }
        )