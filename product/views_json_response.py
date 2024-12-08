from django.core.paginator import Paginator
from django.http import (
    JsonResponse,
    HttpRequest
)
from django.views import View

from product.models import Product

COUNT_OF_PRODUCTS = 9


class JsonFurnitureResponse(View):

    def get(self, request: HttpRequest) -> JsonResponse:
        page = request.GET.get("page")
        name = request.GET.get("name")
        queryset = (Product.objects.select_related("brand").
                    filter(type__name="garden_furniture"))
        if name:
            queryset = queryset.filter(name__icontains=name)
        paginator = Paginator(queryset, COUNT_OF_PRODUCTS)
        page_object = paginator.get_page(page)

        res = [
            {
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "id": product.id,
                "brand": product.brand.name,
                "type": "садові меблі",
                "photo": product.photo.url if product.photo else ""
            }
            for product in page_object
        ]

        return JsonResponse(res, safe=False)


class JsonGrillProductsResponse(View):

    def get(self, request: HttpRequest) -> JsonResponse:
        page = request.GET.get("page")
        name = request.GET.get("name")
        queryset = (Product.objects.select_related("brand").
                    filter(type__name="grill_products"))
        if name:
            queryset = queryset.filter(name__icontains=name)
        paginator = Paginator(queryset, COUNT_OF_PRODUCTS)
        page_object = paginator.get_page(page)

        res = [
            {
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "id": product.id,
                "brand": product.brand.name,
                "type": "товари для барбекю",
                "photo": product.photo.url if product.photo else ""
            }
            for product in page_object
        ]

        return JsonResponse(res, safe=False)


class JsonCampingProductsResponse(View):

    def get(self, request: HttpRequest) -> JsonResponse:
        page = request.GET.get("page")
        name = request.GET.get("name")
        queryset = (Product.objects.select_related("brand").
                    filter(type__name="camping_products"))
        if name:
            queryset = queryset.filter(name__icontains=name)
        paginator = Paginator(queryset, COUNT_OF_PRODUCTS)
        page_object = paginator.get_page(page)

        res = [
            {
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "id": product.id,
                "brand": product.brand.name,
                "type": "товари для відпочинку",
                "photo": product.photo.url if product.photo else ""
            }
            for product in page_object
        ]

        return JsonResponse(res, safe=False)
