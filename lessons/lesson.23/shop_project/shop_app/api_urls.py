from sys import prefix

from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from rest_framework import permissions

from . import api_views

app_name = "shop_app_api"


router = DefaultRouter()
router.register(
    prefix=r"categories",
    viewset=api_views.CategoryViewSet,
    basename="category",
)
router.register(
    prefix=r"products",
    viewset=api_views.ProductViewSet,
    basename="product",
)
# urlpatterns = router.urls

router.register(
    prefix=r'filter-products',
    viewset=api_views.FilteringProductViewSet,
    basename='filter-product',
)


schema_view = get_schema_view(
   openapi.Info(
      title="Products API",
      default_version='v1',
      description="Product shop",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="admin@admin.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        "top-categories/",
        api_views.CategoriesTopListAPIView.as_view(),
        name="top-categories",
    ),
    path(
        "min-categories/<int:pk>/",
        api_views.CategoryDetailAPIView.as_view(),
        name="min-category-details",
    ),
    # path("api/", include(router.urls)),
    *router.urls,
    # docs
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
