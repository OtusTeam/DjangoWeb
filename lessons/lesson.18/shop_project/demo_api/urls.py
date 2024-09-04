from django.urls import path

from .views import (
    PingApiView,
)

app_name = "demo_api"

urlpatterns = [
    path("ping/", PingApiView.as_view(), name="ping"),
]
