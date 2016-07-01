from django.db import models


class BaseNotification(models.Model):

    sender = models.CharField(
        max_length=128,
    )
    receiver = models.CharField(
        max_length=128,
    )

    content = models.TextField(
    )

    response_status_code = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def send_notification(self):
        raise NotImplementedError
