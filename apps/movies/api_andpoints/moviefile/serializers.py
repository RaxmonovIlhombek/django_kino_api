from rest_framework import serializers
from apps.movies.models import MovieFile



class MovieFileDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieFile
        fields = ['id', 'language', 'movie', 'file']


