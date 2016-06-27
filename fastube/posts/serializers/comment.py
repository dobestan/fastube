from rest_framework import serializers

from posts.models import Comment


class CommentModelSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source="user.username", )

    class Meta:
        model = Comment
        fields = [
            "username",

            "content",
        ]
