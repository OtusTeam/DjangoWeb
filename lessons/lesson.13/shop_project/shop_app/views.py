"""
Create
Read
Update
Delete
"""
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    DeleteView, UpdateView,
)

from shop_app.models import Category, Product
from shop_app.forms import CategoryForm


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


class CategoryCreateView(CreateView):
    template_name = "shop_app/category-create.html"
    model = Category
    form_class = CategoryForm
    # success_url = reverse_lazy("shop_app:categories")

    # success_url = reverse_lazy("shop_app:categories")

    # def get_success_url(self):
    #     return reverse("shop_app:category", kwargs={"pk": self.object.pk})
    #


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy("shop_app:categories")


class CategoryUpdateView(UpdateView):
    template_name = "shop_app/category-update.html"
    model = Category
    form_class = CategoryForm

    # def get_success_url(self):
    #     return reverse("shop_app:category", kwargs={"pk": self.object.pk})


class ProductsListView(ListView):
    # model = Product
    queryset = Product.objects.filter(archived=False).all()


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = [
        "title",
        "description",
        "price",
        "categories",
    ]

    # success_url = reverse_lazy("shop_app:products")
    # def get_success_url(self):
    #     return reverse("shop_app:product", kwargs={"pk": self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("shop_app:products")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class ProductUpdateView(UpdateView):
    template_name_suffix = "_update_form"
    model = Product
    fields = [
        "title",
        "description",
        "price",
        "categories",
    ]
