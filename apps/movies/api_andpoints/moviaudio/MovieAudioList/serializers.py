from rest_framework import serializers

from apps.movies.models import MovieAudio


class MovieAudioListSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieAudio
        fields = '__all__'