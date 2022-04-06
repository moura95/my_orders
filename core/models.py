from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Seller(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=120)
    tax_id = models.CharField(max_length=30)