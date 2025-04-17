from rest_framework import viewsets

from movies.models import Movie, AgeRating
from movies.serializers import (
    MovieSerializer,
    MovieSerializerExtended,
    AgeRatingSerializer,
)


class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if self.action == "retrieve":
            qs = qs.select_related("age_rating")
        return qs

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieSerializerExtended
        return MovieSerializer

    # @action(detail=False, methods=['get'], url_path='age-ratings/(?P<age_rating>[^/.]+)', url_name='age-rating-movies')
    # def age_rating_movies(self, request, age_rating=None):
    #     # redis = ...
    #     try:
    #         # redis.set("age_rating", age_rating)
    #         # Filter movies by the provided age rating
    #         movies = self.queryset.filter(age_rating__name=age_rating)
    #     except AgeRating.DoesNotExist:
    #         return Response({"detail": "Age rating not found."}, status=status.HTTP_404_NOT_FOUND)
    #
    #     serializer = self.get_serializer(movies, many=True)
    #     return Response(serializer.data)


class AgeRatingViewSet(viewsets.ModelViewSet):
    queryset = AgeRating.objects.all()
    serializer_class = AgeRatingSerializer
