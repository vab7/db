from django.contrib import admin
from .models import *


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number', 'cvv', 'deadline')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'address')


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'courier', 'date', 'cost')


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'time')


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price_product', 'price_purchase', 'count', 'image')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'login', 'phone', 'address', 'gender', 'email')


@admin.register(StatusOrder)
class StatusOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Pay)
class PayAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Getting)
class GettingAdmin(admin.ModelAdmin):
    list_dislay = ('id', 'title')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_dispay = ('id', 'pay')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer', 'rating', 'text', 'review')