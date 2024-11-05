from rest_framework import views
from rest_framework.response import Response

from .serializers import LoginSerializer, RegisterSerializer, UserSerializer
from knox.models import AuthToken

class LoginView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        user_data = UserSerializer(user).data
        token = AuthToken.objects.create(user)[1]
        user_data['token'] = token
        return Response(user_data)
    
class RegisterView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data)
    


