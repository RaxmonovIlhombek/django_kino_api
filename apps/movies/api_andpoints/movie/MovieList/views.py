from rest_framework.views import APIView
from rest_framework.response import Response


from apps.movies.models import Movie
from .serializers import MovieListSerializers



class MovieListView(APIView):
    def get(self, request):
        movie = Movie.objects.all()
        serializers = MovieListSerializers(movie, many=True)
        return Response(serializers.data, status=200)
    
__all__ = ["MovieListView"]    
