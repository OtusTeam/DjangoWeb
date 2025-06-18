from django.contrib import admin
from shop_app.models import Product, Category
import textwrap


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "pk", "title", "categories_list", "description_short", "price"
    list_display_links = ("pk", "title")

    def categories_list(self, obj: Product):
        return ", ".join([category.title for category in obj.categories.all()])

    def description_short(self, obj: Product):
        return textwrap.shorten(obj.description, width=20, placeholder=" <...>")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "pk", "title", "description"
