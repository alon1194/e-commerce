import nested_admin
from django.contrib import admin
from .models import (
    Product,
    ProductColor,
    ProductColorImage,
    ProductVariant,
    Product_images,
    Category,
    Address,
)


class ProductColorImageInline(nested_admin.NestedTabularInline):
    model = ProductColorImage
    extra = 2


class ProductVariantInline(nested_admin.NestedTabularInline):
    model = ProductVariant
    extra = 3


class ProductColorInline(nested_admin.NestedTabularInline):
    model = ProductColor
    extra = 1
    inlines = [
        ProductColorImageInline,
        ProductVariantInline,
    ]


class Product_imagesInline(nested_admin.NestedTabularInline):
    model = Product_images
    extra = 0


@admin.register(Product)
class ProductAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        ProductColorInline,
        Product_imagesInline,
    ]


admin.site.register(Category)
admin.site.register(Address)
admin.site.register(ProductVariant)
admin.site.register(ProductColor)
admin.site.register(Product_images)