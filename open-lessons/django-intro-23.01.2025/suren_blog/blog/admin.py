from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = "title", "status", "published", "created", "author"
    list_filter = "status", "published", "created", "author"
    search_fields = "title", "body"
