from rest_framework.views import APIView
from rest_framework.response import Response

from apps.movies.models import Country
from .serializers import CountryListSeralizers



class CountryListView(APIView):
    def get(self, request):
        country = Country.objects.all()
        serializers = CountryListSeralizers(country, many=True)
        return Response(serializers.data, status=200)


__all__ = ['CountryListView']







