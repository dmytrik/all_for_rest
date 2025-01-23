from django.contrib.admin.sites import site
from django.test import TestCase

from product.admin import (
    ProductAdmin,
    BrandAdmin,
    ProductTypeAdmin
)
from product.models import (
    Product,
    Brand,
    ProductType
)


class ProductAdminTest(TestCase):

    def test_product_admin_on_search_field_by_name(self):
        self.product_admin = ProductAdmin(Product, site)
        self.assertIn("name", self.product_admin.search_fields)

    def test_product_admin_on_filter_by_type(self):
        self.product_admin = ProductAdmin(Product, site)
        self.assertIn("type", self.product_admin.list_filter)


class BrandAdminTest(TestCase):

    def test_brand_admin_on_search_field_by_name(self):
        self.brand_admin = BrandAdmin(Brand, site)
        self.assertIn("name", self.brand_admin.search_fields)

    def test_brand_admin_on_filter_by_country(self):
        self.brand_admin = BrandAdmin(Brand, site)
        self.assertIn("country", self.brand_admin.list_filter)


class ProductTypeAdminTest(TestCase):

    def test_product_type_admin_on_search_field_by_name(self):
        self.product_type_admin = ProductTypeAdmin(ProductType, site)
        self.assertIn("name", self.product_type_admin.search_fields)

    def test_product_type_admin_on_filter_by_managers(self):
        self.product_type_admin = ProductTypeAdmin(ProductType, site)
        self.assertIn("managers", self.product_type_admin.list_filter)
