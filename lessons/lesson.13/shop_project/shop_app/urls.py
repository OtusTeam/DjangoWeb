from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from shop_app.views import (
    index,
    IndexView,
    show_products,
    ProductListView,
    ProductListTemplateView,
    ProductDetailView,
    CreateCategoryView,
    CategoryListView,
    ProductCreateView,
    ProductDeleteView,
)

app_name = "shop_app"

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path(
        "profile/", TemplateView.as_view(template_name="dashboard.html"), name="profile"
    ),
    # path('home/', index)
    path("address/", IndexView.as_view(), name="home"),
    # path('products/', show_products, name='products'),
    # path('products/', ProductListView.as_view(), name='products'),
    path("products/", ProductListTemplateView.as_view(), name="products"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product"),
    path("create/", CreateCategoryView.as_view(), name="create"),
    path("categories/", CategoryListView.as_view(), name="categories"),
    path('products/create/', ProductCreateView.as_view(), name='create_product'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
]
