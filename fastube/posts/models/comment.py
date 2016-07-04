from django.db import models

from users.models import User


class Comment(models.Model):

    user = models.ForeignKey(User)
    post = models.ForeignKey("Post")

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
