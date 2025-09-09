from rest_framework.views import APIView
from rest_framework.response import Response

from apps.movies.models import PosterImage
from .serializers import PosterImageListSerializers


class PosterImageListView(APIView):
    def get(self, request):
        posterimage = PosterImage.objects.all()
        serializers = PosterImageListSerializers(posterimage, many=True)
        return Response(serializers.data, status=200)
    

__all__ = ['PosterImageListView']    
        









