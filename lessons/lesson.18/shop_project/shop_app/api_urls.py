from django.urls import path, include
from rest_framework.routers import DefaultRouter

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
]
