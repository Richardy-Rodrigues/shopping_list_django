from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UsersAPIView.as_view(), name='users'),
    path('users/<int:pk>/', views.UserAPIView.as_view(), name='detail_user'),
    path('products/', views.ProductsAPIView.as_view(), name='products'),
    path('products/<int:pk>/', views.ProductAPIView.as_view(), name='detail_product'),
    path('categories/', views.CategoriesAPIView.as_view(), name='categories'),
    path('categories/<int:pk>/', views.CategoryAPIView.as_view(), name='detail_category'),
]