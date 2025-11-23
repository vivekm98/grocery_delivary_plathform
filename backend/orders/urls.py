from django.urls import path
from . import views

urlpatterns = [

    path('delivery/',views.DeliverySlotListView.as_view(),name="deliverys"),
    path('delivery/<int:pk>/',views.DeliverySlotRetrieveView.as_view(),name="delivery"),
    path('order/', views.OrderListView.as_view(), name="orders"),
    path('order/<int:pk>/', views.OrderRetrieveView.as_view(), name="order"),
    path('orderitem/', views.OrderItemListView.as_view(), name="orderitems"),
    path('orderitem/<int:pk>/', views.OrderItemRetrieveView.as_view(), name="orderitem"),


]