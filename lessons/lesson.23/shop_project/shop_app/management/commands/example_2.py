from datetime import datetime

from django.core.management import BaseCommand
from rest_framework import serializers

from .py_models import FooBar


class FooBarSerializer(serializers.Serializer):
    spam = serializers.CharField()
    eggs = serializers.CharField()
    created_at = serializers.DateTimeField(default=datetime.now)
    tags = serializers.ListField(
        child=serializers.CharField(),
        default=tuple,
    )

    def create(self, validated_data):
        return FooBar(**validated_data)

    def update(self, instance, validated_data):
        instance.spam = validated_data.get("spam", instance.spam)
        instance.eggs = validated_data.get("eggs", instance.eggs)
        instance.created_at = validated_data.get("created_at", instance.created_at)
        instance.tags = tuple(validated_data.get("tags", instance.tags))
        # instance.save()
        return instance


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Start demo renderer #1"))
        new_data = {"spam": "spam val", "eggs": "eggs val"}
        serializer = FooBarSerializer(data=new_data)
        serializer.is_valid(raise_exception=True)
        foo_bar = serializer.save()
        print("created foobar", foo_bar)
        update_data = {"eggs": "six pack", "tags": ("fizz", "buzz")}
        serializer = FooBarSerializer(instance=foo_bar, data=update_data, partial=True)
        serializer.is_valid(raise_exception=True)
        new_foo_bar = serializer.save()
        print("updated foobar", foo_bar)
        print("is foo bar the same?", foo_bar is new_foo_bar)
        self.stdout.write(self.style.SUCCESS("Finished demo renderer #1"))
