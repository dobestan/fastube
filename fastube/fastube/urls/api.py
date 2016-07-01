from django.conf.urls import url, include

from posts.api import *


urlpatterns = [
    url(r'^posts/', include([
        url(r'^$', PostListAPIView.as_view(), name="list"),
        url(r'^(?P<slug>\w+)/comments/$', PostCommentListCreateAPIView.as_view(), name="comments"),
    ], namespace="posts")),
]
