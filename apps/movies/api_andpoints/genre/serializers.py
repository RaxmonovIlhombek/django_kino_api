from rest_framework import serializers

from apps.movies.models import Genre


class GenreDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']



