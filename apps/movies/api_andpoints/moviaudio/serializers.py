from rest_framework import serializers

from apps.movies.models import MovieAudio



class MovieAudioDetailSerializer(serializers.ModelSerializer):    
    class Meta:
        model = MovieAudio
        fields = ['id', 'language', 'movie', 'name']