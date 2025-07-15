from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework.authtoken.models import Token

import requests

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


class CartsAPIView(generics.ListCreateAPIView):
    queryset = models.CartModel.objects.all()
    serializer_class = serializers.CartSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return models.CartModel.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        cart_finalized = models.CartModel.objects.filter(user=self.request.user, finalized=False).exists()
        if not cart_finalized:
            serializer.save(user=self.request.user)

class CartAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CartModel.objects.all()
    serializer_class = serializers.CartSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return models.CartModel.objects.filter(user=self.request.user)
        
class CartItemsAPIView(generics.ListCreateAPIView):
    queryset = models.CartItemModel.objects.all()
    serializer_class = serializers.CartItemSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return models.CartItemModel.objects.filter(cart__user=self.request.user, product__user=self.request.user)

    def perform_create(self, serializer):
        try:
            cart = models.CartModel.objects.filter(user=self.request.user, finalized=False)

            if not cart.exists():
                user_token = Token.objects.filter(user=self.request.user)
                url = 'http://localhost:8000/api/v1/carts/'
                requests.post(url=url, headers={'Authorization': f"Token {user_token[0]}"})

            serializer.save(cart=cart.order_by('-dt_created').first())
        except Exception as err:
            print(err)
    
class CartItemAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CartItemModel.objects.all()
    serializer_class = serializers.CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.CartItemModel.objects.filter(cart__user=self.request.user, product__user=self.request.user)

    def perform_destroy(self, instance):
        try:
            instance.delete()

            has_item_in_cart = models.CartItemModel.objects.select_related('cart').filter(cart=instance.cart, cart__user=self.request.user, product__user=self.request.user).count()

            if has_item_in_cart == 0:
                user_token = Token.objects.filter(user=self.request.user)
                url = f"http://localhost:8000/api/v1/carts/{instance.cart}/"
                requests.delete(url=url, headers={'Authorization': f"Token {user_token[0]}"})

        except Exception as err:
            print(err)
