from rest_framework import serializers
from shop_app.models import Category, Product


class CategoryMinimalSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "description",
            "id_hash",
            "name_hash",
        )

    id_hash = serializers.IntegerField()
    name_hash = serializers.IntegerField()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "description",
        )


class CategoryHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "self",
        )

    self = serializers.HyperlinkedIdentityField(
        view_name="shop_app_api:category-detail",
    )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "description",
            "price",
            "archived",
            "categories",
        )

    # categories = serializers.StringRelatedField(many=True)
    # categories = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name="shop_app_api:category-detail",
    # )
    categories = CategoryHyperlinkedModelSerializer(
        many=True,
        required=False,
    )


class ProductSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "description",
            "price",
            "archived",
            "categories",
        )

    # categories = serializers.StringRelatedField(many=True)
    # categories = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name="shop_app_api:category-detail",
    # )
    categories = serializers.PrimaryKeyRelatedField(
        many=True,
        required=False,
        queryset=Category.objects.all()
    )
