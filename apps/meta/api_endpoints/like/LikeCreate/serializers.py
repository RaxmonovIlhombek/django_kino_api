from rest_framework import serializers
from apps.meta.models import Like

class LikeCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


