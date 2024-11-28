from django.urls import path
from accounts.views import (
    ManagerListView,
    ManagerCreateView
)


urlpatterns = [
    path("", ManagerListView.as_view(), name="manager-list"),
    path("create/", ManagerCreateView.as_view(), name="manager-create")
]

app_name = "accounts"
