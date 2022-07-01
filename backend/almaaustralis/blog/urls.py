from django.urls import path
from blog.api.views.post_comment_views import PostCommentListAPIView
from blog.api.views.tema_views import TemaListAPIView
from blog.api.views.post_views import * 

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post_detail'),
    path('posts/<int:pk>/comments/', PostCommentListAPIView.as_view(), name='comment_list'),
    path('temas/', TemaListAPIView.as_view(), name='tema_list'),
]
