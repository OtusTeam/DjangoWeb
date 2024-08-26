"""
Create
Read
Update
Delete
"""

from celery.result import AsyncResult
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)

from shop_app.models import Category, Product, Order
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
    # queryset = Category.objects.order_by("name").all()
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
    queryset = (
        Product.objects.filter(archived=False).prefetch_related("categories").all()
    )


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

    # def form_valid(self, form):
    #     self.object.send_created_email()
    #     return super().form_valid(form)


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


class OrdersListView(ListView):
    queryset = (
        Order.objects
        # .prefetch_related("order_products")
        # .prefetch_related("order_products__product")
        .prefetch_related("order_products__product__categories")
        .select_related("user")
        .all()
    )


def task_status(request: HttpRequest) -> HttpResponse:
    context = {}
    task_id = request.GET.get("task_id")
    result = AsyncResult(task_id)
    is_ready = result.ready()
    status = result.status
    task_result = result.result
    context.update(
        task_id=task_id,
        is_ready=is_ready,
        status=status,
        result=task_result,
    )
    return render(
        request=request,
        template_name="shop_app/task_status.html",
        context=context,
    )
