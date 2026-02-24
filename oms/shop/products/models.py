from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        help_text="Category name"
    )
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=8, 
        decimal_places=2,
        validators=[MinValueValidator(0)]  # price must be >= 0
    )
    stock = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)]  # stock must be >= 0
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
    )
    sku = models.CharField(
        max_length=50,
        unique=True,
        db_index=True,
        help_text="Internal stock-keeping unit",
        default="DEFAULT_SKU"  # <--- default value for existing rows
        )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()
        if self.price > 9999.99:
            raise ValidationError({'price': "Price cannot exceed 9999.99"})

    class Meta:
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(fields=['name', 'category'], name='unique_product_per_category'),
            models.CheckConstraint(check=models.Q(price__gte=0), name='price_non_negative'),
        ]

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    products = models.ManyToManyField(Product, related_name="tags")

    def __str__(self):
        return self.name