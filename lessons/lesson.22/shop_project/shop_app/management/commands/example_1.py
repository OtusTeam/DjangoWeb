from io import BytesIO
from datetime import datetime

from django.core.management import BaseCommand
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from shop_app.models import Product
from .py_models import FooBar

# from shop_app.serializers import ProductSerializer


class NonUnicodeRenderer(JSONRenderer):
    ensure_ascii = False


class FooBarSerializer(serializers.Serializer):
    spam = serializers.CharField()
    eggs = serializers.CharField()
    created_at = serializers.DateTimeField()
    tags = serializers.ListField(child=serializers.CharField())


class ProductSimpleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    archived = serializers.BooleanField()


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Start demo renderer #1"))
        product = Product.objects.first()
        serializer = ProductSimpleSerializer(instance=product)
        # print("Serializer:", serializer)
        print("Serializer data:", serializer.data)

        products = Product.objects.all()
        serializer_many = ProductSimpleSerializer(instance=products, many=True)
        print("Serializer m data:", serializer_many.data)

        renderer = JSONRenderer()
        json_bytes_product = renderer.render(serializer.data)
        print("json bytes:", json_bytes_product)
        non_unicode_renderer = NonUnicodeRenderer()
        print("ensure ascii", non_unicode_renderer.ensure_ascii)
        print(
            "many products json bytes:",
            non_unicode_renderer.render(serializer_many.data),
        )

        foo_bar = FooBar(
            spam="spam qwe",
            eggs="eggs abc",
            created_at=datetime.now(),
            tags=("python", "monty"),
        )
        print("foo bar:", foo_bar)
        serializer_foobar = FooBarSerializer(instance=foo_bar)
        print("foo bar serializer data:", serializer_foobar.data)

        rendered_foobar = renderer.render(serializer_foobar.data)
        print("rendered json bytes:", rendered_foobar)

        print()
        print()
        parser = JSONParser()
        file_foobar = BytesIO(rendered_foobar)
        file_foobar.seek(0)
        data_foobar: dict = parser.parse(file_foobar)
        print("parse bytes, result:", data_foobar)

        data_foobar.pop("spam")
        serializer_foobar = FooBarSerializer(data=data_foobar)
        print("is valid foobar data:", serializer_foobar.is_valid())
        print("foobar data:", serializer_foobar.data)
        print("foobar validated_data:", serializer_foobar.validated_data)
        print("foobar serializer errors:", serializer_foobar.errors)
        print(renderer.render(serializer_foobar.errors))

        self.stdout.write(self.style.SUCCESS("Finished demo renderer #1"))
