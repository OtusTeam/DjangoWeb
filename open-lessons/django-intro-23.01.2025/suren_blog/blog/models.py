from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):

    class Meta:
        ordering = ["-published"]
        indexes = [
            models.Index(fields=["-published"]),
        ]

    class Status(models.TextChoices):
        DRAFT = "DR", "Draft"
        PUBLISHED = "PB", "Published"

    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT,
        db_index=True,
    )
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_posts",
    )
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
