from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from product.models import ProductType


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_manager(instance, **kwargs):
    product_type = None

    if instance.position == "furniture_seller":
        product_type = ProductType.objects.get(name="garden_furniture")
    if instance.position == "grill_seller":
        product_type = ProductType.objects.get(name="grill_products")
    if instance.position == "camping_seller":
        product_type = ProductType.objects.get(name="camping_products")

    product_type.managers.add(instance)
