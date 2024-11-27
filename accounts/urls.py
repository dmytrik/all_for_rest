from django.urls import path
from accounts.views import ManagerListView


urlpatterns = [
    path("", ManagerListView.as_view(), name="manager-list")
]

app_name = "accounts"
