from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.meta.api_endpoints.like.LikeCreate.serializers import LikeCreateSerializers 




class LikeCreateView(APIView):
    serializer_class = LikeCreateSerializers

