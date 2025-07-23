from rest_framework import routers
from .views import CategoryViewSet, AnimalViewSet, FoodViewSet

router = routers.DefaultRouter()
# router = routers.SimpleRouter()
router.register(r'categories', CategoryViewSet),
router.register(r'animals', AnimalViewSet),
router.register(r'food', FoodViewSet),
