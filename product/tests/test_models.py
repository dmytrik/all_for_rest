from django.test import TestCase

from product.models import (
    Brand,
    ProductType,
    Product
)


class ModelsTests(TestCase):

    def test_brand_str(self):
        brand = Brand.objects.create(
            name="testBrand",
            country="testCountry"
        )
        self.assertEqual(str(brand), f"{brand.name} {brand.country}")

    def test_product_type_str(self):
        product_type = ProductType.objects.create(
            name="grill_products"
        )
        self.assertEqual(str(product_type), product_type.name)

    def test_product_str(self):
        brand = Brand.objects.create(
            name="testBrand",
            country="testCountry"
        )
        type = ProductType.objects.create(
            name="test_product_type"
        )
        product = Product.objects.create(
            name="test_name",
            price=300,
            brand=brand,
            description="test_description",
            type=type,
        )
        self.assertEqual(
            str(product),
            f"{product.name} {product.brand} (price = {product.price})"
        )
