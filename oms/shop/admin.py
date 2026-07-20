


from django.contrib import admin
from .models import Product, ProductColor, ProductVariant, Category, Address


class ProductColorInline(admin.TabularInline):
    model = ProductColor
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductColorInline]

admin.site.register(ProductColor)
admin.site.register(ProductVariant)
admin.site.register(Category)
admin.site.register(Address)