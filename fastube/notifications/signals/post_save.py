from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.models import SMSNotification, SlackNotification


@receiver(post_save, sender=SMSNotification)
@receiver(post_save, sender=SlackNotification)
def post_save_notification(sender, instance, created, **kwargs):
    if created:
        instance.send_notification()
