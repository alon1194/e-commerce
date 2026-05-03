from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"





class Category(models.Model): 
    id = models.AutoField(primary_key = True)
    category_name = models.CharField(max_length = 150, unique = True ,verbosa_name = "category name ")
    category_slug = models.SlugField(unique = True, max_length = 150,  )

    def __str__(self): 
        return self.category_name
    def save (self, *args, **kwargs):
        self.category_slug = slugify (self.category_name)
        return super().save(*args, **kwargs)

class Product(models.Model):
    product_id = models.AutoField(primary_key = True)   
    product_name = models.ChatField(max_length = 150 , unique = True) 
    product_slug = models.SlugField(max_length = 150, unique = True , blank = True )
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'products')
    description = models.TextField(blank = True )
    price = models.DecimalField(max_digits = 10 , decimal_places = 3)
    stock = models.IntegerField()

    def save (self, *args, **kwargs):
        self.product_slug = slugify(self.product_name)
        return super().save(*args, **kwargs)
    def __self__(self):
        return self.product_name