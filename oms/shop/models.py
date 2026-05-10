from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from userauth.models import Custumer





class Address(models.Model):
    Address_ID = models.AutoField(primary_key=True)
    Street = models.CharField(max_length = 50)
    City = models.CharField(max_length = 50 )
    State = models.CharField(max_length = 50)
    Zip_code = models.CharField(max_length = 10)
    Country = models.CharField()
    Custumer = models.ForeignKey(
    Custumer,
    on_delete=models.CASCADE,
    related_name="addresses",
    null=True,
    blank=True
)



    def __str__(self): 
        return f"{self.Street},{self.City} {self.Country}"
    
    class meta: 
        ordering = [ 'City']
        

class Category(models.Model): 
    id = models.AutoField(primary_key = True)
    category_name = models.CharField(max_length = 150, unique = True ,
    verbose_name = "category name ", 
    null=True,
    blank=True)
    category_slug = models.SlugField(unique = True, max_length = 150,  null=True,
    blank=True  )

    def __str__(self): 
        return self.category_name
    def save (self, *args, **kwargs):
        self.category_slug = slugify (self.category_name)
        return super().save(*args, **kwargs)

class Product(models.Model):
    product_id = models.AutoField(primary_key = True)   
    product_name = models.CharField(max_length = 150 , unique = True,   null=True,
    blank=True) 
    product_slug = models.SlugField(max_length = 150, unique = True , blank = True,   null=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'products')
    description = models.TextField(blank = True )
    price = models.DecimalField(max_digits = 10 , decimal_places = 3)
    stock = models.IntegerField()

    def save (self, *args, **kwargs):
        self.product_slug = slugify(self.product_name)
        return super().save(*args, **kwargs)
    def __self__(self):
        return self.product_name


 