from rest_framework import serializers

from apps.movies.models import Language


class LanguageListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
        