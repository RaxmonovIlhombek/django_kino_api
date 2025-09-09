from rest_framework import serializers

from apps.movies.models import MovieFile

class MovieFileListSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieFile
        fields = '__all__'

        