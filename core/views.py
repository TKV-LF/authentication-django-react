from os import access
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer
from .authentication import JWTAuthentication, create_access_token, create_refresh_token, decode_refresh_token, JWTAuthentication
# Create your views here.


class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data

        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Passwords do not match!')
        serializer.save()

        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        if user is None:
            raise exceptions.AuthenticationFailed('Invalid credentials')

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Invalid credentials')

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        response = Response()

        response.set_cookie(key='refresh_token',
                            value=refresh_token, httponly=True)
        response.data = {
            'token': access_token,
        }

        return response


class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        return Response(UserSerializer(request.user).data)


class RefreshTokenAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        id = decode_refresh_token(refresh_token)

        access_token = create_access_token(id)
        return Response({
            'token': access_token,
        })

class LogoutAPIView(APIView):
	def post(self, request):
		response = Response()
		response.delete_cookie(key='refresh_token')
		response.data = {
			"message": "success"
		}

		return response
		
