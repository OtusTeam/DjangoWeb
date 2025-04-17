from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField(
        blank=True,
        null=False,
    )
    release_date = models.DateField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    age_rating = models.ForeignKey(
        to="AgeRating",
        on_delete=models.PROTECT,
        related_name="movies",
        null=True,
    )

    class Meta:
        ordering = ("id",)

    def __str__(self) -> str:
        return self.title


class AgeRating(models.Model):
    name = models.CharField(
        max_length=10,
        primary_key=True,
    )
    description = models.TextField(
        null=False,
        blank=True,
    )

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name
