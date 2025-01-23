import json

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from product.models import (
    ProductType,
    Product,
    Brand
)

FURNITURE_SETS_URL = reverse("product:furniture_sets")
GRILL_PRODUCTS_URL = reverse("product:grill_products")
CAMPING_PRODUCTS_URL = reverse("product:camping_products")
JSON_RESPONSE_FURNITURE_SETS_URL = reverse("product:json-sets")
JSON_RESPONSE_GRILL_PRODUCTS_URL = reverse("product:json-grill-products")
JSON_RESPONSE_CAMPING_PRODUCTS_URL = reverse("product:json-camping-products")
BRANDS_URL = reverse("product:brand-list")
FURNITURE_SETS_SEARCH_WORD = "rita"
GRILL_PRODUCTS_SEARCH_WORD = "smoke"
CAMPING_PRODUCTS_SEARCH_WORD = "jung"


class PublicProductTest(TestCase):

    def test_furniture_sets_login_required(self):
        response = self.client.get(FURNITURE_SETS_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_grill_products_login_required(self):
        response = self.client.get(GRILL_PRODUCTS_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_camping_products_login_required(self):
        response = self.client.get(CAMPING_PRODUCTS_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateProductTest(TestCase):

    def setUp(self):
        self.product_type = ProductType.objects.create(
            name="garden_furniture"
        )
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test1234"
        )
        self.client.force_login(self.user)

    def test_retrieve_product_pages(self):
        res_furniture_sets = self.client.get(FURNITURE_SETS_URL)
        res_grill_products = self.client.get(GRILL_PRODUCTS_URL)
        res_camping_products = self.client.get(CAMPING_PRODUCTS_URL)

        self.assertEqual(res_furniture_sets.status_code, 200)
        self.assertEqual(res_camping_products.status_code, 200)
        self.assertEqual(res_grill_products.status_code, 200)

        self.assertTemplateUsed(
            res_furniture_sets,
            "product/furniture_sets.html"
        )
        self.assertTemplateUsed(
            res_grill_products,
            "product/grill_products.html"
        )
        self.assertTemplateUsed(
            res_camping_products,
            "product/camping_products.html"
        )

    def test_retrieve_furniture_sets(self):
        brand = Brand.objects.create(
            name="test_brand"
        )

        Product.objects.create(
            name="test_furniture_set_1",
            price=200000,
            brand=brand,
            description="test_description",
            type=self.product_type,
        )
        Product.objects.create(
            name="test_furniture_set_2",
            price=200000,
            brand=brand,
            description="test_description",
            type=self.product_type,
        )
        products = [
            {
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "id": product.id,
                "brand": product.brand.name,
                "type": "садові меблі",
                "photo": product.photo.url if product.photo else ""
            }
            for product in Product.objects.all()
        ]
        response = self.client.get(JSON_RESPONSE_FURNITURE_SETS_URL)
        self.assertEqual(json.loads(response.content), products)

    def test_search_furniture_sets(self):
        brand = Brand.objects.create(
            name="test_brand"
        )

        Product.objects.create(
            name="Avrora",
            price=200000,
            brand=brand,
            description="test_description",
            type=self.product_type,
        )
        Product.objects.create(
            name="Rita",
            price=200000,
            brand=brand,
            description="test_description",
            type=self.product_type,
        )

        response = self.client.get(
            f"{JSON_RESPONSE_FURNITURE_SETS_URL}?"
            f"page=1&name={FURNITURE_SETS_SEARCH_WORD}"
        )

        products = [
            {
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "id": product.id,
                "brand": product.brand.name,
                "type": "садові меблі",
                "photo": product.photo.url if product.photo else ""
            }
            for product in Product.objects.filter(
                name__icontains=FURNITURE_SETS_SEARCH_WORD
            )
        ]

        self.assertEqual(json.loads(response.content), products)

    def test_retrieve_grill_products(self):
        brand = Brand.objects.create(
            name="test_brand"
        )
        product_type = ProductType.objects.create(
            name="grill_products"
        )
        Product.objects.create(
            name="test_grill_product_1",
            price=200000,
            brand=brand,
            description="test_description",
            type=product_type,
        )
        Product.objects.create(
            name="test_grill_product_2",
            price=200000,
            brand=brand,
            description="test_description",
            type=product_type,
        )
        products = [
            {
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "id": product.id,
                "brand": product.brand.name,
                "type": "товари для барбекю",
                "photo": product.photo.url if product.photo else ""
            }
            for product in Product.objects.all()
        ]
        response = self.client.get(JSON_RESPONSE_GRILL_PRODUCTS_URL)
        self.assertEqual(json.loads(response.content), products)

    def test_search_grill_products(self):
        brand = Brand.objects.create(
            name="test_brand"
        )
        product_type = ProductType.objects.create(
            name="camping_products"
        )
        Product.objects.create(
            name="smoke_house",
            price=200000,
            brand=brand,
            description="test_description",
            type=product_type,
        )
        Product.objects.create(
            name="did_koptenko",
            price=200000,
            brand=brand,
            description="test_description",
            type=product_type,
        )
        products = [
            {
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "id": product.id,
                "brand": product.brand.name,
                "type": "товари для барбекю",
                "photo": product.photo.url if product.photo else ""
            }
            for product in Product.objects.filter(
                name__icontains=CAMPING_PRODUCTS_SEARCH_WORD
            )
        ]
        response = self.client.get(
            f"{JSON_RESPONSE_CAMPING_PRODUCTS_URL}?"
            f"page=1&name={CAMPING_PRODUCTS_SEARCH_WORD}"
        )
        self.assertEqual(json.loads(response.content), products)

    def test_retrieve_camping_products(self):
        brand = Brand.objects.create(
            name="test_brand"
        )
        product_type = ProductType.objects.create(
            name="camping_products"
        )
        Product.objects.create(
            name="jungle",
            price=200000,
            brand=brand,
            description="test_description",
            type=product_type,
        )
        Product.objects.create(
            name="milti",
            price=200000,
            brand=brand,
            description="test_description",
            type=product_type,
        )
        products = [
            {
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "id": product.id,
                "brand": product.brand.name,
                "type": "товари для відпочинку",
                "photo": product.photo.url if product.photo else ""
            }
            for product in Product.objects.all()
        ]
        response = self.client.get(JSON_RESPONSE_CAMPING_PRODUCTS_URL)
        self.assertEqual(json.loads(response.content), products)

    def test_search_camping_products(self):
        brand = Brand.objects.create(
            name="test_brand"
        )
        product_type = ProductType.objects.create(
            name="camping_products"
        )
        Product.objects.create(
            name="test_camping_product_1",
            price=200000,
            brand=brand,
            description="test_description",
            type=product_type,
        )
        Product.objects.create(
            name="test_camping_product_2",
            price=200000,
            brand=brand,
            description="test_description",
            type=product_type,
        )
        products = [
            {
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "id": product.id,
                "brand": product.brand.name,
                "type": "товари для відпочинку",
                "photo": product.photo.url if product.photo else ""
            }
            for product in Product.objects.all()
        ]
        response = self.client.get(JSON_RESPONSE_CAMPING_PRODUCTS_URL)
        self.assertEqual(json.loads(response.content), products)


class PublicBrandListTest(TestCase):

    def test_brand_list_login_required(self):
        response = self.client.get(BRANDS_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateBrandListTest(TestCase):

    def setUp(self):
        self.product_type = ProductType.objects.create(
            name="garden_furniture"
        )
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test1234"
        )
        self.client.force_login(self.user)

    def test_retrieve_brands(self):
        Brand.objects.create(
            name="test_brand1",
            country="test_country1"
        )
        Brand.objects.create(
            name="test_brand2",
            country="test_country2"
        )
        brands = Brand.objects.all()
        response = self.client.get(BRANDS_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["brand_list"]), list(brands))
        self.assertTemplateUsed(response, "product/brand_list.html")
