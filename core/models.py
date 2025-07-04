from django.db import models
from django.contrib.auth.models import User



class CartModel(models.Model):
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_finalized = models.DateTimeField(blank=True, null=True)
    finalized = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        ordering = ['id']

    def __str__(self):
        return self.id_user
    

class CategoryModel(models.Model):
    description = models.CharField(max_length=100, null=False, blank=False)
    user = models.ForeignKey(User, related_name='users_categories', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

    def __str__(self):
        return self.description
    

class ProductModel(models.Model):
    user = models.ForeignKey(User, related_name='users_products', on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, related_name='categorys', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    recurrent = models.BooleanField(default=True, null=False)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id']

    def __str__(self):
        return f'{self.description} - {self.category} - {self.user}'


class CartItemModel(models.Model):
    product = models.ForeignKey(ProductModel, related_name='products', on_delete=models.CASCADE)
    cart = models.ForeignKey(CartModel, related_name='carts', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(null=False, blank=False)
    unit_value = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    class Meta:
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartsItems'
        unique_together = ['product', 'cart']
        ordering = ['id']
    
    def __str__(self):
        return f"{self.product} - {self.cart}"
