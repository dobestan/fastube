from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model


@receiver(post_save, sender=get_user_model())
def post_save_user(sender, instance, created, **kwargs):
    if created:
        pass
