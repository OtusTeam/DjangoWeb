from django.urls import path, include
from rest_framework import routers

from movies import views

app_name = "movies"

router = routers.DefaultRouter()
router.register("movies", views.MoviesViewSet)
router.register("age-ratings", views.AgeRatingViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
