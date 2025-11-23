from django.urls import path
from . import views
urlpatterns = [

    path('cart',views.CartListView.as_view(),name="cartlist"),
    path('cart/<int:pk>/',views.CartRetrieveView.as_view(),name="cartretrive"),

 ]