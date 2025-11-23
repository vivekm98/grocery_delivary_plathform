
from django.urls import path,include

urlpatterns = [

    path('',include('accounts.urls')),
    path('',include('products.urls')),
    path('', include('cart.urls')),
    path('', include('orders.urls')),
    path('', include('subscription.urls')),
]