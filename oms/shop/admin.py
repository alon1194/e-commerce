from django.contrib import admin

# Register your models here.
from .models import  Address,Category, Product

admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Product)