from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from .serializers import RegisterSerializer,LoginSerializer
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        # Get the user by email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

        # Authenticate using username
        user = authenticate(username=user.username, password=password)
        if user is None:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)

        return Response({
            "user": {
                "id": user.id,
                "email": user.email,
                "username": user.username
            },
            "tokens": {
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }
        }, status=status.HTTP_200_OK)



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()  # add to blacklist
            return Response({"detail": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def forgot_password(request):
    email = request.data.get('email')
    if email is None:
        return Response({"error": "Email required"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        reset_link = f"http://localhost:63342/frontend/reset-password.html?uid={uid}&token={token}"

        send_mail(
            "Reset your password",
            f"Click the link to reset your password: {reset_link}",
            "noreply@grocery.com",
            [email]
        )

    # Security: don't reveal if email exists
    return Response({"message": "If your email exists, a reset link has been sent."})