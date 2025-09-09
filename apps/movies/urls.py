from django.urls import path
from apps.movies.api_andpoints import genre, language, movie, moviaudio


urlpatterns = [
    path('genres/',genre.GenreListView.as_view(), name='genres_list'),
    path('language/',language.LanguageListView.as_view(), name='language_list'),
    path('movies/',movie.MovieListView.as_view(), name='movies_list'),
    path('movieaudio/',moviaudio.MovieAudioListView.as_view(), name='movieaudio_list'),
]


