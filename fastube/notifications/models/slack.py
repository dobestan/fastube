from .base import BaseNotification


class SlackNotification(BaseNotification):

    class Meta:
        verbose_name = "Slack Notification"
        verbose_name_plural = verbose_name
