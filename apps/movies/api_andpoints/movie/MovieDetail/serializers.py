from rest_framework import serializers

from apps.movies.api_andpoints.subtitle.serializers import MovieSubtitleMiniSerializer
from apps.movies.api_andpoints.moviaudio.serializers import MovieAudioDetailSerializer
from apps.movies.models import Movie



class MovieDetailSerializer(serializers.ModelSerializer):
    moviesubtitle_set = MovieSubtitleMiniSerializer(many=True)
    movieaudio_set = MovieAudioDetailSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'country', 'description',
                  'age_restriction', 'year', 'movie_genre',
                  'moviesubtitle_set', 'movieaudio_set',
                  'posterimage_set', 'moviefile_set']