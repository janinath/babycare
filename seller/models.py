from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title=models.TextField(max_length=30,db_column='title',null=True)
    description=models.TextField(max_length=100,db_column='description',null=True)
    category=models.TextField(max_length=20,db_column='category',null=True)
    image=models.ImageField(upload_to="images",null=True,db_column='images')
    price=models.PositiveIntegerField(db_column='price',null=True)
    quantity=models.PositiveIntegerField(db_column='quantity',null=True)
    status=models.TextField(max_length="10",db_column='status',null=True)
    
    
   
