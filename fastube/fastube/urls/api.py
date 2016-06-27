from django.conf.urls import url

from posts.api import *


urlpatterns = [
    url(r'^posts/$', PostListAPIView.as_view()),
]
