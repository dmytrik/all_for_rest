from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from accounts.models import Manager
from accounts.forms import (
    ManagerCreationForm,
    ManagerSearchForm
)


class ManagerListView(LoginRequiredMixin, generic.ListView):
    model = Manager
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ManagerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = ManagerSearchForm(
            initial={
                "username": username
            }
        )
        return context

    def get_queryset(self):
        queryset = Manager.objects.all()
        form = ManagerSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


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


class ManagerUpdateView(generic.UpdateView):
    model = Manager
    fields = ("username", "position")
    success_url = reverse_lazy("accounts:manager-list")
