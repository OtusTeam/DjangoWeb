from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

UserModel = get_user_model()


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["pk"]

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=False, blank=True)

    def get_absolute_url(self):
        return reverse("shop_app:category", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        ordering = ["pk"]

    title = models.CharField(max_length=100, unique=False)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    archived = models.BooleanField(default=False)
    categories = models.ManyToManyField(
        to=Category,
        related_name="products",
        # unique=True,
    )

    def get_absolute_url(self):
        return reverse("shop_app:product", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Order(models.Model):
    class Meta:
        ordering = ["pk"]

    class Status(models.TextChoices):
        NEW = "NEW", "New"
        PENDING = "PENDING", "Pending"
        SHIPPED = "SHIPPED", "Shipped"
        DELIVERED = "DELIVERED", "Delivered"
        CANCELLED = "CANCELLED", "Cancelled"

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.PROTECT,
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.NEW,
    )
    address = models.TextField(null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # products = models.ManyToManyField(
    #     to=Product,
    #     through="OrderProduct",
    # )

    # def __str__(self):
    #     pass


# class UserProfile(models.Model):
#     class Meta:
#         ordering = ["pk"]
#
#     user = models.OneToOneField(to=UserModel, on_delete=models.PROTECT)


# class OrderProduct(models.Model):
#     class Meta:
#         ordering = ["pk"]
#
#     product = models.ForeignKey(
#         to=Product,
#         on_delete=models.PROTECT,
#     )
#     order = models.ForeignKey()
#     quantity = models.IntegerField(default=1)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#
#     def __str__(self):
#         return f"OrderProduct {self.pk} {self.product} {self.quantity} {self.price}"
#
#
# class User:
#
#     def __init__(self, username: str):
#         self.username = username
#
#
# john = User(username="john")
#
# print("!!!!")
# print(type(john))
# print(type(User))
#
# """
# Джон - экземпляр класса User
# Джон типа (of type) User
#
# User of type ...? (metaclass)
# """