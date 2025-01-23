"""
Create
Read
Update
Delete
"""

from django.contrib.auth.mixins import LoginRequiredMixin

# from django.db import transaction
# from django.shortcuts import render
# from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView

from .models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    # model = Post
    queryset = Post.objects.select_related("author")


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        "title",
        "body",
        # "author",
    ]

    # @transaction.atomic
    def form_valid(self, form):
        form.instance.author = self.request.user
        # self.request.user.profile.last_publication = timezone.now()
        return super().form_valid(form)
