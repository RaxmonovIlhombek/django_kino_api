from rest_framework.generics import CreateAPIView, ListAPIView
from apps.meta.models import Comment 
from apps.meta.api_endpoints.comment.CommentCreate.serializers import CommentCreateSerializer,CommentListSerializer
class CommentCreateView(CreateAPIView):
    serializer_class = CommentCreateSerializer

class CommentListView(ListAPIView):
    serializer_class = CommentListSerializer

    def get_queryset(self):
        movie_id = self.kwargs.get("movie_di")
        return Comment.objects.filter(movie_id=movie_id).order_by("-created_at")
