from django.urls import path, include

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("add/", views.PostCreateView.as_view(), name="add"),
]
