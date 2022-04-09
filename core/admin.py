from django.contrib import admin

from .models import Company, Seller, Portage, Customer, Factory, Employer, Product, Factory_Product, Order, OrderItems

# Register your models here.


admin.site.register(Company)
admin.site.register(Seller)
admin.site.register(Portage)
admin.site.register(Customer)
admin.site.register(Factory)
admin.site.register(Employer)
admin.site.register(Product)
admin.site.register(Factory_Product)
admin.site.register(Order)
admin.site.register(OrderItems)
