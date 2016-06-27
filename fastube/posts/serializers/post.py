from rest_framework import serializers

from posts.models import Post


class PostModelSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source="user.username", )

    class Meta:
        model = Post
        fields = [
            "title",
            "content",

            "youtube_original_url",

            "username",
        ]
