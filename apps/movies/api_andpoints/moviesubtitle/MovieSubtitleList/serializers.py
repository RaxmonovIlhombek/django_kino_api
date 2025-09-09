from rest_framework import serializers

from apps.movies.models import MovieSubtitle

class MovieSubtitleListSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieSubtitle
        fields = '__all__'



