from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.TasksIndexView.as_view(), name="index"),
    path("all/", views.AllTasksListView.as_view(), name="all"),
    path("done/", views.DoneTasksListView.as_view(), name="done"),
    path("create/", views.TaskCreateView.as_view(), name="create"),
    path("<int:pk>/", views.TaskDetailView.as_view(), name="detail"),
]
