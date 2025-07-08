from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics

from . import models, serializers


class UsersAPIView(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ProductsAPIView(generics.ListCreateAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return models.ProductModel.objects.filter(user=self.request.user)


class ProductAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return models.ProductModel.objects.filter(user=self.request.user)


class CategoriesAPIView(generics.ListCreateAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return models.CategoryModel.objects.filter(user=self.request.user)


class CategoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return models.CategoryModel.objects.filter(user=self.request.user)


class CartAPIView(generics.ListCreateAPIView):
    queryset = models.CartModel.objects.all()
    serializer_class = serializers.CartSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return models.CartModel.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class CartItemAPIView(generics.ListCreateAPIView):
    queryset = models.CartItemModel.objects.all()
    serializer_class = serializers.CartItemSerializer
    permission_classes = [IsAuthenticated, ]
