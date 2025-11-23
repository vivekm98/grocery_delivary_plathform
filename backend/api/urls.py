from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    CategoryListCreateView,
    CategoryRetrieveUpdateDestroyView,
    UnitListCreateView,
    UnitRetrieveUpdateDestroyView,
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
    CartListCreateView,
    CartRetrieveUpdateDestroyView,
    DeliverySlotListCreateView,
    DeliverySlotRetrieveUpdateDestroyView,
    OrderListCreateView,
    OrderRetrieveUpdateDestroyView,
    OrderItemListCreateView,
    OrderItemRetrieveUpdateDestroyView,
    SubscriptionListCreateView,
    SubscriptionRetrieveUpdateDestroyView
)

urlpatterns = [
    # Authentication
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),

    # Categories
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),

    # Units
    path('units/', UnitListCreateView.as_view(), name='unit-list-create'),
    path('units/<int:pk>/', UnitRetrieveUpdateDestroyView.as_view(), name='unit-detail'),

    # Products
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),

    # Cart
    path('cart/', CartListCreateView.as_view(), name='cart-list-create'),
    path('cart/<int:pk>/', CartRetrieveUpdateDestroyView.as_view(), name='cart-detail'),

    # Delivery Slots
    path('delivery-slots/', DeliverySlotListCreateView.as_view(), name='delivery-slot-list-create'),
    path('delivery-slots/<int:pk>/', DeliverySlotRetrieveUpdateDestroyView.as_view(), name='delivery-slot-detail'),

    # Orders
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),

    # Order Items
    path('order-items/', OrderItemListCreateView.as_view(), name='order-item-list-create'),
    path('order-items/<int:pk>/', OrderItemRetrieveUpdateDestroyView.as_view(), name='order-item-detail'),

    # Subscriptions
    path('subscriptions/', SubscriptionListCreateView.as_view(), name='subscription-list-create'),
    path('subscriptions/<int:pk>/', SubscriptionRetrieveUpdateDestroyView.as_view(), name='subscription-detail'),
]