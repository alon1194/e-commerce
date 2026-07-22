


from django.contrib import admin
from .models import Product, ProductColor, ProductVariant, Category, Address, Product_images


from django.contrib import admin
from .models import Product, ProductColor, Product_images


class ProductColorInline(admin.TabularInline):
    model = ProductColor
    extra = 3


class Product_imagesInline(admin.TabularInline):
    model = Product_images
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductColorInline,
        Product_imagesInline,
    ]
    
admin.site.register(Category)
admin.site.register(Address)
admin.site.register(ProductColor)
admin.site.register(ProductVariant)
admin.site.register(Product_images)