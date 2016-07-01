from .base import BaseNotification


class SMSNotification(BaseNotification):

    class Meta:
        verbose_name = "SMS Notification"
        verbose_name_plural = verbose_name
