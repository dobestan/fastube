from django.db.models.signals import post_save
from django.dispatch import receiver

from posts.models import Post


@receiver(post_save, sender=Post)
def post_save_post(sender, instance, created, **kwargs):
    from hashids import Hashids

    if not instance.hash_id:
        hashids = Hashids(salt="fastube", min_length=6)  # FIXME: should have awesome salt

        instance.hash_id = hashids.encode(instance.id)
        instance.save()
