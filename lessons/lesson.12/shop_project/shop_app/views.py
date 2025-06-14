from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from shop_app.models import Product


class IndexView(TemplateView):
    template_name = "shop_app/index.html"


def index(request):
    return render(request, "shop_app/index.html")


def show_products(request):
    products = Product.objects.all()
    return render(request, "shop_app/products.html", {"products": products})


class ProductListView(ListView):
    model = Product
    template_name = "shop_app/products.html"
    context_object_name = "products"


class ProductListTemplateView(TemplateView):
    template_name = "shop_app/product_list.html"
    extra_context = {"organization": "Компания проект"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
