from django.urls import path
from apps.meta.api_endpoints import watchsession, like, comment


urlpatterns = [
    path('watch-session-create/',
         watchsession.WatchSessionCreateView.as_view(),
         name='watch_session_create'),
    path('like-create/',
         like.LikeCreateView.as_view(),
         name='like_create'),
    path('comment-create/',
         comment.CommentCreateView.as_view(),
         name='comment_create'),          

]