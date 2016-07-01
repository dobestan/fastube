from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model

import requests
from time import sleep


@receiver(post_save, sender=get_user_model())
def post_save_user(sender, instance, created, **kwargs):
    if created:
        sleep(3)

        base_url = "http://api.openapi.io/ppurio/1/message/sms/dobestan"
        headers = {
            'x-waple-authorization': 'MTkyMC0xNDEzODU0NTAwMzU3LTllM2VkOTM3LTYwMTEtNGU2Zi1iZWQ5LTM3NjAxMTNlNmYyMg==',
        }
        data = {
                "send_phone": "01022205736",
                "dest_phone": "01022205736",
                "msg_body": "새로운 회원가입",
        }

        response = requests.post(
            base_url,
            headers=headers,
            data=data,
        )
