from rest_framework import serializers
from mainapp.models import Category, Animal


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AnimalSerializer(serializers.ModelSerializer):
    category = serializers.HyperlinkedRelatedField(view_name='api:category-detail', read_only=True)
    food = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)
    class Meta:
        model = Animal
        fields = '__all__'


class AnimalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'
