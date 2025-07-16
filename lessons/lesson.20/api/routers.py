from rest_framework import routers
from .views import CategoryViewSet, AnimalViewSet

router = routers.DefaultRouter()
# router = routers.SimpleRouter()
router.register(r'categories', CategoryViewSet),
router.register(r'animals', AnimalViewSet)
