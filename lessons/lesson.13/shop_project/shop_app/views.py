'''CRUD for Product, Categories'''
from django.shortcuts import redirect, render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    DeleteView,
)
from shop_app.models import Product, Category
from .forms import CreateCategoryForm, CreateProductForm


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

class CreateCategoryView(CreateView):
    template_name = 'shop_app/product_form.html'
    def get(self, request, *args, **kwargs):
        form = CreateCategoryForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop_app:categories')
        return render(request, self.template_name, {'form': form})

class CategoryListView(ListView):
    model = Category
    template_name = "shop_app/categories.html"
    context_object_name = "categories"
    
class ProductCreateView(CreateView):
    model = Product
    fields = [
        'title',
        'price',
        'description',
        'categories'
    ]
    success_url = '/products/'

class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/products/'