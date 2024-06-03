from django.db import models

from marketplace.models import Category


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    supplier = models.ForeignKey('Supplier', on_delete=models.PROTECT, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()
    article = models.CharField(max_length=100, unique=True, help_text="Unique string product id", db_index=True)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('category', 'quantity')


class ProductDetail(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='details')
    description = models.TextField(null=True, blank=True)
    manufacturing_date = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Details of {self.product.name}"

