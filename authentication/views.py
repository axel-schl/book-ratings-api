from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from .serializers import UserSerializer

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)

     
        if user:
            login(request, user)
            return Response(UserSerializer(user).data,status=status.HTTP_200_OK)

        
        return Response(status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    def post(self, request):
        logout(request)

      
        return Response(status=status.HTTP_200_OK)

class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
   
    print(f"\nRecover your password '{reset_password_token.user.email}' using this token: '{reset_password_token.key}' from API http://localhost:8000/api/auth/reset/confirm/.")