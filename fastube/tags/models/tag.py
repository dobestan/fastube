from django.db import models

from posts.models import Post


class Tag(models.Model):

    name = models.CharField(
        max_length=256,
    )
    post_set = models.ManyToManyField(Post)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return "#{name}".format(name=self.name)

    def __str__(self):
        return self.full_name
