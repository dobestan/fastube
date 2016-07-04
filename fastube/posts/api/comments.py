from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from posts.models import Post
from posts.serializers import CommentModelSerializer


class PostCommentListCreateAPIView(ListAPIView):
    serializer_class = CommentModelSerializer

    def get_queryset(self):
        post = Post.objects.get(hash_id=self.kwargs.get("slug"))
        return post.comment_set.all()

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(hash_id=self.kwargs.get("slug"))
        comment = post.comment_set.create(
            content=request.POST.get("content"),
            user=request.user,
        )

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "username": request.user.username,
                "content": comment.content,
            },
        )
