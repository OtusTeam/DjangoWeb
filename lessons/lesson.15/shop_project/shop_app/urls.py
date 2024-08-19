from django.urls import path

from .views import (
    IndexView,
    CategoriesListView,
    CategoriesMinListView,
    CategoryDetailView,
    ProductsListView,
    ProductDetailView,
    CategoryCreateView,
    ProductCreateView,
    CategoryDeleteView,
    ProductDeleteView,
    CategoryUpdateView,
    ProductUpdateView,
    OrdersListView,
)

app_name = "shop_app"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    # path("", index_view, name="index"),
    path("categories-min/", CategoriesMinListView.as_view(), name="categories-min"),
    path("categories/", CategoriesListView.as_view(), name="categories"),
    path("categories/add/", CategoryCreateView.as_view(), name="category-add"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category"),
    path("categories/<int:pk>/confirm-delete/", CategoryDeleteView.as_view(), name="category-confirm-delete"),
    path("categories/<int:pk>/edit/", CategoryUpdateView.as_view(), name="category-edit"),
    path("products/", ProductsListView.as_view(), name="products"),
    path("products/add/", ProductCreateView.as_view(), name="product-add"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product"),
    path("products/<int:pk>/confirm-delete/", ProductDeleteView.as_view(), name="product-confirm-delete"),
    path("products/<int:pk>/edit/", ProductUpdateView.as_view(), name="product-edit"),
    path("orders/", OrdersListView.as_view(), name="orders"),
]
