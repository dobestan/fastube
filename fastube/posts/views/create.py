from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.shortcuts import render, redirect

from posts.utils import youtube


class PostCreateView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "posts/new.html",
            context={},
        )

    def post(self, request, *args, **kwargs):
        video_id = request.POST.get("video_id")
        title = request.POST.get("title")
        content = request.POST.get("content")

        thumbnail_image = request.FILES.get("thumbnail_image")

        post = request.user.post_set.create(
            video_id=video_id,
            title=title,
            content=content,
            thumbnail_image=thumbnail_image,
        )

        # FIXME: redirect to posts:detail
        return redirect(reverse("posts:create"))


class PostCreateConfirmView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return redirect(reverse("posts:create"))

    def post(self, request, *args, **kwargs):
        video_id = request.POST.get("video_id")
        title = request.POST.get("title")
        content = request.POST.get("content")

        return render(
            request,
            "posts/confirm.html",
            context={
                "video_id": video_id,
                "title": title,
                "content": content,

                "youtube_original_url": youtube.get_youtube_original_url(video_id),
                "youtube_embed_url": youtube.get_youtube_embed_url(video_id),

                "youtube_thumbnail_image_url": youtube.get_youtube_thumbnail_image_url(video_id),
            },
        )
