from rest_framework import serializers
from apps.movies.models import Country


class CountryListSeralizers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


