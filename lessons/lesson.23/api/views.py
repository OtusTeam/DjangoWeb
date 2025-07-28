from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import (
    viewsets,
    views,
    response,
    mixins,
    decorators,
    permissions,
)
from rest_framework.permissions import DjangoModelPermissions

from mainapp.models import Category, Animal, Food
from .serializers import CategorySerializer, AnimalSerializer, AnimalCreateSerializer, FoodSerializer
from . import filters
from . paginators import TimezonePagination, CustomCursorPagination
from .permissions import IsFoodMaster


# class AnimalListView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="Создать животное",
))
@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="Получить список животных",
    tags=['Животные', 'Список'],
))
class AnimalViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    # filterset_fields = ['name']
    filterset_class = filters.AnimalFilter
    # pagination_class = TimezonePagination
    pagination_class = CustomCursorPagination

    def get_queryset(self):
        return Animal.objects.all().prefetch_related('food')

    @decorators.action(detail=True, methods=['get'])
    def log_animal(self, request, pk=None):
        animal = self.get_object()
        print('Logging....')
        print(animal)
        return response.Response({'status': 'done...'})

    def get_serializer_class(self):
        if self.action == 'create':
            return AnimalCreateSerializer
        return self.serializer_class


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer


class CategoryList(views.APIView):

    def get(self, request, format=None):
        quetyset = Category.objects.all()
        serializer = CategorySerializer(quetyset, many=True)
        response_json = serializer.data
        # return response.Response({})
        return response.Response(response_json)


class FoodViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [DjangoModelPermissions]
