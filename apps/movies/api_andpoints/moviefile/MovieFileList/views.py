from rest_framework.views import APIView
from rest_framework.response import Response

from apps.movies.models import MovieFile
from .serializers import MovieFileListSerializers



class MovieFileListView(APIView):
    def get(self, request):
        moviefile = MovieFile.objects.all()
        serializers = MovieFileListSerializers(moviefile, many=True)
        return Response(serializers.data, status=200)
    

__all__ = ['MovieFileListView']    



