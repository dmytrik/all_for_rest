from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views import View

from product.models import Product


class JsonFurnitureResponse(View):
    @staticmethod
    def get(request):
        page = request.GET.get("page")
        queryset = Product.objects.select_related("brand").filter(type__name="garden_furniture")
        paginator = Paginator(queryset, 9)
        page_object = paginator.get_page(page)

        res = [
            {
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "id": product.id,
                "brand": product.brand.name,
                "type": "садові меблі",
                "photo": product.photo.url
            }
            for product in page_object
        ]

        return JsonResponse(res, safe=False)


class JsonGrillProductsResponse(View):
    @staticmethod
    def get(request):
        page = request.GET.get("page")
        queryset = Product.objects.select_related("brand").filter(type__name="grill_products")
        paginator = Paginator(queryset, 9)
        page_object = paginator.get_page(page)

        res = [
            {
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "id": product.id,
                "brand": product.brand.name,
                "type": "товари для барбекю",
                "photo": product.photo.url
            }
            for product in page_object
        ]

        return JsonResponse(res, safe=False)


class JsonCampingProductsResponse(View):
    @staticmethod
    def get(request):
        page = request.GET.get("page")
        queryset = Product.objects.select_related("brand").filter(type__name="camping_products")
        paginator = Paginator(queryset, 9)
        page_object = paginator.get_page(page)

        res = [
            {
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "id": product.id,
                "brand": product.brand.name,
                "type": "товари для відпочинку",
                "photo": product.photo.url
            }
            for product in page_object
        ]

        return JsonResponse(res, safe=False)