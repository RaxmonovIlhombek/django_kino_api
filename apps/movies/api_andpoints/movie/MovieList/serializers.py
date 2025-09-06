from rest_framework import serializers

from apps.movies.models import Movie


class MovieListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'