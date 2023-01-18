from django.contrib import admin

from .models import Company, Seller, Product, Order, OrderItem

# Register your models here.


admin.site.register(Company)
admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
