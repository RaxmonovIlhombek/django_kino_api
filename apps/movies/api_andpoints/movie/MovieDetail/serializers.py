from rest_framework import serializers

from apps.movies.api_andpoints.subtitle.serializers import MovieSubtitleMiniSerializer
from apps.movies.api_andpoints.moviaudio.serializers import MovieAudioDetailSerializer
from apps.movies.api_andpoints.posterimage.serializers import PosterImageDetailSeializers
from apps.movies.api_andpoints.moviefile.serializers import MovieFileDetailSerializers
from apps.movies.api_andpoints.genre.serializers import GenreDetailSerializers
from apps.movies.models import Movie



class MovieDetailSerializer(serializers.ModelSerializer):
    moviesubtitle_set = MovieSubtitleMiniSerializer(many=True)
    movieaudio_set = MovieAudioDetailSerializer(many=True)
    posterimage_set = PosterImageDetailSeializers(many=True)
    moviefile_set = MovieFileDetailSerializers(many=True)
    movie_genre = GenreDetailSerializers(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'country', 'description',
                  'age_restriction', 'year', 'movie_genre',
                  'moviesubtitle_set', 'movieaudio_set',
                  'posterimage_set', 'moviefile_set']