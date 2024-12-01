from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from product.models import ProductType
from accounts.forms import ManagerCreationForm

MANAGER_CREATE_URL = reverse("accounts:manager-create")


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

        self.manager_data = {
            "username": "test_new_user",
            "password1": "test_password1",
            "password2": "test_password1",
            "position": "grill_seller",
            "first_name": "test_first_test",
            "last_name": "test_last_test",
        }

        self.manager_invalid_data = {
            "username": "test_new_user",
            "password1": "test_password1",
            "password2": "test_password1",
            "position": "test_position",
            "first_name": "test_first_test",
            "last_name": "test_last_test",
        }

    def test_manager_creation_form_is_valid(self):
        form = ManagerCreationForm(data=self.manager_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, self.manager_data)

    def test_creation_driver(self):
        product_type = ProductType.objects.create(
            name="grill_products"
        )
        self.client.post(MANAGER_CREATE_URL, data=self.manager_data)
        manager = get_user_model().objects.get(
            username=self.manager_data["username"]
        )
        self.assertEqual(
            manager.first_name,
            self.manager_data["first_name"]
        )
        self.assertEqual(
            manager.position,
            self.manager_data["position"]
        )

    def test_creation_manager_with_invalid_data(self):
        self.client.post(MANAGER_CREATE_URL, data=self.manager_invalid_data)
        manager = get_user_model().objects.filter(
            username=self.manager_invalid_data["username"]
        )
        self.assertEqual(len(manager), 0)
