from django.urls import path

from .views import (
    IndexView,
    CategoriesListView,
    CategoriesMinListView,
    CategoryDetailView,
    ProductsListView,
    ProductDetailView,
)

app_name = "shop_app"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    # path("", index_view, name="index"),
    path("categories-min/", CategoriesMinListView.as_view(), name="categories-min"),
    path("categories/", CategoriesListView.as_view(), name="categories"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category"),
    path("products/", ProductsListView.as_view(), name="products"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product"),
]
