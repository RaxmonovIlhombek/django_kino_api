from rest_framework import serializers
from apps.meta.models import WatchSession

class WatchSessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchSession
        fields = '__all__'