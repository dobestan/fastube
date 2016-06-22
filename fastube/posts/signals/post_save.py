from django.db.models.signals import post_save
from django.dispatch import receiver

from posts.models import Post


@receiver(post_save, sender=Post)
def post_save_post(sender, instance, created, **kwargs):
    from hashids import Hashids
    import requests
    from bs4 import BeautifulSoup

    if not instance.hash_id:
        hashids = Hashids(salt="fastube", min_length=6)  # FIXME: should have awesome salt

        instance.hash_id = hashids.encode(instance.id)
        instance.save()

    if created:
        response = requests.get(instance.youtube_original_url)
        dom = BeautifulSoup(response.content, "html.parser")
        title_element = dom.select_one("#watch-headline-title")
        title = title_element.text.strip()

        instance.video_original_title = title
        instance.save()
