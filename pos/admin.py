from django.contrib import admin
from .models import Product, Order, OrderItem

#register your models here
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
