from rest_framework.views import APIView
from rest_framework.response import Response


from apps.movies.models import Genre
from .serializers import GenreListSerializers



class GenreListView(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        seializers = GenreListSerializers(genres, many=True)
        return Response(seializers.data, status=200)


__all__= ['GenreListView']