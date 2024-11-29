from django.urls import path
from accounts.views import (
    ManagerListView,
    ManagerDetailView,
    ManagerCreateView
)


urlpatterns = [
    path("", ManagerListView.as_view(), name="manager-list"),
    path("<int:pk>/", ManagerDetailView.as_view(), name="manager-detail"),
    path("create/", ManagerCreateView.as_view(), name="manager-create")
]

app_name = "accounts"
