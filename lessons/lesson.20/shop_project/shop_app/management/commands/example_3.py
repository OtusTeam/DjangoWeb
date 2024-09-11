from collections.abc import Iterable
from datetime import datetime

from django.core.management import BaseCommand
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .py_models import FooBar


def validate_unique_values(values: Iterable):
    if len(set(values)) != len(tuple(values)):
        raise serializers.ValidationError("All values must be unique")


class FooBarSerializer(serializers.Serializer):
    spam = serializers.CharField()
    eggs = serializers.CharField()
    created_at = serializers.DateTimeField(default=datetime.now)
    tags = serializers.ListField(
        child=serializers.CharField(),
        default=tuple,
        validators=[validate_unique_values],
    )

    def validate_spam(self, value: str):
        if value == "spam":
            raise serializers.ValidationError(
                "spam field should be different from 'spam'"
            )
        return value.lower()

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
        # new_data = {"spam": "Spam Value", "eggs": "eggs val"}
        new_data = {"spam": "spam", "eggs": "eggs val", "tags": ["a", "b", "a"]}
        serializer = FooBarSerializer(data=new_data)
        serializer.is_valid()
        print("errors:", serializer.errors)
        print("data:", serializer.data)

        renderer = JSONRenderer()
        print("render errors:", renderer.render(serializer.errors))
        self.stdout.write(self.style.SUCCESS("Finished demo renderer #1"))
