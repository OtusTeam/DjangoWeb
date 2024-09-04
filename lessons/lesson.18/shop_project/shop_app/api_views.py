"""
Model ViewSet:
- get list
- get details
- update (partial) - PATCH
- update (full) - PUT
- delete
"""

from django.db.models.functions import Lower
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Category, Product
from .serializers import (
    CategoryMinimalSerializer,
    CategoryDetailSerializer,
    CategorySerializer,
    ProductSerializer,
)


class CategoriesTopListAPIView(ListAPIView):
    """
    Top Categories view

    Top categories in our shop.
    Rating is based on alphabet.
    """

    queryset = (
        Category.objects
        # all to lower case
        .annotate(name_lower=Lower("name"))
        # sort by lower case
        .order_by("name_lower").all()[:10]
    )
    serializer_class = CategoryMinimalSerializer


class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
