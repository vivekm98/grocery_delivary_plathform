
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import  SubscriptionSerializer
from rest_framework import generics
from .models import  Subscription
# Create your views here.
class SubscriptionListView(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

class SubscriptionRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]