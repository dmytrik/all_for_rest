from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View, generic

from accounts.models import Manager
from product.models import Product, Brand
from product.forms import ProductSearchForm


class Index(LoginRequiredMixin, View):

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:

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

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        context = {
            "form": ProductSearchForm()
        }
        return render(request, "product/furniture_sets.html", context)


class GrillProductsView(LoginRequiredMixin, View):

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        context = {
            "form": ProductSearchForm()
        }
        return render(request, "product/grill_products.html", context)


class CampingProductsView(LoginRequiredMixin, View):

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        context = {
            "form": ProductSearchForm()
        }
        return render(request, "product/camping_products.html", context)



class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        condition = ((self.request.user.position == "furniture_seller" and self.object.type.name == "garden_furniture")
                     or (self.request.user.position == "grill_seller" and self.object.type.name == "grill_products")
                     or (self.request.user.position == "camping_seller" and self.object.type.name == "camping_products"))
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


class BrandListView(LoginRequiredMixin, generic.ListView):
    model = Brand


class BrandDetailView(LoginRequiredMixin, generic.DetailView):
    model = Brand


class BrandUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Brand
    fields = ("name",)
    success_url = reverse_lazy("product:brand-list")


class BrandDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Brand
    success_url = reverse_lazy("product:brand-list")


class BrandCreateView(LoginRequiredMixin, generic.CreateView):
    model = Brand
    fields = ("name",)
    success_url = reverse_lazy("product:brand-list")

