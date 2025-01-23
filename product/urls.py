from django.urls import (
    path,
    include
)

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
    ProductDeleteView,
    ProductCreateView
)
from product.views_json_response import (
    JsonFurnitureResponse,
    JsonGrillProductsResponse,
    JsonCampingProductsResponse
)


json_patterns = [
    path(
        "json-sets/",
        JsonFurnitureResponse.as_view(),
        name="json-sets"
    ),
    path(
        "json-camping-products/",
        JsonCampingProductsResponse.as_view(),
        name="json-camping-products"
    ),
    path(
        "json-grill-products/",
        JsonGrillProductsResponse.as_view(),
        name="json-grill-products"
    )
]

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path(
        "furniture-sets/",
        FurnitureSetsView.as_view(),
        name="furniture_sets"
    ),
    path(
        "grill-products/",
        GrillProductsView.as_view(),
        name="grill_products"
    ),
    path(
        "camping-products/",
        CampingProductsView.as_view(),
        name="camping_products"
    ),
    path(
        "furniture-sets/<int:pk>/",
        ProductDetailView.as_view(),
        name="product-detail"
    ),
    path(
        "grill-products/<int:pk>/",
        ProductDetailView.as_view(),
        name="product-detail"
    ),
    path(
        "camping-products/<int:pk>/",
        ProductDetailView.as_view(),
        name="product-detail"
    ),
    path(
        "products/<int:pk>/",
        ProductDetailView.as_view(),
        name="product-detail"
    ),
    path(
        "products/<int:pk>/update/",
        ProductUpdateView.as_view(),
        name="product-update"
    ),
    path(
        "products/<int:pk>/delete/",
        ProductDeleteView.as_view(),
        name="product-delete"
    ),
    path(
        "products/create/",
        ProductCreateView.as_view(),
        name="product-create"
    ),
    path(
        "brands/",
        BrandListView.as_view(),
        name="brand-list"
    ),
    path(
        "brands/<int:pk>/",
        BrandDetailView.as_view(),
        name="brand-detail"
    ),
    path(
        "brands/<int:pk>/update/",
        BrandUpdateView.as_view(),
        name="brand-update"
    ),
    path(
        "brands/<int:pk>/delete/",
        BrandDeleteView.as_view(),
        name="brand-delete"
    ),
    path(
        "brands/create/",
        BrandCreateView.as_view(),
        name="brand-create"
    ),
    path("json/", include(json_patterns))
]


app_name = "product"
