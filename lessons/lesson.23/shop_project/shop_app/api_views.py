"""
Model ViewSet:
- get list
- get details
- update (partial) - PATCH
- update (full) - PUT
- delete
"""
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.functions import Lower
from django.utils import timezone
from rest_framework import viewsets, mixins, pagination
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    AllowAny,
)
from rest_framework.response import Response

from .models import Category, Product
from .serializers import (
    CategoryMinimalSerializer,
    CategoryDetailSerializer,
    CategorySerializer,
    CategorySerializerV2,
    ProductSerializer,
    ProductSerializerCreate,
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
    # serializer_class = CategorySerializer

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return CategorySerializerV2
        return CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated | AllowAny]
    # permission_classes = [IsAdminUser & IsRegisteredMonthAgo]



class TimezonePagination(pagination.PageNumberPagination):
    page_size = 5

    def get_paginated_response(self, data):
        return Response({
            'current_time': timezone.now(),
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })


# FIltering pagination api для Products
# get (list), get (detail), post (list),
class FilteringProductViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # serializer_class = ProductSerializerCreate
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [AllowAny]
    # pagination_class = PageNumberPagination
    pagination_class = TimezonePagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'archived']


    def get_serializer_class(self):
        if self.action == 'create':
            return ProductSerializerCreate
        return ProductSerializer

    @action(detail=True, methods=['get'])
    def check_price(self, request, pk=None):
        product = self.get_object()
        result = product.price > 100
        return Response({'status': result})
