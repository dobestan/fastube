from rest_framework.generics import ListAPIView

from posts.models import Post
from posts.serializers import CommentModelSerializer


class PostCommentListAPIView(ListAPIView):
    serializer_class = CommentModelSerializer

    def get_queryset(self):
        post = Post.objects.get(hash_id=self.kwargs.get("slug"))
        return post.comment_set.all()
