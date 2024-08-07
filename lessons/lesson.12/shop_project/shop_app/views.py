"""
Create
Read
Update
Delete
"""

from django.views.generic import TemplateView, ListView, DetailView

from shop_app.models import Category, Product


class IndexView(TemplateView):
    template_name = "shop_app/index.html"


class CategoriesMinListView(TemplateView):
    template_name = "shop_app/categories.html"

    extra_context = {
        "pi": 3.1415,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            categories=Category.objects.all(),
        )
        return context


class CategoriesListView(ListView):
    model = Category
    template_name = "shop_app/categories.html"
    context_object_name = "categories"


class CategoryDetailView(DetailView):
    model = Category


class ProductsListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
