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
