from django.views.generic import View
from django.http.response import HttpResponse


class PostListAPIView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("posts:list")
