from django.urls import path
from . import views

urlpatterns = [
    # Categories
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryRetrieveView.as_view(), name='category-detail'),

    # Posters
    path('posters/', views.Posterview.as_view(), name='poster-list-create'),

    # Units
    path('units/',views. UnitListView.as_view(), name='unit-list'),
    path('units/<int:pk>/',views.UnitRetrieveView.as_view(), name='unit-detail'),

    # Products
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductRetrieView.as_view(), name='product-detail'),
]


