from django.contrib import admin

from .models import Customer, Product, Cart, OrderPlaced


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'locality', 'city', 'pincode', 'state')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'selling_price', 'discounted_price', 'description', 'brand', 'category', 'product_image')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity')


@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'customer', 'quantity', 'ordered_date', 'status')
