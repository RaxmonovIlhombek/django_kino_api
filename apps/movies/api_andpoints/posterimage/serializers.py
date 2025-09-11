from rest_framework import serializers

from apps.movies.models import PosterImage

class PosterImageDetailSeializers(serializers.ModelSerializer):
    class Meta:
        model = PosterImage
        fields = ['id','language','movie','image']







        