import textwrap

from django.contrib import admin

from .models import Category, Product, Order, OrderProduct


class CategoryInline(admin.TabularInline):
    model = Product.categories.through


class ProductInline(admin.TabularInline):
    model = Category.products.through


class OrdersForProductInline(admin.TabularInline):
    model = Product.orders.through


class ProductsForOrderInline(admin.TabularInline):
    model = Order.products.through


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = "pk", "name", "description"
    list_display_links = "pk", "name"
    # list_filter = "name", "description"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
        OrdersForProductInline,
    ]
    list_display = "pk", "title", "price", "categories_list", "description_short", "archived"
    list_display_links = "pk", "title"
    list_filter = "categories",

    def categories_list(self, obj: Product) -> str:
        categories = obj.categories.all()
        return ", ".join(c.name for c in categories)

    def description_short(self, obj: Product) -> str:
        return textwrap.shorten(
            obj.description,
            width=50,
            # placeholder="...",
        )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductsForOrderInline,
    ]
    list_display = "pk", "user", "status", "address"
    list_display_links = "pk", "user", "status"
    list_filter = "status",


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = "pk", "order", "product", "quantity", "price"
    list_display_links = "pk", "order", "product"
