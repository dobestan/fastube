from django.apps import AppConfig


class NotificationsAppConfig(AppConfig):
    name = "notifications"

    def ready(self):
        from notifications.signals.post_save import post_save_notification
