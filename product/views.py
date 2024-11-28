from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View, generic
from django.views.decorators.http import condition
from urllib3 import request

from accounts.models import Manager
from product.models import Product, Brand


class Index(View):

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


class FurnitureSetsView(View):

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "product/furniture_sets.html")


class JsonFurnitureResponse(View):
    @staticmethod
    def get(request):
        page = request.GET.get("page")
        if not page:
            page = 1
        to_ = int(page) * 9
        from_ = to_ - 9
        sets = Product.objects.select_related("brand").filter(type__name="garden_furniture")[from_:to_]
        res = []
        for set in sets:
            res.append({
                "name": set.name,
                "price": set.price,
                "description": set.description,
                "id": set.id,
                "brand": set.brand.name,
                "type": "садові меблі",
                "photo": set.photo.url
            })
        return JsonResponse(res, safe=False)


class GrillProductsView(View):

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "product/grill_products.html")


class JsonGrillProductsResponse(View):
    @staticmethod
    def get(request):
        page = request.GET.get("page")
        if not page:
            page = 1
        to_ = int(page) * 9
        from_ = to_ - 9
        sets = Product.objects.select_related("brand").filter(type__name="grill_products")[from_:to_]
        res = []
        for set in sets:
            res.append({
                "name": set.name,
                "price": set.price,
                "description": set.description,
                "id": set.id,
                "brand": set.brand.name,
                "type": "товари для барбекю",
                "photo": set.photo.url
            })
        return JsonResponse(res, safe=False)


class CampingProductsView(View):

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "product/camping_products.html")


class JsonCampingProductsResponse(View):
    @staticmethod
    def get(request):
        page = request.GET.get("page")
        if not page:
            page = 1
        to_ = int(page) * 9
        from_ = to_ - 9
        sets = Product.objects.select_related("brand").filter(type__name="camping_products")[from_:to_]
        res = []
        for set in sets:
            res.append({
                "name": set.name,
                "price": set.price,
                "description": set.description,
                "id": set.id,
                "brand": set.brand.name,
                "type": "товари для відпочинку",
                "photo": set.photo.url
            })
        return JsonResponse(res, safe=False)


class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        condition = ((self.request.user.position == "furniture_seller" and self.object.type.name == "garden_furniture")
                     or (self.request.user.position == "grill_seller" and self.object.type.name == "grill_products")
                     or (self.request.user.position == "camping_seller" and self.object.type.name == "camping_products"))
        context["condition"] = condition
        return context


class ProductCreateView(generic.CreateView):
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("product:index")


class ProductUpdateView(generic.UpdateView):
    model = Product
    fields = ("name", "price", "brand", "description", "photo")
    success_url = reverse_lazy("product:index")


class BrandListView(generic.ListView):
    model = Brand


class BrandDetailView(generic.DetailView):
    model = Brand


class BrandCreateView(generic.CreateView):
    model = Brand
    fields = ("name",)
    success_url = reverse_lazy("product:brand-list")

