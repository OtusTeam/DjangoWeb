from rest_framework import (
    viewsets,
    views,
    response,
    mixins,
    decorators,
)
from mainapp.models import Category, Animal
from .serializers import CategorySerializer, AnimalSerializer, AnimalCreateSerializer
from . import filters
from . paginators import TimezonePagination, CustomCursorPagination


# class AnimalListView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

class AnimalViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
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
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryList(views.APIView):

    def get(self, request, format=None):
        quetyset = Category.objects.all()
        serializer = CategorySerializer(quetyset, many=True)
        response_json = serializer.data
        # return response.Response({})
        return response.Response(response_json)
