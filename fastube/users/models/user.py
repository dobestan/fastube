from django.contrib.auth.models import AbstractUser
from django.db import models

from .follow import Follow


class User(AbstractUser):

    phonenumber = models.CharField(
        max_length=16,
        blank=True,
        null=True,
    )

    # follow 라는 행위에 대해서,
    # follower ( 주체 ) => followee ( 객체 )

    follower_set = models.ManyToManyField(
        "self",
        symmetrical=False,
        through=Follow,
        through_fields=("followee", "follower"),
        related_name="followee_set",
    )
