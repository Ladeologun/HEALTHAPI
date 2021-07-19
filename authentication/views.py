from django.contrib.auth import get_user_model,authenticate
from rest_framework import generics, permissions, status,response
from authentication.serializers import RegisterSerializer,LoginSerializer
from rest_framework.authtoken.models import Token

class RegisterUserView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    """Create new user in the system"""
    serializer_class = RegisterSerializer

    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)
        fullname = user_data.get('fullname', '')
        email = user_data.get('email', '')
        mobile_number = user_data.get('mobile_number', '')
        password = user_data.get('password', '')
        age = user_data.get('age', '')

        if not serializer.is_valid():
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = get_user_model().objects.create(fullname=fullname, email=email,
                                               mobile_number=mobile_number, password=password,age=age)
        user.set_password(password)
        user.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        if email is None or password is None:
            return response.Response({'invalid_credentials': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=email, password=password)

        if not user:
            return response.Response({'invalid_credentials': 'Ensure both email and password are correct'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(user)
        token, _ = Token.objects.get_or_create(user=user)
        return response.Response({'message':'success','token': token.key}, status=status.HTTP_200_OK)

