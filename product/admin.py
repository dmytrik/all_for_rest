from django.contrib import admin

from product.models import Product, ProductType, Brand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("type",)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("country",)


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("managers",)
