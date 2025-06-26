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

    def __str__(self):
        return f"Заказ #{self.pk}"

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