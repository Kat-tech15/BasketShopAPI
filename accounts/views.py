<<<<<<< HEAD
from rest_framework import permissions, generics
=======
from rest_framework import generics, permissions 
>>>>>>> 534f0acf66985d63608978708c7b18620adcaec1
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
<<<<<<< HEAD
from .serializers import UserSerializer
=======
from .serializers import UserSerializer,LoginSerializer, EmptySerializer
>>>>>>> 534f0acf66985d63608978708c7b18620adcaec1


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfuly!'},
                                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(generics.GenericAPIView):
<<<<<<< HEAD
    serializer_class = UserSerializer
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
=======
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
>>>>>>> 534f0acf66985d63608978708c7b18620adcaec1

        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh),
                             'access': str(refresh.access_token),
                              'message': 'Logged in successfully!',
            })
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(generics.GenericAPIView):
<<<<<<< HEAD
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
        except:
            pass
        return Response({'message': 'Logged out successfully.'}, status=status.HTTP_200_OK)
=======
    serializer_class = EmptySerializer

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        if hasattr(request.user, 'access_token'):
            request.user.access_token.delete()

        return Response({'message': 'User Logged out successfully.'}, status=status.HTTP_200_OK)
>>>>>>> 534f0acf66985d63608978708c7b18620adcaec1
