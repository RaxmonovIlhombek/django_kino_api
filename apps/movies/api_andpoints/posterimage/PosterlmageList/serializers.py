from rest_framework import serializers

from apps.movies.models import Posterlmage


class PosterImageListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Posterlmage
        fields = '__all__'



