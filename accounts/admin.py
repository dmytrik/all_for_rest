from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Manager


@admin.register(Manager)
class ManagerAdmin(UserAdmin):
    list_filter = ("position",)
