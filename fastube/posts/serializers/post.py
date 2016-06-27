from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostModelSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
        ]
