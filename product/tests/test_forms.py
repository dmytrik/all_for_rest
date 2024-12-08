from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from product.models import (
    ProductType,
    Brand,
    Product
)

PRODUCT_CREATION_URL = reverse("product:product-create")
BRAND_CREATION_URL = reverse("product:brand-create")


class FormsTest(TestCase):

    def setUp(self):
        self.product_type = ProductType.objects.create(
            name="garden_furniture"
        )
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test1234"
        )
        self.client.force_login(self.user)

        self.brand = Brand.objects.create(
            name="test_brand",
            country="test_country"
        )

        self.product_data = {
            "name": "test_product_name",
            "price": 30000,
            "brand": self.brand.id,
            "type": self.product_type.id,
            "description": "test_description"
        }

        self.product_update_data = {
            "name": "test_product_name",
            "price": 40000,
            "brand": self.brand.id,
            "type": self.product_type.id,
            "description": "test_description"
        }

        self.brand_data = {
            "name": "test_name",
            "country": "test_country"
        }

        self.brand_update_data = {
            "name": "test_name",
            "country": "updated_country"
        }

    def test_product_create_with_valid_data(self):
        response = self.client.post(
            PRODUCT_CREATION_URL,
            data=self.product_data
        )

        product = Product.objects.get(name=self.product_data["name"])
        self.assertEqual(response.status_code, 302)
        self.assertEqual(product.price, self.product_data.get("price"))

    def test_brand_create_with_valid_data(self):
        response = self.client.post(
            BRAND_CREATION_URL,
            data=self.brand_data
        )
        brand = Brand.objects.get(name=self.brand_data["name"])
        self.assertEqual(response.status_code, 302)
        self.assertEqual(brand.country, self.brand_data["country"])

    def test_product_create_with_invalid_data(self):
        self.client.post(
            PRODUCT_CREATION_URL,
            data={
                "name": "test",
                "price": 20000
            }
        )
        product = Product.objects.filter(name="test")
        self.assertEqual(len(product), 0)

    def test_create_brand_with_invalid_data(self):
        self.client.post(
            BRAND_CREATION_URL,
            data={
                "name": "test"
            }
        )
        brand = Brand.objects.filter(name="test")
        self.assertEqual(len(brand), 0)

    def test_update_product(self):
        self.client.post(
            PRODUCT_CREATION_URL,
            data=self.product_data
        )
        product_before = Product.objects.get(name=self.product_data["name"])

        response = self.client.post(
            reverse(
                "product:product-update",
                kwargs={"pk": product_before.id}
            ),
            data=self.product_update_data
        )

        product_after = Product.objects.get(id=product_before.id)

        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(product_before.price, product_after.price)

    def test_update_brand(self):
        self.client.post(
            BRAND_CREATION_URL,
            data=self.brand_data
        )
        brand_before = Brand.objects.get(name=self.brand_data["name"])

        response = self.client.post(
            reverse("product:brand-update", kwargs={"pk": brand_before.id}),
            data=self.brand_update_data
        )

        brand_after = Brand.objects.get(id=brand_before.id)

        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(brand_before.country, brand_after.country)
