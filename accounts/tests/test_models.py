from django.contrib.auth import get_user_model
from django.test import TestCase

from product.models import ProductType


class ModelsTests(TestCase):

    def test_manager_str(self):
        product_type = ProductType.objects.create(
            name="grill_products"
        )
        manager = get_user_model().objects.create(
            username="test_username",
            password="test1234",
            position="grill_seller"
        )
        self.assertEqual(
            str(manager),
            f"{manager.username} ({manager.position})"
        )
