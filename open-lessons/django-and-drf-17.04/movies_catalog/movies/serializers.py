from rest_framework import serializers

from movies.models import Movie, AgeRating


class AgeRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeRating
        fields = (
            "name",
            "description",
        )


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "release_date",
            "duration",
            "age_rating",
        )


class MovieSerializerExtended(MovieSerializer):
    age_rating = AgeRatingSerializer(many=False)

    class Meta(MovieSerializer.Meta): ...
