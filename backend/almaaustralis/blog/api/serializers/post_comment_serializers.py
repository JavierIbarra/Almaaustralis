from blog.models import PostComment
from rest_framework import serializers


class PostCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostComment
        exclude = ('created',)