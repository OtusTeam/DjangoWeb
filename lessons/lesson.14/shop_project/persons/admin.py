from django.contrib import admin

from .models import Person, Manager


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "age",
    list_display_links = "pk", "name"


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = "person_ptr_id", "name", "job_title", "experience"
    list_display_links = "person_ptr_id", "name", "job_title"
