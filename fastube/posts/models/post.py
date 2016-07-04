from django.core.urlresolvers import reverse
from django.db import models

from users.models import User


class Post(models.Model):

    user = models.ForeignKey(User)

    hash_id = models.CharField(
        max_length=8,
        blank=True,
        null=True,
    )

    video_id = models.CharField(
        max_length=16,
    )
    video_original_title = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )

    title = models.CharField(
        max_length=256,
    )
    content = models.TextField()

    thumbnail_image = models.ImageField(
        blank=True,
        null=True,
    )

    like_user_set = models.ManyToManyField(
        User,
        related_name="like_post_set",
        through="Like",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_youtube_thumbnail_image_url(self):
        from posts.utils.youtube import get_youtube_thumbnail_image_url\
            as get_youtube_thumbnail_image_url_from_video_id
        return get_youtube_thumbnail_image_url_from_video_id(self.video_id)
    youtube_thumbnail_image_url = property(get_youtube_thumbnail_image_url)

    def get_thumbnail_image_url(self):
        if self.thumbnail_image:
            return self.thumbnail_image.url
        return self.youtube_thumbnail_image_url
    thumbnail_image_url = property(get_thumbnail_image_url)

    def get_youtube_original_url(self):
        from posts.utils.youtube import get_youtube_original_url as get_youtube_original_url_from_video_id
        return get_youtube_original_url_from_video_id(self.video_id)
    youtube_original_url = property(get_youtube_original_url)

    def get_youtube_embed_url(self):
        from posts.utils.youtube import get_youtube_embed_url as get_youtube_embed_url_from_video_id
        return get_youtube_embed_url_from_video_id(self.video_id)
    youtube_embed_url = property(get_youtube_embed_url)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={
            "slug": self.hash_id,
        })
