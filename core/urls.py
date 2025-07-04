from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UsersAPIView.as_view(), name='users'),
    path('users/<int:pk>/', views.UserAPIView.as_view(), name='detail_user'),
    path('products/', views.ProductsAPIView.as_view(), name='products'),
    path('products/<int:pk>/', views.ProductAPIView.as_view(), name='detail_product'),
]