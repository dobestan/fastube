import requests
from time import sleep

from celery import Task


class SimpleTask(Task):

    def run(self):
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
