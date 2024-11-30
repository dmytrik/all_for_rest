from django.urls import path
from product.views import (
    Index,
    FurnitureSetsView,
    GrillProductsView,
    CampingProductsView,
    BrandListView,
    BrandDetailView,
    BrandCreateView,
    BrandUpdateView,
    BrandDeleteView,
    ProductDetailView,
    ProductUpdateView,
    ProductCreateView
)
from product.views_json_response import (
    JsonFurnitureResponse,
    JsonGrillProductsResponse,
    JsonCampingProductsResponse
)


urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("furniture_sets/", FurnitureSetsView.as_view(), name="furniture_sets"),
    path("grill_products/", GrillProductsView.as_view(), name="grill_products"),
    path("camping_products/", CampingProductsView.as_view(), name="camping_products"),
    path("furniture_sets/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("grill_products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("camping_products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"),
    path("products/create/", ProductCreateView.as_view(), name="product-create"),
    path("brands/", BrandListView.as_view(), name="brand-list"),
    path("brands/<int:pk>/", BrandDetailView.as_view(), name="brand-detail"),
    path("brands/<int:pk>/update", BrandUpdateView.as_view(), name="brand-update"),
    path("brands/<int:pk>/delete", BrandDeleteView.as_view(), name="brand-delete"),
    path("brands/create", BrandCreateView.as_view(), name="brand-create"),
]

urlpatterns.extend([
    path("json-sets/", JsonFurnitureResponse.as_view(), name="json-sets"),
    path("json-camping-products/", JsonCampingProductsResponse.as_view(), name="json-camping-products"),
    path("json-grill-products/", JsonGrillProductsResponse.as_view(), name="json-grill-products")
])

app_name = "product"
