from django.contrib import admin
from shop_app.models import Product, Category, Order
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
'''
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="orders"
    )

    status = models.CharField(
        max_length=20,
        verbose_name="Статус заказа",
        choices=Status.choices,
        default=Status.NEW
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    products = models.ManyToManyField(
        to="Product",
        related_name="orders",
        through="OrderProduct",
        verbose_name="Товары заказа",
    )
    
'''
class OrderProductInline(admin.TabularInline):
    model = Order.products.through

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderProductInline
    ]
    list_display = ["pk", "status", "created_at", "updated_at", "user"]
    list_display_links = ("pk", "status", 'user')


    