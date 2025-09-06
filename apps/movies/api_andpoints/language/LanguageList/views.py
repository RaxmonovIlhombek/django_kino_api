from rest_framework.views import APIView
from rest_framework.response import Response


from apps.movies.models import Language
from .serializers import LanguageListSerializers


class LanguageListView(APIView):
    def get(self,request):
        language = Language.objects.all()
        serializers = LanguageListSerializers(language, many=True)
        return Response(serializers.data, status=200)
    
__all__= ['LanguageListView']

