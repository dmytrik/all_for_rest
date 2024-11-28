from django.urls import reverse_lazy
from django.views import generic

from accounts.models import Manager
from accounts.forms import ManagerCreationForm


class ManagerListView(generic.ListView):
    model = Manager


class ManagerCreateView(generic.CreateView):
    model = Manager
    form_class = ManagerCreationForm
    success_url = reverse_lazy("login")