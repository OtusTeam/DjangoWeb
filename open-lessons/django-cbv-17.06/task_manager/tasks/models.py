from django.db import models
from django.urls import reverse


class Task(models.Model):

    class Meta:
        ordering = "id",

    title = models.CharField(max_length=255)
    description = models.TextField(null=False, blank=True)
    done = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("tasks:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
