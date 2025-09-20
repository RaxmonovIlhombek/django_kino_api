from rest_framework import serializers
from apps.meta.models import Comment

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "movie", "watch_session", "text", "created_at"]


class CommentListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "movie_title", "text", "created_at"]
