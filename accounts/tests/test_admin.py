from django.contrib.admin.sites import site
from django.test import TestCase

from accounts.admin import ManagerAdmin
from accounts.models import Manager


class ProductAdminTest(TestCase):

    def test_manager_admin_on_filter_by_position(self):
        self.manager_admin = ManagerAdmin(Manager, site)
        self.assertIn("position", self.manager_admin.list_filter)
