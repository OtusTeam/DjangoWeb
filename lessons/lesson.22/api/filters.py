from django_filters import rest_framework as filters
from mainapp.models import Animal


class AnimalFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = Animal
        fields = ['name']
