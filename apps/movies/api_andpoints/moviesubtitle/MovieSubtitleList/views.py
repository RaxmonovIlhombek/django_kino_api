from rest_framework.views import APIView
from rest_framework.response import Response


from apps.movies.models import MovieSubtitle
from .serializers import MovieSubtitleListSerializers



class MovieSubtitleListView(APIView):
    def get(felf,crequest):
        moviesubtitle = MovieSubtitle.objects.all()
        serializers = MovieSubtitleListSerializers(moviesubtitle, many=True)
        return Response(serializers.data, status=200)
    


__all__ = ['MovieSubtitleListView']    