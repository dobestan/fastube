from celery import Task

import requests


class SendNotificationBaseTask(Task):

    def get_object(self, object_id):
        raise NotImplementedError

    def get_api_base_url(self):
        raise NotImplementedError

    def get_headers(self):
        raise NotImplementedError

    def get_data(self, object):
        raise NotImplementedError

    def run(self, object_id):

        object = self.get_object(object_id)

        api_base_url = self.get_api_base_url()
        headers = self.get_headers()
        data = self.get_data(object)

        response = requests.post(
            api_base_url,
            headers=headers,
            data=data,
        )

        object.response_status_code = response.status_code
        object.save()
