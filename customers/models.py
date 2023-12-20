from django.db import models
from seller.models import Product
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
class Customer(models.Model):
    c_name=models.TextField(max_length=50,db_column='name',null=True)
    c_email=models.TextField(max_length=50,db_column='email',null=True)
    c_mob=models.TextField(max_length=12,db_column='mobile',null=True)
    c_pswd=models.TextField(max_length=100,db_column='password',null=True)
    otp=models.TextField(max_length=6,db_column='otp',null=True)
    status=models.TextField(max_length=10,db_column='status',null=True)
    class Meta:
        db_table='customer'
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='cart_items',null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    p_image=models.ImageField(db_column='image',null=True)
    p_name=models.TextField(max_length=50,db_column='name',null=True)
    p_quantity=models.PositiveIntegerField(db_column='quantity',null=True)
    p_price=models.PositiveIntegerField(db_column='price',null=True)
    p_total=models.PositiveIntegerField(db_column='total',null=True)
    class Meta:
        db_table='cart'





    