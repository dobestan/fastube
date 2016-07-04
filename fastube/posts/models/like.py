from django.db import models

from users.models import User


class Like(models.Model):

    user = models.ForeignKey(User)
    post = models.ForeignKey("Post")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
