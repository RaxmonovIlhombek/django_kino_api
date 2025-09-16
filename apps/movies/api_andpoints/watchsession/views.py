from rest_framework.response import Response
from rest_framework.views import APIView


from apps.movies.models import WatchSession
from .serializers import WatchSessionSerializers


class WatchSessionView(APIView):
    def get(self, request):
        watchsession = WatchSession.objects.all()
        serializers = WatchSessionSerializers(watchsession, many=True )
        return Response(serializers.data, status=200)
    
__all__ = ['WatchSessionView']    




