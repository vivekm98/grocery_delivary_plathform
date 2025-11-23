# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from rest_framework.permissions import AllowAny,IsAuthenticated
# from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import LoginSerializer,RegisterSerializer,CartSerializer,ProductSerializer,DeliverySlotSerializer
# from .serializers import OrderSerializer,CategorySerializer,UnitSerializer,OrderItemSerializer,SubscriptionSerializer
# from rest_framework import generics
# from .models import  Cart, Product, DeliverySlot, Order,Category,Unit,OrderItem,Subscription
#
# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer
#     permission_classes = [AllowAny]
#
# class LoginView(APIView):
#     permission_classes = [AllowAny]
#
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         email = serializer.validated_data['email']
#         password = serializer.validated_data['password']
#
#         # Get the user by email
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
#
#         # Authenticate using username
#         user = authenticate(username=user.username, password=password)
#         if user is None:
#             return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
#
#         # Generate JWT tokens
#         refresh = RefreshToken.for_user(user)
#
#         return Response({
#             "user": {
#                 "id": user.id,
#                 "email": user.email,
#                 "username": user.username
#             },
#             "tokens": {
#                 "refresh": str(refresh),
#                 "access": str(refresh.access_token)
#             }
#         }, status=status.HTTP_200_OK)
#
#
# class CategoryListCreateView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [IsAuthenticated]
#
# class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [IsAuthenticated]
#
# # -----------------------------
# # Unit Views
# # -----------------------------
#
# class UnitListCreateView(generics.ListCreateAPIView):
#     queryset = Unit.objects.all()
#     serializer_class = UnitSerializer
#     permission_classes = [IsAuthenticated]
#
# class UnitRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Unit.objects.all()
#     serializer_class = UnitSerializer
#     permission_classes = [IsAuthenticated]
#
# # -----------------------------
# # Product Views
# # -----------------------------
#
# class ProductListCreateView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated]
#
# class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated]
#
# # -----------------------------
# # Cart Views
# # -----------------------------
#
# class CartListCreateView(generics.ListCreateAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer
#     permission_classes = [IsAuthenticated]
#
# class CartRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer
#     permission_classes = [IsAuthenticated]
#
# # -----------------------------
# # Delivery Slot Views
# # -----------------------------
#
# class DeliverySlotListCreateView(generics.ListCreateAPIView):
#     queryset = DeliverySlot.objects.all()
#     serializer_class = DeliverySlotSerializer
#     permission_classes = [IsAuthenticated]
#
# class DeliverySlotRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = DeliverySlot.objects.all()
#     serializer_class = DeliverySlotSerializer
#     permission_classes = [IsAuthenticated]
#
# # -----------------------------
# # Order Views
# # -----------------------------
#
# class OrderListCreateView(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated]
#
# class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated]
#
# # -----------------------------
# # OrderItem Views
# # -----------------------------
#
# class OrderItemListCreateView(generics.ListCreateAPIView):
#     queryset = OrderItem.objects.all()
#     serializer_class = OrderItemSerializer
#     permission_classes = [IsAuthenticated]
#
# class OrderItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = OrderItem.objects.all()
#     serializer_class = OrderItemSerializer
#     permission_classes = [IsAuthenticated]
#
# # -----------------------------
# # Subscription Views
# # -----------------------------
#
# class SubscriptionListCreateView(generics.ListCreateAPIView):
#     queryset = Subscription.objects.all()
#     serializer_class = SubscriptionSerializer
#     permission_classes = [IsAuthenticated]
#
# class SubscriptionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Subscription.objects.all()
#     serializer_class = SubscriptionSerializer
#     permission_classes = [IsAuthenticated]