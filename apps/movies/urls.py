from django.urls import path
from apps.movies.api_andpoints import genre


urlpatterns = [
    path('genres/',genre.GenreListView.as_view(), name='genres_list'),
]


