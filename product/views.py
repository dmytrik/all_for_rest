from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import (
    HttpRequest,
    HttpResponse
)
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View, generic

from accounts.models import Manager
from product.models import Product, Brand
from product.forms import ProductSearchForm, BrandSearchForm


class Index(LoginRequiredMixin, View):

    def get(self, request: HttpRequest) -> HttpResponse:

        count_of_products = Product.objects.count()
        count_of_brands = Brand.objects.count()
        count_of_managers = Manager.objects.count()

        context = {
            "count_of_products": count_of_products,
            "count_of_brands": count_of_brands,
            "count_of_managers": count_of_managers
        }

        return render(request, "product/index.html", context=context)


class FurnitureSetsView(LoginRequiredMixin, View):

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": ProductSearchForm()
        }
        return render(request, "product/furniture_sets.html", context)


class GrillProductsView(LoginRequiredMixin, View):

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": ProductSearchForm()
        }
        return render(request, "product/grill_products.html", context)


class CampingProductsView(LoginRequiredMixin, View):

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": ProductSearchForm()
        }
        return render(request, "product/camping_products.html", context)


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        condition_dict = {
            "furniture_seller": "garden_furniture",
            "grill_seller": "grill_products",
            "camping_seller": "camping_products"
        }
        condition = (
                condition_dict[self.request.user.position] == self.object.type.name
        )
        context["condition"] = condition
        return context


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("product:index")


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    fields = ("name", "price", "brand", "description", "photo")
    success_url = reverse_lazy("product:index")


class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy("product:index")


class BrandListView(LoginRequiredMixin, generic.ListView):
    model = Brand
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BrandListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = BrandSearchForm(
            initial={
                "name": name
            }
        )
        return context

    def get_queryset(self):
        queryset = Brand.objects.all()
        form = BrandSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class BrandDetailView(LoginRequiredMixin, generic.DetailView):
    model = Brand


class BrandUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Brand
    fields = ("name", "country")
    success_url = reverse_lazy("product:brand-list")


class BrandDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Brand
    success_url = reverse_lazy("product:brand-list")


class BrandCreateView(LoginRequiredMixin, generic.CreateView):
    model = Brand
    fields = ("name", "country")
    success_url = reverse_lazy("product:brand-list")
