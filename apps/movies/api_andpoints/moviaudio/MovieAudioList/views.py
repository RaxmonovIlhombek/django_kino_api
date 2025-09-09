from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MovieAudioListSerializers
from apps.movies.models import MovieAudio



class MovieAudioListView(APIView):
    def get(self, request):
        movieaudio = MovieAudio.objects.all()
        serializers = MovieAudioListSerializers(movieaudio, many=True)
        return Response(serializers.data, status=200)

__all__ = ["MovieAudioListView"]    





