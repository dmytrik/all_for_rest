from django.db import models
from django_resized import ResizedImageField

from accounts.models import Manager


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} {self.country}"


class ProductType(models.Model):
    TYPE_CHOICES = (
        ("garden_furniture", "garden_furniture"),
        ("grill_products", "grill_products"),
        ("camping_products", "camping_products"),
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        choices=TYPE_CHOICES,
        default="garden_furniture"
    )
    managers = models.ManyToManyField(Manager, related_name="types_products")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True, related_name="products"
    )
    description = models.TextField()
    type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        null=True,
        related_name="products"
    )
    photo = ResizedImageField(
        force_format="WEBP",
        quality=75,
        upload_to="photos/",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name} {self.brand} (price = {self.price})"
