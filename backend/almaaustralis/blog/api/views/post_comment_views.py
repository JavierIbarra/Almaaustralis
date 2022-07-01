from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from blog.models import PostComment


from blog.models import Post
from blog.api.serializers.post_comment_serializers import PostCommentSerializer

class PostCommentListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return PostComment.objects.filter(post = self.kwargs['pk'])

class PostCommentCreateAPIView(generics.CreateAPIView):
    serializer_class = PostCommentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return PostComment.objects.all()
    