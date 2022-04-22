from django.contrib.auth.models import User

# Create your models here.
from django.db import models


class Seller(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=120)
    tax_id = models.CharField(max_length=30)


class Company(models.Model):
    name = models.CharField(max_length=120)
    cnpj = models.CharField(max_length=120)
    fantasy_name = models.CharField(max_length=120, null=True, blank=True)
    ie = models.CharField(max_length=120, null=True, blank=True)
    fone = models.CharField(max_length=120, null=True, blank=True)
    fone2 = models.CharField(max_length=120, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return ' '.join([self.name, self.cnpj])


class Portage(models.Model):
    company_id = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Transportadora"
        verbose_name_plural = "Transportadora"


class Customer(models.Model):
    company_id = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)


class Factory(models.Model):
    company_id = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)


class Employer(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    fone = models.CharField(max_length=120, null=True, blank=True)
    email = models.CharField(max_length=120, null=True, blank=True)
    active = models.BooleanField(default=True)
    customer_id = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return ' '.join([self.name])


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120, blank=True, null=True)
    cod = models.CharField(max_length=15, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    ipi = models.FloatField()
    active = models.BooleanField(default=True)
    factory_id = models.ForeignKey(Factory, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}, {self.description}'


class Factory_Product(models.Model):
    product_id = models.ManyToManyField(Product)
    factory_id = models.ManyToManyField(Factory)


class Order(models.Model):
    shipping_enum = (
                        (1, 'CIF'),
                        (2, 'FOB'),
                    )
    status_enum = (
        (1, 'Cotacao'),
        (2, 'Aprovado'),
        (3, 'Cancelado')
    )
    status = models.IntegerField(choices=status_enum, default=1)
    shipping = models.IntegerField(choices=shipping_enum, default=1)
    seller_id = models.ForeignKey(Seller, null=True, on_delete=models.SET_NULL)
    portage_id = models.ForeignKey(Portage, null=True, blank=True, on_delete=models.SET_NULL)
    customer_id = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    observation = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItems(models.Model):
    order_id = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    product_id = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    price_with_discount = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
    discount = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
