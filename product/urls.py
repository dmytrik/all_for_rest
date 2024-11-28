from django.urls import path
from product.views import (
    Index,
    FurnitureSetsView,
    GrillProductsView,
    CampingProductsView,
    BrandListView,
    JsonFurnitureResponse,
    JsonCampingProductsResponse,
    JsonGrillProductsResponse,
    ProductDetailView,
    ProductUpdateView,
    ProductCreateView
)

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("furniture_sets/", FurnitureSetsView.as_view(), name="furniture_sets"),
    path("grill_products/", GrillProductsView.as_view(), name="grill_products"),
    path("camping_products/", CampingProductsView.as_view(), name="camping_products"),
    path("furniture_sets/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("grill_products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("camping_products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("furniture_sets/<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"),
    path("grill_products/<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"),
    path("camping_products/<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"),
    path("furniture_sets/create/", ProductCreateView.as_view(), name="product-create"),
    path("grill_products/create/", ProductCreateView.as_view(), name="product-create"),
    path("camping_products/create/", ProductCreateView.as_view(), name="product-create"),
    path("brands/", BrandListView.as_view(), name="brand-list"),
    path("json-sets/", JsonFurnitureResponse.as_view(), name="json-sets"),
    path("json-camping-products/", JsonCampingProductsResponse.as_view(), name="json-camping-products"),
    path("json-grill-products/", JsonGrillProductsResponse.as_view(), name="json-grill-products"),
]

app_name = "product"
