from django.urls import path
from . import views

urlpatterns = [

    path('subscription/', views.SubscriptionListView.as_view(), name='category-list'),
    path('subscription/<int:pk>/', views.SubscriptionRetrieveView.as_view(), name='category-detail'),


]