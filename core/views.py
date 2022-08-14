from urllib import response
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer
from .authentication import create_access_token, create_refresh_token, decode_access_token
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

		response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
		response.data = {
			'token': access_token,
		}
		
		return response

class UserAPIView(APIView):
	def get(self, request):
		auth = get_authorization_header(request).split()
		if auth and len(auth) == 2:
			token = auth[1].decode('utf-8')
			id = decode_access_token(token)
			user = User.objects.get(pk=id)

			if user:
				serializer = UserSerializer(user)
				return Response(serializer.data)

		raise exceptions.AuthenticationFailed('unauthenticated')
