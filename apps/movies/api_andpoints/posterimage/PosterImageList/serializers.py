from rest_framework import serializers

from apps.movies.models import PosterImage


class PosterImageListSerializers(serializers.ModelSerializer):
    class Meta:
        model = PosterImage
        fields = '__all__'



