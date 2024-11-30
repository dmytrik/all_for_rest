from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from accounts.models import Manager
from accounts.forms import ManagerCreationForm


class ManagerListView(LoginRequiredMixin, generic.ListView):
    model = Manager


class ManagerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Manager
    success_url = reverse_lazy("accounts:manager-list")

    def get_context_data(self, **kwargs):
        context = super(ManagerDetailView, self).get_context_data(**kwargs)
        product_types = self.object.types_products.prefetch_related("products")
        products = sum([
            list(type.products.all())
            for type in product_types
        ], [])

        context["products"] = products

        return context


class ManagerCreateView(generic.CreateView):
    model = Manager
    form_class = ManagerCreationForm
    success_url = reverse_lazy("login")
