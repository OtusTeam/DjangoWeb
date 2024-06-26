from random import randint

from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
)

from tasks.models import Task

ANSWER = 42


class TasksIndexView(TemplateView):
    template_name = "tasks/index.html"

    extra_context = {
        "answer": ANSWER,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            number=randint(1, 100),
        )
        return context


class AllTasksListView(ListView):
    model = Task


class DoneTasksListView(ListView):
    extra_context = {
        "title": "Done tasks",
    }
    queryset = Task.objects.filter(done=True).all()


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    template_name_suffix = "_create_form"
    fields = "title", "description"

    # success_url = reverse_lazy("tasks:all")
