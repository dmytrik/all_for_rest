from django.contrib.auth import get_user_model
from django.urls import reverse

from django.test import TestCase

from product.models import ProductType

MANAGERS_URL = reverse("accounts:manager-list")


class PublicManagerTest(TestCase):

    def test_manager_list_login_required(self):
        response = self.client.get(MANAGERS_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateManagerTest(TestCase):

    def setUp(self):
        self.product_type = ProductType.objects.create(
            name="garden_furniture"
        )
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test1234"
        )
        self.client.force_login(self.user)

    def test_retrieve_managers_page(self):
        response = self.client.get(MANAGERS_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/manager_list.html")

    def test_retrieve_managers(self):
        get_user_model().objects.create_user(
            username="test_username1",
            password="test_password1"
        )
        get_user_model().objects.create_user(
            username="test_username2",
            password="test_password2"
        )
        managers = get_user_model().objects.all()
        response = self.client.get(MANAGERS_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["manager_list"]),
            list(managers)
        )
