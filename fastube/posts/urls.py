from django.conf.urls import url

from posts.views import *


urlpatterns = [
    url(r'^new/$', PostCreateFormView.as_view(), name="signup"),
]
