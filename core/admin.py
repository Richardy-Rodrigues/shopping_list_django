from django.contrib import admin
from . import models

@admin.register(models.ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'category_id', 'price', 'description', 'recurrent')

@admin.register(models.CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'description')

@admin.register(models.CartModel)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'dt_created', 'dt_finalized', 'finalized')

@admin.register(models.CartItemModel)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'cart_id', 'quantity', 'unit_value')
