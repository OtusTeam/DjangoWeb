import textwrap

from django.contrib import admin

from movies.models import Movie, AgeRating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "short_description",
        "release_date",
        "duration",
    )
    list_display_links = ("title",)
    list_filter = ("title",)
    search_fields = (
        "title",
        "description",
    )

    def short_description(self, obj: Movie) -> str:
        return textwrap.wrap(
            obj.description,
            width=50,
        )[0]


@admin.register(AgeRating)
class AgeRatingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "short_description",
    )
    list_display_links = ("name",)
    list_filter = ("name",)
    search_fields = (
        "name",
        "description",
    )

    def short_description(self, obj: Movie) -> str:
        return textwrap.wrap(
            obj.description,
            width=50,
        )[0]
