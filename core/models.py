from datetime import timedelta

from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.utils import timezone


class Seller(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=120)
    pix = models.CharField(max_length=120, null=True, blank=True)
    email = models.CharField(max_length=120, null=True, blank=True)
    phone = models.CharField(max_length=120, null=True, blank=True)
    phone2 = models.CharField(max_length=120, null=True, blank=True)
    cpfcnpj = models.CharField(max_length=30)
    observation = models.TextField(null=True, blank=True)

class Company(models.Model):
    company_enum = (
        (1, 'Customer'),
        (2, 'Factory'),
        (2, 'Portage'),
        (2, 'Company'),
    )
    type = models.IntegerField(choices=company_enum, default=1)
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120, null=True, blank=True)
    website = models.CharField(max_length=120, null=True, blank=True)
    logo_url = models.CharField(max_length=120, null=True, blank=True)
    street = models.CharField(max_length=120, null=True, blank=True)
    number = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120, null=True, blank=True)
    state = models.CharField(max_length=120, null=True, blank=True)
    zip_code = models.CharField(max_length=120, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    cpfcnpj = models.CharField(max_length=120)
    fantasy_name = models.CharField(max_length=120, null=True, blank=True)
    ie = models.CharField(max_length=120, null=True, blank=True)
    phone = models.CharField(max_length=120, null=True, blank=True)
    phone2 = models.CharField(max_length=120, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='user_id')


    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return ' '.join([self.name, self.cnpj])



class Catalog(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Catalog'
        verbose_name_plural = 'Catalogs'

    def __str__(self):
        return ' '.join([self.name, self.description])



class Order (models.Model):
    shipping_enum = (
        (1, 'CIF'),
        (2, 'FOB'),
    )
    status_enum = (
        (1, 'Cotacao'),
        (2, 'Aprovado'),
        (3, 'Cancelado')
    )
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    factory = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL,related_name='factory')
    customer = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL, related_name='customer')
    portage = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL, related_name='portage')
    seller_id = models.ForeignKey(Seller, null=True, on_delete=models.SET_NULL)
    url_pdf = models.CharField(max_length=120)
    buyer = models.CharField(max_length=120)
    status=models.IntegerField(choices=status_enum, default=1)
    shipping=models.IntegerField(choices=shipping_enum, default=1)
    expire_order = models.DateTimeField(auto_now=timezone.now() + timedelta(days=10))
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return ' '.join([self.user_id, self.factory, self.customer, self.portage, self.status])


class Product(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    factory = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    catalog = models.ForeignKey(Catalog, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ipi = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=120)
    uni = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    image_url = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return ' '.join([self.name, self.code])



class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'

    def __str__(self):
        return ' '.join([self.order, self.product])

class Plan(models.Model):
    plan_enum = (
        ("Intermediate", 'Intermediate'),
        ("Advanced", 'Advanced'),
    )
    plan = models.CharField(max_length=20, choices=plan_enum, default="Advanced")
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_at = models.DateTimeField(auto_now_add=True)