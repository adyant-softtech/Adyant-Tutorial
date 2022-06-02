from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        o_serializer = self.serializer_class(data=request.data, context = {'request': request})
        o_serializer.is_valid(raise_exception=True)
        user = o_serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        username = request.data.get('username')
        password = request.data.get('password')

        auth_user = authenticate(request, username = username, password = password)

        if auth_user is not None:
            login(request, auth_user)
            data = {
                'token': token.key,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'username': user.username,
            }
        else:
            pass
        
        return Response(data)

