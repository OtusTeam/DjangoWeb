'''
from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Product(models.Model):
    class Meta:
        ordering = ["pk"]
        verbose_name_plural = "Товары"

    title = models.CharField(max_length=200, unique=True, verbose_name="Название")
    description = models.TextField(null=False, blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    categories = models.ManyToManyField(
        to="Category", related_name="products", verbose_name="Категория"
    )

    def __str__(self):
        return self.title


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Категории"
        ordering = ["pk"]

    title = models.CharField(
        max_length=200, unique=True, verbose_name="Название категории"
    )
    description = models.TextField(
        null=False, blank=True, verbose_name="Описание категории"
    )


    def __str__(self):
        return self.title

class Order(models.Model):
    class Meta:
        verbose_name_plural = "Заказы"
        ordering = ["pk"]
    
    class Status(models.TextChoices):
        NEW = "NEW", "Новый"
        CANCELLED = "CANCELLED", "Отменённый"
        PROCESSED = "PROCESSED", "Обработанный"
        IN_DELIVERY = "IN_DELIVERY", "В доставке"
        DELIVERED = "DELIVERED", "Доставленный"
    
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

class OrderProduct(models.Model):
    class Meta:
        verbose_name_plural = "Товары в заказах"
        ordering = ["pk"]

    order = models.ForeignKey(
        to=Order,
        on_delete=models.PROTECT,
        verbose_name="Заказ",
        related_name="order_products",
        blank=True,
    )

    product = models.ForeignKey(
        to=Product,
        on_delete=models.PROTECT,
        verbose_name="Товар",
        related_name="order_products",
        blank=True,
    )

    quantity = models.IntegerField(default=1, verbose_name="Количество товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена товара")
'''
from django.core.management.base import BaseCommand
from shop_app.models import Order, Product, Category, OrderProduct
from django.db.models import F, Count, Sum, Prefetch
from django.db.models.functions import Length
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Command(BaseCommand):
    help = 'Shows examples of commands'

    def create_categories_fast(self):
        new_names = ('laptops', 'smartphones', 'tablets', 'smartwatches')
        new_categories = [Category(title=name) for name in new_names]
        Category.objects.bulk_create(new_categories)

    def show_short_categories(self):
        categories_qs = Category.objects.annotate(name_len=Length('title')).filter(name_len__lt=8).all()
        for category in categories_qs:
            self.stdout.write(f'{category} - {category.name_len}')


    def create_categories_slow(self):
        new_names = ('fans', 'earphones', 'modiles', 'vr-glasses')
        for name in new_names:
            Category.objects.create(title=name)

    def simple_filtres(self):
        op_qs = OrderProduct.objects.filter(quantity=1).select_related("product")
        for op in op_qs:
            self.stdout.write(f'{op.product} - {op.order}')

    def categories_count(self):
        count_cats = Category.objects.count()
        self.stdout.write(f'Количество категорий: {count_cats}')

    def show_price_mult_count(self):
        op_qs = OrderProduct.objects.annotate(full_price=F('quantity') * F('price')).filter(full_price__gt=100).all()
        op_qs = OrderProduct.objects.annotate(full_price=F('quantity') * F('price')).filter(quantity__lte=2).all()
        for op in op_qs:
            self.stdout.write(f'{op.product} | {op.price} * {op.quantity} = {op.full_price}')

    def show_order_with_op(self):
        order_qs = Order.objects.all()
        for order in order_qs:
            self.stdout.write(f'{order} - {[order for order in order.products.all().prefetch_related("order_products")]}')

    def defer_example(self):
        order_qs = Order.objects.defer("updated_at", 'created_at').all()
        for order in order_qs:
            print(order)

    def show_order_with_op_details(self):
        orders_qs = Order.objects.annotate(
            op_count=Count('order_products__pk'),
            total_quantity=Sum('order_products__quantity'),
        ).all()

        for order in orders_qs:
            self.stdout.write(f'Order {order.pk} have status is {order.status}')
            self.stdout.write(f'{order} - {order.op_count}, {order.total_quantity}')

    def show_users_with_orders(self):
        users_qs = UserModel.objects.prefetch_related('orders').all()
        for user in users_qs:
            self.stdout.write(f'{user.username} - {user.orders.all()}')

    def check_user_exists(self, name:str):
        user = UserModel.objects.filter(username=name)
        prefix = '' if user.exists() else "doesn't "
        self.stdout.write(f'User {user} {prefix}exists!')

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE('Start commands...'))

        # self.create_categories_slow()
        # self.create_categories_fast()
        # self.simple_filtres()
        # self.categories_count()
        # self.show_price_mult_count()
        # self.show_order_with_op()
        # self.defer_example()
        # self.show_order_with_op_details()
        # self.show_users_with_orders()
        # self.check_user_exists('guest')
        self.show_short_categories()
        self.stdout.write(self.style.SUCCESS('Command finished!'))