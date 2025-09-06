from rest_framework import serializers

from apps.movies.models import Genre


class GenreListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']
